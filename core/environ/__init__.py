import os
import django


def setup():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pfc_demo.settings')
    django.setup()
