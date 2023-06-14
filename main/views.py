from django.shortcuts import render, redirect
from .models import UserMessage, Category, Projects


def IndexView(request):
    if request.method == 'POST':
        post_name = request.POST.get('name')
        post_email = request.POST.get('email')
        post_subject = request.POST.get('subject')
        post_message = request.POST.get('message')
        
        add = UserMessage(name = post_name,
                          email = post_email,
                          subject = post_subject,
                          message = post_message,
        )
        add.save()
        return redirect('/')
    
    projects = Projects.objects.all()
    category = Category.objects.all()
    context = {
        'projects': projects,
        'category': category
    }
    
    return render(request, 'main/index.html', context=context)
