from django.shortcuts import render, redirect
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


def settings(request):
    return render(request, "soldpins.html")


def history(request):
    return render(request, "history.html")


def wallet(request):
    return render(request, "wallet.html")


def updatecard(request):
    return render(request, "updatecard.html")


def payment(request):
    return render(request, "payment.html")


def unsoldpins(request):
    mtn100pins = Pin.objects.filter(network='MTN', value='100')
    mtn200pins = Pin.objects.filter(network='MTN', value='200')
    mtn500pins = Pin.objects.filter(network='MTN', value='500')
    mtn1000pins = Pin.objects.filter(network='MTN', value='1000')
    mtn1500pins = Pin.objects.filter(network='MTN', value='1500')
    mtn2000pins = Pin.objects.filter(network='MTN', value='2000')

    glo100pins = Pin.objects.filter(network='GLO', value='100')
    glo200pins = Pin.objects.filter(network='GLO', value='200')
    glo500pins = Pin.objects.filter(network='GLO', value='500')
    glo1000pins = Pin.objects.filter(network='GLO', value='1000')
    glo1500pins = Pin.objects.filter(network='GLO', value='1500')
    glo2000pins = Pin.objects.filter(network='GLO', value='2000')

    eti100pins = Pin.objects.filter(network='ETISALAT', value='100')
    eti200pins = Pin.objects.filter(network='ETISALAT', value='200')
    eti500pins = Pin.objects.filter(network='ETISALAT', value='500')
    eti1000pins = Pin.objects.filter(network='ETISALAT', value='1000')
    eti1500pins = Pin.objects.filter(network='ETISALAT', value='1500')
    eti2000pins = Pin.objects.filter(network='ETISALAT', value='2000')

    airtel100pins = Pin.objects.filter(network='AIRTEL', value='100')
    airtel200pins = Pin.objects.filter(network='AIRTEL', value='200')
    airtel500pins = Pin.objects.filter(network='AIRTEL', value='500')
    airtel1000pins = Pin.objects.filter(network='AIRTEL', value='1000')
    airtel1500pins = Pin.objects.filter(network='AIRTEL', value='1500')
    airtel2000pins = Pin.objects.filter(network='AIRTEL', value='2000')

    context = {
        'mtn100pins': mtn100pins,
        'mtn200pins': mtn200pins,
        'mtn500pins': mtn500pins,
        'mtn1000pins': mtn1000pins,
        'mtn1500pins': mtn1500pins,
        'mtn2000pins': mtn2000pins,

        'glo100pins': glo100pins,
        'glo200pins': glo200pins,
        'glo500pins': glo500pins,
        'glo1000pins': glo1000pins,
        'glo1500pins': glo1500pins,
        'glo2000pins': glo2000pins,

        'eti100pins': eti100pins,
        'eti200pins': eti200pins,
        'eti500pins': eti500pins,
        'eti1000pins': eti1000pins,
        'eti1500pins': eti1500pins,
        'eti2000pins': eti2000pins,

        'airtel100pins': airtel100pins,
        'airtel200pins': airtel200pins,
        'airtel500pins': airtel500pins,
        'airtel1000pins': airtel1000pins,
        'airtel1500pins': airtel1500pins,
        'airtel2000pins': airtel2000pins,
    }
    return render(request, "unsoldpins.html", context)


# delete pin
def deletepin(request, pk):
    Pin.objects.filter(id=pk).delete()
    return redirect('/unsoldpins/')


def userprofile(request):
    return render(request, "userprofile.html")
