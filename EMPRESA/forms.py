from django import forms

class FormEmailSend(forms.Form):
    name  = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'name *', 'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'last_name *', 'class': 'form-control'}))
    number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'number *', 'class': 'form-control'}))
    from_email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'comment *', 'class': 'form-control'}))