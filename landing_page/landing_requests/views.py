from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib import messages
# from django.core.mail import send_mail

from .forms import CreateReqeustForm


def index(request):
    template = 'main.html'
    return render(request, template)


def about(request):
    template = 'landing_page/about.html'
    return render(request, template)


def form_sent(request):
    template = 'landing_page/form_sent.html'
    return render(request, template)


def create_request(request):
    template = 'landing_page/offer.html'
    if request.method == 'POST':
        form = CreateReqeustForm(
            request.POST or None
        )
        if form.is_valid():
            if not request.POST.get('agreement', None) == None:
                data = form.save(commit=False)
                data.save()
                # subject = form.cleaned_data['msisdn']
                # message = form.cleaned_data['comments']
                # sender = 'sender@example.com'
                # email = form.cleaned_data['email']
                # recipient = []
                # recipient.append(email)
                # send_mail(subject, message, sender, recipient, fail_silently=False)
                return redirect('landing_requests:form_sent_page')
            else:
                messages.error(request, 'without your agreement, we will not be able to process the request')
                return redirect('landing_requests:offer_page')
    else:
        form = CreateReqeustForm()
    return(render(request, template, {'form': form}))
