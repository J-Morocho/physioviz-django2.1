# Generated by Django 2.2.3 on 2019-07-18 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_number', models.IntegerField(default=0)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(max_length=1)),
                ('height_cm', models.FloatField()),
                ('weight_kg', models.FloatField()),
            ],
        ),
    ]
