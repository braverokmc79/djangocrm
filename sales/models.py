from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class 아이디(AbstractUser):
    pass


class UserProfile(models.Model):
    회원 = models.OneToOneField(아이디, on_delete=models.CASCADE)

    def __str__(self):
        return self.회원.username


class Person(models.Model):
    회원 = models.OneToOneField(아이디, on_delete=models.CASCADE)
    조직 = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.회원.email


class Sale(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


def 회원생성signal(sender, instance, created, **kwargs):
    print("****  instance, created  :",sender, instance, created)
    if created:
        UserProfile.objects.create(회원=instance)
        print(f"새로운 회원이 생성되었습니다: {instance.username}")


post_save.connect(회원생성signal, sender=아이디)
