from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.TextField(unique = True, help_text=_('category name'))

    def __str__(self):
        return f'{self.name}'

class AdsCategory(models.Model):
    ads = models.ForeignKey("Ads", on_delete = models.CASCADE)
    category = models.ForeignKey("Category", on_delete = models.CASCADE)

class Ads(models.Model):
    tanks = 'TN'
    heals = 'HL'
    damage_dealers = 'DD'
    merchants = 'MH'
    potion_makers = 'PM'
    spellcasters = 'SC'
    other = 'OT'


    CONTENT_TYPE = [
        (tanks, 'Танки'),
        (heals, 'Хилы'),
        (damage_dealers, 'ДД'),
        (merchants, 'Торговцы'),
        (potion_makers, 'Зельевар'),
        (spellcasters, 'Мастера заклинаний'),
    ]

    id = models.AutoField(primary_key=True, auto_created=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    materials_paths = models.JSONField(default=[])
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=9000)
    content_type = models.CharField(max_length=2,
                                choices = CONTENT_TYPE,
                                default = other)
    category = models.ManyToManyField("Category", through='AdsCategory')
    time_create = models.DateTimeField(auto_now_add=True, null=True)

    def get_absolute_url(self):
        return f"/ads/{self.pk}"
    

class Reviews(models.Model):
    accepted = 'AT'
    rejected = 'RJ'

    CONTENT_TYPE = [
        (accepted, 'Принято'),
        (rejected, 'Отклонено'),
    ]
    
    id = models.AutoField(primary_key=True, auto_created=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=9000)
    advert = models.ForeignKey(Ads, on_delete=models.CASCADE)
    category_type = models.CharField(max_length=2, choices=CONTENT_TYPE, default=accepted)

    def __str__(self):
        return self.text
        