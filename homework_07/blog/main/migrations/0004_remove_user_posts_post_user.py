# Generated by Django 5.0.3 on 2024-03-31 17:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_post_user_user_posts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='posts',
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='main.user'),
            preserve_default=False,
        ),
    ]
