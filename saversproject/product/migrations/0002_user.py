# Generated by Django 2.2.3 on 2019-07-19 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=45)),
                ('pw', models.CharField(max_length=45)),
                ('tel', models.CharField(max_length=45)),
                ('monthly_amount', models.CharField(max_length=45)),
                ('donate_value', models.IntegerField(default=0)),
                ('coin', models.IntegerField(default=0)),
                ('post_code', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
