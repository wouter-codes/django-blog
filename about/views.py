from urllib import request
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from .models import About
from .forms import CollaborateRequestForm

# Create your views here.
def about_page(request):
    """
    Display the About page.

    **Context**

    ``about``
        The first (and only) instance of :model:`about.About`.

    **Template:**

    :template:`about.html`
    """
    about_queryset = About.objects.all().order_by('-updated_on').first()

    if request.method == "POST":
        collaborate_form = CollaborateRequestForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received! I endeavour to respond within 2 working days.'
            )

    collaborate_form = CollaborateRequestForm()

    return render(
        request,
        "about/about.html",
        {"about": about_queryset,
         "collaborate_form": collaborate_form,
         },
    )
