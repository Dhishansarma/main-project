from django.shortcuts import render, get_object_or_404
from .models import Photo,RaspberryPiProject,NodemcuProject,ArduinoProject
from .forms import WorkshopForm, CareerForm, ProjectOrderForm,Photoform,rasproform,Nodeform
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    return render(request, "index.html")

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

def rasproject_list(request):
    projects = RaspberryPiProject.objects.all()
    return render(request, 'raspro.html', {'projects': projects})

def ardiproject(request):
    projects2 = ArduinoProject.objects.all()
    return render(request, 'ardopro.html', {'ardprojects': projects2})

def nodeproject(request):
    projects3 = NodemcuProject.objects.all()
    return render(request, 'nodepro.html', {'noprojects': projects3})

def Nodeproject_list(request, project_id):
    nodeprojects = get_object_or_404(NodemcuProject, id=project_id)
    if isinstance(nodeprojects.component, str):
        component_list = [c.strip() for c in nodeprojects.component.split(",")]
    else:
        component_list = nodeprojects.component
    return render(request, 'nodeprodetails.html', {'nodeprojects': nodeprojects, 'components': component_list})

def ardiproject_list(request, project_id):
    ardoprojects = get_object_or_404(ArduinoProject, id=project_id)
    if isinstance(ardoprojects.component, str):
        component_list = [c.strip() for c in ardoprojects.component.split(",")]
    else:
        component_list = ardoprojects.component
    return render(request, 'ardoprodetails.html', {'ardinoprojects': ardoprojects, 'component': component_list})

def rasprodet(request, project_id):
    raspberry_project = get_object_or_404(RaspberryPiProject, id=project_id)
    if isinstance(raspberry_project.component, str):
        component_list = [c.strip() for c in raspberry_project.component.split(",")]
    else:
        component_list = raspberry_project.component
    return render(request, 'rasprodetails.html', {'raspberry_project': raspberry_project,
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