# Generated by Django 5.1 on 2024-08-27 07:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0002_collaborator_note_collaborator"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name="collaborator",
            old_name="note",
            new_name="note_id",
        ),
        migrations.RenameField(
            model_name="collaborator",
            old_name="user",
            new_name="user_id",
        ),
        migrations.AlterUniqueTogether(
            name="collaborator",
            unique_together={("user_id", "note_id")},
        ),
    ]
