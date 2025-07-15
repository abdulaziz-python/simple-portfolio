from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_view, name='about'),
    path('projects/', views.projects_view, name='projects'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
    
    # API endpoints
    path('api/projects/', views.api_projects, name='api_projects'),
    path('api/skills/', views.api_skills, name='api_skills'),
]
