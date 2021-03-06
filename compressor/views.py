from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import FormCompressor
from .models import ImageCompressor

# Create your views here.
def index(request):
    context = {}
    img_count = ImageCompressor.objects.all().count() + 1

    if request.POST:
        form = FormCompressor(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Image berhasil di compress!")

            if 'submit' in request.POST:
                img_data = ImageCompressor.objects.filter(id=img_count)
                context.update({'img_data': img_data})

        else:
            messages.error(request, "Terjadi kesalahan.")
    else:
        form = FormCompressor()

    context.update({
        'form': form,
    })
    return render(request, 'index.html', context)