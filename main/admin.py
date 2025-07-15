from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import About, Experience, Project, ContactMessage, Skill

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'location', 'years_of_experience', 'updated_at']
    fields = [
        'name', 'title', 'description', 'profile_image', 'resume_file',
        'github_username', 'telegram_username', 'blog_handle', 'channel_handle',
        'linkedin_url', 'twitter_url', 'website_url',
        'skills', 'location', 'email', 'phone',
        'years_of_experience', 'current_status',
        'meta_description', 'meta_keywords'
    ]
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'title', 'description', 'profile_image', 'resume_file')
        }),
        ('Contact Information', {
            'fields': ('location', 'email', 'phone')
        }),
        ('Social Links', {
            'fields': ('github_username', 'telegram_username', 'blog_handle', 'channel_handle',
                      'linkedin_url', 'twitter_url', 'website_url')
        }),
        ('Professional Information', {
            'fields': ('skills', 'years_of_experience', 'current_status')
        }),
        ('SEO', {
            'fields': ('meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        # Only allow one About instance
        return not About.objects.exists()

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company_or_institution', 'experience_type', 'start_date', 'is_current', 'order']
    list_filter = ['experience_type', 'is_current', 'start_date']
    search_fields = ['title', 'company_or_institution', 'description', 'skills_used']
    ordering = ['-start_date', 'order']
    date_hierarchy = 'start_date'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'company_or_institution', 'location', 'experience_type', 'website_url')
        }),
        ('Duration', {
            'fields': ('start_date', 'end_date', 'is_current')
        }),
        ('Details', {
            'fields': ('description', 'skills_used', 'achievements', 'order')
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related()

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'is_featured', 'is_public', 'order', 'created_at']
    list_filter = ['is_featured', 'is_public', 'status', 'created_at']
    search_fields = ['title', 'description', 'frameworks', 'client']
    ordering = ['-is_featured', 'order', '-created_at']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'slug', 'description', 'detailed_description', 'frameworks')
        }),
        ('Project Details', {
            'fields': ('status', 'start_date', 'end_date', 'client', 'team_size')
        }),
        ('Links', {
            'fields': ('project_link', 'github_link', 'demo_link')
        }),
        ('Media', {
            'fields': ('image', 'gallery_images')
        }),
        ('Display Options', {
            'fields': ('is_featured', 'is_public', 'order')
        }),
        ('SEO', {
            'fields': ('meta_description',),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request)
    
    def view_project(self, obj):
        if obj.project_link:
            return format_html('<a href="{}" target="_blank">View Live</a>', obj.project_link)
        return '-'
    view_project.short_description = 'Live Project'

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'priority', 'is_read', 'is_replied', 'created_at']
    list_filter = ['is_read', 'is_replied', 'priority', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['name', 'email', 'subject', 'message', 'phone', 'company', 
                      'ip_address', 'user_agent', 'created_at', 'updated_at']
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Message Information', {
            'fields': ('name', 'email', 'phone', 'company', 'subject', 'message', 'priority')
        }),
        ('Status', {
            'fields': ('is_read', 'is_replied', 'reply_message', 'replied_at')
        }),
        ('Metadata', {
            'fields': ('ip_address', 'user_agent', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        return False
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
        self.message_user(request, f"{queryset.count()} messages marked as read.")
    mark_as_read.short_description = "Mark selected messages as read"
    
    def mark_as_replied(self, request, queryset):
        from django.utils import timezone
        queryset.update(is_replied=True, replied_at=timezone.now())
        self.message_user(request, f"{queryset.count()} messages marked as replied.")
    mark_as_replied.short_description = "Mark selected messages as replied"
    
    actions = ['mark_as_read', 'mark_as_replied']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'years_of_experience', 'is_featured', 'order']
    list_filter = ['category', 'proficiency', 'is_featured']
    search_fields = ['name', 'description']
    ordering = ['category', 'order', 'name']
    
    fieldsets = (
        ('Skill Information', {
            'fields': ('name', 'category', 'proficiency', 'years_of_experience', 'description')
        }),
        ('Display', {
            'fields': ('icon_class', 'color', 'is_featured', 'order')
        }),
    )

# Customize admin site
admin.site.site_header = "Abdulaziz Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Portfolio Administration"
admin.site.site_url = "/"
