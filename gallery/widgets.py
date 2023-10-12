# gallery/widgets.py

from django import forms
from django.forms import FileInput

class CustomFileInput(forms.FileInput):
    def value_from_datadict(self, data, files, name):
        return files.getlist(name)

class MultipleFileInput(FileInput):
    def value_from_datadict(self, data, files, name):
        return files.getlist(name)
    def value_omitted_from_data(self, data, files, name):
        # 원래의 검증을 건너뜁니다.
        return False
    # template_name = 'forms/widgets/multiple_input.html'

    # def value_from_datadict(self, data, files, name):
    #     return files.getlist(name)