# Generated by Django 5.0.7 on 2024-07-22 09:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_follow_delete_friend'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='audio/')),
            ],
        ),
        migrations.AlterField(
            model_name='follow',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_follow_requests', to=settings.AUTH_USER_MODEL),
        ),
    ]
