from urllib import request
from django.shortcuts import get_object_or_404, render
from .models import About

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

    return render(
        request,
        "about/about.html",
        {"about": about_queryset},
    )
