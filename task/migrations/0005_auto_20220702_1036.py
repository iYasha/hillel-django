# Generated by Django 3.1 on 2022-07-02 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20220702_1034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='task_id',
            new_name='task',
        ),
    ]
