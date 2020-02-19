from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings
from incidents.views import *
from auth.views import user_login, user_logout

domestic_incidents = {
    'comps': "country='United States'",
    'filename': 'International-Incidents.kmz',
    'title': 'Current Domestic Incidents',
}

international_incidents = {
    'comps': "country<>'United States'",
    'filename': 'International-Incidents.kmz',
    'title': 'Current International Incidents',
}

urlpatterns = patterns(
    'fusion.incidents.views',
    (r'facilities/domestic/', domestic),
    (r'facilities/international/', international),
    (r'facilities/nc4/', nc4),
    (r'incidents/domestic/', 'current_incidents', domestic_incidents),
    (r'incidents/international/', 'current_incidents', international_incidents),
#    (r'weeklystats/$', weekly_stats),
    (r'reporting/$', search),
    (r'reporting/reg/$', search_reg),
    (r'reporting/reg/details/', details_reg),
    (r'reporting/reg/details_vw/', details_reg_vw),
    (r'reporting/details/', details),
    (r'reporting/google_earth/', kml),
    (r'reporting/excel/', csv_out),
    url(r'login/', user_login, name='login'),
    url(r'logout/', user_logout, name='logout'),
#    (r'images/$', images)
    # (r'^reporting/', include('reporting.foo.urls')),
    # (r'^admin/', include('django.contrib.admin.urls')),
) + static('script', document_root=settings.STATIC_JS_ROOT)

urlpatterns += static('style', document_root=settings.STATIC_CSS_ROOT)
urlpatterns += static('images', document_root=settings.STATIC_IMAGES_ROOT)
urlpatterns += static('icons', document_root=settings.STATIC_ICONS_ROOT)