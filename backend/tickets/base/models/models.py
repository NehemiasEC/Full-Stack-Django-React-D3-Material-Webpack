import json
import uuid
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils.crypto import get_random_string

def cachedfile_name(instance, filename:str)->str:
    secret = get_random_string(length=12)
    return 'cachedfiles/%s.%s.%s'%(instance.id, secret, filename.split('.')[-1])



class CachedFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    expires = models.DateTimeField(null=True,blank=True)
    date = models.DateTimeField(null=True,blank=True)
    filename = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    file = models.FileField(null=True,blank=True,upload_to=cachedfile_name)




@receiver(post_delete, sender = CachedFile)
def cached_file_delete(sender, instance, **kwargs):
    if instance.file:
        instance.file.delete(False)





class LoggingMixin:
    def log_action(self, action, data=None, user=None, api_token=None, auth=None, save=True):
        from .log import LogEntry