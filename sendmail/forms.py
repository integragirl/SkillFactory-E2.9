from django import forms
from sendmail.models import MailPost


class MailPostForm(forms.ModelForm):
    class Meta:
        model = MailPost
        fields = '__all__'
        #fields = ['name']
