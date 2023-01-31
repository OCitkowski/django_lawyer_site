from django import forms
# from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Checkbox


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label='name')
    email_address = forms.EmailField(max_length=50, label='email address')
    phone = forms.CharField(max_length=15, label='phone number')
    message = forms.CharField(widget=forms.Textarea, max_length=5000, label='message')
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)