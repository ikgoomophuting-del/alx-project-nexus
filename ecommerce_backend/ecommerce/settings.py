import os
import stripe
from pathlib import Path
from datetime import timedelta
from decouple import config
import dj_database_url

# -----------------------------------
# BASE CONFIG
# -----------------------------------

SECRET_KEY = os.getenv("SECRET_KEY", config("SECRET_KEY", default="unsafe-dev-secret"))
DEBUG = os.getenv("DEBUG", "False") == "True"

# Stripe keys (optional)
STRIPE_SECRET_KEY = config("STRIPE_SECRET_KEY", default="")
STRIPE_PUBLISHABLE_KEY = config("STRIPE_PUBLISHABLE_KEY", default="")
STRIPE_WEBHOOK_SECRET = config("STRIPE_WEBHOOK_SECRET", default="")

if STRIPE_SECRET_KEY:
    stripe.api_key = STRIPE_SECRET_KEY

BASE_DIR = Path(__file__).resolve().parent.parent

# ALLOWED_HOSTS: don't include protocol (no http://)
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost").split(",")


# -----------------------------------
# APPLICATIONS
# -----------------------------------

INSTALLED_APPS = [
    # Django core
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third party
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_yasg",
    "corsheaders",
    "django_filters",

    # Local apps
    "core",
    "products",
    "users",
    "accounts",
]


# -----------------------------------
# MIDDLEWARE
# -----------------------------------

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # custom middleware
    "core.middleware.request_logging.RequestLoggingMiddleware",
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
        "DIRS": [BASE_DIR / "templates"],
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
# DATABASE (use DATABASE_URL in production)
# -----------------------------------

DATABASES = {
    "default": dj_database_url.config(default=os.environ.get("DATABASE_URL", f"sqlite:///{BASE_DIR/'db.sqlite3'}"))
}


# -----------------------------------
# CUSTOM USER MODEL
# -----------------------------------

AUTH_USER_MODEL = "accounts.User"


# -----------------------------------
# PASSWORD VALIDATION
# -----------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# -----------------------------------
# INTERNATIONALIZATION
# -----------------------------------

LANGUAGE_CODE = "en-us"
TIME_ZONE = os.getenv("TIME_ZONE", "Africa/Johannesburg")
USE_I18N = True
USE_TZ = True


# -----------------------------------
# STATIC & MEDIA FILES
# -----------------------------------

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# -----------------------------------
# DJANGO REST FRAMEWORK (DRF)
# -----------------------------------

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ),
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.OrderingFilter",
        "rest_framework.filters.SearchFilter",
    ),
    "DEFAULT_PAGINATION_CLASS": "core.pagination.default_pagination.DefaultPagination",
    "PAGE_SIZE": int(os.getenv("PAGE_SIZE", 12)),
}


# -----------------------------------
# SIMPLE JWT CONFIG (Tokens)
# -----------------------------------

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=int(os.getenv("ACCESS_TOKEN_MINUTES", 60))),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=int(os.getenv("REFRESH_TOKEN_DAYS", 1))),
    "AUTH_HEADER_TYPES": ("Bearer",),
}


# -----------------------------------
# CORS (Frontend Integration)
# -----------------------------------

CORS_ALLOW_ALL_ORIGINS = True


# -----------------------------------
# SWAGGER/DRF-YASG CONFIG
# -----------------------------------

SWAGGER_SETTINGS = {
    "USE_SESSION_AUTH": False,
    "SECURITY_DEFINITIONS": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
        }
    },
}


# -----------------------------------
# LOGGING CONFIG
# -----------------------------------

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} → {message}",
            "style": "{",
        }
    },
    "loggers": {
        "django": {"handlers": ["console"], "level": "INFO"},
        "core.middleware.request_logging": {"handlers": ["console"], "level": "INFO"},
    },
}


# -----------------------------------
# RENDER.COM DEPLOYMENT SETTINGS
# -----------------------------------

RENDER = os.environ.get("RENDER", None)

if RENDER:
    DEBUG = False
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    # Append Render external hostname if provided
    render_host = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
    if render_host:
        ALLOWED_HOSTS.append(render_host)


# convenience: allow specifying ALLOWED_HOSTS via env var (comma separated)
env_hosts = os.environ.get("ALLOWED_HOSTS")
if env_hosts:
    for h in env_hosts.split(","):
        h = h.strip()
        if h and h not in ALLOWED_HOSTS:
            ALLOWED_HOSTS.append(h)
