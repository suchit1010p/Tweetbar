from django.shortcuts import redirect
from django.urls import reverse

def home(request):
    return redirect(reverse('tweet_list'))