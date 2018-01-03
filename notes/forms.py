from django import forms
from .models import Note, Responsavel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

class NoteForm(forms.ModelForm):	
	descricao = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Note
		fields = (
		'responsavel',
		'descricao',		
		)

	def clean_responsavel(self):
		responsavel = self.cleaned_data['responsavel']
		if Responsavel.objects.filter(responsavel=responsavel).exists() == False:
			raise ValidationError("Responsavel não cadastrado")			
		return responsavel

class ResponsavelForm(forms.ModelForm):	
	class Meta:
		model = Responsavel		
		fields = (
		'responsavel',
		'descricao'
		)

	def clean_responsavel(self):
		responsavel = self.cleaned_data['responsavel']
		if Responsavel.objects.filter(responsavel=responsavel).exists():
			raise ValidationError("Responsavel já cadastrado")			
		return responsavel

class ResponsavelFormEdit(forms.ModelForm):	
	class Meta:
		model = Responsavel		
		fields = (
		'responsavel',
		'descricao'
		)	

class EditProfileForm(UserChangeForm):
	class Meta:
		model = User
		fields = (
		'email',
		'first_name',
		'last_name',
		'password'
		)


class RegisterProfileForm(UserCreationForm):
	email = forms.EmailField(required=True)
	
	class Meta:
		model = User
		fields = (
		'username',
		'email',
		'first_name',
		'last_name',
		'password1',
		'password2'
		)		

	def save(self, commit=True):
		user = super(RegisterProfileForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()