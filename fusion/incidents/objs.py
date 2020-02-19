import re
import datetime

from dateutil import parser

class objdict(dict):
    def __getattr__(self, key):
        return self[key]
    def __setattr__(self, key, val):
        self[key] = val

class OracleTime(datetime.datetime):
    def __str__(self):
#        return "'" + self.strftime('%d-%b-%y %I.%M.%S.000000000 %p') + "'"
        return "TO_TIMESTAMP('%s', 'DD-MM-YYYY HH24:MI')" % \
            self.strftime('%d-%m-%Y %H:%M')

    def __unicode__(self):
        return unicode(str(self))

class Category:
    def __init__(self, name, db_name):
        self.name = name
        self.db_name = db_name
    
    def parse(self, data):
#        return "'" + data.strip().replace(r"'", r"\'") + "'"
        return "'%s'" % data.strip().replace(r"'", r"\'")

class DateCat(Category):
    parser = re.compile(r'(\d{1,2})\/(\d{1,2})\/(\d{4}) (\d{1,2}):(\d{1,2}):?(\d{1,2})?\s?(am|pm)')

#     def parse(self, data):
#         m = self.parser.match(data.strip().lower())
#         if m:
#             groups = m.groups()
#             data = [int(d) for d in groups[:-1] if d is not None]
#             if groups[6] == 'pm':
#                 data[3] += 12
#                 data[3] %= 24
#             try:
#                 return OracleTime(data[2], data[0], data[1], data[3], data[4])
#             except IndexError, e:
#                 raise Exception(str(data))
#         return None
    def parse(self, data):
        return "TO_TIMESTAMP('%s', 'DD-MM-YYYY HH24:MI')" % parser.parse(data).strftime('%d-%m-%Y %H:%M')


class SeverityCat(Category):
    severities = {
        'minor': 1,
        'moderate': 2,
        'severe': 3,
        'extreme': 4,
    }

    def parse(self, data):
        return self.severities[data.lower()]
