import string
from random import *

from django.db import models


def report_number():
    last_report = IncidentReport.objects.all().order_by("id").last()
    if not last_report:
        return 'FRN0001'
    report_no = last_report.report_no
    report_int = int(report_no.split('FRN')[-1])
    width = 4
    new_report_int = report_int + 1
    formatted = (width - len(str(new_report_int))) * '0' + str(new_report_int)
    new_report_no = 'FRN' + str(formatted)
    return new_report_no


class IncidentReport(models.Model):
    NATURE_OF_REPORT = (
        ("Smuggling", "Smuggling"),
        ('Fraud', 'Fraud'),
        ('Extortion', 'Extortion'),
        ('Bribery', 'Bribery'),
        ('Corruption', 'Corruption'),
        ('Misappropriation', 'Misappropriation'),
        ('Other', 'Other'),
        ("Nepotism", 'Nepotism'),
        ('Procurement Fraud', 'Procurement Fraud'),
        ('Racism', 'Racism'),
        ('Theft', 'Theft'),
        ('Sexual Harassment', 'Sexual Harassment'),
        ('Criminal', 'Criminal'),
        ('Unethical', 'Unethical'),
        ('Other', 'Other')
    )

    STATION = (
        ('Harare', 'Harare'),
        ("Victoria Falls", "Victoria Falls"),
        ('Bulawayo', 'Bulawayo'),
        ('Kariba', 'Kariba'),
        ('Other', 'Other'),
    )
    # ---------------------Background--information--------------------------------------------#
    report_no = models.CharField(max_length=500, default=report_number, null=True, blank=True)
    nature_of_report = models.CharField(default=0, max_length=20, choices=NATURE_OF_REPORT)
    station = models.CharField(default=0, max_length=20, choices=STATION)
    other_station = models.CharField(max_length=100, null=True, blank=True)
    date_of_incident = models.DateField()
    time_of_incident = models.TimeField()
    location_of_incident = models.CharField(max_length=100, null=False, blank=False)
    # specific_location = models.CharField(max_length=100)
    # ------------Parties-involved---------------------#
    name_of_party_involved = models.CharField(max_length=100, null=True, blank=True)
    organisation = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=100, null=True, blank=True)
    # ---------------------------Incident--Detail---------------------------------------------------#
    incident_detail = models.TextField(max_length=3000, null=False, blank=False)
    # ----------------------------Upload--Supporting--evidence-----------------------------------------------#
    upload_evidence = models.FileField(upload_to='tipoff_media/', null=True, blank=True)
    # ----------------------------contact--details--------------------------------------------------#
    Full_Name = models.CharField(max_length=100, null=True, blank=True)
    Position_Title = models.CharField(max_length=100, null=True, blank=True)
    Phone_no = models.CharField(max_length=100, null=100, blank=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.report_no

def random_code():
    characters = string.ascii_letters + string.digits
    password = "".join(choice(characters) for x in range(randint(4, 12)))
    return password

class Tracking(models.Model):
    STATUS = (
        ('Evaluation', 'Evaluation'),
        ("Investigation", "Investigation"),
        ('Disciplinary ', 'Disciplinary'),
        ('Insufficient', 'Insufficient Evidence'),
        ('Closed', 'Closed'),
    )
    report_number = models.ForeignKey(IncidentReport, on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=11, default=random_code(), null=True, blank=True,unique=True)
    report_status = models.CharField(choices=STATUS,max_length=20, null=True)
    additional_details = models.TextField(max_length=3000, null=True, blank=True)





