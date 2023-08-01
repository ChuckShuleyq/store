from django.http import Http404
from django.shortcuts import redirect

def page_not_found_view(request):
    return redirect('home')