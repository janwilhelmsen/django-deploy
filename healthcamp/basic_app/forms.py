from django import forms
from django.contrib.auth.models import User
from basic_app.models import Person,Village,Journal,JournalEntries,Campain,Staff,User


class PersonForm(forms.ModelForm):
    # village = forms.ModelChoiceField(queryset=Village.objects.all(),empty_label=None)

    class Meta():
        model = Person
        fields =('firstname','lastname','age','sex','village')
        # fields = ('__all__')


class VillageForm(forms.ModelForm):

    class Meta():
        model = Village
        fields = ('name','country')


class VillagePopupForm(forms.ModelForm):

    class Meta():
        model = Village
        fields = ('name','country')


class JournalEntries(forms.ModelForm):
    model = JournalEntries


class Campain(forms.ModelForm):
    model = Campain


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('role','telephone','title','profil_pic')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')
