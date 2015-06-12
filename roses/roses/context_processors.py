from datetime import datetime
from django.utils.timezone import utc
from django.utils.translation import ugettext_lazy, ugettext
from django.utils.translation import ugettext_lazy as _
def account_age_message(request):
    """
    Provide to template context the number of years a User has been registered

    The crude year calculation is taken from : http://stackoverflow.com/q/4436957/364088
    """
    user = request.user
    if user.is_authenticated():
        now = datetime.utcnow().replace(tzinfo=utc)
        mship_lngth_delta = now - user.date_joined
        difference_in_years = (mship_lngth_delta.days + mship_lngth_delta.seconds/86400)/365.2425
        if difference_in_years < 1:
            welcome_msg = _("Welcome newcomer")
        else:
            welcome_msg = _("Congratulations, you are a %(y)s years veteran")\
                    % {'y': int(difference_in_years)}
    else:
        welcome_msg = ""
    return {'WELCOME_MSG': welcome_msg }




