from django import forms
from .models import Resume

CHOICES_GENDER = [('1', 'Male'), ('2', 'Female'), ('3', 'Other')]
CHOICES_JOBCITY = [('1', 'Mumbai'), ('2', 'Pune'), ('3', 'Delhi')]
class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES_GENDER)
    job_city = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={"class":"inline"}), choices=CHOICES_JOBCITY)

    class Meta:
        model = Resume
        
        # this will handle the fiels sequence too
        fields = ['name','dob','locality','city','pin','state','mobile','email','profile_image','my_file','gender','job_city'
        ]
        
        # this will add the lable wrt fields name
        labels = {
            "name":"Name",
            "dob":"Date Of Birth",
            "locality":"Locality",
            "city":"City",
            "pin":"Pin Code",
            "state":"State",
            "mobile":"Contact No.",
            "email":"Email ID",
            "job_city":"Job Prefer City",
            "profile_image":"Select Profile",
            "my_file":"Select Resume"
        }

        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "dob":forms.DateInput(attrs={"class":"form-control"}),
            "locality":forms.TextInput(attrs={"class":"form-control"}),
            "city":forms.TextInput(attrs={"class":"form-control"}),
            "pin":forms.TextInput(attrs={"class":"form-control"}),
            "state":forms.TextInput(attrs={"class":"form-control"}),
            "mobile":forms.NumberInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "job_city":forms.TextInput(attrs={"class":"form-control"}),
            "profile_image":forms.FileInput(attrs={"class":"form-control"}),
            "my_file":forms.FileInput(attrs={"class":"form-control"})
        }

         