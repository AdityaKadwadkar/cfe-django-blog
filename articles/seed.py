from django.contrib.auth import get_user_model
from articles.models import Article
from django.utils import timezone

def run():
    User = get_user_model()

    # Create superuser if not exists
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="admin123"
        )
        print("Superuser created: admin / admin123")
    else:
        print("Superuser already exists")

    # Create sample articles
    if Article.objects.count() == 0:
        Article.objects.create(
            title="Welcome to the Django Blog",
            content="This is your first automatically generated article.",
            publish_date=timezone.now()
        )
        Article.objects.create(
            title="Deployed on Render!",
            content="Your Django app is successfully deployed on Render.",
            publish_date=timezone.now()
        )
        print("Sample articles created.")
    else:
        print("Articles already exist.")
