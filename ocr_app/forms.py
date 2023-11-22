from django import forms
from django.db import models

class AngleChoices(models.TextChoices):
    no = 'no', '回転しない'
    right = 'right', '右に回転'
    left = 'left', '左に回転'

class OutputChoices(models.TextChoices):
    webpage = 'wepage', 'ウェブページに表示'
    excel= 'excel', 'エクセルシートに保存と表示'
    
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
   
class OutputChoiceForm(forms.Form):
   output = forms.fields.ChoiceField(
        choices=OutputChoices.choices,
        required = True,
        label='\n(option)     結果の表示',
    )    
    