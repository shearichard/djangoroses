"""roses URL Configuration"""

from django.conf.urls import include, url
from django.contrib import admin

from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required, permission_required
from django.conf.urls.i18n import i18n_patterns

from rosebiology.views import HomePageView, SpeciesList, SpeciesDetailView, SpeciesCreate, SpeciesDelete, SpeciesUpdate    
from rosebiology import views

#Initial set of urls we *don't*
#want translated, this includes the 
#django provided view which does swiching based
#on a POST request and would also include robots.txt
#if we had one.
urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
]
 
#Subsequent set of urls we *do*
#want translated
urlpatterns += i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^species/$', SpeciesList.as_view(), name='specieslist'),
    url(r'^species/add/$', SpeciesCreate.as_view(), name='species_add'),
    url(r'^species/delete/(?P<pk>[0-9]+)/$', SpeciesDelete.as_view(), name='species_delete'),
    url(r'^species/update/(?P<pk>[0-9]+)/$', SpeciesUpdate.as_view(), name='species_update'),
    url(r'^species/display/(?P<pk>[-\w]+)/$', SpeciesDetailView.as_view(), name='species_display'),
    url(r'^species/restricted/$', views.this_is_restricted, name='this_is_restricted'),
    url(r'^species/restrictedlots/$', views.this_is_even_more_restricted, name='this_is_even_more_restricted'),
    url(r'^species/register/$', views.register, name='register'),
    url(r'^species/login/$', views.user_login, name='login'),
    url(r'^species/logout/$', views.user_logout, name='logout'),
    url(r'^species/set_timezone/$', views.set_timezone, name='set_timezone'),
)
