from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from store.signals import order_placed
from users.models import Profile


@receiver(order_placed)
def send_email_when_order_is_placed(sender, **kwargs):

    # if "store.models.Order'" in str(sender):
    print(f"Hello from signals. {kwargs['created']}")


@receiver(post_save, sender=get_user_model())
def send_email_when_user_is_created(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
        print('Hiiiiiiiiiiiiiiiiiiiiiiii')
