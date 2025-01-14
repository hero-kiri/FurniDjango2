# FurniDjango

## Клонирование проекта

```bash
git clone git@github.com:hero-kiri/FurniDjango.git
cd FurniDjango
```

## Настройка виртуального окружения

1. Установите виртуальное окружение:

```bash
virtualenv venv
```

2. Активируйте виртуальное окружение:

- Для macOS и Linux:

```bash
source venv/bin/activate
```

- Для Windows:

```bash
venv\Scripts\activate
```

## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Создание файла `.env`

Создайте файл `.env` в корневой директории проекта и добавьте необходимые переменные окружения. Например:

```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url
```

## Применение миграций

```bash
python manage.py migrate
```

Теперь ваш проект готов к запуску!