import json
from django.core.management.base import BaseCommand

from genshin_app.models import Element, Character, WeaponType, Rarity


class Command(BaseCommand):
    help = 'Load characters from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='The path to the JSON file')

    def handle(self, *args, **kwargs):
        character_count = 0
        json_file = kwargs['json_file']

        with open(json_file, 'r') as file:
            data = json.load(file)

        for _character in data['data']:
            try:
                weapon_type = WeaponType.get_by_label(_character['weapon'])
                element = Element.get_by_label(_character['element'])
                rarity = Rarity.get_by_rate(_character['rarity'])

                character, created = Character.objects.get_or_create(
                    name=_character['name'],
                    rarity=rarity,
                    weapon_type=weapon_type,
                    element=element,
                    wiki_link=_character['link'],
                )
                if created:
                    character_count += 1
                    print(f'{character.name} created successfully')
            except:
                print(f'Could not create {_character["name"]}')

        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {character_count} characters from JSON'))
