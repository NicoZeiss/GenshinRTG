from django.contrib import admin

from .models import Element, Character, WeaponType, Rarity


class ElementAdmin(admin.ModelAdmin):
    list_display = ('label', 'slug',)
    exclude = ('slug',)


class RarityAdmin(admin.ModelAdmin):
    list_display = ('label', 'slug', 'rate',)
    exclude = ('slug',)


class WeaponTypeAdmin(admin.ModelAdmin):
    list_display = ('label', 'slug',)
    exclude = ('slug',)


class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'element', 'rarity', 'weapon_type', 'slug',)
    list_editable = ('element',)
    exclude = ('slug',)


admin.site.register(Element, ElementAdmin)
admin.site.register(Rarity, RarityAdmin)
admin.site.register(WeaponType, WeaponTypeAdmin)
admin.site.register(Character, CharacterAdmin)
