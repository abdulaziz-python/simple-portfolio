from django.core.management.base import BaseCommand
from django.utils import timezone
from main.models import About, Experience, Project

class Command(BaseCommand):
    help = 'Setup initial data for the portfolio'

    def handle(self, *args, **options):
        self.stdout.write('Setting up initial data...')
        
        # Create About instance if it doesn't exist
        if not About.objects.exists():
            about = About.objects.create(
                name='Abdulaziz Hamidjonov',
                title='AI/ML & Backend Developer',
                description='Passionate AI/ML and Backend Developer specializing in Python, Django, and Telegram Bot development. Experienced in building scalable web applications, machine learning solutions, and automated systems.',
                github_username='abdulaziz-python',
                telegram_username='ablaze_coder',
                blog_handle='@fikrlog_all',
                channel_handle='@pythonnews_uzbekistan',
                skills='Python, Django, DRF, TensorFlow, Aiogram, Telebot, PostgreSQL, Git, Docker, AI/ML, Payment Systems',
                location='Tashkent, Uzbekistan',
                years_of_experience=3,
                current_status='Available for new opportunities'
            )
            self.stdout.write(self.style.SUCCESS('Created About instance'))
        
        # Create sample experiences
        experiences_data = [
            {
                'title': 'Senior Backend Developer',
                'company_or_institution': 'Tech Solutions Inc.',
                'location': 'Tashkent, Uzbekistan',
                'start_date': '2023-01-01',
                'is_current': True,
                'description': 'Leading backend development projects using Django and PostgreSQL. Developed scalable APIs, implemented payment systems, and created automated Telegram bots for business processes.',
                'experience_type': 'work',
                'skills_used': 'Python, Django, PostgreSQL, Redis, Docker',
                'order': 1
            },
            {
                'title': 'AI/ML Developer',
                'company_or_institution': 'DataTech Solutions',
                'location': 'Remote',
                'start_date': '2022-03-01',
                'end_date': '2022-12-31',
                'description': 'Developed machine learning models using TensorFlow and Python. Created data analysis pipelines and implemented recommendation systems.',
                'experience_type': 'work',
                'skills_used': 'Python, TensorFlow, Pandas, NumPy, Scikit-learn',
                'order': 2
            },
            {
                'title': 'Computer Science Degree',
                'company_or_institution': 'Tashkent University of Information Technologies',
                'location': 'Tashkent, Uzbekistan',
                'start_date': '2019-09-01',
                'end_date': '2023-06-30',
                'description': 'Bachelor\'s degree in Computer Science with focus on Software Engineering and Artificial Intelligence.',
                'experience_type': 'education',
                'order': 1
            }
        ]
        
        for exp_data in experiences_data:
            if not Experience.objects.filter(title=exp_data['title'], company_or_institution=exp_data['company_or_institution']).exists():
                Experience.objects.create(**exp_data)
                self.stdout.write(f'Created experience: {exp_data["title"]}')
        
        # Create sample projects
        projects_data = [
            {
                'title': 'AI-Powered Telegram Bot',
                'description': 'An intelligent Telegram bot that uses natural language processing to provide automated customer support. Features include sentiment analysis, automated responses, and integration with business systems.',
                'frameworks': 'Python, Aiogram, TensorFlow, PostgreSQL, Docker',
                'github_link': 'https://github.com/abdulaziz-python/ai-telegram-bot',
                'is_featured': True,
                'order': 1
            },
            {
                'title': 'E-commerce Payment System',
                'description': 'A secure payment processing system for e-commerce platforms. Supports multiple payment gateways, handles transactions securely, and provides detailed analytics.',
                'frameworks': 'Django, DRF, PostgreSQL, Redis, Celery',
                'github_link': 'https://github.com/abdulaziz-python/payment-system',
                'is_featured': True,
                'order': 2
            },
            {
                'title': 'Machine Learning Data Pipeline',
                'description': 'An automated data processing pipeline for machine learning workflows. Features data ingestion, preprocessing, model training, and deployment automation.',
                'frameworks': 'Python, TensorFlow, Apache Airflow, Docker, Kubernetes',
                'github_link': 'https://github.com/abdulaziz-python/ml-pipeline',
                'is_featured': True,
                'order': 3
            }
        ]
        
        for proj_data in projects_data:
            if not Project.objects.filter(title=proj_data['title']).exists():
                Project.objects.create(**proj_data)
                self.stdout.write(f'Created project: {proj_data["title"]}')
        
        self.stdout.write(self.style.SUCCESS('Initial data setup completed!'))
