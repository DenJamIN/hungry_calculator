# Generated by Django 4.1.1 on 2023-11-14 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_participant_groups_alter_group_organizer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='requisites',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Реквизиты'),
        ),
    ]