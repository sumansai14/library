# Create your views here.
from django.http import HttpResponse
from books.model import Book
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as authlogin
from django.contrib.auth.decorators import login_required, user_passes_test

