# Generated by Django 3.2.16 on 2023-07-27 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0006_alter_follow_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='following',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='following', to='auth.user'),
        ),
    ]