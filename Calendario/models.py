from django.db import models
from django.urls import reverse
from Pacientes.models import Paciente
from django.core.exceptions import ValidationError
from datetime import datetime

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

    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:    #edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end: #outter limits
            overlap = True
        return overlap

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('La hora final debe ser posterior a la hora inicial')

        events = Event.objects.filter()
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                    raise ValidationError(
                        'Ya hay otra cita en esta hora: ' +
                            event.start_time.strftime(r"%m/%d/%Y, %H:%M:%S")+ '---' + event.end_time.strftime(r"%m/%d/%Y, %H:%M:%S"))