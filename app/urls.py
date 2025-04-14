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
    path('rasprojectli', views.rasproject_list, name='rasprojectli'),
    path('nodeprodetails/<int:project_id>/', views.Nodeproject_list, name='nodeprodetails'),
    path('ardinoprodetails/<int:project_id>/', views.ardiproject_list, name='ardinoprodetails'),
    path('rasprodetails/<int:project_id>/', views.rasprodet, name='rasprodetails'),
    path("send_order_email/", views.send_project_email, name="send_order_email"),
    path('ardproli', views.ardiproject, name='ardproli'),
    path('nodeproli', views.nodeproject, name='nodeproli'),
    path("team/", views.team, name="team"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
