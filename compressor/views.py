from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import FormCompressor
from .models import ImageCompressor

# Create your views here.
def index(request):
    if request.POST:
        form = FormCompressor(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Image berhasil di compress!")
        else:
            messages.error(request, "Terjadi kesalahan.")
    else:
        form = FormCompressor()

    context = {
        'form': form
    }
    return render(request, 'index.html', context)