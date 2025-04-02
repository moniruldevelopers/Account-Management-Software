from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget
from django.forms.widgets import DateInput


class TransactionCategoryForm(forms.ModelForm):
    class Meta:
        model = TransactionCategory
        fields = ['name', 'description']


class UploadExcelForm(forms.Form):
    file = forms.FileField()


class TransactionForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = Transaction
        fields = ['transaction_by', 'category', 'transaction_type', 'price', 
                  'invoice_no', 'invoice_id', 'invoice_date', 'check_no', 'description']
        widgets = {
            'transaction_by': forms.Select(attrs={'class': 'form-control select2'}),
            'category': forms.Select(attrs={'class': 'form-control select2'}),
            'transaction_type': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'maxlength': '10'}),
            'invoice_no': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '15'}),
            'invoice_id': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '15'}),
            'invoice_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'check_no': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '15'}),
        }
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price
    





class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'profile_picture']  # Add 'profile_picture' here
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}), #add profile picture widget
        }


# OfficeItem Form
class OfficeItemForm(forms.ModelForm):
    class Meta:
        model = OfficeItem
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }




class BorrowManagementForm(forms.ModelForm):
    return_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        required=False  # Ensures the field is optional
    )
    office_item = forms.ModelChoiceField(
        queryset=OfficeItem.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control select2'})
    )
    
    # Modify user field to display username + full name
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control select2'})
    )

    class Meta:
        model = BorrowManagement
        fields = ['user', 'office_item', 'return_date']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control select2'}),
            'office_item': forms.Select(attrs={'class': 'form-control select2'}),
        }

    def clean_return_date(self):
        return_date = self.cleaned_data.get('return_date')
        if return_date and return_date < self.instance.created_at:
            raise forms.ValidationError("Return date cannot be before the borrow date.")
        return return_date

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the display of the user field to show both username and full name
        self.fields['user'].queryset = User.objects.all()
        self.fields['user'].label_from_instance = lambda user: f"{user.username} ({user.get_full_name()})"