# -*- coding: utf-8 -*-
import csv
import json
import logging
import os

from datetime import datetime
from io import BytesIO
from zipfile import ZipFile

from django.db import connection
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.conf import settings
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from fusion.incidents.comp import make_comp, Col, DateCol, AnalystCol
from fusion.incidents.models import Attachments, Facility


logger = logging.getLogger(__name__)

rt_conditions_cols = {
    'inc': Col('Incident Category', 'acti.incidentcategory'),
    'inctype': Col('Incident Type', 'acti.incidenttype'),
    'dateoc': DateCol('Date Occurred', 'acti.dateoccurred'),
    'update': DateCol('Updated Date', 'acti.updateddate'),
    'city': Col('City', 'acti.city'),
    'cnty': Col('County', 'acti.county'),
    'st': Col('State', 'acti.stateprovince'),
    'cntry': Col('Country', 'acti.country'),
    'reg': Col('Region', 'acti.region'),
    'int': Col('Internal Comments', 'acti.comments'),
    'sev': Col('Severity', 'acti.severity'),
    'annum': AnalystCol('Analyst', "replace(acti.createdby,' ','')"),
    'desc': Col('Description', 'acti.description'),
    'intcom': Col('Conversationlog', 'acti.conversationlog'),
    'source': Col('Confirmation source', 'acti.infosource'),
    'quality': Col('Confirmation quality', 'acti.infoquality'),
    'program': Col('Program', 'acti.program'),
}

regional_conditions_cols = {
    'title': Col('Title', 'di.itemtitle'),
    'severity': Col('Severity', 'di.ItemSignificance'),
    'dateoc': DateCol('Date Occurred', 'di.CREATEDDATE'),
    'dateexp': DateCol('Expiration Date', 'di.ITEMEXPIRATIONDATE'),
    'city': Col('City', 'di.city'),
    'cntry': Col('Country', 'di.country'),
    'region': Col('Region', 'tl.esaregion'),
    'event': Col('Special Event', 'di.itemevent'),
    'body': Col('Body', 'di.ItemText'),
}

vw_conditions_cols = {
    'title': Col('Title', 'subject'),
    'severity': Col('Severity', 'severity'),
    'dateoc': DateCol('Date Occurred', 'CREATEDDATE'),
    'dateexp': DateCol('Expiration Date', 'updatedby'), # This wont work with any condition
    'city': Col('City', 'city'),
    'cntry': Col('Country', 'valuelabel'),
    'event': Col('Special Event', 'updatedby'),
    'body': Col('Body', 'updatedby'),
}


FAC_COLS = [
    'facilityname', 'createdby', 'createddate', 'latitude', 'longitude',
    'street', 'city', 'county', 'district', 'stateprovince', 'region',
    'country', 'updatedby', 'updateddate', 'facilityid'
]


def getFacilities():
    return Facility.objects.exclude(
        createdby__in=('Taylor Obitz', 'Luis Garcia'),
        createdby__contains='DEMO'
    ).order_by('updateddate')


def nonNC4Facilities():
    return getFacilities().exclude(facilityname__contains='NC4')


fac_query = """
SELECT incidentcategory, COUNT(DISTINCT incidentid) num
FROM fusion.tbl_incactivity
WHERE country %s 'United States'
  AND createddate BETWEEN TO_TIMESTAMP('%s', 'YYYY-MM-DD HH24:MI')
      AND TO_TIMESTAMP('%s', 'YYYY-MM-DD HH24:MI')
  AND activitystatus <> 'ARCHIVED'
GROUP BY incidentcategory
ORDER BY incidentcategory
"""

latest_cols = [
    'incactivityid',  'incidentid',  'incidentcategory', 'incidenttype',
    'updateddate',  'severity',  'city', 'stateprovince',  'country',  'gist',
    'latitude',  'longitude', 'dateoccurred', 'description', 'infosource',
    'infoquality', 'county', 'updatedby', 'street', 'postal', 'approximate',
    'commentflag', 'conversationlog', 'notifyrule',
]

vw_cols = [
    'doclibid', 'createddate', 'updateddate', 'subject', 'description',
    'publishdate', 'effectivedate', 'doctype', 'severity', 'docattachid',
    'label', 'country', 'city', 'region', 'wktgeoms', 'valuelabel'
]

regional_cols = [
    'itemid', 'createddate', 'itemsignificance', 'country', 'itemcountryline',
    'itemtitle', 'synopsis', 'itemexpirationdate', 'itemevent', 'city',
    'latitude', 'longitude', 'region', 'itemsummary', 'itemtext',
    'itemattributetoactor', 'itemcategory', 'itemassessment'
]

regional_cols_only = [
    'itemid', 'createddate', 'itemsignificance', 'country', 'itemcountryline',
    'itemtitle', 'synopsis',  'itemtype'
]

regional_cols_count_only = ['count(*)']

if os.name == 'posix':
    kmz_images_path = '/app/fusion/'
else:
    kmz_images_path = 'D:/django/fusion/'

kmz_cols = [
    'description', 'severity', 'incidenttype', 'incidentcategory', 'latitude',
    'longitude', 'dateoccurred', 'gist', 'street', 'city', 'stateprovince',
    'postal', 'country', 'infosource'
]


def makeCSVResponse(rows, filename, cols=FAC_COLS):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % filename
    writer = csv.writer(response)
    writer.writerow([col.upper() for col in cols])
    for row in rows:
        writer.writerow([getattr(row, col) for col in cols])
    return response

#cache = lambda delay:lambda func:cache_page(func, delay)

#@cache(60*60*12)
@login_required
@csrf_exempt
def domestic(req):
    return makeCSVResponse(nonNC4Facilities().filter(country='United States'),
                           'domestic')

#@cache(60*60*12)
@login_required
@csrf_exempt
def international(req):
    return makeCSVResponse(
        nonNC4Facilities().exclude(country='United States'), 'international'
    )


#@cache(60*60*12)
@login_required
@csrf_exempt
def nc4(req):
    return makeCSVResponse(
        getFacilities().filter(facilityname__contains='NC4'),
        'NC4_Facilities'
    )


class PostRow(object):
    def __init__(self, post, id):
        self.post = post
        self.id = id

    def __getitem__(self, name):
        return self.post[name+self.id]

    def get(self, key, default):
        return self.post.get(key, default)

    def getlist(self, name):
        return self.post.getlist(name+self.id)


def makeRow(post, id):
    return PostRow(post, id)


def makeComps(post, conditions_cols):
    l = []
    for id in post['ids'].split(','):
        row = makeRow(post, id)
        if row['type'] in conditions_cols:
            l.append(make_comp(row, post, conditions_cols))

    if (post['searchtype'] != 'regional' and
            'cybertech' in post and
            post['cybertech'] == '1'):
        l.append("acti.updatedby LIKE 'CyberTech%'")
    elif (post['searchtype'] != 'regional' and
            'nc4' in post and
            post['nc4'] == '1'):
        l.append("acti.updatedby LIKE 'NC4%'")
    return l


class FormattedDateTime(datetime):
    def __new__(self, dt):
        return datetime.__new__(
            self, dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second,
            dt.microsecond, dt.tzinfo)

    def __str__(self):
        return self.strftime('%m/%d/%Y %H:%M')


class RowDict(dict):
    def __init__(self, row, cols):
        for name, val in zip(cols, row):
            self[name] = val
        self['style'] = '%s_%s' % ('a', 'b')

    def __setitem__(self, name, value):
        if type(value) is datetime:
            dict.__setitem__(self, name, FormattedDateTime(value))
        elif hasattr(value, 'read'):
            dict.__setitem__(self, name, value.read())
        else:
            dict.__setitem__(self, name, value)

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __hasattr__(self, name):
        return name in self


def makeObjs(cursor, cols):
    return [RowDict(row, cols) for row in cursor]


def joinVWComps(comps):
    if not comps:
        return ''
    else:
        return ' AND ' + ' AND '.join(comps)


def getRegionalObjects(post, cols=regional_cols):
    comps = makeComps(post,regional_conditions_cols)
    #post['vw']='true';
    comps_vw = makeComps(post,vw_conditions_cols)
    dict = {'itemtitle': 'subject', 'ItemSignificance': 'severity', 'CREATEDDATE': 'CREATEDDATE'}
    f = open(os.path.join(settings.BASE_DIR, 'RegionalAllObjects.txt'), 'w')
    #f.write("getallobj " + comps[0])
    has_region = False
    for compp in comps:
        if 'esaregion' in compp:
            region_field, region_value = compp.split('=')
            f.write("Region " + compp)
            f.write("Region_val " + region_value)
            has_region = True

    if has_region:
        query = """
        (
            SELECT TO_CHAR(itemid) as itemid, createddate, itemsignificance,
            country, itemcountryline, itemtitle, synopsis,
            'dailyitems' as itemtype
            FROM transecur.dailyitems di
            WHERE di.itemid IN (
                Select DISTINCT di.itemid
                FROM transecur.dailyitems di, TranSecur.itemLocations il,
                    transecur.locations tl
                WHERE di.primary_id=il.dailyitems_key
                AND il.locationid=tl.locationid AND %s
            )
            UNION
            SELECT doclibid as itemid, createddate, severity as itemsignificance,
            l.country as country, attrs.valuelabel as itemcountryline,
            subject as itemtitle, '' as synopsis, doctype as itemtype
            FROM vw_documents, table(vw_documents.locations) l,
                table(vw_documents.nc4attrs) attrs
            WHERE (doctype='SEB' OR doctype='SR')
            AND attrs.numval IN (
                SELECT locationid from transecur.locations where esaregion=%s
            ) %s
        ) ORDER BY CREATEDDATE DESC
        """
        query %= (' AND '.join(comps), ''.join(region_value),joinVWComps(comps_vw))

    else:
        query = """(SELECT TO_CHAR(itemid) as itemid, createddate, itemsignificance, country, itemcountryline, itemtitle, synopsis, 'dailyitems' as itemtype
        FROM transecur.dailyitems di WHERE %s
        UNION
        select doclibid as itemid, createddate, severity as itemsignificance, l.country as country, attrs.valuelabel as itemcountryline, subject as itemtitle,
        '' as synopsis, doctype as itemtype
        from vw_documents,table(vw_documents.locations) l, table(vw_documents.nc4attrs) attrs WHERE (doctype='SEB' OR doctype='SR') %s) ORDER BY CREATEDDATE DESC"""
        query %= (' AND '.join(comps), joinVWComps(comps_vw))

        #query_di_region = """(SELECT TO_CHAR(itemid) as itemid, createddate, itemsignificance, country, itemcountryline, itemtitle, synopsis, 'dailyitems' as itemtype
        #FROM transecur.dailyitems di WHERE %s"""
    #query_di_region = """Select DISTINCT di.itemid FROM transecur.dailyitems di, TranSecur.itemLocations il, transecur.locations tl
    #        WHERE di.primary_id=il.dailyitems_key AND il.locationid=tl.locationid AND tl.esaregion='Middle East'"""
    #query_vw =     """ UNION select doclibid as itemid, createddate, severity as itemsignificance, l.country as country, attrs.valuelabel as itemcountryline, subject as itemtitle,
    #   '' as synopsis, doctype as itemtype
    #    from vw_documents,table(vw_documents.locations) l, table(vw_documents.nc4attrs) attrs WHERE (doctype='SEB' OR doctype='SR') %s) ORDER BY CREATEDDATE DESC"""

    #query =''.join([query_di_region, query_vw])
        #select doclibid, l.country, l.city from fusion.vw_documents, table(fusion.vw_documents.locations) l;
        #select  DOCLIBID, l.valuelabel from fusion.vw_documents, table(fusion.vw_documents.nc4attrs) l ORDER BY UPDATEDDATE DESC



    cursor = connection.cursor()
    # query_di_region %= (' AND '.join(comps))
    # for xx in regional_conditions_cols:
    #     f.write(xx))
    # f.write("post " + json.dumps(post))
    f.write("getallobj " + query)
    cursor.execute("""begin security_mgr.namelogin('nc4admin'); end;/""")
    cursor.execute(query.replace('%', '%%'))
    f.close()
    return makeObjs(cursor, cols), query


def getObjects(post, cols=latest_cols):
    comps = makeComps(post, rt_conditions_cols)
    if 'scope_limitation' in post and post['scope_limitation'] != 'all':
        return getLatestObjects(post, cols, comps)
    else:
        my_dict = {}
        allActivityObjs, query = getAllObjects(post, cols, comps)
        if 'incident_history' in post and post['incident_history'] == '1':
            for obj in allActivityObjs:
                activity_id = obj['incactivityid']
                my_dict[activity_id] = 1

            allIncActivitiesObjs, query = getAllIncObjects(post, cols, comps)
            f = open(os.path.join(settings.BASE_DIR,
                                  'DifferentialActivities.txt'), 'w')

            for obj in allIncActivitiesObjs:
                activity_id = obj['incactivityid']
                if activity_id not in my_dict:
                    obj['out_window'] = 1
                    f.write("outside " + str(obj['incidentid']))
                    f.write("\n")
                else:
                    f.write(str(obj['incidentid']))
                    f.write("\n")
            return allIncActivitiesObjs, query
        else:
            return allActivityObjs, query


def getAllObjects(post, cols, comps):
    query = """
        SELECT %s FROM tbl_incactivity acti, tbl_incidents inci
        WHERE inci.incidentid = acti.incidentid
        AND %s
        ORDER BY inci.createddate DESC,
                 acti.updateddate DESC,
                 acti.incactivityid DESC
    """

    query %= (', '.join(['acti.'+c+" "+c for c in cols]), ' AND '.join(comps))
    print(query)
    cursor = connection.cursor()
    # cursor.execute("begin security_mgr.naMELOGIN('nc4admin'); commit; end;")
    cursor.execute(query.replace('%', '%%'))
    return makeObjs(cursor, cols), query


def getAllIncObjects(post, cols, comps):
    query = """
    SELECT %s FROM tbl_incactivity acti_outer, tbl_incidents inci
    WHERE inci.incidentid = acti_outer.incidentid
    AND acti_outer.INCIDENTID IN (
        SELECT DISTINCT(INCIDENTID)
        FROM tbl_incactivity acti WHERE  %s
    ) ORDER BY inci.createddate DESC,
               acti_outer.updateddate DESC,
               acti_outer.incactivityid DESC
    """
    query %= (', '.join(['acti_outer.'+c+" "+c for c in cols]), ' AND '.join(comps))
    cursor = connection.cursor()
    # cursor.execute("begin security_mgr.naMELOGIN('nc4admin'); commit; end;")
    cursor.execute(query.replace('%', '%%'))
    return makeObjs(cursor, cols), query


def getLatestObjects(post, cols, comps):
    query = """
    SELECT %s FROM tbl_incactivity acti, (%s) maxinc, tbl_incidents inci
    WHERE inci.incidentid = acti.incidentid
    AND inci.incidentid = maxinc.incidentid
    AND (maxinc.incactivityid=acti.incactivityid
    AND maxinc.incidentid=acti.incidentid)
    AND acti.dateoccurred <= CURRENT_TIMESTAMP
    ORDER BY acti.createddate DESC,
             acti.updateddate,
             acti.incactivityid
    """
    inner_final = """
    SELECT MAX(incactivityid) incactivityid, incidentid
    FROM tbl_incactivity WHERE %s GROUP BY incidentid
    """

    inner_initial = """
    SELECT MIN(incactivityid) incactivityid, incidentid
    FROM tbl_incactivity WHERE %s GROUP BY incidentid
    """

    # Check here what is selected by the User.
    if 'scope_limitation' not in post or post['scope_limitation'] == 'final':
        inner = inner_final
        inner %= ' AND '.join([c.replace("acti.", "") for c in comps])
    elif 'scope_limitation' in post and post['scope_limitation'] == 'initial':
        inner = inner_initial
        inner %= ' AND '.join([c.replace("acti.", "") for c in comps])
    elif 'scope_limitation' in post and post['scope_limitation'] == 'both':
        inner_initial %= ' AND '.join([c.replace("acti.", "") for c in comps])
        inner_final %= ' AND '.join([c.replace("acti.", "") for c in comps])
        inner = inner_initial + " UNION " + inner_final

    # inner %= ' AND '.join(comps)
    query %= (', '.join(['acti.'+c for c in cols]), inner)
    cursor = connection.cursor()
    # cursor.execute("begin security_mgr.naMELOGIN('nc4admin'); commit; end;")
    cursor.execute(query.replace('%', '%%'))
    return makeObjs(cursor, cols), query


@login_required
@csrf_exempt
def search_reg(request):
    if request.method == 'GET':
        return render(request, 'incidents/reporting/search_reg.html', {})
    types = {
        'Search': html_reg,
        'Excel': csv_out,
        'Google Earth': kml,
    }

    is_refine = request.POST.get('refine') == 'yes'
    if is_refine:
        criteria = request.POST.get('search_criteria')
        print(criteria)
        return render(request, 'incidents/reporting/search_reg.html', {
            'criteria': criteria,
            'is_refine': is_refine
        })
    else:
        for id in request.POST['ids'].split(','):
            if not request.POST.get('field'+id, None):
                # Possible XSS attack but it's internal (bad assumption?)
                return render(request, 'incidents/reporting/search_reg.html',
                              request.POST)
        return types[request.POST['type']](request)


@login_required
@csrf_exempt
def search(request):
    if request.method == 'GET':
        return render(request, 'incidents/reporting/search.html', {})
    types = {
        'Search': html,
        'Excel': csv_out,
        'Google Earth': kml,
    }

    is_refine = request.POST.get('refine') == 'yes'
    if is_refine:
        criteria = request.POST.get('search_criteria')
        print(criteria)
        return render(request, 'incidents/reporting/search.html', {
            'criteria': criteria,
            'is_refine': is_refine
        })
    else:
        for id in request.POST['ids'].split(','):
            if not request.POST.get('field'+id, None):
                # Possible XSS attack but it's internal (bad assumption?)
                return render(request, 'incidents/reporting/search.html',
                              request.POST)
        return types[request.POST['type']](request)


@login_required
@csrf_exempt
def html(request):
    objs, query = getObjects(request.POST)
    currInc = None
    isOff = True
    total_rows = 0
    total_incidents = 0
    for row in objs:
        if row.incidentid != currInc:
            isOff = not isOff
            currInc = row.incidentid
            total_incidents += 1
        row.off = isOff
        total_rows += 1

    post_data = {}
    for key, value in request.POST.lists():
        if len(value) == 1:
            post_data[key] = value[0]
        if len(value) > 1:
            post_data[key] = value
    return render(request, 'incidents/reporting/results.html', {
        'criteria': json.dumps(post_data),
        'total_rows': total_rows,
        'total_incidents': total_incidents,
        'objs': None if 'statistics_only' in post_data and
        post_data['statistics_only'] == "1" else objs
    })


@login_required
@csrf_exempt
def html_reg(request):
    post_data = {}
    for key, value in request.POST.lists():
        if len(value) == 1:
            post_data[key] = value[0]
        if len(value) > 1:
            post_data[key] = value

    objs, query = getRegionalObjects(
        request.POST,
        regional_cols_count_only if 'statistics_only' in post_data and
        post_data['statistics_only'] == "1" else regional_cols_only
    )

    prev_row = None
    isOff = True
    total_rows = 0
    total_incidents = 0
    duplicates = []
    f = open(os.path.join(settings.BASE_DIR, 'Django_values.txt'), 'w')
    for index, row in enumerate(objs):
        if row.itemtype == 'SEB' or row.itemtype == 'SR':
            f.write("\n NEW LINE " + str(row.itemcountryline))
            if prev_row is not None and row.itemid == prev_row.itemid:
                duplicates.append(prev_row)
                # new_country = str(row.country) + str(prev_row.country)
                # f.write("new_country " + new_country)
                # prev_countryline = prev_row.itemcountryline \
                #     if prev_row.country != prev_row.itemcountryline else ""
                row['itemcountryline'] = row.itemcountryline \
                    if row.country != row.itemcountryline else ""
                seperator = ' , ' if row.itemcountryline != "" else ' '
                row['itemcountryline'] = row.itemcountryline + seperator + \
                    prev_row.itemcountryline
                f.write("\n " + str(row.itemcountryline))
            else:
                row['itemcountryline'] = row.itemcountryline \
                    if row.country != row.itemcountryline else ""

        prev_row = row
        objs[index] = row

    for x in duplicates:
        objs.remove(x)
    f.close()

    return render(request, 'incidents/reporting/results_reg.html', {
        'criteria': json.dumps(post_data),
        'total_rows': objs[0]['count(*)'] if 'statistics_only' in post_data and
        post_data['statistics_only'] == "1" else len(objs),
        'objs': None if 'statistics_only' in post_data and
        post_data['statistics_only'] == "1" else objs
    })


@login_required
@csrf_exempt
def kml(req):
    cols = latest_cols

    placemarks, query = getLatestObjects(
        req.POST, cols, makeComps(req.POST, rt_conditions_cols)
    )
    now = datetime.now().isoformat()
    name = 'Search Results @ %s' % now
    styles = set([obj['style'] for obj in placemarks])

    response = HttpResponse(content_type='application/vnd.google-earth.kmz')
    response['Content-Disposition'] = f"attachment; filename=Search-{now}.kmz"
    zf, sio = get_images_kmz(styles)
    c = Context(locals())
    strr = get_template('reporting/reporting.kml').render(c)
    aaa = strr.encode('utf-8')
    zf.writestr('doc.kml', aaa)
    zf.close()
    response.write(sio.getvalue())
    return response


def get_images_kmz(styles):
    styles = ['incident_%s.gif' % style.lower() for style in styles]
    sio = BytesIO()
    zf = ZipFile(sio, 'w')
    for f in (f for f in os.listdir(kmz_images_path) if f.lower() in styles):
        zf.writestr(kmz_images_path+f, 'images/%s' % f)
    return zf, sio


@login_required
@csrf_exempt
def csv_out(req):
    cols = latest_cols

    filename = 'Search-%s.csv' % datetime.now().isoformat()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    writer = csv.writer(response)
    writer.writerow(cols)
    objs, query = getObjects(req.POST, cols)
    latest_inc = None
    total_rows = 0
    total_incidents = 0
    for obj in objs:
        writer.writerow([obj[i] for i in cols])
        if latest_inc != obj['incidentid']:
            latest_inc = obj['incidentid']
            total_incidents += 1
        total_rows += 1
    writer.writerow(['Total Incidents', total_incidents])
    writer.writerow(['Total Reports', total_rows])
    return response


@login_required
@csrf_exempt
def details(req):

    cursor = connection.cursor()
#    cursor.execute("begin security_mgr.naMELOGIN('nc4admin'); commit; end;")
#   f = open("c:/www/Stats2.txt",'w')
#   f.write(req.GET['incactid'])
#   f.close()
    cols = [
        'updateddate', 'dateoccurred', 'incidentcategory', 'incidenttype',
        'county', 'street', 'stateprovince', 'latitude', 'longitude', 'city',
        'country', 'updatedby', 'gist', 'description', 'severity', 'postal',
        'approximate', 'notifyrule', 'infosource', 'infoquality',
        'conversationlog', 'attachmentlist', 'program'
    ]

    try:
        incactivityid = req.GET['incactid']
    except Exception:
        return HttpResponseNotFound()
#    cursor = connection.cursor()
#    cursor.execute("begin security_mgr.naMELOGIN('nc4admin'); commit; end;")
#     incactivity = IncActivity.objects.get(incactivityid=incactivityid)
#     attachments = str(incactivity.attachmentlist)
#     if attachments is not None and attachments != '':
#         print type(attachments)
#         attachments = Attachments.objects.filter(
#             attachmentid__in=attachments.split(','))
# WHY?: Because trying to access the incactivity.attachmentlist
#       raises an "LOB vairable no longer available" exception
#    query = "SELECT %s FROM fusion.incactivity WHERE"
#            " incactivityid=TO_TIMESTAMP('%s', 'MM/DD/YYYY HH24:MI:SS')"
#    cursor = connection.cursor()
#    query = "SELECT %s FROM fusion.tbl_incactivity WHERE"
#            " incactivityid=TO_TIMESTAMP('%s', 'DD-MON-YY HH.MI.SS PM')"
    incactivityid = req.GET['incactid']
    incidentid = req.GET['incidentid']
    buf = incactivityid.split()
    time = buf[1].rsplit('.')
    #03.19.59.543000000
    #second = int(time[2])
    minute = int(time[1])
    time[1] = str(minute+1)
    #if(second==59):
    #    time[1] = str(minute+1)
    #    time[2] = str(01)
    #else:
    #    time[2] = str(second+1)
    newtime = '.'.join(time)
    buf[1] = newtime
    buf = ' '.join(buf)

    query = """
    SELECT %s
    FROM tbl_incactivity
    WHERE incidentid='%s'
    AND incactivityid BETWEEN TO_TIMESTAMP('%s', 'DD-MON-YY HH.MI.SS PM')
    AND TO_TIMESTAMP('%s', 'DD-MON-YY HH.MI.SS PM')
    """ % (','.join(cols), incidentid, incactivityid, buf)

    cursor.execute(query)
    incident = RowDict(cursor.fetchone(), cols)

    attachments = None
    if incident.attachmentlist:
        ids = str(incident.attachmentlist).split(',')
        attachments = Attachments.objects.filter(attachid__in=ids)
        attach_query = """SELECT label,linkdata,mimetype FROM tbl_incattachments WHERE attachid IN (%s)"""
        format_strings = ','.join(['%s'] * len(ids))
        # query_categories = "SELECT FULLYQUALIFIED FROM fusion.tbl_category WHERE categoryid IN (%s)" % (','.join(ids))
        cursor.execute(attach_query % format_strings, tuple(ids))
        # f.write("\nQuery3 " + query_categories)
        attachments = makeObjs(cursor, ['label', 'linkdata', 'mimetype'])
    else:
        attachments = None
    # DMARK - TEST.  REMOVE NEXT LINE TO ENABLE ATTACHMENTS.
    # attachments = None
    # f = open("c:/www/Stats2.txt",'w')
    # f.write(req.GET['incactid'])
    # f.close()
    return render(
        req,
        'incidents/reporting/details.html',
        {
            'incident': incident,
            'attachments': attachments,
            'incactivityid': incactivityid
        })


@login_required
@csrf_exempt
def details_reg(req):
    cursor = connection.cursor()
    try:
        itemid = req.GET['itemid']
    except Exception:
        return HttpResponseNotFound()
    cols = ','.join(regional_cols)
    parms = (cols, itemid)
    query = "SELECT %s FROM transecur.dailyitems WHERE itemid=%s" % (','.join(regional_cols), itemid)
    f = open("D:/django/details_reg.txt",'w')
    cursor.execute(query)
    f.write("\nQuery1=" + query + "\nParms=" + str(parms))
    item = RowDict(cursor.fetchone(), regional_cols)
    f.write("\nItem=" + str(item))

    # Actors
    if item['itemattributetoactor']:
        ids = tuple(item['itemattributetoactor'].split(','))
        format_strings = ','.join(['%s'] * len(ids))
        query_actors = "SELECT ACTORNAME FROM transecur.actors WHERE primary_id IN (%s)"
        cursor.execute(query_actors % format_strings, ids)
        f.write("\nQuery3 " + query_actors)
        actors = makeObjs(cursor, ['ACTORNAME'])
    else:
        actors = None

    # Categories
    ids = tuple(item['itemcategory'].split(','))
    format_strings = ','.join(['%s'] * len(ids))
    query_categories = "SELECT FULLYQUALIFIED FROM tbl_category WHERE categoryid IN (%s)"
    cursor.execute(query_categories % format_strings, ids)
    f.write("\nQuery3 " + query_categories + ', ids = ' + str(ids))
    categories = makeObjs(cursor, ['FULLYQUALIFIED'])

    f.close()
    # SELECt * FROM fusion.tbl_category where categoryid IN
    # if incident.attachmentlist:
    #     ids = str(incident.attachmentlist).split(',')
    #     attachments = Attachments.objects.filter(attachid__in=ids)
    #     attach_query = """SELECT * FROM fusion.tbl_incattachments WHERE attachid IN %s""" % ('(%s)' % ', '.join(["'%s'" % id for id in ids]))
    # else:
    #     attachments = None
    # DMARK - TEST.  REMOVE NEXT LINE TO ENABLE ATTACHMENTS.
    # attachments = None
    # f = open("c:/www/Stats2.txt",'w')
    # f.write(req.GET['incactid'])
    # f.close()
    return render(
        req,
        'incidents/reporting/details_reg.html',
        {
            'item': item,
            'actors': actors,
            'categories': categories,
            'attachments': None
        }
    )


@login_required
@csrf_exempt
def details_reg_vw(req):

    cursor = connection.cursor()
    try:
        itemid = req.GET['itemid']
    except Exception:
        return HttpResponseNotFound()

    f = open("D:/details_reg_vw.txt",'w')

    #query_locations = "SELECT l.valuelabel as valuelabel FROM vw_documents, table(vw_documents.nc4attrs) l WHERE vw_documents.doclibid='%s'" % (itemid)
    #f.write(query_locations)
    #cursor.execute("""begin security_mgr.namelogin('nc4admin'); end;/""")
    #cursor.execute(query_locations)
    #objectss =  makeObjs(cursor, ['valuelabel']), query_locations
    #for object1 in objectss:
        #f.write(object1['valuelabel']))

    # query = """SELECT vw_documents.doclibid,vw_documents.createddate,vw_documents.updateddate,vw_documents.subject,vw_documents.description,
            # vw_documents.publishdate,vw_documents.effectivedate,vw_documents.doctype,vw_documents.severity,VW_DOCATTACH.docattachid, VW_DOCATTACH.label,
            # l.country, l.city, l.region,l.wktgeoms FROM vw_documents, table(vw_documents.locations) l, VW_DOCATTACH
            # WHERE VW_DOCATTACH.doclibid=vw_documents.doclibid AND vw_documents.doclibid='%s'""" % (itemid)

    query = """SELECT vw_documents.doclibid,vw_documents.createddate,vw_documents.updateddate,vw_documents.subject,vw_documents.description,
            vw_documents.publishdate,vw_documents.effectivedate,vw_documents.doctype,vw_documents.severity,VW_DOCATTACH.docattachid, VW_DOCATTACH.label,
            l.country, l.city, l.region,l.wktgeoms, attrs.valuelabel FROM vw_documents, table(vw_documents.locations) l,  table(vw_documents.nc4attrs) attrs, VW_DOCATTACH
            WHERE VW_DOCATTACH.doclibid=vw_documents.doclibid AND vw_documents.doclibid='%s'""" % (itemid)

    #f.write(query)
    cursor.execute("""begin security_mgr.namelogin('nc4admin'); end;/""")
    cursor.execute(query)
    # item = RowDict(cursor.fetchone(), vw_cols)
    # f.write(str(item))

    items = makeObjs(cursor, vw_cols), query
    item = None
    secondary_location = ""
    for item1 in items[0]:
        if item1['country'] != item1['valuelabel']:
            if secondary_location != "":
                secondary_location = secondary_location + " , " + \
                    item1['valuelabel']
            else:
                secondary_location = item1['valuelabel']
        else:
            item = item1
    item['secondary_location'] = secondary_location

    # Actors
    # ids=["'"+e+"'" for e in str(item['itemattributetoactor']).split(',')]
    # query_actors = "SELECT ACTORNAME FROM transecur.actors WHERE primary_id IN (%s)" % (','.join(ids))
    # cursor.execute(query_actors)
    # f.write("\nQuery3 " + query_actors)
    # actors = makeObjs(cursor, ['ACTORNAME'])

    # Categories
    # ids=["'"+e+"'" for e in str(item['itemcategory']).split(',')]
    # query_categories = "SELECT FULLYQUALIFIED FROM fusion.tbl_category WHERE categoryid IN (%s)" % (','.join(ids))
    # cursor.execute(query_categories)
    # f.write("\nQuery3 " + query_categories)
    # categories = makeObjs(cursor, ['FULLYQUALIFIED'])

    f.close()
    # SELECt * FROM fusion.tbl_category where categoryid IN
    # if incident.attachmentlist:
    #     ids = str(incident.attachmentlist).split(',')
    #     attachments = Attachments.objects.filter(attachid__in=ids)
    #     attach_query = """SELECT * FROM fusion.tbl_incattachments WHERE attachid IN %s""" % ('(%s)' % ', '.join(["'%s'" % id for id in ids]))
    # else:
    #     attachments = None
    # DMARK - TEST.  REMOVE NEXT LINE TO ENABLE ATTACHMENTS.
    # attachments = None
    # f = open("c:/www/Stats2.txt",'w')
    # f.write(req.GET['incactid'])
    # f.close()
    return render(
        req,
        'incidents/reporting/details_reg_vw.html',
        {
            'item': item,
            'actors': None,
            'categories': None,
            'attachments': None
        }
    )


@login_required
@csrf_exempt
def domestic_incidents(request):
    return current_incidents(
        request, "country='United States'", 'Domestic-Incidents.kmz',
        'Current Domestic Incidents')


@login_required
def current_incidents(request, comps, filename, title, cols=kmz_cols):
    if type(comps) is str:
        comps = [comps]
    query = """
        SELECT %(cols)s
        FROM tbl_incidents INT
        INNER JOIN tbl_incactivity act ON INT.latestactivityid = act.incactivityid
        WHERE %(comps)s
        """
    query %= {'cols': ', '.join(cols), 'comps': ' AND '.join(comps+["currentstatus='OPEN'"])}
    cursor = connection.cursor()
    # cursor.execute("begin security_mgr.naMELOGIN('nc4admin'); commit; end;")
    cursor.execute(query)
    return make_kmz(makeObjs(cursor, cols), filename, title)


def make_kmz(placemarks, filename, name):
    styles = set([obj['style'] for obj in placemarks])
    response = HttpResponse(content_type='application/vnd.google-earth.kmz')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    zf, sio = get_images_kmz(styles)
    c = Context(locals())
    zf.writestr('doc.kml', get_template('reporting/reporting.kml').render(c))
    zf.close()
    response.write(sio.getvalue())
    return response
