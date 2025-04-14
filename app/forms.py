from django import forms
from .models import Workshop, CareerApplication, ProjectOrder,Photo,RaspberryPiProject,NodemcuProject,ArduinoProject

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

class rasproform(forms.ModelForm):
    class Meta:
        model = RaspberryPiProject
        fields = '__all__'


class Nodeform(forms.ModelForm):
    class Meta:
        model = NodemcuProject
        fields = '__all__'


class Ardunioform(forms.ModelForm):
    class Meta:
        model = ArduinoProject
        fields = '__all__'

