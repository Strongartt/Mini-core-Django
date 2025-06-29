from django.db import models
from.vendedor import Vendedor
from .regla import Regla

class Venta(models.Model):
    Vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    regla = models.ForeignKey(Regla, on_delete=models.CASCADE)
    fecha_venta = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Venta de {self.vendedor.nombre} por ${self.monto} el {self.fecha_venta}"
    