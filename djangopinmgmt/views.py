from django.shortcuts import render
from .models import Pin


def index(request):
    return render(request, "index.html")


def signup(request):
    return render(request, "signup.html")


def forgotpass1(request):
    return render(request, "forgotpass1.html")


def forgotpass2(request):
    return render(request, "confirmpass.html")


def emailverify(request):
    return render(request, "emailverify.html")


def soldpins(request):
    return render(request, "soldpins.html")


def unsoldpins(request):
    mtn100pins = Pin.objects.filter(network='MTN', value='100')
    mtn200pins = Pin.objects.filter(network='MTN', value='200')
    mtn500pins = Pin.objects.filter(network='MTN', value='500')
    mtn1000pins = Pin.objects.filter(network='MTN', value='1000')
    mtn1500pins = Pin.objects.filter(network='MTN', value='1500')
    mtn2000pins = Pin.objects.filter(network='MTN', value='2000')

    context = {
        'mtn100pins': mtn100pins,
        'mtn200pins': mtn200pins,
        'mtn500pins': mtn500pins,
        'mtn1000pins': mtn1000pins,
        'mtn1500pins': mtn1500pins,
        'mtn2000pins': mtn2000pins,
    }
    return render(request, "unsoldpins.html", context)


def userprofile(request):
    return render(request, "userprofile.html")
