from django.shortcuts import render

from .models import Character, Element, WeaponType, Rarity


# def index(request):
#     context = {
#         'characters': Character.objects.all(),
#     }
#     return render(request, 'genshin_app/pages/index.html', context=context)


def index(request):
    element_ids = request.GET.getlist('element', [str(element.id) for element in Element.objects.all()])
    weapon_ids = request.GET.getlist('weapon', [str(weapon.id) for weapon in WeaponType.objects.all()])
    rarity_ids = request.GET.getlist('rarity', [str(rarity.id) for rarity in Rarity.objects.all()])

    characters = Character.objects.all()

    characters = (characters
                  .filter(element_id__in=element_ids)
                  .filter(weapon_type_id__in=weapon_ids)
                  .filter(rarity_id__in=rarity_ids))

    context = {
        'characters': characters,

        'elements': Element.objects.all(),
        'weapons': WeaponType.objects.all(),
        'rarities': Rarity.objects.all(),

        'selected_elements': element_ids,
        'selected_weapons': weapon_ids,
        'selected_rarities': rarity_ids,
    }

    return render(request, 'genshin_app/pages/index.html', context=context)
