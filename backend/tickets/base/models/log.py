import json
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.html import escape
from django.utils.translation import pgettext_lazy, ugettext_lazy as _

from tickets.base.signals import logentry_object_link
