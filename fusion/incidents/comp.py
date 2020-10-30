#!/usr/bin/env python

from dateutil import parser


class Op(object):
    def __init__(self, op):
        self.op = op

    def pre_parse(self, val):
        """Modify the actual value before it gets escaped.
        e.g add wildcard characters for LIKE operators"""
        return val

    def post_parse(self, val):
        return val


class StringOp(Op):
    def __init__(self, op, val_template):
        Op.__init__(self, op)
        self.val_template = val_template

    def pre_parse(self, val):
        return self.val_template % val


class Col(object):
    def __init__(self, name, col):
        self.name = name
        self.col = col

    def parse(self, val):
        return "'%s'" % val.replace("'", r"\'")


class DateCol(Col):
    def parse(self, val):
        val = parser.parse(val).strftime('%d-%m-%Y %H:%M')
        return "TO_TIMESTAMP('%s', 'DD-MM-YYYY HH24:MI')" % val


class AnalystCol(Col):
    def parse(self, val):
        return "'%s'" % val


def make_parse_chain(op, col):
    return lambda field: op.post_parse(col.parse(op.pre_parse(field)))


class RowDict(dict):
    def getlist(self, key):
        return self[key]


def make_comp(row, post, columns):
    # op = operators[row['op'] if row.get('not', '0') == '0' else '!'+row['op']]  # noqa
    # if row.get('not', '0') == '0':
    #     op = operators[row['op']]
    # else:
    #     op = operators['!'+row['op']]

    if row['not'] == '1':
        op = operators['!'+row['op']]
    else:
        op = operators[row['op']]
    # if(post['searchtype']=='regional'):
    #     if(post.has_key('vw') and post['vw']=='true'):
    #         col = columns_vw[row['type']]
    #     else:
    #         col = columns_regional[row['type']]
    # else:
    #     col = columns[row['type']]
    col = columns[row['type']]

    parse_chain = make_parse_chain(op, col)
    if op.op in list_ops:
        vals = (parse_chain(val) for val in row.getlist('field'))
        val = '(%s)' % ', '.join(vals)
    else:
        val = parse_chain(row['field'])
    if row['cs'] == '1' or row['type'] == 'dateoc':
        comp = '%(col)s %(op)s %(val)s' % {
            'col': col.col, 'op': op.op, 'val': val
        }
    else:
        comp = 'lower(%(col)s) %(op)s %(val)s' % {
            'col': col.col, 'op': op.op, 'val': val.lower()
        }
    # We can add in UI for the Case Insensitive for each row and check here

    return comp


list_ops = set(['IN', 'NOT IN'])

operators = {
    'eq': Op('='), '!eq': Op('<>'), 'lt': Op('<'), '!lt': Op('>='),
    'gt': Op('>'), '!gt': Op('<='), 'lte': Op('<='), '!lte': Op('>'),
    'gte': Op('>='), '!gte': Op('<'),
    'con': StringOp('LIKE', '%%%s%%'), '!con': StringOp('NOT LIKE', '%%%s%%'),
    'strt': StringOp('LIKE', '%%%s'), '!strt': StringOp('NOT LIKE', '%%%s'),
    'in': Op('IN'), '!in': Op('NOT IN'),
}

columns = {
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

columns_regional = {
    'title': Col('Title', 'itemtitle'),
    'severity': Col('Severity', 'ItemSignificance'),
    'dateoc': DateCol('Date Occurred', 'CREATEDDATE'),
    'dateexp': DateCol('Expiration Date', 'ITEMEXPIRATIONDATE'),
    'city': Col('City', 'city'),
    'cntry': Col('Country', 'country'),
    'region': Col('Region', 'region'),
    'event': Col('Special Event', 'itemevent'),
    'body': Col('Body', 'ItemText'),
}

columns_vw = {
    'title': Col('Title', 'subject'),
    'severity': Col('Severity', 'severity'),
    'dateoc': DateCol('Date Occurred', 'CREATEDDATE'),
}

if __name__ == '__main__':
    assert make_comp({'op': 'eq', 'col': 'inccat', 'field': 'Fire'}) == \
        "incidentcategory = 'Fire'"
    assert make_comp(
        {'op': 'eq', 'not': 1, 'col': 'inccat', 'field': 'Fire'}) == \
        "incidentcategory <> 'Fire'"
    assert make_comp(
        {'op': 'lt', 'col': 'dateoc', 'field': '01/21/2008 1:40 pm'}) == \
        "dateoccurred < TO_TIMESTAMP('21-01-2008 13:40', 'DD-MM-YYYY HH24:MI')"
    assert make_comp({'op': 'con', 'col': 'st', 'field': 'CA'}) == \
        "stateprovince LIKE '%CA%'"
    assert make_comp(
        {'op': 'con', 'not': '1', 'col': 'cnty', 'field': 'Orange'}) \
        == "county NOT LIKE '%Orange%'"
    assert make_comp({'op': 'in', 'col': 'st', 'field': ['CA', 'FL']}) == \
        "stateprovince IN ('CA', 'FL')"
    assert make_comp(
        {'op': 'in', 'not': '1', 'col': 'cnty',
         'field': ['Los Angeles', 'Orange']}) == \
        "county NOT IN ('Los Angeles', 'Orange')"
