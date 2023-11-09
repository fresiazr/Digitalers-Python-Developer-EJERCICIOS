from django.db import models

class Alumno(models.Model):
    MATERIAS = (
        # Licenciatura en Informática
        ("Programación Lógica", "Programación Lógica"),
        ("Álgebra", "Álgebra"),
        ("Programación Orientada a Objetos", "Programación Orientada a Objetos"),
        # Licenciatura en Economía
        ("Administración I", "Administración I"),
        ("Contabilidad", "Contabilidad"),
        ("Principios de Economía", "Principios de Economía"),
        # Abogacía
        ("Introducción al Derecho", "Introducción al Derecho"),
        ("Teoría de la Persona", "Teoría de la Persona"),
        ("Derecho Penal I", "Derecho Penal I"),
        )
    
    nombre = models.CharField(max_length=128)
    edad = models.IntegerField()
    materia = models.CharField(max_length=128, choices=MATERIAS)
