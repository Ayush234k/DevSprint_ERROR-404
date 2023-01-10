<<<<<<< Updated upstream
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_backend.settings')

=======
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_backend.settings')

>>>>>>> Stashed changes
application = get_asgi_application()