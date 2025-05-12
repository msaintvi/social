from django.apps import AppConfig


class SocialConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'social'
    
    def ready(self):
        from . import seed  # You will create this next
        seed.run()
