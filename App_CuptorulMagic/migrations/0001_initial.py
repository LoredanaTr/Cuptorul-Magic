# Generated by Django 4.2.7 on 2024-01-06 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('is_logged', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('available_quantity', models.PositiveIntegerField(default=0)),
                ('ingredients', models.TextField(null=True)),
                ('weight_grams', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_CuptorulMagic.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_CuptorulMagic.customuser')),
            ],
        ),
    ]
