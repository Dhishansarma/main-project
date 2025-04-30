from django.db import models
class Workshop(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    designation = models.CharField(max_length=50)
    institute = models.CharField(max_length=200)
    course = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class CareerApplication(models.Model):
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    job_type = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    resume = models.FileField(upload_to="resumes/")

    def __str__(self):
        return f"{self.name} - {self.job_type}"

class ProjectOrder(models.Model):
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=200)
    degree = models.CharField(max_length=50)
    stream = models.CharField(max_length=100)
    year = models.IntegerField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    project = models.CharField(max_length=100)
    project_type = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name


class ArduinoProject(models.Model):
    title = models.CharField(max_length=200)
    description1 = models.TextField()    
    component=models.CharField(max_length=200, default="Default Component")
    title_image = models.ImageField(upload_to='ardproli',null=True, blank=True)
   
    def __str__(self):
        return self.title

class AWSProjects(models.Model):
    title = models.CharField(max_length=200)
    description1 = models.TextField()
    
    Requirements=models.CharField(max_length=200, default="Default Component")
    title_image = models.ImageField(upload_to='ardproli',null=True, blank=True)
   
    def __str__(self):
        return self.title


class WebDevelopmentprojects(models.Model):
    title = models.CharField(max_length=200)
    description1 = models.TextField()
    Requirements=models.CharField(max_length=200, default="Default Component")
    title_image = models.ImageField(upload_to='ardproli',null=True, blank=True)
    
    def __str__(self):
        return self.title

class Internship(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    college = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    address = models.TextField()
    