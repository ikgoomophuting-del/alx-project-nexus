import os
import stripe
from pathlib import Path
from datetime import timedelta
from decouple import config

# -----------------------------------
# BASE CONFIG
# -----------------------------------

SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
DEBUG = os.getenv("DEBUG", "True") == "True"

STRIPE_SECRET_KEY = config("STRIPE_SECRET_KEY")
STRIPE_PUBLISHABLE_KEY = config("STRIPE_PUBLISHABLE_KEY")
STRIPE_WEBHOOK_SECRET = config("STRIPE_WEBHOOK_SECRET")

stripe.api_key = STRIPE_SECRET_KEY

BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ["https://alx-project-nexus-3h8j.onrender.com"]  # For Render deployment


# -----------------------------------
# APPLICATIONS
# -----------------------------------

INSTALLED_APPS = [
    # Django core apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party packages
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_yasg",
    "corsheaders",
    "django_filters",

    # Local apps
    "core",
    "products",
    "users",
    "accounts",  # ← added (Custom user, permissions, auth extras)
]


# -----------------------------------
# MIDDLEWARE
# -----------------------------------

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    ...
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


    # Custom logging middleware (corrected path)
    "core.middleware.request_logging.RequestLoggingMiddleware",

    # Role-based access middleware from accounts
    "accounts.middleware.RoleRequiredMiddleware",
]


# -----------------------------------
# URL CONFIG
# -----------------------------------

ROOT_URLCONF = "ecommerce.urls"
DOMAIN_URL = config("DOMAIN_URL", default="http://localhost:8000")

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ecommerce.wsgi.application"
ASGI_APPLICATION = "ecommerce.asgi.application"


# -----------------------------------
# DATABASE CONFIG (PostgreSQL)
# -----------------------------------

DATABASES = {
    import dj_database_url

    'default': dj_database_url.config(default=os.environ.get("DATABASE_URL"))
}
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "5432"),
        "NAME": os.getenv("DB_NAME", "your_db"),
        "USER": os.getenv("DB_USER", "your_user"),
        "PASSWORD": os.getenv("DB_PASSWORD", "your_password"),
    }
    
}


# -----------------------------------
# CUSTOM USER MODEL
# -----------------------------------

AUTH_USER_MODEL = "accounts.User"   # ← FIXED (your User is inside accounts app)


# -----------------------------------
# PASSWORD VALIDATION
# -----------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
]


# -----------------------------------
# INTERNATIONALIZATION
# -----------------------------------

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# -----------------------------------
# STATIC & MEDIA FILES
# -----------------------------------

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# -----------------------------------
# DJANGO REST FRAMEWORK (DRF)
# -----------------------------------

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),

    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend"
    ],

    # Global pagination
    "DEFAULT_PAGINATION_CLASS": "core.pagination.CustomPagination",
    "PAGE_SIZE": 10,
}


# -----------------------------------
# SIMPLE JWT CONFIG (Tokens)
# -----------------------------------

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": ("Bearer",),
}


# -----------------------------------
# CORS (Frontend Integration)
# -----------------------------------

CORS_ALLOW_ALL_ORIGINS = True


# -----------------------------------
# SWAGGER CONFIG
# -----------------------------------

SWAGGER_SETTINGS = {
    "USE_SESSION_AUTH": False,
    "SECURITY_DEFINITIONS": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        }
    },
}


# -----------------------------------
# LOGGING CONFIG
# -----------------------------------

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },

    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} → {message}",
            "style": "{",
        }
    },

    "loggers": {
        "django": {"handlers": ["console"], "level": "INFO"},
        "core.middleware.request_logging": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}


# -----------------------------------
# RENDER.COM DEPLOYMENT SETTINGS
# -----------------------------------

RENDER = os.environ.get("RENDER", None)

if RENDER:
    DEBUG = False
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    ALLOWED_HOSTS.append(os.environ.get("RENDER_EXTERNAL_HOSTNAME"))

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

