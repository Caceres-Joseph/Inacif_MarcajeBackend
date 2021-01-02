# Generated by Django 2.1 on 2021-01-02 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiM02_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('ubi_codigo', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
    ]
