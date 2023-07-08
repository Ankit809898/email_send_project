from django.shortcuts import render, redirect
from .forms import EmailForm
from django.core.mail import EmailMessage
from .models import Email


def Email_view(request):
    form = EmailForm()
    if request.method == "POST":
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            subject = "WELCOME MAIL"
            message = "-------------"
            attach = form.cleaned_data.get('attach')
            recepient = request.POST['email']
            form.save()
            var = EmailMessage(
                subject,
                message,
                "yogeshdadure258@gmail.com",
                [recepient],
            )
            var.attach(attach.name, attach.read(), attach.content_type)
            var.send()
            return redirect('email_url')
    template_name = 'crud_app/add_email.html'
    context = {'form': form}
    return render(request, template_name, context)
