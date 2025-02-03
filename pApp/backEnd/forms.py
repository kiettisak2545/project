from django import forms
from pApp.models import slips

class SlipForm(forms.ModelForm):
    class Meta:
        model = slips
        fields = ["slip", "deposit"]
