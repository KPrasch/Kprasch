
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "19836268-fc9a-4024-ab5e-01bc03ff32c49fb24dfb-07f4-4f8b-b69a-64e896ca019bde50ed04-7b07-49cc-a6f6-1d8fcc013392"
NEVERCACHE_KEY = "8afa3e66-41a5-44a8-be50-70f79efdf0de3cd42f2a-2f1c-42d2-abbe-00ae1530a27f9907cc2e-6d0d-487d-a05c-b28d4db733db"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
