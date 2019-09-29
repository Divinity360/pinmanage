from django.shortcuts import render


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
    return render(request, "unsoldpins.html")

def userprofile(request):
    return render(request, "userprofile.html")

