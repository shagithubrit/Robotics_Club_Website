# Generated by Django 3.0.3 on 2021-02-08 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_merge_20210206_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='imagelink',
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='default-blog.png', upload_to='blogs'),
        ),
    ]
