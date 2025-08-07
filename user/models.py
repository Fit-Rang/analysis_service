from django.db import models
from django.db.models import Exists, OuterRef
from django.contrib.postgres.fields import ArrayField

class Profile(models.Model):
    id = models.CharField(primary_key=True, max_length=12)
    email = models.EmailField(unique=True, max_length=100)
    full_name = models.CharField(max_length=150)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    profile_picture_url = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'profile'

class Dossier(models.Model):
    id = models.UUIDField(primary_key=True)
    owner = models.ForeignKey(Profile, to_field='id', db_column='owner_id', on_delete=models.DO_NOTHING)
    face_type = models.TextField()
    skin_tone = models.TextField()
    body_type = models.TextField()
    gender = models.TextField()
    preferred_colors = ArrayField(models.TextField(), default=list)
    disliked_colors = ArrayField(models.TextField(), default=list)
    height = models.TextField(null=True, blank=True)
    weight = models.TextField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'dossier'
        unique_together = (('id', 'owner'),)

class DossierAccess(models.Model):
    dossier = models.ForeignKey(Dossier, db_column='dossier_id', on_delete=models.DO_NOTHING)
    profile = models.ForeignKey(Profile, db_column='profile_id', on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dossier_access'
        unique_together = (('dossier', 'profile'),)

def get_profiles(profile_id):
    accessible_dossier_ids = DossierAccess.objects.filter(
        profile_id=profile_id,
        dossier__owner_id=OuterRef('id')
    ).values('dossier_id')

    return Profile.objects.filter(
        Exists(accessible_dossier_ids)
    )

