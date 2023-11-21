from django.urls import path
from . import views
from .views import export_to_excel

#app_name = 'excelapp'
urlpatterns = [
    path('', views.index, name='index'),   # 一覧
    path('export/', export_to_excel, name='export_to_excel'),
]
