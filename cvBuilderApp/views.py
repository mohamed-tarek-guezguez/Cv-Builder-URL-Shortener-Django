from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accountsApp.forms import updateTemplate
from django.contrib import messages

# Create your views here.
def home(request):

    context = {
        'title': 'Home Page',
    }

    if request.user.is_authenticated:
        if request.method == 'POST':
            temp = updateTemplate(request.POST, request.FILES, instance=request.user.profile)
            if temp.is_valid():
                temp.save()
                messages.success(request, f'Your Template has been Saved!')
                return redirect('/')
        else:
            temp = updateTemplate(instance=request.user.profile)
        
        context['temp'] = temp

    return render(request, 'home.ejs', context)

def Detail(request, slug):
    detail = User.objects.get(username=slug)
    template = detail.profile.template

    context = {
        'title': detail.profile.name,
        'detail': detail,
    }

    return render(request, template, context)
