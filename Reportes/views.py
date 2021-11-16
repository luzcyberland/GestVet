from datetime import date
from django.db.models.fields import FloatField
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.db.models.functions import Coalesce
from django.db.models import Sum
from Facturacion.models import DetalleFactura, Factura
from datetime import datetime



from Reportes.forms import ReportForm

# Create your views here.
class ReportesViews(TemplateView):
    template_name = 'reportes/reportes.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                detalles = DetalleFactura.objects.all()
                search = Factura.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(fecha__range=[start_date, end_date]).exclude(estado_factura='Pendiente')
                for s in search:
                    data.append([
                       s.nro_factura,
                       s.cliente.nombre_cliente,
                       s.fecha.strftime(r'%Y-%m-%d'),
                       format(s.total, '.2f')
                    ])

                total = search.aggregate(r=Coalesce(Sum('total',output_field=FloatField()), 0.00)).get('r')

                data.append([
                    '---',
                    '---',
                    '---',
                    format(total, '.2f'),
                ])
                print('fecha:',type(data[0][2]), data[0][2])
                print('start-end:',type(start_date), start_date)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            print('Error:',e, end_date,end_date)
            pass
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reporte_list'] = reverse_lazy('reportes')
        context['form'] = ReportForm()
        return context

