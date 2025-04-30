from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("workshop/", views.workshop, name="workshop"),
    path("careers/", views.careers, name="careers"),
    path("project/", views.project, name="project"),
    path('about/', views.about_view, name='about'),
    path('event/', views.event, name='event'),
    path('photo/', views.photo, name='photo'),
    path('AWSli', views.AWS, name='AWSli'),
    path('Weblidetails/<int:project_id>/', views.WebDevelopment_list, name='Weblidetails'),
    path('ardinoprodetails/<int:project_id>/', views.ardiproject_list, name='ardinoprodetails'),
    path('AWSlidet/<int:project_id>/', views.AWS_list, name='AWSlidet'),
    path("send_order_email/", views.send_project_email, name="send_order_email"),
    path('ardproli', views.ardiproject, name='ardproli'),
    path('Webli', views.WebDevelopment, name='Webli'),
    path("team/", views.team, name="team"),
    path('internship-registration/', views.internship_registration, name='internship-registration'),
    path("internship/", views.Internship, name="internship"),
    





] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
