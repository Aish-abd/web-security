from django.apps import AppConfig


class OtppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'otpp'
    def ready(self):
        import otpp.signals

 
