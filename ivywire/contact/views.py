# Create your views here.
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('name', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['name'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['ivywireline@gmail.com'],
            )
            return HttpResponseRedirect('/contact/')
    return render(request, 'contact.html', {
        'errors': errors,
        'name': request.POST.get('name', ''),
        'message': request.POST.get('message', ''),
        'email': request.POST.get('email', ''),
    })
