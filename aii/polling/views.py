from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ImageForm





def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'polling/pool.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'polling/pool.html', {'form': form})
