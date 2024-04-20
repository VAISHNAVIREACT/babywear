from django import forms
from .models import Product
from django.core.validators import RegexValidator


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'image']
class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile = forms.CharField(max_length=15, validators=[RegexValidator(r'^\d+$', 'Enter a valid mobile number.')])
    Address = forms.CharField(max_length=500)


from .models import Customer

class SignUpForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']




class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)                  



from django import forms
from .models import TrackingDetail

class TrackingDetailForm(forms.ModelForm):
    class Meta:
        model = TrackingDetail
        fields = ['date', 'location', 'status']