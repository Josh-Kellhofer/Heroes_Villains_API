# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6kuv5w#8#@)bu4*14f4qw+3rme*!lf!892jod^6kag$+9=oaqu'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroes_villains_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Shamgar1'
    }
}