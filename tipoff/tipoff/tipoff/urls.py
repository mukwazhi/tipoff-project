# coding=utf-8
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import reporting.views
import displays.views
import contact.views
import django.contrib.auth.views
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', reporting.views.home, name='home'),
    url(r'^report_form/', reporting.views.report_form, name='report_form'),
    url(r'^article/(?P<slug>[\w-]+)/$', displays.views.article, name='article'),
    url(r'^detailed_report/(?P<report_no>[\w-]+)/$', reporting.views.detailed_report, name='detailed_report'),
    url(r'^report_list/$', reporting.views.report_list, name='report_list'),
    url(r'^analysis/', reporting.views.analysis, name='analysis'),
    url(r'^about/', reporting.views.about, name='about'),
    url(r'^track/', reporting.views.track, name='track'),
    url(r'^thanks/', reporting.views.thanks, name='thanks'),
    # ----------------------Admin-user-logging--------------------------------#
    url(r'^login/$', django.contrib.auth.views.login, name='login',  ),
    url(r'^accounts/logout/$', django.contrib.auth.views.logout, name='logout', kwargs={'next_page': '/login'}),
    # ---------------------------PDF-------------------------------------------#
    # url(r'^print_users/$', reporting.views.print_users, name='print_users'),
    url(r'^some_view/(?P<report_no>[\w-]+)/$', reporting.views.some_view, name='some_view'),
    # -----------------------------contact--------------------------------------#
    url(r'^contact/$', contact.views.contact, name='contact'),
    url(r'^captcha/', include('captcha.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
