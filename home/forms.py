"""forms imports"""
from django import forms
from art.models import Newsletter


class MailForm(forms.ModelForm):
    """creates the form for joing the mailing list"""
    class Meta:
        model = Newsletter
        fields = ('join', )
