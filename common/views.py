from django.shortcuts import render  
from django.contrib.auth.forms import AuthenticationForm  
from django.contrib import auth  
from django.http.response import HttpResponseRedirect  
from django.urls import reverse_lazy  
from django.template import loader

from django.views.generic import FormView  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth import login, authenticate  
from common.forms import ProfileCreationForm
from django.views.generic import  UpdateView

from common.models import UserProfile

from allauth.socialaccount.models import SocialAccount
import uuid
  


def profile(request):  
    context = {}  
    if request.user.is_authenticated:  
        context['username'] = request.user.username
        try:
            soc_user = SocialAccount.objects.get(provider='github', user=request.user)
            try:
                context['name'] = SocialAccount.objects.get(provider='github', user=request.user).extra_data['name']
                context['age'] = SocialAccount.objects.get(provider='github', user=request.user).extra_data['age']
                context['city'] = SocialAccount.objects.get(provider='github', user=request.user).extra_data['city']
                context['github_url'] = SocialAccount.objects.get(provider='github', user=request.user).extra_data['html_url']
                context['id'] = SocialAccount.objects.get(provider='github', user=request.user).extra_data['id']     

                return render(request, 'profile.html', context)
                
            except KeyError:
                return HttpResponseRedirect(reverse_lazy('common:socprofile-create'))

        except SocialAccount.DoesNotExist:
            try:
                context['name'] = UserProfile.objects.get(user=request.user).name
                context['age'] = UserProfile.objects.get(user=request.user).age
                context['city'] = UserProfile.objects.get(user=request.user).city
                context['id'] = UserProfile.objects.get(user=request.user).id
            except UserProfile.DoesNotExist:
                return HttpResponseRedirect(reverse_lazy('common:profile-create'))

    return render(request, 'profile.html', context)


class RegisterView(FormView):  
  
    form_class = UserCreationForm  
  
    def form_valid(self, form):  
        form.save()  
        username = form.cleaned_data.get('username')  
        raw_password = form.cleaned_data.get('password1')  
        login(self.request, authenticate(username=username, password=raw_password))  
        return super(RegisterView, self).form_valid(form)  
  
  
class CreateUserProfile(FormView):

    success_url = reverse_lazy("common:profile")
    form_class = ProfileCreationForm  
    template_name = 'profile-create.html'  
	
    def dispatch(self, request, *args, **kwargs):  
        if self.request.user.is_anonymous:  
            return HttpResponseRedirect(reverse_lazy('common:login'))  
        return super(CreateUserProfile, self).dispatch(request, *args, **kwargs)  
  
    def form_valid(self, form):  
        instance = form.save(commit=False)  
        instance.user = self.request.user  
        instance.save()  
        return super(CreateUserProfile, self).form_valid(form)


from django.http import HttpResponse
 
def CreateSocUserProfile(request):
    errors = []
    form = {}
    if request.POST:
         
        soc_user = SocialAccount.objects.get(user=request.user)
        a=request.POST.get('name')
        print(a)
        print(soc_user)
        b=soc_user.extra_data
        print(b)

        soc_user.extra_data['name'] = request.POST.get('name')
        soc_user.extra_data['age'] = request.POST.get('age')
        soc_user.extra_data['city'] = request.POST.get('city')
        b['name'] = request.POST.get('name')
        print(b)
        soc_user.save()
        return HttpResponseRedirect(reverse_lazy('common:profile'))

    return render(request, 'profile-create-soc.html')
         

def SocProfileUpdate(request):
    errors = []
    form = {}
    if request.POST:
         
        soc_user = SocialAccount.objects.get(user=request.user)
        soc_user.extra_data['name'] = request.POST.get('name')
        soc_user.extra_data['age'] = request.POST.get('age')
        soc_user.extra_data['city'] = request.POST.get('city')
        soc_user.save()
        return HttpResponseRedirect(reverse_lazy('common:profile'))

    return render(request, 'profile-update-soc.html')


class ProfileUpdate(UpdateView):
    model = UserProfile
    form_class = ProfileCreationForm 
    success_url = reverse_lazy('common:profile')  
    template_name = 'profile-update.html'

