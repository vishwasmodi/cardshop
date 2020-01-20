# Generated by Django 2.2.4 on 2020-01-20 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_configuration_content_nomad'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='content_mathews',
            field=models.BooleanField(default=False, help_text='Math Mathews Android App', verbose_name='Math Mathews'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('fr', 'Français')], default='en', help_text='Hotspot interface language', max_length=3),
        ),
    ]