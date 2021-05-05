from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
import PIL
from PIL import Image

# Create your views here.
def index(request):
    asd = 'This is Rafli'
    context = {
        'a': asd
    }
    
    return render(request, 'index.html', context)