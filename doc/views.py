from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from doc.models import USERPROFILE, PATIENTDETAILS

def index(request):
    """Create a new user using custom user model we created using below function"""
    USER = USERPROFILE.objects.all()
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        if password1 == password2:
            password = request.POST.get('password1', '')
        else:
            messages.error(request, "Account not created.Entered Password does not match with confirm password")
            return redirect("doc:home")
        newuser = USERPROFILE.objects.create_user(email=email, name=name, password=password)
        messages.success(request, "Your registeration has been successfull. Please login!")
        return redirect("doc:home")

    return render(request, 'home.html')


def handlelogin(request):
    if request.method == "POST":
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Your login is successful.")
            return redirect("doc:patient")
        else:
            messages.error(request, "Invalid id or password")
            return redirect("doc:home")
    else:
        return HttpResponse('404 - Not found')


def handlelogout(request):
    logout(request)
    messages.success(request, "Your have successfully logged out")
    return redirect("doc:home")


def patient(request):
    if request.method == "POST":
        first_name = request.POST.get('inputname', '')
        last_name = request.POST.get('inputlname', '')
        full_name = request.POST.get('inputname', '') + " " + request.POST.get('inputlname', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        age = request.POST.get('age', '')
        gendermale = request.POST.get('gendermale', 'off')
        print(gendermale)
        genderfemale = request.POST.get('genderfemale', 'off')
        print(genderfemale)
        address_line1 = request.POST.get('inputAddress', '')
        address_line2 = request.POST.get('inputAddress2', '')
        city = request.POST.get('inputCity', '')
        state = request.POST.get('state', '')
        country = request.POST.get('country', '')
        postal_Code = request.POST.get('inputZip', '')
        disease = request.POST.get('disease', '')
        prescription = request.POST.get('prescription', '')
        prescription_date = request.POST.get('prescription_date', '')
        sex = ""
        if gendermale == 'on':
            sex = "Male"
        elif genderfemale == 'on':
            sex = "Female"
        print(sex)


        patient = PATIENTDETAILS(first_name=first_name, last_name=last_name, full_name=full_name,
                                 email=email, phone=phone, age=age, sex=sex, address_line1=address_line1,
                                 address_line2=address_line2, city=city, state=state, country=country, postal_Code=postal_Code,
                                 disease=disease, prescription=prescription, prescription_date=prescription_date)
        patient.save()
        return redirect("doc:patient")
    return render(request, 'patient.html')

def search(request):
    name = request.GET['search_inputname']
    phone = request.GET['search_phone']
    all_patients = PATIENTDETAILS.objects.filter(full_name=name, phone=phone)
    params = {'all_patients': all_patients}

    return render(request, 'search.html', params)


