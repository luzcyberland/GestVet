from django.conf.urls import url
from . import views

app_name = 'Calendario'
urlpatterns = [
    url('calendario/', views.CalendarView.as_view(), name='calendar'),
    url('citas/nuevo/', views.event, name='event_new'),
	url('citas/editar/(?P<event_id>\d+)/', views.event, name='event_edit'),
]