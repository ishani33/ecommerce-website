from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from allauth.account.forms import SignupForm


# Create your views here.
def home(request):
    #context=locals() ----> puts everything in each view's context so we don't prefer using locals. The lack of specificity is the major drawback while using locals.
    context={}
    template='home.html'
    return render(request,template,context)

def about(request):
    context={}
    template='about.html'
    return render(request,template,context)

@login_required
def userProfile(request):
    user = request.user
    context={'user':user}
    template='profile.html'
    return render(request,template,context)
