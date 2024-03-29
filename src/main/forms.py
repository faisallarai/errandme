from django import forms

from .tasks import send_contact_email


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'palceholder': 'Your name'}))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(
        attrs={"placeholder": 'Phone Number'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"placeholder": 'Email Address'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={"placeholder": 'Message'}))

    def send_email(self):
        send_contact_email.delay(self.cleaned_data)
