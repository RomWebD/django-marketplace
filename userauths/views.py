from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.conf import settings

# Create your views here.
from userauths.forms import UserRegisterForm

User = settings.AUTH_USER_MODEL


def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Hey {username}, You account was created successfully"
            )
            new_user = authenticate(
                username=form.cleaned_data["email"],
                password=form.cleaned_data["password1"],
            )
            login(request, new_user)
            return redirect("core:index")

        context = {"form": form}
        return render(request, "userauths/sign-up.html", context)

    else:
        form = UserRegisterForm()

        context = {"form": form}
        return render(request, "userauths/sign-up.html", context)


def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, "Hey you are already Loggen in.")
        return redirect("core:index")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.object.get(email=email)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You are logged in")
                return redirect("core:index")
            else:
                messages.warning(request, "User Does Not Exist, create an account.")
        except:
            messages.warning(request, f"User with {email} does not exist")

    context = {}
    return render(request, "userauths/sign-in.html", context)


def logout_view(
    request,
):
    logout(request)
    messages.success(request, "You logged out.")
    return redirect("userauths:sign-in")
