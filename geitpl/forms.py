from django import forms 

class dummyForm(forms.Form):  # Corrected 'From' to 'Form'
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="Email")
    position = forms.CharField(label="Position", max_length=100)


