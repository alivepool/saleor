# Generated by Django 3.1.1 on 2020-10-15 11:07

from django.db import migrations


def create_temporary_channel(apps, schema_editor):
    # TODO: REMOVE ME BEFORE MERGE TO MASTER
    # This migration is needed for test deployments
    Channel = apps.get_model("channel", "Channel")

    if Channel.objects.all().count() > 0:
        Channel.objects.create(
            name="Other Channel USD",
            slug="other-usd-channel",
            currency_code="USD",
            is_active=True,
        )


class Migration(migrations.Migration):

    dependencies = [
        ("channel", "0002_channel_availability"),
        ("discount", "0023_voucher_channel_listing"),
        ("product", "0133_collection_channel_listing"),
        ("checkout", "0030_checkout_channel_listing"),
        ("shipping", "0023_auto_20200910_1000"),
        ("order", "0090_order_channel_listing"),
        ("shipping", "0022_shipping_method_channel_listing"),
    ]

    operations = [
        migrations.RunPython(create_temporary_channel, migrations.RunPython.noop),
    ]
