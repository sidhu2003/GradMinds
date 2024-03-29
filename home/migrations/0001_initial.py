# Generated by Django 5.0.2 on 2024-03-01 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferred_branch', models.CharField(choices=[('CE', 'Civil Engineering'), ('ME', 'Mechanical Engineering'), ('ECE', 'Electronics and Communication Engineering'), ('CSE', 'Computer Science and Engineering'), ('EEE', 'Electrical and Electronics Engineering'), ('CHE', 'Chemical Engineering'), ('MET', 'Metallurgy Engineering'), ('AE', 'Aerospace Engineering'), ('BT', 'Biotechnology')], max_length=3)),
                ('score', models.FloatField()),
                ('category', models.CharField(choices=[('OBC', 'Other Backward Class'), ('GEN', 'General'), ('SC', 'Scheduled Caste'), ('ST', 'Scheduled Tribe')], max_length=3)),
                ('state', models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'), ('Lakshadweep', 'Lakshadweep'), ('Delhi', 'Delhi'), ('Puducherry', 'Puducherry')], max_length=50)),
            ],
        ),
    ]
