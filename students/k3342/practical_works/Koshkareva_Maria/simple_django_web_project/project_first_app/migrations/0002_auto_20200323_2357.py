# Generated by Django 3.0.4 on 2020-03-23 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver_license',
            name='type',
            field=models.CharField(choices=[('A', 'A: motorcycle; tricycle; quadricycle; engine capacity<50cm^2; weight<400kg'), ('A1', 'A1: motorcycle; tricycle; weight<550kg'), ('B', 'B: car'), ('B1', 'B1: tricycle; quadricycle; weight<550kg, engine capacity<50cm^2'), ('C', 'C: truck; weight>3500kg; trailer<750kg'), ('C1', 'C1: truck; 3500<weight<7500kg; trailer<750kg'), ('D', 'D: passenger vehicle; trailer<750kg; seats>8'), ('D1', 'D1: passenger vehicle; trailer<750kg; 8<seats<16'), ('BE', 'BE: car with trailer'), ('CE', 'CE: truck; weight>3500kg; trailer>750kg'), ('C1E', 'C1E: truck; trailer>750kg; truck+trailer<12000kg'), ('DE', 'DE: passenger vehicle; trailer>750kg OR articulated bus'), ('D1E', 'D1E: bus not for passengers; trailer>750kg'), ('M', 'M: quadricycle; scooter; weight<350kg; engine capacity<50cm^2 '), ('Tm', 'Tm: tram'), ('Tb', 'Tb: trolleybus')], max_length=3),
        ),
    ]