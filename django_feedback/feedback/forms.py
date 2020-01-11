from django import forms
from .models import Manager,Employee

class EmployeeForm(forms.Form):
    manager = forms.ModelChoiceField()
    comment=forms.Textarea()

    class Meta:
        model = Employee
        fields = ('manager','comment')
