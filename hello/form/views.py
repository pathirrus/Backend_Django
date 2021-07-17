from django.shortcuts import render
from form.models import Message
from django.shortcuts import redirect
from form.forms import ContactForm
from form.forms import MessageForm



# Create your views here.


# Formularz HTML
def contact1(request):
    if request.POST:
        data = request.POST
        if "%" in data.get('name'):
            return redirect('form:contact1')

        Message.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            category=data.get('category'),
            subject=data.get('subject'),
            body=data.get('body')
        )

        return redirect('form:contact1')

    return render(
        request,
        'form/contact1.html',
    )


# Formularze DJANGO:

def contact2(request):
    if request.method == "POST":
        form = ContactForm(request.POST)        #forma związana
        if form.is_valid():
            data = form.cleaned_data

            Message.objects.create(
                name=data.get('name'),
                email=data.get('email'),
                category=data.get('category'),
                subject=data.get('subject'),
                body=data.get('body')
            )
        return redirect('form:contact2')   #forma niezwiązana

    form = ContactForm()

    return render(
        request,
        'form/contact2.html',
        context={
            'form': form,
        }
    )


# Django Model Form
def contact3(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        form.save()
        return redirect("form:contact3")

    form = MessageForm()  # unbound form

    return render(
        request,
        'form/contact3.html',
        context={
            'form': form,
        }
    )