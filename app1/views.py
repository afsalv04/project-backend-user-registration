from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import UserProfile,Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def members(request):
    return HttpResponse("Hello World")


def afsal(request):
    return HttpResponse("hello Afsal")


def  index(request):
    return render (request,"index.html")

# def user_login(request):
#     return render (request,"login.html")

# def signup(request):
#     return render (request,"signup.html")

def shop(request):
    return render (request,"shop.html")

def services(request):
    return render (request,"services.html")

def contactus(request):
    return render (request,"contactus.html")

def checkout(request):
    return render (request,"checkout.html")

def cart(request):
    return render (request,"cart.html")

# def singleproduct(request):
#     return render (request,"singleproduct.html")

def thankyou(request):
    return render (request,"thankyou.html")

def about(request):
    return render (request,"about.html")










def signup(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Basic validation
        if password != confirm_password:
            return render(request, 'signup.html', {'error_message': 'Passwords do not match'})

        # Check if username (which is email) already exists
        if User.objects.filter(username=email).exists():
            return render(request, 'signup.html', {'error_message': 'Email already exists'})

        try:
            # Create user, setting username to email
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = fullname
            user.save()

            # Create profile linked to user
            UserProfile.objects.create(user=user, mobile=mobile)

            # Log the user in immediately (optional)
            login(request, user)

            # Redirect to login page or home page as you want
            return redirect('user_login')

        except Exception as e:
            # Log the error for debugging and show a friendly message
            print(f"Error creating user or profile: {e}")
            return render(request, 'signup.html', {'error_message': 'An error occurred during registration. Please try again.'})

    # If GET request, just render signup form
    return render(request, 'signup.html')



def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # authenticate expects username, which you set as email
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid email or password'})

    return render(request, 'login.html')


def home(request):
    return render(request, 'index.html')



def  single1(request):
    return render (request,"single1.html")



def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html',{'products':products})


def singleproduct(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'singleproduct.html', {'product': product})




