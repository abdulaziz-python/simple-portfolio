from django.db import models
from django.core.validators import URLValidator

class About(models.Model):
    name = models.CharField(max_length=100, default="Abdulaziz Hamidjonov")
    title = models.CharField(max_length=200, default="AI/ML & Backend Developer")
    description = models.TextField(
        default="Passionate AI/ML and Backend Developer specializing in Python, Django, and Telegram Bot development. "
                "Experienced in building scalable web applications, machine learning solutions, and automated systems."
    )
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume_file = models.FileField(upload_to='resume/', blank=True, null=True)
    
    # Social Links
    github_username = models.CharField(max_length=100, default="abdulaziz-python")
    telegram_username = models.CharField(max_length=100, default="ablaze_coder")
    blog_handle = models.CharField(max_length=100, default="@fikrlog_all")
    channel_handle = models.CharField(max_length=100, default="@pythonnews_uzbekistan")
    
    # Skills
    skills = models.TextField(
        default="Python, Django, DRF, TensorFlow, Aiogram, Telebot, PostgreSQL, Git, Docker, AI/ML, Payment Systems"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"
    
    def __str__(self):
        return f"{self.name} - {self.title}"

class Experience(models.Model):
    EXPERIENCE_TYPES = [
        ('work', 'Work Experience'),
        ('education', 'Education'),
        ('certification', 'Certification'),
    ]
    
    title = models.CharField(max_length=200)
    company_or_institution = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    experience_type = models.CharField(max_length=20, choices=EXPERIENCE_TYPES, default='work')
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['-start_date', 'order']
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"
    
    def __str__(self):
        return f"{self.title} at {self.company_or_institution}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    frameworks = models.CharField(
        max_length=500,
        help_text="Comma-separated list of frameworks/technologies used"
    )
    project_link = models.URLField(blank=True, null=True, help_text="Live project URL")
    github_link = models.URLField(blank=True, null=True, help_text="GitHub repository URL")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-is_featured', 'order', '-created_at']
        verbose_name = "Project"
        verbose_name_plural = "Projects"
    
    def __str__(self):
        return self.title
    
    def get_frameworks_list(self):
        return [fw.strip() for fw in self.frameworks.split(',') if fw.strip()]

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
