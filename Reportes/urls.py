from django.urls import path 
from django.contrib.auth.decorators import login_required

from Reportes.views import ReportesViews

urlpatterns = [
    path('vista_reportes/', login_required(ReportesViews.as_view()), name="reportes")]