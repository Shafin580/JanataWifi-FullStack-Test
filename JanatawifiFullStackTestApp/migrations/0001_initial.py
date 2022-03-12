# Generated by Django 4.0.3 on 2022-03-11 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, verbose_name='date')),
                ('trade_code', models.CharField(max_length=150, verbose_name='trade_code')),
                ('high', models.FloatField(verbose_name='high')),
                ('low', models.FloatField(verbose_name='low')),
                ('open', models.FloatField(verbose_name='open')),
                ('close', models.FloatField(verbose_name='close')),
                ('volume', models.BigIntegerField(verbose_name='volume')),
            ],
        ),
    ]