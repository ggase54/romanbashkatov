# Generated by Django 4.0.6 on 2022-08-15 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_alter_post_options_alter_message_email1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Image'),
        ),
    ]
