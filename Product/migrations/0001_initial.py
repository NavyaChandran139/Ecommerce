# Generated by Django 4.1.2 on 2023-01-16 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('productId', models.AutoField(primary_key=True, serialize=False)),
                ('produc_tName', models.CharField(max_length=255)),
                ('product_Brand', models.CharField(max_length=255)),
                ('product_Discription', models.CharField(max_length=1000)),
                ('product_price', models.IntegerField()),
                ('product_image', models.ImageField(upload_to='product_image')),
                ('merchant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
