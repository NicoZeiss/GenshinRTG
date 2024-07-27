from django.db.models.signals import post_migrate
from django.dispatch import receiver

from . import settings as app_settings
from .models import Element, WeaponType, Rarity





@receiver(post_migrate)
def populate_data(sender, **kwargs):
    if sender.name == 'genshin_app':
        for element in app_settings.GENSHIN_ELEMENTS:
            Element.objects.get_or_create(label=element)

        for weapon_type in app_settings.GENSHIN_WEAPON_TYPES:
            WeaponType.objects.get_or_create(label=weapon_type)

        for rarity in app_settings.GENSHIN_RARITIES:
            Rarity.objects.get_or_create(label=rarity['label'], rate=rarity['rate'])
