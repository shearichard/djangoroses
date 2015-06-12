import logging
import sys
import traceback

try:
    import simplejson
except ImportError:
    import json as simplejson

import pytz
from datetime import datetime, date
 
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.mail import mail_admins
from django.http import Http404, HttpResponseServerError
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils import timezone

logger = logging.getLogger(__name__)
 
class TimeZoneMiddleware(object):
    def process_request(self, request):
        tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()

class GoingDown(object):
    def process_request(self, request):
        '''
        Redirects all requests to another url when the system is down
        '''
        from django.utils.timezone import utc
        from django.http import HttpResponseRedirect 
        if settings.SYSDOWNTIMEUTC and settings.SYSUPTIMEUTC:
            now = datetime.utcnow().replace(tzinfo=utc)
            if (now > settings.SYSDOWNTIMEUTC) and (now < settings.SYSUPTIMEUTC):
                return HttpResponseRedirect(settings.SYSDOWNINFOPAGE)
        else:
            pass


    def process_template_response(self, request, response):
        '''
        Warns users the system is going down at a given time
        '''
        DWNMSG = '''"Stop and smell" will be doing down in {} seconds'''
        from django.utils.timezone import utc
        from django.http import HttpResponseRedirect 
        if settings.SYSDOWNTIMEUTC and settings.SYSUPTIMEUTC:
            now = datetime.utcnow().replace(tzinfo=utc)
            if now < settings.SYSDOWNTIMEUTC and now < settings.SYSUPTIMEUTC:
                sysdown_delta = settings.SYSDOWNTIMEUTC - now
                response.context_data['SYSTEM_MESSAGE'] = DWNMSG.format(str(sysdown_delta.seconds)) 
        else:
            pass

        return response

