from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile

def upload_image(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ProfileForm()
    return render(request, 'iapp/upload.html', {'form': form})


def image_list(request):
    profiles = Profile.objects.all()
    return render(request, 'iapp/image_list.html', {'profiles': profiles})
