from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from fusion.incidents.views import (
    domestic,
    international,
    nc4,
    search,
    search_reg,
    details_reg,
    details_reg_vw,
    details,
    kml,
    csv_out)
from django.contrib.auth.views import LoginView, LogoutView

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

urlpatterns = [
    path('facilities/domestic/', domestic),
    path('facilities/international/', international),
    path('facilities/nc4/', nc4),
#    path('incidents/domestic/', 'current_incidents', domestic_incidents),
#    path('incidents/international/', 'current_incidents', international_incidents),
#    (r'weeklystats/$', weekly_stats),
    path('reporting/', search),
    path('reporting/reg/', search_reg),
    path('reporting/reg/details/', details_reg),
    path('reporting/reg/details_vw/', details_reg_vw),
    path('reporting/details/', details),
    path('reporting/google_earth/', kml),
    path('reporting/excel/', csv_out),
    path('login/', LoginView.as_view() ,name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
#    (r'images/$', images)
    # (r'^reporting/', include('reporting.foo.urls')),
    # (r'^admin/', include('django.contrib.admin.urls')),
]
