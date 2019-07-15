# Generated by Django 2.2.2 on 2019-06-29 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='agent',
            name='slug',
            field=models.SlugField(max_length=20, unique=True),
        ),
    ]