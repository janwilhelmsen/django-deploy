from django.shortcuts import render
from basic_app.forms import VillageForm,PersonForm,VillagePopupForm,StaffForm,UserForm
from basic_app.models import Person

#Login function
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    return render(request,'basic_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def admin(request):
    return render(request,'basic_app/admin.html')

@login_required
def person(request):
    personlst= Person.objects.order_by('lastname')
    #print (personlst)
    person_dict = {'person':personlst}
    #print (person_dict)
        #
        # user_list = Userlist.objects.order_by('first_name')
        # user_dict = {"users":user_list}

    return render(request,'basic_app/person.html',context=person_dict)

@login_required
def registration(request):

    missing_village = True
    person = PersonForm()
    if request.method=='POST':
        person = PersonForm(data=request.POST)

        if person.is_valid():
            person.save(commit=True) # = PersonForm.save(commit=True)
            person = PersonForm()
            return render(request,'basic_app/registration.html',{'person':person})
        else:
            print (person.errors)
    else:
        return render(request,'basic_app/registration.html',{'person':person})

@login_required
def patient(request):
    return render(request,'basic_app/patient.html')

@login_required
def pharmacy(request):
    return render(request,'basic_app/pharmacy.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)

            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponse("Account not active")
            print ("Username:  {} and Password {}".format(username,Password))
            return HttpResponse("invalid Login details supplied")
            return render(request,'basic_app/login.html')
    else:
        return render(request,'basic_app/login.html',{})


@login_required
def villages(request):
    villages_form = VillageForm()
    if request.method=='POST':
        print ("POSTING")
        villages_form = VillageForm(data=request.POST)
        #print (villages_form)
        if villages_form.is_valid():
            print (villages_form.cleaned_data['name'])
            village=villages_form.save(commit=True)
            villages_form=VillageForm()
            return render(request,'basic_app/village.html',{'villages_form':villages_form})
    else:
        return render(request,'basic_app/village.html',{'villages_form':villages_form})

@login_required
def villagespop(request):
    popupform=VillagePopupForm()
    if request.method=='POST':
        popupform=VillageForm(data=request.POST)
        if popupform.is_valid():
            popupform.save(commit=True)
            return render(request,'basic_app/villages_added.html')
    else:
        return render(request,'basic_app/villagespop.html',{'popupform':popupform})

@login_required
def staff(request):
    registered = False
    staffmember_dict=StaffForm()
    user_form_dict=UserForm()

    if request.method == 'POST':
        staffmember_dict = StaffForm(data=request.POST)
        user_form_dict = UserForm(data=request.POST)

        if staffmember_dict.is_valid() and user_form_dict.is_valid():
            user = user_form_dict.save()
            user.set_password(user.password)
            user.save()

            staffmember = staffmember_dict.save(commit=False)
            staffmember.user = user

            if 'profil_pic' in request.FILES:
                staffmember.profil_pic = request.FILES['profil_pic']
            staffmember.save()

            registered=True
        else:
            print (staffmember.errors,user.errors)
    else:
        staffmember_dict = StaffForm()
        user_form_dict = UserForm()



    return render(request,'basic_app/staff-reg.html',{'staffmember_dict':staffmember_dict,'user_form_dict':user_form_dict})

# def user(request):
#     user_form=UserForm()
#     return render(request,'basic_app/staff-reg.html',{'user_form':user_form})
