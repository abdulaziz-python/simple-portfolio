from django.db import models
from django.core.validators import URLValidator, EmailValidator
from django.utils import timezone
from django.urls import reverse
import uuid

class TimeStampedModel(models.Model):
    """Abstract base class with created_at and updated_at fields"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class About(TimeStampedModel):
    """Model for personal information and about section"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
    
    # Additional social links
    linkedin_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)
    
    # Skills and expertise
    skills = models.TextField(
        default="Python, Django, DRF, TensorFlow, Aiogram, Telebot, PostgreSQL, Git, Docker, AI/ML, Payment Systems"
    )
    
    # Location and contact
    location = models.CharField(max_length=100, blank=True, default="Tashkent, Uzbekistan")
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    # Professional info
    years_of_experience = models.PositiveIntegerField(default=3)
    current_status = models.CharField(
        max_length=100, 
        default="Available for new opportunities",
        help_text="Current availability status"
    )
    
    # SEO fields
    meta_description = models.TextField(
        max_length=160, 
        blank=True,
        help_text="Meta description for SEO (max 160 characters)"
    )
    meta_keywords = models.TextField(
        blank=True,
        help_text="Comma-separated keywords for SEO"
    )
    
    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"
    
    def __str__(self):
        return f"{self.name} - {self.title}"
    
    def get_skills_list(self):
        """Return skills as a list"""
        return [skill.strip() for skill in self.skills.split(',') if skill.strip()]
    
    def get_social_links(self):
        """Return all social links as a dictionary"""
        links = {}
        if self.github_username:
            links['github'] = f"https://github.com/{self.github_username}"
        if self.telegram_username:
            links['telegram'] = f"https://t.me/{self.telegram_username}"
        if self.blog_handle:
            handle = self.blog_handle.lstrip('@')
            links['blog'] = f"https://t.me/{handle}"
        if self.channel_handle:
            handle = self.channel_handle.lstrip('@')
            links['channel'] = f"https://t.me/{handle}"
        if self.linkedin_url:
            links['linkedin'] = self.linkedin_url
        if self.twitter_url:
            links['twitter'] = self.twitter_url
        if self.website_url:
            links['website'] = self.website_url
        return links

class Experience(TimeStampedModel):
    """Model for work experience, education, and certifications"""
    EXPERIENCE_TYPES = [
        ('work', 'Work Experience'),
        ('education', 'Education'),
        ('certification', 'Certification'),
        ('volunteer', 'Volunteer Work'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    company_or_institution = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    experience_type = models.CharField(max_length=20, choices=EXPERIENCE_TYPES, default='work')
    order = models.PositiveIntegerField(default=0, help_text="Order for display (lower numbers first)")
    
    # Additional fields
    website_url = models.URLField(blank=True, null=True)
    skills_used = models.TextField(
        blank=True,
        help_text="Comma-separated list of skills used in this role"
    )
    achievements = models.TextField(
        blank=True,
        help_text="Key achievements and accomplishments"
    )
    
    class Meta:
        ordering = ['-start_date', 'order']
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"
    
    def __str__(self):
        return f"{self.title} at {self.company_or_institution}"
    
    def get_duration(self):
        """Calculate duration of experience"""
        end = self.end_date or timezone.now().date()
        duration = end - self.start_date
        years = duration.days // 365
        months = (duration.days % 365) // 30
        
        if years > 0:
            return f"{years} year{'s' if years > 1 else ''}" + (f" {months} month{'s' if months > 1 else ''}" if months > 0 else "")
        elif months > 0:
            return f"{months} month{'s' if months > 1 else ''}"
        else:
            return "Less than a month"
    
    def get_skills_list(self):
        """Return skills as a list"""
        if not self.skills_used:
            return []
        return [skill.strip() for skill in self.skills_used.split(',') if skill.strip()]

class Project(TimeStampedModel):
    """Model for portfolio projects"""
    STATUS_CHOICES = [
        ('planning', 'Planning'),
        ('development', 'In Development'),
        ('completed', 'Completed'),
        ('maintenance', 'Maintenance'),
        ('archived', 'Archived'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    detailed_description = models.TextField(
        blank=True,
        help_text="Detailed project description for project detail page"
    )
    
    # Technologies and frameworks
    frameworks = models.CharField(
        max_length=500,
        help_text="Comma-separated list of frameworks/technologies used"
    )
    
    # Links
    project_link = models.URLField(blank=True, null=True, help_text="Live project URL")
    github_link = models.URLField(blank=True, null=True, help_text="GitHub repository URL")
    demo_link = models.URLField(blank=True, null=True, help_text="Demo or preview URL")
    
    # Media
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    gallery_images = models.TextField(
        blank=True,
        help_text="Comma-separated list of additional image URLs"
    )
    
    # Project details
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    client = models.CharField(max_length=200, blank=True, help_text="Client or company name")
    team_size = models.PositiveIntegerField(blank=True, null=True)
    
    # Display options
    is_featured = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0, help_text="Order for display (lower numbers first)")
    
    # SEO
    meta_description = models.TextField(
        max_length=160, 
        blank=True,
        help_text="Meta description for SEO (max 160 characters)"
    )
    
    class Meta:
        ordering = ['-is_featured', 'order', '-created_at']
        verbose_name = "Project"
        verbose_name_plural = "Projects"
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('main:project_detail', kwargs={'project_id': self.id})
    
    def get_frameworks_list(self):
        """Return frameworks as a list"""
        return [fw.strip() for fw in self.frameworks.split(',') if fw.strip()]
    
    def get_gallery_images(self):
        """Return gallery images as a list"""
        if not self.gallery_images:
            return []
        return [img.strip() for img in self.gallery_images.split(',') if img.strip()]
    
    def get_duration(self):
        """Calculate project duration"""
        if not self.start_date:
            return None
        
        end = self.end_date or timezone.now().date()
        duration = end - self.start_date
        
        if duration.days < 30:
            return f"{duration.days} days"
        elif duration.days < 365:
            months = duration.days // 30
            return f"{months} month{'s' if months > 1 else ''}"
        else:
            years = duration.days // 365
            return f"{years} year{'s' if years > 1 else ''}"

class ContactMessage(TimeStampedModel):
    """Model for contact form messages"""
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator()])
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    # Additional fields
    phone = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    
    # Status tracking
    is_read = models.BooleanField(default=False)
    is_replied = models.BooleanField(default=False)
    reply_message = models.TextField(blank=True, null=True)
    replied_at = models.DateTimeField(blank=True, null=True)
    
    # Metadata
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
    
    def mark_as_read(self):
        """Mark message as read"""
        self.is_read = True
        self.save(update_fields=['is_read'])
    
    def mark_as_replied(self, reply_message=None):
        """Mark message as replied"""
        self.is_replied = True
        self.replied_at = timezone.now()
        if reply_message:
            self.reply_message = reply_message
        self.save(update_fields=['is_replied', 'replied_at', 'reply_message'])

class Skill(TimeStampedModel):
    """Model for individual skills with proficiency levels"""
    PROFICIENCY_LEVELS = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]
    
    SKILL_CATEGORIES = [
        ('programming', 'Programming Languages'),
        ('framework', 'Frameworks & Libraries'),
        ('database', 'Databases'),
        ('tool', 'Tools & Software'),
        ('cloud', 'Cloud & DevOps'),
        ('ai_ml', 'AI/ML & Data Science'),
        ('other', 'Other'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES, default='other')
    proficiency = models.CharField(max_length=20, choices=PROFICIENCY_LEVELS, default='intermediate')
    years_of_experience = models.PositiveIntegerField(default=1)
    description = models.TextField(blank=True)
    icon_class = models.CharField(
        max_length=50, 
        blank=True,
        help_text="CSS class for icon (e.g., 'fab fa-python')"
    )
    color = models.CharField(
        max_length=7, 
        blank=True,
        help_text="Hex color code for skill badge"
    )
    order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['category', 'order', 'name']
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
    
    def __str__(self):
        return f"{self.name} ({self.get_proficiency_display()})"
    
    def get_proficiency_percentage(self):
        """Get proficiency as percentage"""
        levels = {
            'beginner': 25,
            'intermediate': 50,
            'advanced': 75,
            'expert': 100,
        }
        return levels.get(self.proficiency, 50)
