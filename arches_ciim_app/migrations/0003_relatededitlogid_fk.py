from django.db.migrations.recorder import MigrationRecorder
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("arches_ciim_app", "0002_add_plugin"),
    ]

    def update_all_relatededitlogids(apps, schema_editor):
        """
        Function to update all existing LREs.  If many in the database, this migration could take a while.
        """
        EditLog = apps.get_model("models", "EditLog")
        LatestResourceEdit = apps.get_model("arches_ciim_app", "LatestResourceEdit")

        lres = LatestResourceEdit.objects.all()
        for lre in lres:
            edit = (
                EditLog.objects.order_by("resourceinstanceid", "-timestamp")
                .distinct("resourceinstanceid")
                .get(resourceinstanceid=lre.resourceinstanceid)
            )
            lre.relatededitlogid = edit
            lre.save()

    def remove_all_relatededitlogids(apps, schema_editor):
        """
        Empty reverse function, as the reverse migration will delete the column and contents.
        """
        ...

    operations = [
        migrations.RenameField(
            model_name="latestresourceedit",
            old_name="editlogid",
            new_name="latestresourceeditid",
        ),
        migrations.AddField(
            model_name="latestresourceedit",
            name="relatededitlogid",
            field=models.OneToOneField(
                blank=True,
                db_column="relatededitlogid",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="models.editlog",
            ),
        ),
        migrations.RunPython(
            update_all_relatededitlogids, remove_all_relatededitlogids
        ),
    ]
