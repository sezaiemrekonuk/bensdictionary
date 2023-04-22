from django import forms
from .models import Correct

class CorrectionForm(forms.ModelForm):
    class Meta:
        model = Correct
        fields = ['corrector', 'correction']