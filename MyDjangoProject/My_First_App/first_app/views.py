from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import  Topic, WebPage, Employee
from .import forms
from first_app.forms import Employee_Login_From,UserForm,UserProfileInfoForm

#import for Login functionalities
from django.contrib.auth import  authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import  login_required


# Create your views here.
'''
def index(request):
    return HttpResponse('Hello world!!!')
'''
def index(request):
    my_dict={'insert_me': "Hello I am from views.py !!!"}
    #return render(request, 'index.html', context=my_dict)
    return render(request, 'index.html')



def rockUs(request):
    return render(request, 'first_app/rockTheWorld.html')

def DemoView(request):
    webpage_list= WebPage.objects.order_by('name')
    webpage_dict = {"WebPage_Records": webpage_list}



    return render(request, 'first_app/DemoView.html',context=webpage_dict)

# We have one class 'MyReg_Form' in forms.py. Now we have included forms.py, and we can
#create the instance of the class 'MyReg_Form' like in the below view method
def MyRegView(request):
    form_obj1 = forms.MyReg_Form(request.POST)
    if request.method == 'POST' and form_obj1.is_valid():

        print("Form is valid")
        print("Name Entered - "+form_obj1.cleaned_data['name'])
        print("Email Entered - "+form_obj1.cleaned_data['email'])
        print("Text input - "+form_obj1.cleaned_data['text'])


        '''
        #if form_obj.is_valid():
            #print("Form is valid")
            #if Form is valid do something
        '''

        '''
        print("Validation successful")
        print("Data entered by user - \n")
        print(form_obj.Cleaned_data['name'])
        print(form_obj.Cleaned_data['email'])
        print(form_obj.Cleaned_data['text'])    
        '''




    else:
        print("Request type is Get")
        form_obj1 = forms.MyReg_Form()


    return render(request,'first_app/MyReg.html',{"form_key1": form_obj1})

def EmployeeLogin(request):
    form=Employee_Login_From
    if request.method=='POST':
        print("Request type is post")
        form= Employee_Login_From(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Form is Invalid")
    return render(request,'first_app/EmployeeLogin.html', {'form':form})

def PageOne(request):

    return render(request,'first_app/PageOne.html')

def PageTwo(request):

    return render(request,'first_app/PageTwo.html')
def Registration(request):
    registered= False
    if request.method == "POST":
        """
            Invoke both the forms 1.user_form  2.UserProfileInfoForm in the views
            in forms.py 
            1. UserForm is linked with django's default model User
            2. UserProfileInfoForm is linked with model UserProfileInfo which describes the two additional fields
        """
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            """
                The above line is actually relates to object reference 'user' defined in model.py by user = models.OneToOneField(User, on_delete='Cascade')
                
            """

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered=True
        else:
            print("Form is invalid. Errors - "+user_form.errors + profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()

    return render(request,'first_app/Registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered':registered,
                   })
def AppHomePage(request):
    Context_Dir= {"Line1": "This site is undergoing development. Thanks for being patient.",
                  "Line2": "This is a short note",
                  }
    return render(request,'first_app/AppHomePage.html',Context_Dir)

def user_login(request):
    if request.method == 'POST':
        username = request.Get('username')
        password = request.Get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active():
                login(request, user)
                return HttpResponseRedirect(reverse('AppHomePage'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Login Failed")
            print("Username: {} and Password:{}".format(username,password))
            print("Invalid credentials supplied")
    else:
        return render(request,'first_app/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('AppHomePage'))
