#!/usr/bin/env python
#! -*- encoding:utf-8 -*-

from django.db import models
from userprofile.models import BaseProfile

GENDER_CHOICES = ( ('F', u'女'), ('M', u'男'),)

class Profile ( BaseProfile ):
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)