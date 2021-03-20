from django import forms

class registrationForm(forms.Form):
    name = forms.CharField(label='Type your name here. Ex: FirstName LastName', max_length=100)
    email = forms.EmailField(label='Type your email adress here', max_length= 100)
    password = forms.CharField(widget=forms.PasswordInput)

    def get_email(self):
        return self.email

class loginForm(forms.Form):
    email = forms.EmailField(label='Type your email adress here', max_length= 100)
    password = forms.CharField(widget=forms.PasswordInput)

