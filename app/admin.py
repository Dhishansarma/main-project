

# Register your models here.
from django.contrib import admin
from .models import  Workshop, CareerApplication, ProjectOrder,Photo,ArduinoProject,AWSProjects,WebDevelopmentprojects, Internship

# Custom Admin Display for Projects
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'description', 'created_at')
#     search_fields = ('name',)

class AWSAdmin(admin.ModelAdmin):
    list_display = ('title','title_image','description1')

class WebDevelopmentAdmin(admin.ModelAdmin):
    list_display = ('title','title_image','description1')

class ArduinoAdmin(admin.ModelAdmin):
    list_display = ('title','title_image','description1')

class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mobile', 'email', 'course')
    search_fields = ('name', 'email')

class CareerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'job_type', 'qualification')
    search_fields = ('name', 'email')

class ProjectOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'project', 'project_type', 'title')
    search_fields = ('name', 'email')

class InternshipAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'email', 'mobile')
    search_fields = ('name', 'email')

# Registering Models
# admin.site.register(Project, ProjectAdmin)
admin.site.register(AWSProjects, AWSAdmin)
admin.site.register(WebDevelopmentprojects, WebDevelopmentAdmin)
admin.site.register(ArduinoProject, ArduinoAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(CareerApplication, CareerAdmin)
admin.site.register(ProjectOrder, ProjectOrderAdmin)
admin.site.register(Photo)
admin.site.register(Internship,InternshipAdmin)