from django.core.management.base import BaseCommand
from articles.seed import run

class Command(BaseCommand):
    help = "Seed database with initial data"

    def handle(self, *args, **kwargs):
        run()
        self.stdout.write(self.style.SUCCESS("Database seeded successfully"))
