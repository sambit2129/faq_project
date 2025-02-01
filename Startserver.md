
# Starting the Server

Follow the steps below to start the Django server and run the application:

## Prerequisites
Make sure you have the following installed:
- Python 3.8+
- pip (Python package installer)
- Redis (if caching is used)
- Django
- Django CKEditor (for WYSIWYG support)
- Googletrans (for translation support)

### Step 1: Install Dependencies

Navigate to your project directory and install all the required dependencies using pip.

```bash
pip install -r requirements.txt
```

If you don’t have the `requirements.txt` file, manually install the required libraries:

```bash
pip install django
pip install django-ckeditor
pip install googletrans==4.0.0-rc1
pip install redis
pip install djangorestframework
pip install psycopg2  # For PostgreSQL database (or use the appropriate database connector)
pip install pytest
```

### Step 2: Configure Database and Redis

1. **Configure Database:**
   Update your `settings.py` with your database configuration (e.g., PostgreSQL, SQLite, MySQL).

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'faq_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

2. **Configure Redis:**
   Add the following settings for Redis caching:

```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

### Step 3: Apply Migrations

Run the migrations to set up your database schema:

```bash
python manage.py migrate
```

### Step 4: Create a Superuser (Optional)

If you want to access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to create your superuser.

### Step 5: Start the Server

Start the development server with the following command:

```bash
python manage.py runserver
```

Your server should now be running at `http://127.0.0.1:8000/`.

### Step 6: Access the API

Once the server is running, you can access the API to manage FAQs.

- **Get FAQs in English (default)**

```bash
curl http://localhost:8000/api/faqs/
```

- **Get FAQs in Hindi**

```bash
curl http://localhost:8000/api/faqs/?lang=hi
```

- **Get FAQs in Bengali**

```bash
curl http://localhost:8000/api/faqs/?lang=bn
```

### Step 7: Testing

If you'd like to run tests, use pytest:

```bash
pytest
```

Ensure all your models, API responses, and caching are working correctly.

### Troubleshooting

If you encounter any issues, try the following:

1. **Issue: "ModuleNotFoundError"**
   - Solution: Install the missing module using `pip install <module_name>`.

2. **Issue: "Redis connection error"**
   - Solution: Make sure Redis is running and the connection URL is correct in `settings.py`.

3. **Issue: Database migration errors**
   - Solution: Make sure your database credentials are correct and the migrations are applied successfully.

### Conclusion

Once you complete these steps, your server should be up and running with the multilingual FAQ system, WYSIWYG editor, and caching enabled.
