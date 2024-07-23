from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver

from blog.models import Post
from mailings.models import Mailing
from users.models import User


@receiver(post_save, sender=User)
def post_save_content_manager(sender, instance, created, **kwargs):
    if created and 'sky.pro' in instance.email and 'manager' not in instance.email:

        content_group, created = Group.objects.get_or_create(name='Контент менеджер')

        # Получаем разрешения
        content_type = ContentType.objects.get_for_model(Post)
        permission1 = Permission.objects.get(codename='view_post', content_type=content_type)
        permission2 = Permission.objects.get(codename='add_post', content_type=content_type)
        permission3 = Permission.objects.get(codename='change_post', content_type=content_type)
        permission4 = Permission.objects.get(codename='delete_post', content_type=content_type)

        # Добавляем разрешения к группе
        content_group.permissions.add(permission1, permission2, permission3, permission4)

        # Добавляем пользователя в группу
        content_group.user_set.add(instance)
        instance.is_active = True

        instance.save()


@receiver(post_save, sender=User)
def post_save_manager(sender, instance, created, **kwargs):
    if created and 'manager' in instance.email:

        manager_group, created = Group.objects.get_or_create(name='Менеджер')

        # Получаем разрешения
        content_type_user = ContentType.objects.get_for_model(User)
        permission1 = Permission.objects.get(codename='view_user', content_type=content_type_user)
        permission2 = Permission.objects.get(codename='change_user', content_type=content_type_user)

        content_type_mailings = ContentType.objects.get_for_model(Mailing)
        permission3 = Permission.objects.get(codename='view_mailing', content_type=content_type_mailings)
        permission4 = Permission.objects.get(codename='delete_mailing', content_type=content_type_mailings)



        # Добавляем разрешения к группе
        manager_group.permissions.add(permission1, permission2, permission3, permission4)

        # Добавляем пользователя в группу
        manager_group.user_set.add(instance)
        instance.is_active = True
        instance.is_staff = True

        instance.save()
