from django import forms

class RegistrationForm(forms.Form):
    uname = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    pwd = forms.CharField(max_length=100, required=True)
    cpwd = forms.CharField(max_length=100, required=True)

def validate_form(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data["uname"]
            email = form.cleaned_data["email"]
            pwd = form.cleaned_data["pwd"]
            cpwd = form.cleaned_data["cpwd"]

            if uname == "":
                return "Username cannot be empty!"
            elif not uname.isalnum() or len(uname) < 4:
                return "User name field requires at least 6 letters and numbers"
            elif email == "":
                return "Email cannot be empty!"
            elif pwd == "":
                return "Please enter password"
            elif not pwd.isalnum() or len(pwd) < 8:
                return "Password must be at least 8 characters long and contain only letters and numbers"
            elif cpwd != pwd:
                return "Confirm Password not match"
            else:
                #submit the form
                return "Form submitted successfully"
        else:
            return "Invalid form data"
    else:
        form = RegistrationForm()
        return render(request, "registration_form.html", {"form": form})
