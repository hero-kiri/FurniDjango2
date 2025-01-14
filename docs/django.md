# Руководство по созданию проекта Django
## О Django

Django — это высокоуровневый веб-фреймворк на языке Python, который позволяет быстро создавать безопасные и поддерживаемые веб-приложения. Он был разработан с акцентом на автоматизацию и повторное использование кода, что делает его идеальным выбором для создания сложных веб-сайтов и веб-приложений.

### Основные особенности Django

- **Быстрое развитие:** Django позволяет разработчикам сосредоточиться на написании кода, а не на решении рутинных задач.
- **Безопасность:** Django включает множество встроенных механизмов защиты от распространенных угроз, таких как SQL-инъекции, XSS и CSRF.
- **Масштабируемость:** Django легко масштабируется, что позволяет использовать его как для небольших проектов, так и для крупных веб-приложений.
- **Поддержка ORM:** Django включает мощный ORM (Object-Relational Mapping), который упрощает работу с базами данных.
- **Шаблоны:** Django использует систему шаблонов, которая позволяет отделить логику приложения от представления.
- **Сообщество:** Django имеет большое и активное сообщество, которое постоянно разрабатывает новые библиотеки и расширения.
нового приложения внутри проекта используйте команду:

### Полезные ссылки

- [Официальная документация Django](https://docs.djangoproject.com/)
- [Django на GitHub](https://github.com/django/django)
- [Django Packages](https://djangopackages.org/)

---
### 1 Создание проекта
---
```bash
# Создайте папку проекта
mkdir FurniDjango
# Зайти в папку
cd FurniDjango

# Создайте проект Django с именем core
django-admin startproject core .
```

- **Что делает `django-admin startproject core .`?**  
  Создает проект с базовой структурой, включая папку `core`, содержащую настройки и конфигурацию.

---


### 1.2 Создание и активация виртуального окружения

```bash
# Установите virtualenv, если он еще не установлен
pip install virtualenv

# Создайте виртуальное окружение
virtualenv venv

# Активируйте виртуальное окружение
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
```
- **Зачем нужно виртуальное окружение?**  
  Оно изолирует зависимости проекта, предотвращая конфликты между библиотеками разных проектов.

---
## 2. Установка Django и других зависимостей

### 2.1 Установка Django

```bash
pip install django
```

### 2.2 Установка других зависимостей

- Установите библиотеку Pillow для работы с изображениями:
    ```bash
    pip install pillow
    ```

- Установите библиотеку python-dotenv для работы с переменными окружения:
    ```bash
    pip install python-dotenv
    ```

### 2.3 Создание файла `.env`

- Создайте файл `.env` в корневой папке проекта:
    ```bash
    touch .env
    ```

- В файле `.env` укажите переменные окружения, например:
    ```
    DEBUG=True
    SECRET_KEY=your_secret_key
    DATABASE_URL=postgres://user:password@localhost:5432/dbname
    ```

- **Зачем нужны эти библиотеки?**
    - **Pillow:** Позволяет работать с изображениями, такими как загрузка, изменение размера и сохранение.
    - **python-dotenv:** Позволяет загружать переменные окружения из файла `.env`, что упрощает управление конфигурацией проекта.
---

## 3. Организация приложений

### 3.1 Создание папки для приложений

```bash
mkdir apps
```

### 3.2 Создание приложений

```bash
# Создайте приложения
python manage.py startapp mainapp
python manage.py startapp orders
python manage.py startapp shop
python manage.py startapp users
```

### 3.3 Перемещение приложений в папку `apps`

```bash
mv mainapp apps/
mv orders apps/
mv shop apps/
mv users apps/
```

### 3.4 Настройка приложений

- В каждом приложении открой `apps.py` и обнови значение `name`:

```python
class MainappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.mainapp'
```

### 3.5 Подключение приложений в `settings.py`

- В файле `core/settings.py` добавьте приложения в `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'apps.mainapp',
    'apps.orders',
    'apps.shop',
    'apps.users',
]
```

---

## 4. Маршруты (urls.py)

### 4.1 Настройка основных маршрутов

- В `core/urls.py` подключите маршруты приложений:
(Если у вас нет urls.py внутри приложений или нет urlpatterns в urls.py то у вас будет показвать ошибку)
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.mainapp.urls')),
    path('orders/', include('apps.orders.urls')),
    path('shop/', include('apps.shop.urls')),
    path('users/', include('apps.users.urls')),
]
```

### 4.2 Создание файлов маршрутов для приложений

- В каждом приложении создайте файл `urls.py`, если его нет:

```python
# apps/mainapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # пример маршрута
]
```

---

## 5. Работа со статикой и шаблонами

### 5.1 Статические файлы

- Создайте папку `static/` для хранения CSS, JS и изображений:
  ```bash
  mkdir static
  ```

- Настройте `STATIC_URL` в `core/settings.py`:

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
```

### 5.2 Шаблоны

- Создайте папку `templates/` для HTML-шаблонов:
  ```bash
  mkdir templates
  ```

- Настройте `TEMPLATES` в `core/settings.py`:

```python
TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / "templates"],
        ...
    },
]
```

---

## 6. Документация проекта

### 6.1 Создание папки для документации

```bash
mkdir docs
touch docs/django.md docs/mainapp.md docs/users.md docs/django_commands.md
```

---

## 7. Зависимости и игнорируемые файлы

### 7.1 Создание файла зависимостей

- Сохраните все установленные библиотеки в файл `requirements.txt`:
  ```bash
  pip freeze > requirements.txt
  ```

### 7.2 Создание файла `.gitignore`

- Добавьте файл `.gitignore` для исключения лишних файлов из репозитория:
  ```bash
  echo "venv/" > .gitignore
  echo "__pycache__/" >> .gitignore
  echo "*.pyc" >> .gitignore
  echo "db.sqlite3" >> .gitignore
  echo ".env" >> .gitignore
  ```

---

## 8. Запуск проекта

```bash
python manage.py runserver
```

- **Проверка работы:**  
  Откройте браузер и перейдите по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## 9. Советы по масштабируемости проекта

- **Разделяйте приложения:**  
  Каждое приложение должно быть независимым и отвечать за свою зону ответственности (например, управление заказами, пользователями, каталогом товаров).
- **Используйте документацию:**  
  Храните описание архитектуры и приложений в папке `docs/`.
- **Добавляйте тесты:**  
  Пишите тесты для приложений в файле `tests.py`, чтобы проверять работоспособность кода.
- **Организуйте код:**  
  Для больших приложений используйте поддиректории (например, для моделей, представлений и маршрутов).

---

## Полная структура проекта

```
FurniDjango/
├── apps/
│   ├── mainapp/
│   ├── orders/
│   ├── shop/
│   └── users/
├── core/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── docs/
│   ├── django_commands.md
│   ├── django.md
│   ├── mainapp.md
│   └── users.md
├── manage.py
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
│   ├── index.html
│   └── other_templates.html
├── venv/
│   ├── bin/
│   ├── lib/
│   └── pyvenv.cfg
├── requirements.txt
└── .gitignore
```
