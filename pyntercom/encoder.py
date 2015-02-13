import json
import datetime
import calendar

def datetime_to_unix_timestamp(dtt):
    return calendar.timegm(dtt.utctimetuple())

class JSONEncoder(json.JSONEncoder):
    """Encoder that converts datetimes to unix timestamps"""

    def default(self, o):
        if isinstance(o, datetime.datetime):
            return datetime_to_unix_timestamp(o)

        return super(JSONEncoder, self).default(o)