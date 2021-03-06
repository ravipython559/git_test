"""
Django settings for bits project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from pytz import timezone as indiantime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7jw!t#1ekye(gl%%2^@9g_(@qgbn3tq8(prh+@9glw$t3j6fx#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
SECURE_SSL_REDIRECT = True
ALLOWED_HOSTS = ['35.154.166.13','wilpadmissions.bits-pilani.ac.in']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

TEMPLATE_DEBUG = DEBUG

EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp-wilp.bits-pilani.ac.in'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'admission@wilp.bits-pilani.ac.in'
#EMAIL_HOST_PASSWORD = 'fab045b9-b851-4baa-a46b-7fb15a0a67d3'
#FROM_EMAIL = 'noreply@wilp.bits-pilani.ac.in'

EMAIL_HOST = 'smtp-wilp.bits-pilani.ac.in'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'admission-2020-12-06@wilp.bits-pilani.ac.in'
EMAIL_HOST_PASSWORD = 'aaad95a9-bbb0-4284-9311-cfade73de1f7'
FROM_EMAIL = 'noreply@wilp.bits-pilani.ac.in'

DEFAULT_FROM_EMAIL = FROM_EMAIL
SERVER_EMAIL = EMAIL_HOST_USER

# Application definition

INSTALLED_APPS = [
    'registration',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'crispy_forms',
    'storages',
    'django_extensions',
    'registrations',
    'easy_pdf',
    'bits_admin',
    'rest_framework',
    'rest_framework.authtoken',
    'django_countries',
    'localflavor',
    'widget_tweaks',
    'ckeditor',
    'ckeditor_uploader',
    'daterange_filter',
    'import_export',
    'bits_rest',
    'application_specific',
    'waiver',
    'easy_thumbnails',
    'validatedfile',
    'datetimewidget',
    'super_reviewer',
    'table',
    'django_celery_results',
    'django_celery_beat',
    'payment_reviewer',
    'business_dev',
    'sub_reviewer',
    'certificate',
    'semester_api',
    'adhoc',
    'djcelery_email',
]

CRISPY_TEMPLATE_PACK = 'uni_form'

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'bits.urls'
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'

CELERY_EMAIL_TASK_CONFIG = {
    'name' : 'djcelery_email_send_multiple',
    'ignore_result': True,
    'default_retry_delay': 30 * 60,
    'max_retries': 2 * 24 * 7,
}




TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'bits.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bitsdb',
        'USER': 'root',
        'PASSWORD': r'b!t$Db2017rd$',
        'HOST': 'bitsdbmumbai.cosqzd7ygxjn.ap-south-1.rds.amazonaws.com',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.'
        'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

INDIAN_TIME_ZONE = indiantime('Asia/Kolkata')
TIME_ZONE = INDIAN_TIME_ZONE.zone

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

DEFAULT_FILE_STORAGE = 'bits.bits_storage.MediaStorage'
# STATICFILES_STORAGE = 'bits.bits_storage.StaticStorage'
AWS_ACCESS_KEY_ID = 'AKIAI2VBEJAEPIDKWYFQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'bits-application-files'
AWS_QUERYSTRING_AUTH = False
S3_USE_SIGV4 = True
AWS_REGION_NAME = 'ap-south-1'
AWS_S3_CUSTOM_DOMAIN = '{0}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)
AWS_S3_STORAGE = 's3'

S3_URL = '{0}.s3.ap-south-1.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)
S3_MEDIA_DIR = 'media'
#MEDIA_URL = 'https://{0}/{1}/'.format(S3_URL, S3_MEDIA_DIR)
MEDIA_URL = '/application-center-media/'
PROJECT_DIR = os.path.dirname(BASE_DIR)
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'bits','media')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.environ['HOME'], 'ac-dir', 'ac','static')
STATICFILES_DIRS = (os.path.join(BASE_DIR, "bits/ac-static-new"), )

LOGIN_REDIRECT_URL = '/registrations/bits-login/'
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar': [["Format", "Bold", "Italic", "Underline", "Strike",
                     "SpellChecker"],
                    ['NumberedList', 'BulletedList', "Indent", "Outdent",
                     'JustifyLeft', 'JustifyCenter', 'JustifyRight',
                     'JustifyBlock'],
                    ['Styles', 'Font', 'FontSize'],
                    ['TextColor', 'BGColor'],
                    ["Link", "Unlink", "Anchor",
                    "SectionLink", "Subscript", "Superscript"],
                    ['Undo', 'Redo'], ["Source"],
                    ["Maximize"]],

    }
}

PAYMENT_HOST = 'http://localhost:8080'
PAYMENT_FUNCT = '/PaymentIntegrationKit/rest/integration/'
PAYMENT_URL = PAYMENT_HOST + PAYMENT_FUNCT + 'getNewTxn'
PAYMENT_RESPONSE_URL = PAYMENT_HOST + PAYMENT_FUNCT + 'returnTxnDtls'


AUTHENTICATION_BACKENDS = [
    'bits.backends.UserModelEmailBackend', 
    'bits.backends.UserModelEmailApiBackend',
    #'bits.backends.UserModelEmailBackendLocal',
]    # Login w/ email


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ' [%(asctime)s] [%(levelname)s] [%(name)s] %(message)s'
        },
        'simple': {
            'format': ' %(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': 'logs/messages.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
        },
        'file_errors': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': 'logs/errors.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True
        }
    },
    'loggers': {
        'main': {
            'handlers': ['console', 'file', 'file_errors', 'mail_admins'],
            'level': 'DEBUG'
        },
        'caching': {
            'handlers': ['console', 'file', 'file_errors'],
            'level': 'DEBUG'
        }
    }
}


from django.core.urlresolvers import reverse_lazy
APP_STATUS = (
    ('Application Fee Paid,Documents Uploaded',
        'Application Submitted','',''),#0
    ('Application under Review',
        'Application under review','',''),#1
    ('Application under review. Requires Escalation',
        'Application under review','',''),#2
    ('Documents to be Resubmitted',
        'Documents to be Resubmitted','Resubmit Documents',
        reverse_lazy('registrationForm:reload-documentation')),#3
    ('Documents resubmitted. Pending Review',
        'Application under review','',''),#4
    ('Shortlisted',
        'Application under review','',''),#5
    ('Shortlisted. Offer Mail Sent',
        'Shortlisted','Accept/Decline Program Offer',
        reverse_lazy('registrationForm:accept-reject')),#6
    ('Rejected',
        'Application under review','',''),#7
    ('Rejected. Reject Mail Sent',
        'Admission Not Offered','View Details',
        reverse_lazy('registrationForm:view-bitsrejectionreason')),#8
    ('Accepted by Applicant',
        'Offer Accepted by Applicant','Pay Admission Fees',
        reverse_lazy('registrationForm:pay-fee-adm')),#9
    ('Declined by Applicant',
        'Offer Declined by Applicant','',''),#10
    ('Admission Fee Paid',
        'Admission Fee Paid','View/Download Offer Letter',
        reverse_lazy('registrationForm:offer-letter')),#11
    ('Submitted',
        'Submitted','',''),#12
    ('Application Fees Paid','Application Fees Paid','',''),#13
    ('Application Fee Paid,Documents Uploaded In Progress',
        'Application Fee Paid,Documents Uploaded In Progress','',''),#14
    ('Escalated. Under review by Super reviewer',
        'Application under review by higher authorities',
        '', ''),#15
    ('Resubmit','Resubmit Application Form','',''),#16
    ('Level-1 review Completed', 'Application under review',
        '', ''),#17
    ('Pre-Selected','Pre-Selected','',''),#18
    ('Pre-Rejected','Pre-Rejected','',''),#19
    )

ORACLE_AMOUNT = 15000
ADMISSION_FEES = 15000
PHONENUMBER_DEFAULT_REGION = 'IN'
PHONENUMBER_DEFAULT_FORMAT = 'INTERNATIONAL'

THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (300, 70)},
        'year_thumb': {
            'size': (300, 100),
            'autocrop': True,
            'crop': 'smart',
            'upscale': True,
        },
        'zip_thumb': {
            'size': (150, 150),
            'autocrop': True,
            'crop': 'smart',
            'upscale': True,
        },
    },
}

USE_L10N = True
USE_TZ = True 
USE_I18N = True

DATETIME_INPUT_FORMATS = [
    # '%Y-%m-%d %H:%M:%S',
    # '%Y-%m-%d %H:%M:%S.%f',
    # '%Y-%m-%d %H:%M',
    # '%Y-%m-%d',
    # '%Y/%m/%d %H:%M:%S',
    # '%Y/%m/%d %H:%M:%S.%f',
    # '%Y/%m/%d %H:%M',
    # '%Y/%m/%d',
    # '%d/%m/%Y %H:%M:%S'
    # '%d/%m/%Y %H:%M:%S.%f',
    # '%d/%m/%Y %H:%M',
    # '%d/%m/%Y',
    # '%d/%m/%y %H:%M:%S',
    # '%d/%m/%y %H:%M:%S.%f',
    # '%d/%m/%y %H:%M',
    # '%d/%m/%y',
    '%d-%m-%Y %H:%M:%S'
    '%d-%m-%Y %H:%M:%S.%f',
    '%d-%m-%Y %H:%M',
    '%d-%m-%Y',
    '%d-%m-%y %H:%M:%S',
    '%d-%m-%y %H:%M:%S.%f',
    '%d-%m-%y %H:%M',
    '%d-%m-%y',
]

CELERY_RESULT_BACKEND = 'django-db'

BROKER_URL = 'redis://localhost:6379/0'

CELERY_TIMEZONE = indiantime('Asia/Kolkata').zone
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_RESULT_SERIALIZER = 'pickle'
CELERY_IMPORTS=("bits_admin.task")
CELERY_IGNORE_RESULT = False
CELERYBEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

SDMS_URL = r'https://sdms.bits-pilani.ac.in/api/v1/profile/add' #production


PAYTM_MERCHANT_KEY = r"Ob4Lj9S!HkkxjUVb"
PAYTM_MERCHANT_ID = "BITSPi42890113368555"
PAYTM_WEBSITE = 'WEBPROD'
PAYTM_TRANSACTION_STATUS_URL = "https://securegw.paytm.in/order/status"
PAYTM_PAYMENT_URL = "https://securegw.paytm.in/order/process"
PAYTM_INDUSTRY_TYPE_ID = "PrivateEducation"


EDUVANZ_URL = 'https://eduvanz.com/quickemi/login'
EDUVANZ_USERNAME = 'bitspilaniregular'
EDUVANZ_PASSWORD = 'lsgbeid29bns578bskbdbkw'
EDUVANZ_CLIENT_INSTITUTE_ID = '1'
EDUVANZ_CLIENT_LOCATION_ID = '1'
EDUVANZ_KYC_ADDRESS_COUNTRY = '1'

ADHOC_EDUVANZ_URL = 'https://eduvanz.com/quickemi/login'
ADHOC_EDUVANZ_USERNAME = 'bitspilaniadhoc'
ADHOC_EDUVANZ_PASSWORD = 'huebn62dju86bvg8'
ADHOC_EDUVANZ_CLIENT_INSTITUTE_ID = '1'
ADHOC_EDUVANZ_CLIENT_LOCATION_ID = '1'
ADHOC_EDUVANZ_KYC_ADDRESS_COUNTRY = '1'


EZCRED_URL = 'https://creditengine.ezcred.in'
EZCRED_USERNAME = 'bitspilani.agent'
EZCRED_PASSWORD = 'EzCred@123'
EZCRED_PARTNER_ID = 'BITSPILANI100'

#salesforce

SF_AUTH_URL = 'https://login.salesforce.com/services/oauth2/token'
SF_USERNAME = r'wilpuser@bits.com'
SF_PASSWORD = 'salesforce1'
SF_CLIENT_ID = r'3MVG9pe2TCoA1Pf4xjd13Dg0X72R4rC_eZcnp43Pr9K17x6sMz_uSnkQsmVJro2jTGR_euxn7rEjO4IzbrnYz'
SF_CLIENT_SECRET = r'0175FCD9EA1C4971D03CEEA8D0DE63D6838B084E79BFB73563C451FC6B9B55A5'
SF_GRANT_TYPE = 'password'

#propelld

PROPELLD_URL = 'https://live.propelld.com/v1/'
PROPELLD_CLIENT_ID = 'LRo-Oxe84hQtPBOSvN--EC4E9ISRvXMs724f8883-1686-5616-881f-f05d1572fc09'
PROPELLD_CLIENT_SECRET = 'G_orlosE6tBl7a_aIS_eG1aTiDSF7VFEc99b6186-115d-55c1-9f49-99354e2b0f4d'
PROPELLD_CALLBACK_KEY = 'bits'

from django.contrib.staticfiles.storage import staticfiles_storage
STATIC_URL_FUNC = staticfiles_storage.url

try:
    from .local_settings import *
except:
    print("No local settings found.")
