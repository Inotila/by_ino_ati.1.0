from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from art.models import Newsletter
from .forms import MailForm


def index(request):
    """
    render index view
    """
    if request.user.is_authenticated:
        user = get_object_or_404(User, username=request.user)
        submitted_form = Newsletter.objects.filter(user=user).count()
        mail_form = MailForm(request.POST, initial={'user': request.user})

        if request.method == "POST":
            if mail_form.is_valid():
                mail_form.instance.user = user
                mail_form.save()
                if request.POST.get("join"):
                    messages.success(
                        request,
                        "You have successfully joined the mailing list!")
                else:
                    messages.error(
                        request,
                        "You have select to not join the mailing list.")
                submitted_form = 1
    else:
        submitted_form = 0
        mail_form = MailForm()
    
    context = {
        "submitted_form": submitted_form,
        "mail_form": mail_form,
    }
    
    return render(request, 'home/index.html', context)
