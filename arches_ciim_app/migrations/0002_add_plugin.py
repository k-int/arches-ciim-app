from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("arches_ciim_app", "0001_initial")]

    def add_plugin(apps, schema_editor):
        Plugin = apps.get_model("models", "Plugin")

        if not Plugin.objects.filter(
            pk="eb53e958-9ddf-40a9-8acd-da2b27df8340"
        ).exists():
            Plugin.objects.update_or_create(
                pluginid="eb53e958-9ddf-40a9-8acd-da2b27df8340",
                name="CIIM Integration Dashboard",
                icon="fa fa-link",
                component="views/components/plugins/ciim_integration_dashboard",
                componentname="ciim_integration_dashboard",
                slug="ciim_integration_dashboard",
                config={"show": True, "is_workflow": True, "description": ""},
                sortorder=1,
            )

    def remove_plugin(apps, schema_editor):
        Plugin = apps.get_model("models", "Plugin")

        for plugin in Plugin.objects.filter(pk="eb53e958-9ddf-40a9-8acd-da2b27df8340"):
            plugin.delete()

    operations = [
        migrations.RunPython(add_plugin, remove_plugin),
    ]
