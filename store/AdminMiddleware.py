from django.shortcuts import redirect
from django.urls import resolve
from django.urls import reverse
from django.http import HttpRequest, Http404
class RestrictAdminLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        if not request.user.is_superuser and request.path == '/admin/':
            # Redirect non-admin users to a different page
            return redirect(reverse('product:home'))  # Change 'home' to the URL name of the desired page
        response = self.get_response(request)
        return response




