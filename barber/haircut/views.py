from django.shortcuts import render
from django.shortcuts import render
from .models import Haircut
from .forms import ContactForm
from . import forms
# Create your views here.
def index(request):
    barb = Haircut.objects.all()


    return render(request, "haircut/index.html",{"barb":barb})

def contact(request):

    form = forms.ContactForm()
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.save()
            return index(request)
    else:
        form = ContactForm

    return render(request, 'haircut/contact.html',{"form":form})


def gallery(request):

    return render(request, 'haircut/gallery.html')


def about(request):

    return render(request, 'haircut/about.html')

def price(request):

    return render(request, 'haircut/price.html')
