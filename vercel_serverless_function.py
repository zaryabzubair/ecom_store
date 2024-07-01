from django.core.handlers.wsgi import WSGIHandler
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse

# Set the Django settings module for Vercel deployment
settings.configure()

# Initialize Django application
application = get_wsgi_application()

# Handler function for incoming requests
def handler(request, *args, **kwargs):
    # Initialize Django's WSGI handler
    django_handler = WSGIHandler()

    # Pass request to Django application
    response = django_handler(request)

    # Return HTTP response to serverless function
    return HttpResponse(
        content=response.content,
        status=response.status_code,
        headers=response._headers.values(),
    )
