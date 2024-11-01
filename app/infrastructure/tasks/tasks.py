from app.infrastructure.tasks.celery_app import celery
from PIL import Image
from pathlib import Path


@celery.task
def process_pic(
    path: str,
):
    img_path = Path(path)
    img = Image.open(img_path)
    img_resized_1000_500 = img.resize((1000, 500))
    img_resized_200_100 = img.resize((200, 100))
    img_resized_1000_500.save(f"app/infrastructure/frontend/static/images/img_resized_1000_500_{img_path.name}")
    img_resized_200_100.save(f"app/infrastructure/frontend/static/images/img_resized_200_100_{img_path.name}")

    