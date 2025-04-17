# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Student

# # Create your views here.

# def home(request):
#     # return HttpResponse("Hello")
#     return render(request, "home.html")

# def contact(request):
#     return render(request, "contact.html")

# def about(request):
#     return render(request, "about.html")

# def register(request):
#     return render(request, "register.html")

# def registerdata(request):
#     # print(request.method)
#     # print(request.POST)
#     # print(request.GET)
#     # print(request.FILES)
#     # print(request.COOKIES)
#     # print(request.META)
#     # print(request.SETTINGS)
#     username= request.POST.get('username')
#     email= request.POST.get('email')
#     detail= request.POST.get('detail')
#     phone= request.POST.get('phone')
#     dob= request.POST.get('dob')
#     subscribe= request.POST.getlist('subscribe')
#     gender= request.POST.get('gender')
#     image= request.POST.get('image')
#     file= request.POST.get('file')
#     password= request.POST.get('password')
#     cpassword= request.POST.get('cpassword')
    
#     print(username, email, detail, phone, dob, subscribe, gender, password, cpassword, file, image)
   
#     Student.objects.create(stu_name=username, stu_email=email, stu_dis=detail, stu_contact=phone, stu_dob=dob, stu_quali=subscribe, stu_gender=gender, stu_image=image, stu_file=file,stu_password=password)

    
#     user = Student.objects.filter(stu_email=email)
#     if user:
#         msg="User Already Exist"
#         return render (request, 'regster.html', {'msg':msg})
#     else :
#         if password==cpassword:
#             Student.objects.create(stu_email=email)
#             msg="Registration Successful!"
#             return render (request, 'login.html', {'msg':msg})
#         else:
#             msg="Password and Confirm Password not matched"
#             userdata={
#                 "username":username,
#                 "email":email,
#                 "detail":detail,
#                 "phone":phone,
#                 "dob": dob,
#                 "subscribe": subscribe,
#                 "gender": gender,
#                 "image": image,
#                 "file" :file,
#             }
#             return render(request, "regster.html",{msg:msg, "data":userdata})


# def login(request):
#     return render(request, "login.html")

#     if request.method=="POST":
#         email=request.POST.get("e.mail")
#         password=request.POST.get("password")





# def registerdata(request):
#     if request.method == 'POST':
#         student = Student(
#             stu_name=request.POST['stu_name'],
#             stu_email=request.POST['stu_email'],
#             stu_dis=request.POST['stu_dis'],
#             stu_contact=request.POST['stu_contact'],
#             stu_dob=request.POST['stu_dob'],
#             stu_qualification=request.POST['stu_quali'],
#             stu_gender=request.POST['stu_gender'],
#             stu_image=request.FILES.get('stu_image'),
#             stu_file=request.FILES.get('stu_file'),
#             stu_password=request.POST['stu_password'],
#         )
#         student.save()
#         # Any other logic
#     return render(request, 'your_template.html')















#         # from django.shortcuts import render
# # from django.http import HttpResponse
# # from .models import Student
# # from datetime import datetime


# # def home(request):
# #     return render(request,'home.html')

# # def contact(request):
# #     return render(request,'contact.html')

# # def register(request):
# #     return render(request,'register.html')

# # def login(request):
# #     return render(request,'login.html')

# # def about(request):
# #     return render(request,'about.html')

# # def registerdata(request):
# #     if request.method == 'POST':
# #         print(request.POST)
        
# #         name = request.POST.get('username')  
# #         email = request.POST.get('email')
# #         address = request.POST.get('address')
# #         dis = request.POST.get('dis')
# #         contact = request.POST.get('contact')
# #         dob = request.POST.get('dob')
# #         qualification = request.POST.get('qualification')
# #         gender = request.POST.get('gender')
# #         image = request.FILES.get('profile-pic')
# #         document = request.FILES.get('resume')
# #         password = request.POST.get('password')

# #         if not name:
# #             print("Name field is empty!")
        
# #         if dob:
# #             try:
# #                 dob = datetime.strptime(dob, '%Y-%m-%d').date()  # Convert string to date format
# #             except ValueError:
# #                 print("Invalid date format for DOB!")
# #                 dob = None  # Handle invalid date format case

# #         if name and dob:
# #             Student.objects.create(
# #                 Stu_name=name,
# #                 Stu_email=email,
# #                 Stu_address=address,
# #                 Stu_dis=dis,
# #                 Stu_contact=contact,
# #                 Stu_dob=dob,
# #                 Stu_qualification=qualification,
# #                 Stu_gender=gender,
# #                 Stu_image=image,
# #                 Stu_document=document,
# #                 Stu_password=password
# #             )
# #             return render(request, 'success.html')  # Optional success page
# #         else:
# #             print("Name or DOB is missing!")
# #             return render(request, 'register.html', {'error': 'Please fill in all required fields.'})  # Return with error
# #     else:
# #         return render(request, 'register.html')





from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.

def home(request):
    return render(request, "home.html")

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

        # Ensure no duplicate entries for the same email
        if Student.objects.filter(Stu_email=email).exists():
            msg = "User already exists!"
            return render(request, 'register.html', {'msg': msg})

        # Check if password and confirm password match
        if password == cpassword:
            student = Student(
                Stu_name=username,
                Stu_email=email,
                Stu_dis=detail,
                Stu_contact=phone,
                Stu_dob=dob,
                Stu_qualification=",".join(subscribe),  # Store as comma-separated string
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
