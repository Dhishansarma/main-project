

# Register your models here.
from django.contrib import admin
from .models import  Workshop, CareerApplication, ProjectOrder,Photo,RaspberryPiProject,NodemcuProject,ArduinoProject

# Custom Admin Display for Projects
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'description', 'created_at')
#     search_fields = ('name',)

class RaspberryPiAdmin(admin.ModelAdmin):
    list_display = ('title','image','description1','description2','Price')

class NodeMCUAdmin(admin.ModelAdmin):
    list_display = ('title','image','description1','description2','Price')

class ArduinoAdmin(admin.ModelAdmin):
    list_display = ('title','image','description1','description2','Price')

class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mobile', 'email', 'course')
    search_fields = ('name', 'email')

class CareerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'job_type', 'qualification')
    search_fields = ('name', 'email')

class ProjectOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'project', 'project_type', 'title')
    search_fields = ('name', 'email')



# Registering Models
# admin.site.register(Project, ProjectAdmin)
admin.site.register(RaspberryPiProject, RaspberryPiAdmin)
admin.site.register(NodemcuProject, NodeMCUAdmin)
admin.site.register(ArduinoProject, ArduinoAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(CareerApplication, CareerAdmin)
admin.site.register(ProjectOrder, ProjectOrderAdmin)
admin.site.register(Photo)
