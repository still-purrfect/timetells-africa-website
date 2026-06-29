from .forms import QuoteRequestForm, ContactForm
from django.shortcuts import render
from .models import Service, Project, ContactMessage
from django.contrib import messages


def home(request):

    services = Service.objects.all()
    projects = Project.objects.all()

    context = {
        "services": services,
        "projects": projects,
    }

    return render(request, "core/home.html", context)


def about(request):
    """
    About Page
    """
    return render(request, "core/about.html")


def services(request):

    services = Service.objects.all()

    context = {
        "services": services
    }

    return render(request, "core/services.html", context)


def projects(request):

    projects = Project.objects.all()

    context = {
        "projects": projects
    }

    return render(request, "core/projects.html", context)


def contact(request):

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Thank you for contacting us. We have received your message and will get back to you soon."
            )

            form = ContactForm()

    else:

        form = ContactForm()

    return render(
        request,
        "core/contact.html",
        {
            "form": form
        }
    )

def quote(request):

    if request.method == "POST":

        form = QuoteRequestForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Thank you! Your quote request has been submitted successfully. We will contact you soon."
            )

            form = QuoteRequestForm()

    else:

        form = QuoteRequestForm()

    return render(request, "core/quote.html", {
        "form": form
    })


def careers(request):
    """
    Careers Page
    """
    return render(request, "core/careers.html")


def blog(request):
    """
    Blog Page
    """
    return render(request, "core/blog.html")

