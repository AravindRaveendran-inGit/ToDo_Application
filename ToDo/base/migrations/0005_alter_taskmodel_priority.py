# Generated by Django 3.2.7 on 2021-11-18 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_taskmodel_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='priority',
            field=models.CharField(choices=[('🙂 ', 'low'), ('🤨 ', 'medium'), (' 😡 ', 'urgent')], default='low', max_length=7),
        ),
    ]
