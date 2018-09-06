import string
import uuid
from collections import OrderedDict
from datetime import datetime, time
from operator import attrgetter


import pytz

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.files.storage import default_storage
from django.core.mail import get_connection
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import Exists, OuterRef, Q
from django.template.defaultfilters import date as _date
from django.utils.crypto import get_random_string
from django.utils.functional import cached_property
from django.utils.timezone import make_aware, now
from django.utils.translation import ugettext_lazy as _

from i18nfield.fields import I18nCharField, I18nTextField

from tickets.base.models.base import LoggedModel