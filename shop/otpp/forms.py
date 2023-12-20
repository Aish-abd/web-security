from django import forms 
from .models import Code


class MFAForm(forms.ModelForm):
    number=forms.CharField(label='code',help_text='Enter SMS Verification code')

    class Meta:
        model=Code
        fields=('number',)