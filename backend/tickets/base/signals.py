import warnings
from typing import Any, Callable, List, Tuple

import django.dispatch
from django.apps import apps
from django.conf import settings
from django.dispatch.dispatcher import NO_RECEIVERS

from .models import Event