from django.shortcuts import render
from django.conf import settings
import pyrebase
from ecommerce.firebase_config import FIREBASE_CONFIG
import logging

firebase = pyrebase.initialize_app(FIREBASE_CONFIG)
db = firebase.database()

logger = logging.getLogger(__name__)


def product_list(request):
    return render(request, 'store/product_list.html', {})