from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ("emp_id","name","mobileno","designation")
        labels = {
            "emp_id":"Employee id",
            "name":"Full Name",
            "mobileno":"Mobile Number",
        }

        def __init__(self,*args,**kwargs):
            super(EmployeeForm, self).__init__(*args,**kwargs)
            self.fields["designation"].empty_label = "Select"