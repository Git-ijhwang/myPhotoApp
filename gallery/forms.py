# gallery/forms.py

from django import forms
from .widgets import MultipleFileInput, CustomFileInput

# from .widgets import CustomFileInput

class BulkUploadForm(forms.Form):
    images = forms.FileField(required=False)
    # images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    # images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    # images = forms.FileField(widget=forms.FileInput(attrs={'multiple': True}), required=False)
    # images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    # images = forms.ImageField(widget=MultipleClearableFileInput(attrs={'multiple': True}), required=False)
    # images = forms.FileField(widget=forms.FileInput(attrs={'multiple': True}), required=False)




    # images = forms.FileField(widget=forms.FileInput(attrs={'multiple': True}))
    # images = forms.FileField(widget=CustomFileInput(attrs={'multiple': 'multiple'}), required=False)
    # images = forms.FileField(widget=MultipleFileInput(attrs={'multiple': True}), required=False)


	# images = forms.MultipleChoiceField(
    #     widget=forms.FileInput(attrs={'multiple': 'multiple'}),
    #     required=False
    # )




