from django.conf import settings
from django.db import models

from model_utils import Choices


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    CREATION_STATUS = Choices(
        (0, 'created', 'Created'),
        (1, 'updated', 'Updated'),
        (2, 'deleted', 'Deleted')
    )
    creation_status = models.PositiveSmallIntegerField(choices=CREATION_STATUS, default=CREATION_STATUS.created)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='position_creations', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='position_updates', on_delete=models.CASCADE)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='position_deletions', on_delete=models.CASCADE,
                                   blank=True, null=True)
