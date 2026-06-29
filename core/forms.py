from django import forms
from .models import QuoteRequest, ContactMessage


class QuoteRequestForm(forms.ModelForm):

    class Meta:
        model = QuoteRequest

        fields = [
            "full_name",
            "email",
            "phone",
            "service",
            "message",
        ]

        widgets = {

            "full_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your full name"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your email"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your phone number"
            }),

            "service": forms.Select(attrs={
                "class": "form-select"
            }),

            "message": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Tell us about your project..."
            }),

        }

class ContactForm(forms.ModelForm):

    class Meta:

        model = ContactMessage

        fields = [
            "full_name",
            "email",
            "subject",
            "message",
        ]

        widgets = {

            "full_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your Name"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Your Email"
            }),

            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Subject"
            }),

            "message": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 6,
                "placeholder": "Type your message..."
            }),

        }        