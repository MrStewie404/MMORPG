from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .tasks import tasks_create_review
from django.dispatch import receiver

from .models import Reviews, Ads

@receiver(post_save, sender=Reviews)
def review_created(instance, created, **kwargs):

    user_target = User.objects.filter(
        id=Ads.objects.get(
            id=instance.advert_id
        ).user_id
    ).get()

    tasks_create_review.apply_async(args=[
        created, 
        user_target.email, 
        user_target.username, 
        instance.user.username, 
        instance.text,
        instance.category_type
    ])