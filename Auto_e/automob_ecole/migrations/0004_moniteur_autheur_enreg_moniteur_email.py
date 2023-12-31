# Generated by Django 4.2.4 on 2023-08-30 23:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('automob_ecole', '0003_alter_moniteur_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='moniteur',
            name='autheur_enreg',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moniteur',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
    ]
