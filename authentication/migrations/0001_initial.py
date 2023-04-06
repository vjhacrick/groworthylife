# Generated by Django 4.2 on 2023-04-05 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('points', models.IntegerField(default=0)),
                ('age', models.IntegerField(default=18)),
                ('standerd', models.CharField(choices=[('8th', '8th'), ('9th', '9th'), ('10th', '10th'), ('11th', '11th'), ('12th', '12th')], default=('8th', '8th'), max_length=50)),
            ],
            options={
                'db_table': 'customer',
            },
            bases=('base.baseuser',),
        ),
    ]