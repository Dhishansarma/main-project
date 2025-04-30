from django import forms
from .models import Workshop, CareerApplication, ProjectOrder,Photo,ArduinoProject,AWSProjects,WebDevelopmentprojects, Internship

class WorkshopForm(forms.ModelForm):
    class Meta:
        model = Workshop
        fields = '__all__'

class CareerForm(forms.ModelForm):
    class Meta:
        model = CareerApplication
        fields = '__all__'

class ProjectOrderForm(forms.ModelForm):
    class Meta:
        model = ProjectOrder
        fields = '__all__'


class Photoform(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'

class Ardunioform(forms.ModelForm):
    class Meta:
        model = ArduinoProject
        fields = '__all__'

class AWSform(forms.ModelForm):
    class Meta:
        model = AWSProjects
        fields = '__all__'


class WebDevelopmentform(forms.ModelForm):
    class Meta:
        model = WebDevelopmentprojects
        fields = '__all__'

class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = ['name', 'mobile', 'email', 'college', 'location', 'address']
        