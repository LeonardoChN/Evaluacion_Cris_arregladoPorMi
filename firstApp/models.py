from django.db import models

# Create your models here.
class Pacientes(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    def __str__(self):
        return self.nombre
    
class Medico(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    def __str__(self):
        return self.nombre
    
class Cita(models.Model):
    asunto = models.CharField(max_length=50)
    fecha = models.DateField()
    paciente = models.ForeignKey(Pacientes,on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico,on_delete=models.CASCADE)