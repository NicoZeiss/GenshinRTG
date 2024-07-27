from django.apps import AppConfig


class GenshinAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'genshin_app'

    def ready(self) -> None:
        import genshin_app.signals
