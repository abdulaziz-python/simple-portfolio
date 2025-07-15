from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Project

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['main:home', 'main:about', 'main:projects']

    def location(self, item):
        return reverse(item)

class ProjectSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Project.objects.filter(is_public=True)

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return obj.get_absolute_url()
