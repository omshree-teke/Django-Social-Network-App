# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from .models import Profile, Relationship
# from friend.models import FriendList

# """ Creating profile when an user creates an account """
# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# """ Saving profile when an user updates his/her account """
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()


# @receiver(post_save, sender=Relationship)
# def post_save_add_to_friends(sender, created, instance, **kwargs):
#     sender_ = instance.sender
#     receiver_ = instance.receiver
#     if instance.status == 'accepted':
#         sender_.friends.add(receiver_.user)
#         receiver_.friends.add(sender_.user)
#         sender_.save()
#         receiver_.save()


# """ Creating friendlist when an user creates an account """
# @receiver(post_save, sender=User)
# def create_friendlist(sender, instance, created, **kwargs):
#     if created:
#         FriendList.objects.create(user=instance)




from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out

from .models import Profile, Relationship
from friend.models import FriendList


# 🔹 Create Profile when User is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# 🔹 Save Profile safely when User is saved
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     Profile.objects.get_or_create(user=instance)


# 🔹 Create FriendList when User is created
@receiver(post_save, sender=User)
def create_friendlist(sender, instance, created, **kwargs):
    if created:
        FriendList.objects.create(user=instance)


# 🔹 Add users to each other's friend list when relationship accepted
@receiver(post_save, sender=Relationship)
def post_save_add_to_friends(sender, instance, created, **kwargs):
    sender_profile = instance.sender
    receiver_profile = instance.receiver

    if instance.status == 'accepted':
        sender_profile.friends.add(receiver_profile.user)
        receiver_profile.friends.add(sender_profile.user)
        sender_profile.save()
        receiver_profile.save()


# 🔹 Set user online when logged in
@receiver(user_logged_in)
def set_user_online(sender, user, request, **kwargs):
    profile, created = Profile.objects.get_or_create(user=user)
    profile.is_online = True
    profile.save()


# 🔹 Set user offline when logged out
@receiver(user_logged_out)
def set_user_offline(sender, user, request, **kwargs):
    profile, created = Profile.objects.get_or_create(user=user)
    profile.is_online = False
    profile.save()