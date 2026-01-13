## Установка

### 1. Установите Python 3
Убедитесь, что Python 3 установлен:
```bash
python --version
```
Если команда не работает, попробуйте:
```bash
python3 --version
```

### 2. Создайте папку проекта
```bash
mkdir mysite
cd mysite
```

### 3. Создайте виртуальное окружение
```bash
python -m venv venv
```

Активируйте окружение:
- macOS / Linux:
  ```bash
  source venv/bin/activate
  ```
- Windows:
  ```bash
  venv\Scripts\activate
  ```
### 4. Установите Django
```bash
pip install django
```


## Создание и запуск проекта

### 1. Создайте Django‑проект
```bash
django-admin startproject config .
```

### 2. Примените миграции
```bash
python manage.py migrate
```

### 3. Запустите сервер разработки
```bash
python manage.py runserver
```

После запуска откройте:
```
http://127.0.0.1:8000/
```

