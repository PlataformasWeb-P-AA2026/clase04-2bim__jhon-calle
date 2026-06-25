from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return "%s %s %s" % (self.nombre, 
                self.apellido,
                self.cedula)
    
    def obtener_nro_tel(self):
        return len(NumeroTelefonico)

class NumeroTelefonico(models.Model):
    telefono = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE,
            related_name="numeros_telefonicos")

    def __str__(self):
        return "%s %s" % (self.telefono, self.tipo)
    
    def obtener_operadora(self):
        op = self.telefono[:3]

        op_claro = [
            "099", "098", "097"
        ]

        op_movistar = [
            "096", "095"
        ]

        if op in op_claro:
            return "Claro"
        elif op in op_movistar:
            return "Movistar"
        else:
            return "Operadora desconocida"