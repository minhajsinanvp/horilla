import os
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Deletes all migration files except __init__.py in all apps'

    def handle(self, *args, **kwargs):
        for app in settings.INSTALLED_APPS:
            try:
                app_path = os.path.join(settings.BASE_DIR, app.replace('.', '/'), 'migrations')
                if os.path.exists(app_path):
                    self.stdout.write(f"Cleaning up migrations in: {app_path}")
                    for filename in os.listdir(app_path):
                        file_path = os.path.join(app_path, filename)
                        if filename != '__init__.py' and os.path.isfile(file_path):
                            os.remove(file_path)
                            self.stdout.write(f"Deleted: {file_path}")
                        else:
                            self.stdout.write(f"Skipped: {file_path}")
            except Exception as e:
                self.stderr.write(f"Error processing app {app}: {e}")

        self.stdout.write(self.style.SUCCESS('Migration cleanup complete.'))