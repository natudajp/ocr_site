from django import forms
from django.db import models

class AngleChoices(models.TextChoices):
    no = 'no', '回転しない'
    right = 'right', '右に回転'
    left = 'left', '左に回転'
    
class UploadFileForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={
        'id': 'file_id'
    }   
    )
    )

class RotateChoiceForm(forms.Form):
   angle = forms.fields.ChoiceField(
        choices=AngleChoices.choices,
        required = True,
        label='\n(option)     図形の回転',
    )    
    