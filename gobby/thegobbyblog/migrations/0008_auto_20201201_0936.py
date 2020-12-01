# Generated by Django 3.1.3 on 2020-12-01 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thegobbyblog', '0007_post_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(max_length=255),
        ),
    ]
