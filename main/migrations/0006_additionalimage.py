# Generated by Django 3.2.5 on 2021-07-12 12:55

from django.db import migrations, models
import django.db.models.deletion
import main.utilities


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=main.utilities.get_timestamp_path, verbose_name='Изображения')),
                ('pp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Допольнительная иллюстрация',
                'verbose_name_plural': 'Допольнительные иллюстрации',
            },
        ),
    ]