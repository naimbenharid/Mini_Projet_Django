from django.shortcuts import render
from django.contrib.auth import login,authenticate
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm


from accounts.forms import UserRegistrationForm
# Create your views here.
def register_view(request):
 #   if request.user.is_authenticated:
    #    return redirect(reverse('locations_voitures:voiture_list'))
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('locations_voitures:voiture_list'))
    else:
        form = UserRegistrationForm()
    return render(
        request=request,
        template_name = "registration/signup.html",
        context={"form": form}
)


def login_view(request):
   # if request.user.is_authenticated:
     #   return redirect(reverse('locations_voitures:voiture_list'))
    
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect(reverse('locations_voitures:voiture_list'))
    else:  # Mettez l'instanciation du formulaire à l'extérieur du bloc else
        form = AuthenticationForm()

    return render(
        request=request,
        template_name="registration/login.html",
        context={"form": form}
    )