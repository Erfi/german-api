# Generated by Django 2.2.4 on 2019-11-05 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0006_auto_20191105_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deck',
            name='from_lang',
        ),
        migrations.RemoveField(
            model_name='deck',
            name='to_lang',
        ),
        migrations.AlterField(
            model_name='deck',
            name='name',
            field=models.CharField(default='Example', max_length=100),
            preserve_default=False,
        ),
    ]