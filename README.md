# Проект сервис Donations.

>Проект, позволяющий собирать пожертвования на различные целевые проекты.

### Используемые технологии:
[![Python][Python-badge]][Python-url]
[![Django][Django-badge]][Django-url]
[![DRF][DRF-badge]][DRF-url]
[![Python-telegram-bot][Python-telegram-bot-badge]][Python-telegram-bot-url]
[![Postgres][Postgres-badge]][Postgres-url]
[![Nginx][Nginx-badge]][Nginx-url]

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/FakaFakaYeah/donation_project.git
```

```
cd cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```
  
Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```


```
в проекте создан шаблон env файла, добавьте вначале точку, заполните значения
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
TITLE=Благотворительного фонда поддержки котиков QRKot
DESCRIPTION=Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.
SECRET= Ваш секретный ключ
```

Выполнить миграции
```
alembic upgrade head
```


Запустить проект можно командой

```
uvicorn app.main:app --reload
```

Проект будет доступен по следующему адресу:

```
http://127.0.0.1:8000 
```

Документация проекта со всеми описаниями и эндпоинтами доступна по адресу:

```
http://127.0.0.1:8000/docs
```
