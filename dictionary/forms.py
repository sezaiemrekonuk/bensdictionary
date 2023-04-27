from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Adınız', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Adınız'}))
    email = forms.EmailField(label='E-posta Adresiniz', widget=forms.TextInput(attrs={'placeholder': 'E-Mail Adresiniz'}))
    subject = forms.CharField(label='Konu', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Konu'}))
    message = forms.CharField(label='Mesajınız', widget=forms.Textarea(attrs={'placeholder': 'Mesajınız'}))
