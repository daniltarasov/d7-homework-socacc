from django import forms  
from common.models import UserProfile
  
  
class ProfileCreationForm(forms.ModelForm):  
  
    class Meta:  
        model = UserProfile  
        fields = ['name', 'age', 'city']
        labels = {'name':'Имя', 'age':'Возраст', 'city':'Город' }


# class ProfileSocAccCreationForm(forms.Form):
#     name = forms.CharField()
#     age = forms.IntegerField()
#     city = forms.CharField()