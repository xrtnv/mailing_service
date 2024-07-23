from django.db.models.signals import post_save
from django.dispatch import receiver

from mailings.models import Mailing, LogMailing


@receiver(post_save, sender=Mailing)
def post_save_mailing(sender, instance, created, **kwargs):

    if created:
        LogMailing.objects.create(mailing_key=instance, id=instance.id)
