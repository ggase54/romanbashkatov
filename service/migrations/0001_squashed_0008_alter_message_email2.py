# Generated by Django 4.0.6 on 2022-08-04 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('service', '0001_initial'), ('service', '0002_alter_post_image'), ('service', '0003_alter_comment_post'), ('service', '0004_message_alter_comment_created_at_and_more'), ('service', '0005_message_email'), ('service', '0006_rename_email_message_email1_message_email2'), ('service', '0007_alter_message_email2'), ('service', '0008_alter_message_email2')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description of post')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Comment')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='service.post')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True, verbose_name='Subject')),
                ('body', models.TextField(verbose_name='Message')),
                ('email1', models.EmailField(default=1, max_length=50, verbose_name='Email')),
                ('email2', models.EmailField(blank=True, max_length=50, null=True, verbose_name='Email_2')),
            ],
        ),
    ]
