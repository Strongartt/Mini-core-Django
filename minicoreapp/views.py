from django.shortcuts import render
from .models import Venta, Regla
from decimal import Decimal
from collections import defaultdict

def filtrar_ventas(request):
    resultados = []
    fecha_inicio = None
    fecha_fin = None

    if request.method == 'POST':
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')

        if fecha_inicio and fecha_fin:
            ventas = Venta.objects.filter(fecha_venta__range=[fecha_inicio, fecha_fin])

            # Sumar ventas por vendedor
            total_por_vendedor = defaultdict(Decimal)

            for venta in ventas:
                vendedor = venta.Vendedor
                total_por_vendedor[vendedor] += venta.monto

            # Obtener todas las reglas ordenadas por monto_minimo ASC
            reglas = Regla.objects.order_by('monto_minimo')

            for vendedor, total_ventas in total_por_vendedor.items():
                porcentaje_aplicado = 0

                # Buscar la regla correcta según el total vendido
                for regla in reglas:
                    if total_ventas >= regla.monto_minimo:
                        porcentaje_aplicado = regla.porcentaje

                comision = total_ventas * (Decimal(porcentaje_aplicado) / Decimal('100'))

                resultados.append({
                    'vendedor': vendedor.nombre,
                    'total_ventas': total_ventas,
                    'porcentaje': porcentaje_aplicado,
                    'comision': round(comision, 2)
                })

    return render(request, 'minicoreapp/filtro_ventas.html', {
        'resultados': resultados,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin
    })
