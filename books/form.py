from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label="Your e-mail addresss")
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.clean_data["message"]
        num_words = len(message.split())
        if num_words < 4:
            raise form.ValidationError("Not enough words")
        return message