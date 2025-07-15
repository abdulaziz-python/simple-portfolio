from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import About, Experience, Project, ContactMessage
import json

def home(request):
    about = About.objects.first()
    if not about:
        # Create default about if none exists
        about = About.objects.create()
    
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    recent_experiences = Experience.objects.all()[:3]
    
    context = {
        'about': about,
        'featured_projects': featured_projects,
        'recent_experiences': recent_experiences,
    }
    return render(request, 'main/home.html', context)

def about_view(request):
    about = About.objects.first()
    if not about:
        about = About.objects.create()
    
    experiences = Experience.objects.all()
    
    context = {
        'about': about,
        'experiences': experiences,
    }
    return render(request, 'main/about.html', context)

def projects_view(request):
    projects = Project.objects.all()
    
    context = {
        'projects': projects,
    }
    return render(request, 'main/projects.html', context)

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    context = {
        'project': project,
    }
    return render(request, 'main/project_detail.html', context)

@csrf_exempt
@require_http_methods(["POST"])
def contact_submit(request):
    try:
        data = json.loads(request.body)
        
        contact_message = ContactMessage.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            subject=data.get('subject'),
            message=data.get('message')
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Thank you for your message! I\'ll get back to you soon.'
        })
    
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': 'Sorry, there was an error sending your message. Please try again.'
        }, status=400)
