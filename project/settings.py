import os

from environs import Env

env = Env()
env.read_env()


DATABASES = {
    'default': {
        'ENGINE': env('MY_ENGINE'),
        'HOST': env('MY_HOST'),
        'PORT': env('MY_PORT'),
        'NAME': env('MY_NAME'),
        'USER': env('MY_USER'),
        'PASSWORD': env('MY_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env('MY_SECRET_KEY')

DEBUG = env.bool('MY_DEBUG')

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
