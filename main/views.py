from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.utils import timezone
from .models import About, Experience, Project, ContactMessage
import json
import logging

logger = logging.getLogger(__name__)

def home(request):
    """Home page view with featured content"""
    try:
        about = About.objects.first()
        if not about:
            # Create default about if none exists
            about = About.objects.create()
        
        featured_projects = Project.objects.filter(is_featured=True).order_by('order', '-created_at')[:3]
        recent_experiences = Experience.objects.all().order_by('-start_date', 'order')[:3]
        
        context = {
            'about': about,
            'featured_projects': featured_projects,
            'recent_experiences': recent_experiences,
            'page_title': 'Home',
        }
        return render(request, 'main/home.html', context)
    except Exception as e:
        logger.error(f"Error in home view: {e}")
        return render(request, 'errors/500.html', status=500)

def about_view(request):
    """About page view with detailed information"""
    try:
        about = About.objects.first()
        if not about:
            about = About.objects.create()
        
        experiences = Experience.objects.all().order_by('-start_date', 'order')
        
        # Group experiences by type
        work_experiences = experiences.filter(experience_type='work')
        education_experiences = experiences.filter(experience_type='education')
        certifications = experiences.filter(experience_type='certification')
        
        context = {
            'about': about,
            'experiences': experiences,
            'work_experiences': work_experiences,
            'education_experiences': education_experiences,
            'certifications': certifications,
            'page_title': 'About',
        }
        return render(request, 'main/about.html', context)
    except Exception as e:
        logger.error(f"Error in about view: {e}")
        return render(request, 'errors/500.html', status=500)

def projects_view(request):
    """Projects page view with filtering and pagination"""
    try:
        projects_list = Project.objects.all().order_by('-is_featured', 'order', '-created_at')
        
        # Search functionality
        search_query = request.GET.get('search', '')
        if search_query:
            projects_list = projects_list.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(frameworks__icontains=search_query)
            )
        
        # Filter by featured
        featured_filter = request.GET.get('featured', '')
        if featured_filter == 'true':
            projects_list = projects_list.filter(is_featured=True)
        
        # Pagination
        paginator = Paginator(projects_list, 6)  # Show 6 projects per page
        page_number = request.GET.get('page')
        projects = paginator.get_page(page_number)
        
        # Get all unique technologies for filter
        all_projects = Project.objects.all()
        technologies = set()
        for project in all_projects:
            for tech in project.get_frameworks_list():
                technologies.add(tech.strip())
        technologies = sorted(list(technologies))
        
        context = {
            'projects': projects,
            'search_query': search_query,
            'featured_filter': featured_filter,
            'technologies': technologies,
            'page_title': 'Projects',
        }
        return render(request, 'main/projects.html', context)
    except Exception as e:
        logger.error(f"Error in projects view: {e}")
        return render(request, 'errors/500.html', status=500)

def project_detail(request, project_id):
    """Project detail view"""
    try:
        project = get_object_or_404(Project, id=project_id)
        
        # Get related projects (same technologies)
        related_projects = Project.objects.exclude(id=project.id).filter(
            frameworks__icontains=project.get_frameworks_list()[0] if project.get_frameworks_list() else ''
        )[:3]
        
        context = {
            'project': project,
            'related_projects': related_projects,
            'page_title': project.title,
        }
        return render(request, 'main/project_detail.html', context)
    except Http404:
        return render(request, 'errors/404.html', status=404)
    except Exception as e:
        logger.error(f"Error in project detail view: {e}")
        return render(request, 'errors/500.html', status=500)

@csrf_exempt
@require_http_methods(["POST"])
def contact_submit(request):
    """Handle contact form submission"""
    try:
        data = json.loads(request.body)
        
        # Validate required fields
        required_fields = ['name', 'email', 'subject', 'message']
        for field in required_fields:
            if not data.get(field, '').strip():
                return JsonResponse({
                    'success': False,
                    'message': f'{field.title()} is required.'
                }, status=400)
        
        # Validate email format
        import re
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, data.get('email', '')):
            return JsonResponse({
                'success': False,
                'message': 'Please enter a valid email address.'
            }, status=400)
        
        # Create contact message
        contact_message = ContactMessage.objects.create(
            name=data.get('name').strip(),
            email=data.get('email').strip().lower(),
            subject=data.get('subject').strip(),
            message=data.get('message').strip()
        )
        
        logger.info(f"New contact message from {contact_message.email}")
        
        return JsonResponse({
            'success': True,
            'message': 'Thank you for your message! I\'ll get back to you within 24 hours.'
        })
    
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': 'Invalid data format.'
        }, status=400)
    except Exception as e:
        logger.error(f"Error in contact submit: {e}")
        return JsonResponse({
            'success': False,
            'message': 'Sorry, there was an error sending your message. Please try again.'
        }, status=500)

def api_projects(request):
    """API endpoint for projects (for AJAX requests)"""
    try:
        projects = Project.objects.all().order_by('-is_featured', 'order', '-created_at')
        
        projects_data = []
        for project in projects:
            projects_data.append({
                'id': project.id,
                'title': project.title,
                'description': project.description,
                'frameworks': project.get_frameworks_list(),
                'project_link': project.project_link,
                'github_link': project.github_link,
                'is_featured': project.is_featured,
                'image_url': project.image.url if project.image else None,
                'created_at': project.created_at.isoformat(),
            })
        
        return JsonResponse({
            'success': True,
            'projects': projects_data
        })
    except Exception as e:
        logger.error(f"Error in API projects: {e}")
        return JsonResponse({
            'success': False,
            'message': 'Error fetching projects.'
        }, status=500)

def api_skills(request):
    """API endpoint for skills"""
    try:
        about = About.objects.first()
        if not about:
            return JsonResponse({
                'success': False,
                'message': 'No skills data found.'
            }, status=404)
        
        skills_list = [skill.strip() for skill in about.skills.split(',') if skill.strip()]
        
        return JsonResponse({
            'success': True,
            'skills': skills_list
        })
    except Exception as e:
        logger.error(f"Error in API skills: {e}")
        return JsonResponse({
            'success': False,
            'message': 'Error fetching skills.'
        }, status=500)

# Error handlers
def handler404(request, exception):
    """Custom 404 error handler"""
    return render(request, 'errors/404.html', status=404)

def handler500(request):
    """Custom 500 error handler"""
    return render(request, 'errors/500.html', status=500)

def handler403(request, exception):
    """Custom 403 error handler"""
    return render(request, 'errors/403.html', status=403)

def handler400(request, exception):
    """Custom 400 error handler"""
    return render(request, 'errors/400.html', status=400)
