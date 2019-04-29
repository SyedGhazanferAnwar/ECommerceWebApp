from django import forms

class NewsUserForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs ={"type":"email","class":"newsletter_input","required":"required"}),label='')
