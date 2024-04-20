from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Product
from BabyBoutique import models,forms
from django.contrib.auth import logout
from  BabyBoutique.models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


from django.views.generic import View



# Create your views here.


def home_view(request):
    return render(request,'home.html')



def shop(request):
    return render(request, 'shop.html')



def admin_login(request):
    if request.method == 'POST':
        # Process form submission here
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticate user or perform other actions
        
        return render(request, 'admin_dashboard.html')  # Redirect to admin dashboard after login
    else:
        return render(request, 'admin_login.html')


# def customer(request):
#     return render(request, 'customer.html')

from django.shortcuts import render


def product_view(request):
    return render(request, 'product_view.html')

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')



def booking(request):
    products = Product.objects.all()  # Retrieve all products from the database
    return render(request, 'booking.html', {'products': products})

def booking_confirmation_view(request):
    # Process booking confirmation logic here
    # This view can be used to display a confirmation message after submitting the booking form
    return render(request, 'booking_confirmation.html')



from django.views.generic import TemplateView

class AboutUsView(TemplateView):
    template_name = 'aboutus.html'



class ContactUsView(View):
    template_name = "contactus.html"

    def get(self, request):
        return render(request, self.template_name)


def cart_view(request):
    product_count_in_cart = 0
    products = None
    total = 0

    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']

        if product_ids:
            product_id_in_cart = [int(pid) for pid in product_ids.split('|') if pid.isdigit()]

            if product_id_in_cart:
                products = models.Product.objects.filter(id__in=product_id_in_cart)
                product_count_in_cart = len(set(product_id_in_cart))

                for p in products:
                    total += p.price

    return render(request, 'cart.html', {'products': products, 'total': total, 'product_count_in_cart': product_count_in_cart})


from django.shortcuts import redirect, get_object_or_404
from .models import Product

def add_to_cart_view(request, product_id):
    # Retrieve the product object
    product = get_object_or_404(Product, pk=product_id)
    
    # Retrieve the cart from session or create a new one if it doesn't exist
    cart = request.session.get('cart', [])
    
    # Add the product to the cart
    cart.append({
        'id': product.id,
        'name': product.name,
        'price': product.price,
        # Add other product details if needed
    })
    
    # Update the session variable
    request.session['cart'] = cart
    
    # Redirect back to the previous page or any specific page
    return redirect('previous-page-url')

def customer_address_view(request):
    product_in_cart=False
    if 'product_ids' in request.COOKIES:
        product_ids=request.COOKIES['product_ids']
        if product_ids !="":
            product_in_cart=True

    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter = product_ids.split('|')
        product_count_in_cart = len(set(counter))
    else:
        product_count_in_cart = 0

    addressForm=forms.AddressForm()

    if request.method == 'POST':
        addressForm = forms.AddressForm(request.POST)
        if addressForm.is_valid():
            Email= addressForm.cleaned_data['Email']
            Mobile= addressForm.cleaned_data['Mobile']
            Address= addressForm.cleaned_data['Address']
            total=0
            if 'product_ids' in request.COOKIES:
                product_ids=request.COOKIES['product_ids']
                if product_ids !="":
                    product_id_in_cart=product_ids.split('|')
                    products=models.Product.objects.all().filter(id__in=product_id_in_cart)
                    for p in products:
                        total=total+p.price
            response = render(request,'payment.html',{'total':total})
            response.set_cookie('Email',Email)
            response.set_cookie('Mobile',Mobile)
            response.set_cookie('Address',Address)
            return response
    return render(request, 'customer_address.html', {'addressForm':addressForm,'product_in_cart':product_in_cart,'product_count_in_cart':product_count_in_cart})



def admin_add_product(request):
    productForm=forms.ProductForm()
    if request.method=='POST':
        productForm=forms.ProductForm(request.POST, request.FILES)
        if productForm.is_valid():
            productForm.save()
        return HttpResponseRedirect('product_view')
    return render(request,'admin_add_product.html',{'productForm':productForm})

def product_view(request):
    products = Product.objects.all()
    return render(request, 'product_view.html', {'products': products})


def delete_product(request,pk):
    products=models.Product.objects.get(id=pk)
    products.delete()
    return redirect('product_view')



from django.http import HttpResponse

def payment(request):
    # This view function could render the payment page HTML template
    return render(request, 'payment.html')

def process_payment(request):
    if request.method == 'POST':
        # Handle payment processing here
        # You can access form data using request.POST.get('field_name')
        # Implement payment processing logic, e.g., charging the card, updating database, etc.
        return HttpResponse('Payment processed successfully')  # Return a success message or redirect to a thank you page
    else:
        return HttpResponse('Method not allowed', status=405)  # Return a method not allowed error if accessed via GET


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('customer_dashboard')  # Assuming 'orders' is the name of the URL pattern for displaying orders
        else:
            # Handle invalid login credentials
            return render(request, 'login.html', {'error_message': 'Invalid email or password'})
    else:
        return render(request, 'login.html')
    



from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a thank you page or any other page after successful signup
            return HttpResponseRedirect('/thank-you/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})




# In your views.py file
from django.shortcuts import redirect
from django.contrib import messages

def addToCartView(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        
        # Add logic to add item to the cart based on product_id and quantity
        
        # For example, you can use Django's session to store cart items temporarily
        cart = request.session.get('cart', {})
        cart[product_id] = int(quantity)
        request.session['cart'] = cart
        
        messages.success(request, 'Item added to cart successfully.')
        return redirect('order_view')
    else:
        return redirect('order_view')



def order_page(request):
    return render(request, 'order.html')




from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm

def admin_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    return redirect('admin_base')  # Replace 'admin_dashboard' with your admin dashboard URL name
                else:
                    error_message = 'You do not have permission to access this page.'
            else:
                error_message = 'Invalid username or password.'
    else:
        form = LoginForm()
        error_message = None
    return render(request, 'adminlogin.html', {'form': form, 'error_message': error_message})



def afterlogin_view(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='customer').exists():
            return redirect('customer-home')
        else:
            return redirect('admin-bashboard')  # Replace 'admin_base' with the appropriate URL name for admin dashboard
    else:
        return redirect('admin_login')  # Redirect to admin login if user is not authenticated

def adminclick_view(request):
    if request.method == 'POST':
        # Process form data, authenticate user, etc.
        # Assuming authentication is successful
        return redirect('afterlogin')  # or redirect to admin panel
    else:
        # Render the login form
        return render(request, 'adminlogin.html')



from django.shortcuts import render, redirect
from .forms import TrackingDetailForm

def add_tracking_details(request):
    if request.method == 'POST':
        form = TrackingDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tracking_details')  # Redirect to a success URL
    else:
        form = TrackingDetailForm()
    return render(request, 'admin_add_tracking.html', {'form': form})


from .models import TrackingDetail

def tracking_details(request):
    # Retrieve all tracking details from the database
    tracking_details = TrackingDetail.objects.all()
    # Render the HTML template with the tracking details
    return render(request, 'tracking_details.html', {'tracking_details': tracking_details})    



def track_shipment(request):
    if request.method == 'POST':
        tracking_number = request.POST.get('tracking_number')
        # Here you can implement logic to retrieve tracking information
        # based on the provided tracking number and pass it to the template
        tracking_info = get_tracking_info(tracking_number)  # Implement this function
        return render(request, 'tracking.html', {'tracking_info': tracking_info})
    else:
        return render(request, 'tracking.html')


