# Generated by Django 2.2.3 on 2019-07-28 21:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mdapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='post',
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
