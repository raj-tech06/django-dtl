from django.shortcuts import render
from django.http import HttpResponse
from .models import Student


def home(request):
    return render(request, "home.html")
    # return HttpResponse('raj')

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def register(request):
    return render(request, "register.html")


def registerdata(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        detail = request.POST.get('detail')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        subscribe = request.POST.getlist('subscribe')
        gender = request.POST.get('gender')
        image = request.FILES.get('profile-pic')
        file = request.FILES.get('resume')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if Student.objects.filter(Stu_email=email).exists():
            msg = "User already exists!"
            return render(request, 'register.html', {'msg': msg})

        if password == cpassword:
            student = Student(
                Stu_name=username,
                Stu_email=email,
                Stu_dis=detail,
                Stu_contact=phone,
                Stu_dob=dob,
                Stu_qualification=",".join(subscribe), 
                Stu_gender=gender,
                Stu_image=image,
                Stu_document=file,
                Stu_password=password
            )
            student.save()
            msg = "Registration successful!"
            return render(request, 'login.html', {'msg': msg})
        else:
            msg = "Password and Confirm Password do not match."
            userdata = {
                "username": username,
                "email": email,
                "detail": detail,
                "phone": phone,
                "dob": dob,
                "subscribe": subscribe,
                "gender": gender,
                "image": image,
                "file": file,
            }
            return render(request, 'register.html', {'msg': msg, 'data': userdata})

    return render(request, 'register.html')

def login(request):
    return render(request, "login.html")


def loginuser(request):
    if request.method == 'POST':
        e = request.POST.get('email')
        p = request.POST.get('password')
        user =Student.objects.filter(Stu_email=e)

        if user:
            userdata=Student.objects.get(Stu_email=e)
            # print(userdata.Stu_name)
            # print(userdata.Stu_password)
            # print(userdata.Stu_email)
            # print(userdata.Stu_contact)
            # print(userdata.Stu_dob)
            # print(userdata.Stu_qualification)
            print(userdata.Stu_contact)

            userdata2={
                'name':userdata.Stu_name,
                'pass':userdata.Stu_password,
                'email':userdata.Stu_email,
                'contact':userdata.Stu_contact,
                'dob':userdata.Stu_dob,
                'pic':userdata.Stu_image,
            }


            p1= userdata.Stu_password

            if p == p1:
                return render(request, 'dashboard.html',{ 'msg': "Login successful!",'userdata':userdata2})
            else:
                pmsg = "Invalid password!"
                return render(request, 'login.html', {'pmsg': pmsg})
        else:
            msg = "Invalid email!"
            return render(request, 'register.html', {'msg': msg})  
    else:
        return render(request, 'login.html')      

      
    # return render(request, "login.html")
    pass


def dashboard(request):
    return render(request, "dashboard.html")
    # return HttpResponse('raj')