from django.db import models
from django.urls import reverse
from Pacientes.models import Paciente

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    cal_paciente = models.ForeignKey(Paciente,on_delete=models.CASCADE)

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'