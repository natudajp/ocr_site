from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('ocrz/', views.HomeView, name='ocrz'),
    path('process_image/', views.process_image, name='process_image'), # New line

]