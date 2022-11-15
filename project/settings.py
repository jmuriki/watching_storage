import os

from environs import Env

env = Env()
env.read_env()


DATABASES = {
    'default': {
        'ENGINE': env('ENV_ENGINE'),
        'HOST': env('ENV_HOST'),
        'PORT': env('ENV_PORT'),
        'NAME': env('ENV_NAME'),
        'USER': env('ENV_USER'),
        'PASSWORD': env('ENV_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env('ENV_SECRET_KEY')

DEBUG = env.bool('ENV_DEBUG')

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
