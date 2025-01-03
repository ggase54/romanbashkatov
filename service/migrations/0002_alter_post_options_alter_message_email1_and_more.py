# Generated by Django 4.0.6 on 2022-08-04 16:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_squashed_0008_alter_message_email2'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterField(
            model_name='message',
            name='email1',
            field=models.EmailField(max_length=50, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Invalid title', regex='^.*post$')], verbose_name='Title'),
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('title', 'description')},
        ),
    ]
