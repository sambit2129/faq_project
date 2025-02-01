
# FAQ Management System with Multilingual Support

This project is a **Django-based FAQ Management System** that allows you to store and manage FAQs with multilingual support, WYSIWYG editor integration, and caching mechanisms for improved performance. The system supports **dynamic translations**, **API access**, and an **admin panel** for managing the FAQs easily.

---

## **Table of Contents**

- [Installation](#installation)
- [API Usage](#api-usage)
- [Features](#features)
- [Testing](#testing)
- [Caching & Performance](#caching--performance)
- [Contributing](#contributing)
- [License](#license)

---

## **Installation**

To get started with the FAQ Management System, follow these installation steps:

### **Prerequisites**

- Python 3.8+
- Django 3.0+
- Redis (for caching)
- Google Translate API key or `googletrans` library

### **Setup Instructions**

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/faq-management-system.git
    cd faq-management-system
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows, use venv\Scripts\activate
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Redis (optional, for caching):**
   - Install Redis if not already installed. Follow instructions for your operating system at [Redis Installation Guide](https://redis.io/download).
   - Run Redis server:

     ```bash
     redis-server
     ```

5. **Set up Google Translate API (optional, for automatic translation):**
   - Sign up for the [Google Cloud Translation API](https://cloud.google.com/translate).
   - Obtain your **API key** and set it as an environment variable or configure it in the settings.

6. **Run migrations to set up the database:**

    ```bash
    python manage.py migrate
    ```

7. **Create a superuser for the admin panel (optional, for managing FAQs via Django Admin):**

    ```bash
    python manage.py createsuperuser
    ```

8. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

Your application will be running at `http://localhost:8000/`.

---

## **API Usage**

### **Fetch FAQs**

#### Default Language (English)

```bash
curl http://localhost:8000/api/faqs/
```

#### Fetch FAQs in Hindi

```bash
curl http://localhost:8000/api/faqs/?lang=hi
```

#### Fetch FAQs in Bengali

```bash
curl http://localhost:8000/api/faqs/?lang=bn
```

### **Create/Update FAQ**

You can send `POST` or `PUT` requests to the `api/faqs/` endpoint to create or update FAQ entries.

**Example (Create FAQ)**

```bash
curl -X POST http://localhost:8000/api/faqs/ \
-H "Content-Type: application/json" \
-d '{"question": "What is Django?", "answer": "<p>Django is a web framework...</p>"}'
```

---

## **Features**

- **Multilingual Support**: Automatically translate FAQ entries to multiple languages such as Hindi, Bengali, etc., using Google Translate API or `googletrans`.
- **WYSIWYG Editor**: Uses `django-ckeditor` to allow rich text editing for FAQ answers.
- **RESTful API**: Exposes APIs for CRUD operations on FAQs, with support for language selection via the `lang` query parameter.
- **Caching with Redis**: Translations are cached using Redis for better performance and reduced API calls.
- **Admin Panel**: A user-friendly Django Admin interface for easy management of FAQs.
- **PEP8 Compliant Code**: Code is written following PEP8 guidelines with proper formatting, naming conventions, and linting tools like `flake8` for Python.

---

## **Testing**

To run the tests for this project:

1. Install test dependencies:

    ```bash
    pip install -r requirements-dev.txt
    ```

2. Run the tests:

    ```bash
    pytest
    ```

Unit tests cover model methods, API responses, and caching functionality.

---

## **Caching & Performance**

- The system uses **Redis** to cache translations, ensuring faster responses and reducing the need for repeated translation calls.
- Translation results are stored in Redis and fetched from the cache to improve API performance.
- Redis must be running on your machine or you must configure it in the settings for caching to work.

---

## **Contributing**

1. **Fork the repository** and clone it locally.
2. Create a **feature branch** (`git checkout -b feature-branch`).
3. Make your changes and **commit** them (`git commit -m "feat: Add new language support"`).
4. **Push your branch** (`git push origin feature-branch`).
5. Create a **pull request** with clear descriptions of the changes.

Please follow the **conventional commit messages**:

- `feat: Add multilingual FAQ model`
- `fix: Improve translation caching`
- `docs: Update README with API examples`

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
