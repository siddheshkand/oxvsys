from django import forms
from . import models


class CustomerDetailForm(forms.ModelForm):
    class Meta:
        model = models.CustomerDetail
        fields = [
            'email',
            'contact_nos',
            'message',
            'requirements',
        ]

    # def __init__(self, *args, **kwargs):
    #     super(CustomerDetailForm, self).__init__(*args, **kwargs)
    #     super().__init__()
    #     self.fields['email'].widget = forms.TextInput(attrs={
    #         'class': 'input',
    #     })
    #     self.fields['message'].widget = forms.TextInput(attrs={
    #         'class': 'textarea',
    #     })
    #     self.fields['requirements'].widget = forms.TextInput(attrs={
    #         'class': 'textarea',
    #     })
