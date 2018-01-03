from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout

# django native user model
User = get_user_model()

# override native user login form
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    # validate form before submission ( custom validation )
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        
        # check if fields filled in
        if username and password:
            # authenticate user
            user = authenticate(username=username,password=password)
            #check if user exists
            if not user:
                raise forms.ValidationError("Wrong username/Password")
            # check if password of user is correct
            if not user.check_password(password):
                raise forms.ValidationError("Wrong username/Password")
            # check if user is active or blocked
            if not user.is_active:
                raise forms.ValidationError("Wrong username/Password")
        # if custom validation respected carry on with native submission and validation
        return super(UserLoginForm, self).clean(*args,*kwargs)

# override native user registration form
class UserRegisterForm(forms.ModelForm):
    # set password fields
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    class Meta:
        model = User
        # set fields to be used in registration form
        fields = ['username','email','password','password2']

    # validation for single field and not the whole form, error message to appear
    # with specified field
    def clean_password2(self):
        # get posted data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        # check if confirmed password and password match
        if password != password2:
            raise forms.ValidationError("Passwords do not match")
        return password

    # user email must be unique
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # check if account with email exists
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email address already exists')
        return email