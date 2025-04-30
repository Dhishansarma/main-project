from django.shortcuts import render, get_object_or_404,redirect
from .models import Photo,ArduinoProject,AWSProjects,WebDevelopmentprojects
from .forms import WorkshopForm, CareerForm, ProjectOrderForm,Photoform,InternshipForm
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

import json

def home(request):
    return render(request, "index.html")

def Internship(request):
    return render(request,"SummerInternship.html")

def workshop(request):
    if request.method == "POST":
        form = WorkshopForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "workshop.html", {"form": form, "message": "Workshop booked successfully!"})
    else:
        form = WorkshopForm()
    return render(request, "workshop.html", {"form": form})

def careers(request):
    if request.method == "POST":
        form = CareerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "careers.html", {"form": form, "message": "Career application submitted successfully!"})
    else:
        form = CareerForm()
    return render(request, "careers.html", {"form": form})
def project(request):
    if request.method == "POST":
        form = ProjectOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "project.html", {"form": form, "message": "Project order submitted successfully!"})
    else:
        form = ProjectOrderForm()
    return render(request, "project.html", {"form": form})


def about_view(request):
    return render(request, 'about.html')

def event(request):
    return render(request, 'events.html')


def photo(request):
    photos = Photo.objects.all()
    return render(request, 'Photos.html', {'photos': photos})

def AWS(request):
    projects = AWSProjects.objects.all()
    return render(request, 'AWS.html', {'projects': projects})

def ardiproject(request):
    projects2 = ArduinoProject.objects.all()
    return render(request, 'ardopro.html', {'ardprojects': projects2})

def WebDevelopment(request):
    projects3 = WebDevelopmentprojects.objects.all()
    return render(request, 'WebDevelopment.html', {'noprojects': projects3})

def AWS_list(request, project_id):
    awsprojects = get_object_or_404(AWSProjects, id=project_id)
    if isinstance(awsprojects.Requirements, str):
        component_list = [c.strip() for c in awsprojects.Requirements.split(",")]
    else:
        component_list = awsprojects.Requirements
    return render(request, 'AWSdetails.html', {'awsprojects': awsprojects, 'components': component_list})

def ardiproject_list(request, project_id):
    ardoprojects = get_object_or_404(ArduinoProject, id=project_id)
    if isinstance(ardoprojects.component, str):
        component_list = [c.strip() for c in ardoprojects.component.split(",")]
    else:
        component_list = ardoprojects.component
    return render(request, 'ardoprodetails.html', {'ardinoprojects': ardoprojects, 'component': component_list})

def WebDevelopment_list(request, project_id):
    WebDevelopment_project = get_object_or_404(WebDevelopmentprojects, id=project_id)
    if isinstance(WebDevelopment_project.Requirements, str):
        component_list = [c.strip() for c in WebDevelopment_project.Requirements.split(",")]
    else:
        component_list = WebDevelopment_project.Requirements
    return render(request, 'WebDevelopmentdetails.html', {' WebDevelopment_project': WebDevelopment_project,
        'component_list': component_list })

@csrf_exempt  # Disable CSRF for simplicity (only use if necessary)
def send_project_email(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Parse JSON data

            # Extract form fields
            name = data.get("name")
            phone = data.get("phone")
            project_type = data.get("Type")
            title = data.get("productTitle")

            # Email content
            subject = f"New Project Order from {name}"
            message = f"""
            Name: {name}
            Phone: {phone}
            Type: {project_type}
            Project Title: {title}
            """
            recipient_email = "dhishansarma@gmail.com"

            # Send email
            send_mail(subject, message, "your-email@example.com", [recipient_email])

            return JsonResponse({"success": True, "message": "Email sent successfully"})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})


def team(request):
    return render(request, "Team.html")

@csrf_exempt  # Only for development
def internship_registration(request):
    if request.method == "POST":
        form = InternshipForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    return JsonResponse({'success': False, 'error': 'Invalid method'})
