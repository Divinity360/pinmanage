"""djangopinmgmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('polls/', include('polls.urls')),

    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("forgotpass1/", views.forgotpass1, name="forgotpass1"),
    path("confirmpass/", views.forgotpass2, name="confirmpass"),
    path("emailverify/", views.emailverify, name="emailverify"),
    path("unsoldpins/", views.unsoldpins, name="unsoldpins"),
    path("soldpins/", views.soldpins, name="soldpins"),
    path("payment/", views.payment, name="payment"),
    path("userprofile/", views.userprofile, name="userprofile"),
    path("settings/", views.settings, name="settings"),
    path("history/", views.history, name="history"),
    path("wallet/", views.wallet, name="wallet"),
    path("updatecard/", views.updatecard, name="updatecard"),
    path("deletepin/<int:pk>", views.deletepin, name="deletepin")
]
