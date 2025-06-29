from django.db import models

class Regla(models.Model):
    porcentaje = models.FloatField()
    monto_minimo = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.porcentaje}% desde ${self.monto_minimo}"
    