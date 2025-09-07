from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages   # ✅ import messages
from .models import Profile

def signup_view(request):
    if request.method == 'POST':
        print("POST data:", request.POST)
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # check passwords match
        if password != confirm_password:
            return render(request, 'signup.html', {"error": "Passwords do not match"})

        if full_name and email and password:
            # ✅ create user (Django hashes automatically)
            user = User.objects.create_user(username=email, email=email, password=password)

            # ✅ save full_name in Profile
            Profile.objects.create(user=user, full_name=full_name)

            print("User created:", user.username)

            # ✅ show success message
            messages.success(request, "Successfully registered! Please sign in.")

            # ✅ redirect to signin
            # return redirect("/signin/")

    return render(request, 'signup.html')


# def signin_view(request):
#     print("Signin view called")
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         # ✅ authenticate using email (username=email since we set it like that above)
#         user = authenticate(request, username=email, password=password)

#         if user is not None:
#             login(request, user)
#             return render(request, 'signin.html', {"message": f"Welcome, {user.profile.full_name}!"})
#         else:
#             return render(request, 'signin.html', {"error": "Invalid credentials"})
def signin_view(request):
    print("Signin view called")
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # ✅ authenticate using email (username=email since we set it like that above)
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'signin.html', {"message": f"Welcome, {user.profile.full_name}!"})
        else:
            return render(request, 'signin.html', {"error": "Invalid credentials"})

    # ✅ This handles GET requests (e.g., when user first visits /signin/)
    return render(request, 'signin.html')

    # return render(request, 'diagnose.html')

from django.shortcuts import render

def diagnose_view(request):
    return render(request, 'diagnose.html')

from django.shortcuts import render

# # Home page
# def index_view(request):
#     return render(request, 'index.html')


# # Accounts
# def signin(request):
#     return render(request, 'accounts/signin.html')

# def signup(request):
#     return render(request, 'accounts/signup.html')

# # Diagnosis
# def diagnose(request):
#     return render(request, 'diagnosis/diagnose.html')
