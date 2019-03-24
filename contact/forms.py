from django import forms

# Create your models here.
class ContactForm(forms.Form):
    firstName      = forms.CharField(widget=forms.TextInput(attrs={"id":"contact_name","class":"contact_input"} ),required = True, max_length=50)
    lastName       = forms.CharField(widget=forms.TextInput(attrs={"id":"contact_last_name","class":"contact_input"}) ,required = True, max_length=50)
    subject        = forms.CharField(widget=forms.TextInput(attrs={"id":"contact_company","class":"contact_input"} ),required = True, max_length=100)
    message        = forms.CharField(widget=forms.Textarea(attrs={"id":"contact_textarea","class":"contact_input"} ),required = True, max_length=5000)
