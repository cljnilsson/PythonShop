# Generated by Django 3.0.4 on 2020-05-15 08:38

from django.db import migrations


class Migration(migrations.Migration):
	atomic = False

	dependencies = [
		('shop', '0004_campaignitems'),
	]

	operations = [
		migrations.RenameModel(
			old_name='CampaignItems',
			new_name='CampaignItem',
		),
	]