# Generated by Django 3.1 on 2022-07-02 11:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0005_auto_20220702_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user_name',
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]