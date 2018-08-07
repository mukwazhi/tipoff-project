from django.contrib import admin
from .models import IncidentReport,Tracking


class IncidentReportAdmin(admin.ModelAdmin):
    list_display = ['report_no', 'nature_of_report','station', 'date_of_incident']

class TrackingAdmin(admin.ModelAdmin):
    list_display = ['report_number', 'tracking_number','report_status']


admin.site.register(IncidentReport, IncidentReportAdmin)
admin.site.register(Tracking, TrackingAdmin)
