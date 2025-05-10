# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    email = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class System(models.Model):

    #__System_FIELDS__
    ip = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    system_type = models.CharField(max_length=255, null=True, blank=True)

    #__System_FIELDS__END

    class Meta:
        verbose_name        = _("System")
        verbose_name_plural = _("System")


class Systemrequest(models.Model):

    #__Systemrequest_FIELDS__
    system_type = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    from_time = models.CharField(max_length=255, null=True, blank=True)
    to_time = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Systemrequest_FIELDS__END

    class Meta:
        verbose_name        = _("Systemrequest")
        verbose_name_plural = _("Systemrequest")


class Systemoccupancy(models.Model):

    #__Systemoccupancy_FIELDS__
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    from_time = models.CharField(max_length=255, null=True, blank=True)
    to_time = models.CharField(max_length=255, null=True, blank=True)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    request = models.ForeignKey(SystemRequest, on_delete=models.CASCADE)

    #__Systemoccupancy_FIELDS__END

    class Meta:
        verbose_name        = _("Systemoccupancy")
        verbose_name_plural = _("Systemoccupancy")



#__MODELS__END
