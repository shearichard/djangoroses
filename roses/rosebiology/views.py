import logging

import pytz

from django.http import HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required

from .models import Species, CommonName  

logger = logging.getLogger(__name__)

class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

class SpeciesList(LoginRequiredMixin, TemplateView):
    template_name = 'rosebiology/species_list.html'


    def get_context_data(self, **kwargs):
        context = super(SpeciesList, self).get_context_data(**kwargs)
        species_list = Species.objects.all()
        lines = []
        for s in species_list:
            lines.append(s)
        paginator = Paginator(lines, 12)
        page = self.request.GET.get('page')
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            show_lines = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            show_lines = paginator.page(paginator.num_pages)
        context['lines'] = show_lines
        return context

class SpeciesDetailView(LoginRequiredMixin, DetailView):

    model = Species
    fields = ['binomial_nomenclature', 'height_and_spread', 'created']

    @method_decorator(permission_required('rosebiology.display_details_species_'))
    def dispatch(self, *args, **kwargs):
        return super(SpeciesDetailView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SpeciesDetailView, self).get_context_data(**kwargs)
        context['common_names_list'] = list()
        
        for cn in self.object.common_name.all():
            context['common_names_list'].append(cn.name)
        return context




class SpeciesCreate(LoginRequiredMixin, CreateView):
    model = Species
    fields = ['binomial_nomenclature', 'height_and_spread']
    success_url = reverse_lazy('specieslist')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return HttpResponseRedirect(reverse_lazy('specieslist'))
        else:
            return super(SpeciesCreate, self).post(request, *args, **kwargs)

    @method_decorator(permission_required('rosebiology.add_species'))
    def dispatch(self, *args, **kwargs):
        return super(SpeciesCreate, self).dispatch(*args, **kwargs)

class SpeciesUpdate(LoginRequiredMixin, UpdateView):
    model = Species
    fields = ['binomial_nomenclature', 'height_and_spread']
    success_url = reverse_lazy('specieslist')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            self.object = self.get_object()
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(SpeciesUpdate, self).post(request, *args, **kwargs)

class SpeciesDelete(LoginRequiredMixin, DeleteView):
    model = Species
    success_url = reverse_lazy('specieslist')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            logger.warning('SpeciesDelete.post CANCEL')
            '''
            raise Exception("This is a test of middleware")
            self.object = self.get_object()
            url = self.get_success_url()
            return HttpResponseRedirect(url)
            '''
            return HttpResponseServerError("This is a test of middleware")
        else:
            print("about to log b")
            logger.info('SpeciesDelete.post EXECUTE')
            return super(SpeciesDelete, self).post(request, *args, **kwargs)

class HomePageView(TemplateView):
    template_name = 'rosebiology/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['timezones'] = pytz.common_timezones
        if False:
            #Hide this for a while
            messages.info(self.request, 'This is a demo of a message.')
        return context

#The `restricted` function is only there to illustrate the 
#@login_required decorator
@login_required
def this_is_restricted(request):
    return HttpResponse('''Since you're logged in you can see this string''')

#The `restricted` function is only there to illustrate the 
#@login_required decorator
@login_required
@permission_required('rosebiology.add_species')
def this_is_even_more_restricted(request):
    print("I am in this_is_even_more_restricted")
    return HttpResponse('''Since you're logged and you have the ability to add Species in you can see this string''')


###########################################################################################
###########################################################################################
###########################################################################################
# This code has been borrowed and adapted lightly from 'Tango with Django 1.7'
###########################################################################################
###########################################################################################
###########################################################################################
from .forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

def register(request):
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()
            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user
            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            # Now we save the UserProfile model instance.
            profile.save()
            # Update our variable to tell the template registration was successful.
            registered = True
        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(user_form.errors, profile_form.errors)
    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    # Render the template depending on the context.
    return render(request,
            'rosebiology/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/species/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Roses account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'rosebiology/login.html', {})


from django.contrib.auth import logout

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')
###########################################################################################
# End of code has been borrowed and adapted lightly from 'Tango with Django 1.7'
###########################################################################################
###########################################################################################
# Start of code borrowed from : http://docs.djangoproject.com/en/1.8/topics/i18n/timezones/ 
###########################################################################################
from django.shortcuts import redirect, render

def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')
    else:
        return render(request, 'template.html', {'timezones': pytz.common_timezones})

###########################################################################################
# End of code borrowed from : http://docs.djangoproject.com/en/1.8/topics/i18n/timezones/ 
###########################################################################################
