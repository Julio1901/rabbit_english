from django import forms

class registrationForm(forms.Form):
    email = forms.EmailField(label='Type your email adress here', max_length= 100)
    password = forms.CharField(widget=forms.PasswordInput)

    def get_email(self):
        return self.email
