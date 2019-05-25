from django.conf import settings
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from model_utils import Choices


class Church(MPTTModel):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    address = models.TextField(blank=True, default="")
    CREATION_STATUS = Choices(
        (0, 'created', 'Created'),
        (1, 'updated', 'Updated'),
        (2, 'deleted', 'Deleted')
    )
    creation_status = models.PositiveSmallIntegerField(choices=CREATION_STATUS, default=CREATION_STATUS.created)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='church_creations', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='church_updates', on_delete=models.CASCADE)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='church_deletions', on_delete=models.CASCADE,
                                   blank=True, null=True)


class ChurchMembership(models.Model):
    church = models.ForeignKey('Church', related_name='members', on_delete=models.CASCADE)
    member = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='church_members', on_delete=models.CASCADE)
    position = models.ForeignKey('positions.Position', related_name='church_positions', on_delete=models.CASCADE)
    CREATION_STATUS = Choices(
        (0, 'created', 'Created'),
        (1, 'updated', 'Updated'),
        (2, 'deleted', 'Deleted')
    )
    creation_status = models.PositiveSmallIntegerField(choices=CREATION_STATUS, default=CREATION_STATUS.created)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='church_membership_creations', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='church_membership_updates', on_delete=models.CASCADE)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='church_membership_deletions', on_delete=models.CASCADE,
                                   blank=True, null=True)
