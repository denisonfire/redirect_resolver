## Установка

Создаем виртуальное окружение

```
$ python3 -m venv redirect_resolver
```

Устанавливаем зависимости

```
$ pip install -r requirements.txt
```

Запускаем тестовый сервер

```
$ FLASK_APP=server flask run --port 5000
```
Запускаем программу

```
$ python resolver.py
```