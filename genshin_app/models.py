from enum import Enum, auto

from django.db import models
from django.utils.text import slugify


class SlugifiedModel(models.Model):
    label = models.CharField(
        max_length=30,
        unique=True,
    )
    slug = models.SlugField(
        max_length=40,
        unique=True,
        blank=True,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.label.capitalize()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.label)
        super().save(*args, **kwargs)

    @classmethod
    def get_by_label(cls, label: str):
        slugified_label = slugify(label)
        return cls.objects.get(slug=slugified_label)


class Element(SlugifiedModel):
    pass


class WeaponType(SlugifiedModel):
    pass


class Rarity(SlugifiedModel):
    rate = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        unique=True,
    )

    @classmethod
    def get_by_rate(cls, rate: int):
        return cls.objects.get(rate=rate)


class Character(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
    )
    slug = models.SlugField(
        max_length=40,
        unique=True,
        blank=True,
    )
    element = models.ForeignKey(
        Element,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    rarity = models.ForeignKey(
        Rarity,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    weapon_type = models.ForeignKey(
        WeaponType,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    wiki_link = models.URLField(
        max_length=500,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name.capitalize()

    def save(self, *args, **kwargs):
        self.name = self.name
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def element_label(self):
        return self.element.__str__()

    @property
    def weapon_type_label(self):
        return self.weapon_type.__str__()

    @property
    def rarity_label(self):
        return self.rarity.__str__()

    @property
    def details(self):
        return f"{self.__str__()} | {self.element_label} | {self.weapon_type_label} | {self.rarity_label}"

    @property
    def description(self):
        return (f"{self.__str__()} is a {self.rarity_label} {self.element_label} character fighting "
                f"with a {self.weapon_type_label}")
