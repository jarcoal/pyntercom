import json
import datetime
import calendar

class JSONEncoder(json.JSONEncoder):
    """Encoder that converts datetimes to unix timestamps"""

    def default(self, o):
        if isinstance(o, datetime.datetime):
            return calendar.timegm(o.utctimetuple())

        return super(JSONEncoder, self).default(o)