from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="myindex"),
    path("alumno/<str:nombre_alumno>", views.alumno, name="alumno"),
    path("nuevo-alumno", views.nuevo_alumno, name="nuevo_alumno"),
    path("actualizar-alumno/<int:pk>", views.actualizar_alumno, name="actualizar_alumno"),
    path("eliminar-alumno/<int:pk>", views.eliminar_alumno, name="eliminar_alumno"),
]