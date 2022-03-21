from django.shortcuts import render
from .models import Pet

# Create your views here.

#View for the index page
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_pets = Pet.objects.all().count()
    recent_pets = Pet.objects.all().order_by('-id')[:10]

    context = {
        'num_pets': num_pets,
        'recent_pets': recent_pets,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
