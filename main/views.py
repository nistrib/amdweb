# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
#
# from main.models import Project
#
# def login_view(request):
#     hardcoded_password = "1234"
#
#     if request.method == "POST":
#         password = request.POST.get("password")
#         if password == hardcoded_password:
#             request.session['logged_in'] = True  # Save login state in session
#             return redirect('home')
#         else:
#             return HttpResponse("Invalid password. Please try again.", status=403)
#
#     return render(request, 'login.html')
#
# def home(request):
#     if not request.session.get('logged_in'):
#         return redirect('login')
#     # Render your home page here
#     return render(request, 'home.html')
#
# def project_control_center(request):
#     return render(request, 'project_control_center.html')
#
#
# def about(request):
#     return render(request, 'about.html')
#
#
# # Arduino Code for Button Turn ON, OFF
# arduino_status = {"status": "OFF"}
#
#
# def update_status(request):
#     # Update status based on button press
#     global arduino_status
#     command = request.GET.get('command')
#     if command in ["ON", "OFF"]:
#         arduino_status["status"] = command
#     return JsonResponse({"status": arduino_status["status"]})
#
# def get_status(request):
#     # Return the current status to the Arduino
#     return JsonResponse(arduino_status)


from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from main.models import Project

def login_view(request):
    hardcoded_password = "1234"

    if request.method == "POST":
        password = request.POST.get("password")
        if password == hardcoded_password:
            request.session['logged_in'] = True  # Save login state in session
            return redirect('home')
        else:
            messages.error(request, 'Invalid password. Please try again.')

    return render(request, 'login.html')

def home(request):
    if not request.session.get('logged_in'):
        return redirect('login')
    # Render your home page here
    return render(request, 'home.html')

def project_control_center(request):
    return render(request, 'project_control_center.html')

def about(request):
    return render(request, 'about.html')

# Arduino Code for Button Turn ON, OFF
arduino_status = {"status": "OFF"}

def update_status(request):
    # Update status based on button press
    global arduino_status
    command = request.GET.get('command')
    if command in ["ON", "OFF"]:
        arduino_status["status"] = command
    return JsonResponse({"status": arduino_status["status"]})

def get_status(request):
    # Return the current status to the Arduino
    return JsonResponse(arduino_status)
