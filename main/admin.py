from django.contrib import admin
from .models import About, Experience, Project, ContactMessage

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'updated_at']
    fields = [
        'name', 'title', 'description', 'profile_image', 'resume_file',
        'github_username', 'telegram_username', 'blog_handle', 'channel_handle',
        'skills'
    ]
    
    def has_add_permission(self, request):
        # Only allow one About instance
        return not About.objects.exists()

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company_or_institution', 'experience_type', 'start_date', 'is_current', 'order']
    list_filter = ['experience_type', 'is_current', 'start_date']
    search_fields = ['title', 'company_or_institution', 'description']
    ordering = ['-start_date', 'order']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'company_or_institution', 'location', 'experience_type')
        }),
        ('Duration', {
            'fields': ('start_date', 'end_date', 'is_current')
        }),
        ('Details', {
            'fields': ('description', 'order')
        }),
    )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_featured', 'order', 'created_at']
    list_filter = ['is_featured', 'created_at']
    search_fields = ['title', 'description', 'frameworks']
    ordering = ['-is_featured', 'order', '-created_at']
    
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'description', 'frameworks')
        }),
        ('Links', {
            'fields': ('project_link', 'github_link')
        }),
        ('Display', {
            'fields': ('image', 'is_featured', 'order')
        }),
    )

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
    ordering = ['-created_at']
    
    def has_add_permission(self, request):
        return False

# Customize admin site
admin.site.site_header = "Abdulaziz Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Portfolio Administration"
