from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import CalendarView, event, eliminarEvent

app_name = 'Calendario'
urlpatterns = [
    url('calendario/', CalendarView.as_view(), name='calendar'),
    url('citas/nuevo/', event, name='event_new'),
	url('citas/editar/(?P<event_id>\d+)/', event, name='event_edit'),
    url('citas/eliminar/(?P<event_id>\d+)/',eliminarEvent,name='delete_event')
	
]