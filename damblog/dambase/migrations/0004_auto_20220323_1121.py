# Generated by Django 4.0.2 on 2022-03-23 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dambase', '0003_post_blockquote_thename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='blockquote_thename',
        ),
        migrations.AddField(
            model_name='post',
            name='blockquote_author_name',
            field=models.CharField(default='Miracle', max_length=100),
        ),
    ]
