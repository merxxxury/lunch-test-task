# Generated by Django 4.2.5 on 2023-10-02 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lunch_api', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='name',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='price',
        ),
        migrations.AlterField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='menu',
            name='votes',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lunch_api.menu')),
            ],
        ),
    ]