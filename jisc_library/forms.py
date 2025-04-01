from django import forms
from .models import *
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils import timezone
from django.db.models import F, CharField, Value
from django.db.models.functions import Concat

class BookUploadForm(forms.Form):
    file = forms.FileField(label="Upload Excel File")

class LibraryRecordForm(forms.ModelForm):
    class Meta:
        model = LibraryRecord
        fields = ['user', 'book', 'shelf_no', 'row_no', 'issue_date', 'returned_date', 'status']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control select2'}),
            'book': forms.Select(attrs={'class': 'form-control select2'}),
            'shelf_no': forms.TextInput(attrs={'class': 'form-control'}),
            'row_no': forms.TextInput(attrs={'class': 'form-control'}),
            'issue_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'returned_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customizing the user queryset to include username and full name
        self.fields['user'].queryset = User.objects.annotate(
            full_name=Concat(F('first_name'), Value(' '), F('last_name'), output_field=CharField())
        )

        # Modify the choices for the user field to show both username and full name
        self.fields['user'].label_from_instance = lambda obj: f"{obj.username} - {obj.full_name}"