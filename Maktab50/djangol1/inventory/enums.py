from django.db import models


class ProductType(models.TextChoices):
    """
    Different types of products
    """
    JPEG = 'JPEG', 'عکس با کیفیت معمولی'
    PSD = 'PSD', 'فایل فتوشاپ'
    AI = 'AI', 'فایل ایلوستریتور'
    TEXT = 'TEXT', 'فایل ورد'
    PRINT = 'PRINT', 'چاپ روی کاغذ'
