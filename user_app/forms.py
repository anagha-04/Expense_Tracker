from django import forms

from user_app.models import User

class UserregistrationForm(forms.ModelForm):

    class Meta:

        model = User

        fields = ['username','first_name','last_name','password','email']

    # username = forms.CharField(max_length=20)

    # first_name = forms.CharField(max_length=10)

    # last_name = forms.CharField(max_length=10)

    # email = forms.EmailField()

    # password =forms.CharField(max_length=20)