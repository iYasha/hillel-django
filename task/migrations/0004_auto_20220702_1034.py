# Generated by Django 3.1 on 2022-07-02 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='task_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='task.task'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rating',
            name='point',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=20),
        ),
    ]
