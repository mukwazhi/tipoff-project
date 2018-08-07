from tracemalloc import Frame
from turtle import Canvas

from django.core.checks import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
from django.shortcuts import render


from .forms import IncidentForm

from displays.models import Information, Brand, Article
from .models import IncidentReport, Tracking
from django.contrib.auth.decorators import login_required



def home(request):
    information = Information.objects.all()
    brand = Brand.objects.all()
    article_blog = Article.objects.all()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    print(num_visits)

    context = {
        "information": information,
        'brand': brand,
        'article_blog': article_blog
    }
    return render(request, 'home.html', context)


def about(request):
    information = Information.objects.all()
    brand = Brand.objects.all()
    article_blog = Article.objects.all()
    context = {
        "information": information,
        'brand': brand,
        'article_blog': article_blog
    }
    return render(request, 'about.html', context)


def report_form(request):
    # report form
    # brand = Brand.objects.all()
    incidentform = IncidentForm()
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            incidentform = form.save(commit=False)
            incidentform.save()
            Tracking.objects.create(report_number=incidentform)
            tracking_token = Tracking.objects.all().last().id
            request.session['tracking_token'] = tracking_token
            return HttpResponseRedirect('/thanks/')
    else:
        
        context = {
            'incidentform': incidentform,
            # 'brand': brand
        }
        return render(request, 'report_form.html', context)

    context = {
        'incidentform': incidentform,
        # 'brand': brand
    }
    return render(request, 'report_form.html', context)

@login_required(login_url='/accounts/login/')
def detailed_report(request, report_no):
    report = IncidentReport.objects.get(report_no=report_no)
    context = {
        'report': report
    }
    return render(request, 'detailed_report.html', context)


@login_required(login_url='/accounts/login/')
def report_list(request):
    report = IncidentReport.objects.all()
    context = {
        'report': report
    }
    return render(request, 'report_listView.html', context)

@login_required(login_url='/accounts/login/')
def analysis(request):
    report = IncidentReport.objects.all().count
    summary = IncidentReport.objects.values('nature_of_report').order_by().annotate(Count('nature_of_report'))
    print(summary)
    # location = IncidentReport.objects.values('location_of_occurence').order_by().annotate(Count('location_of_occurence'))
    station = IncidentReport.objects.values('station').order_by().annotate(Count('station'))
    print(station)
    context = {
        'report': report,
        'summary': summary,
        # 'location': location,
        'station': station,
    }
    return render(request, 'Analysis.html', context)

def track(request):
    q = request.GET.get('q')
    if  q:
        try:
            tracking = Tracking.objects.get(tracking_number=q)
            return render(request,'tracker.html',{'tracking':tracking})
        except ObjectDoesNotExist:
            invalid = "Please enter a valid code"
            return render(request, 'tracking_access.html', {"invalid": invalid})
    else:

        return render(request, 'tracking_access.html', {})

def thanks(request):
    if request.session.session_key:
        tracking = Tracking.objects.all().last()
        return render(request, 'thanks.html',{"tracking":tracking})

    else:
        return HttpResponseRedirect('/report_form/')




# -----------------------PDF-Generator--------------------------------#
from reportlab.pdfgen import canvas
from django.http import HttpResponseRedirect
from reportlab.pdfgen import canvas
from reportlab.pdfgen.canvas import Canvas
from django.http import HttpResponse
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet

from reportlab.lib.units import inch
from io import BytesIO
import datetime


def some_view(request, report_no):
        # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    report = IncidentReport.objects.get(report_no=report_no)

    styles = getSampleStyleSheet()
    styleN = styles['Normal']
    styleH = styles['Heading1']
    story = []
        # add some flowables
    story.append(Paragraph("Fraud Report", styleH))
    story.append(Paragraph("Report No :  " + report.report_no, styleN))
    story.append(Paragraph("Date of Incident :  " + str(report.date_of_incident), styleN))
    story.append(Paragraph("Time of incident : " + str(report.time_of_incident), styleN))
    story.append(Paragraph("Station  : " + report.station, styleN))
    story.append(Paragraph("Specific location  : " + report.specific_location, styleN))
        # ------------Parties-involved---------------------#
    story.append(Paragraph("Parties Involved", styleH))
    story.append(Paragraph("Name of party involved      :" + report.name_of_party_involved, styleN))
    story.append(Paragraph("organisation    : " + report.organisation, styleN))
    story.append(Paragraph("gender    : " + report.gender, styleN))
    story.append(Paragraph("Role     : " + report.role, styleN))
        # ---------------------------Incident--Detail---------------------------------------------------#
    story.append(Paragraph("Incident Detail", styleH))
    story.append(Paragraph("Incident of detail :  " + report.incident_detail, styleN))
        # ----------------------------contact--details--------------------------------------------------#
    story.append(Paragraph("Contact Details", styleH))
    story.append(Paragraph("Name :  " + report.Full_Name, styleN))
    story.append(Paragraph("Position Title :  " + report.Position_Title, styleN))
    story.append(Paragraph("Phone Number:  " + report.Phone_no, styleN))
    story.append(Paragraph("Email:  " + report.email, styleN))

    c = Canvas(response)
    f = Frame( inch, inch, 7 * inch, 10 * inch, )
    f.addFromList(story, c)
    c.save()

    return  response

