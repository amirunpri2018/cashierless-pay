# Generated by Django 3.1.3 on 2020-11-10 05:11

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Cashier', '0004_auto_20201108_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.CharField(default='085266761420', max_length=50)),
                ('nameholder', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('OTOMATIS', 'OTOMATIS'), ('MANUAL', 'MANUAL')], max_length=8)),
                ('standartbonus', models.IntegerField()),
                ('agentbonus', models.IntegerField()),
                ('resellerbonus', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='enterhistory',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 10, 5, 4, 21, 154685, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='exithistory',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 10, 5, 4, 21, 154685, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='/uploads/items/default.png', upload_to='uploads/items/3f3cfd29-59b0-4d7c-8fda-5e22167fec9f/'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 10, 5, 4, 21, 154685, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='foto',
            field=models.ImageField(default='/uploads/foto/default.png', upload_to='uploads/foto/67c54cdc-b184-46e8-ba0e-76c39f0c42db/'),
        ),
        migrations.CreateModel(
            name='TopUpHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record', models.CharField(default='102270C8', max_length=8)),
                ('time', models.DateTimeField(default=datetime.datetime(2020, 11, 10, 5, 4, 21, 154685, tzinfo=utc))),
                ('total', models.IntegerField()),
                ('receive', models.IntegerField()),
                ('codeunik', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('SUCCESS', 'SUCCESS'), ('CANCELED', 'CANCELED')], max_length=8)),
                ('ref', models.CharField(default='-', max_length=50)),
                ('datepaid', models.CharField(default='-', max_length=50)),
                ('frompaid', models.CharField(default='-', max_length=50)),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cashier.paymentmethod')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cashier.user')),
            ],
        ),
    ]
