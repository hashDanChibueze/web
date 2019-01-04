# Generated by Django 2.1.4 on 2019-01-04 19:31

from django.db import migrations

def add_num_tx_processed(apps, schema_editor):
    Subscription = apps.get_model('grants', 'Subscription')
    for subscription in Subscription.objects.all():
        subscription.num_tx_processed = contribution.count()
        subscription.save()

class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0002_auto_20190102_1823'),
    ]

    operations = [
        migrations.RunPython(add_num_tx_processed),
    ]