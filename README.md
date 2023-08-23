# Проект сервис Donations.

### Оглавление
<ol>
 <li><a href="#description">Описание проекта</a></li>
 <li><a href="#stack">Используемые технологии</a></li>
 <li><a href="#architecture">Архитектура проекта</a></li>
 <li><a href="#start_project">Как развернуть проект локально?</a></li>
 <li><a href="#author">Авторы проекта</a></li>
</ol>


---
### Описание проекта:<a name="description"></a>
Проект, позволяющий собирать пожертвования на различные целевые проекты.

---
### **Используемые технологии**<a name="stack"></a>

![](https://img.shields.io/badge/Python-grey?style=for-the-badge&logo=python&logoColor=yellow)
![](https://img.shields.io/badge/Fast_API-3CB371?style=for-the-badge&logo=fastapi&logoColor=white)
![](https://img.shields.io/badge/SQL_Alchemy-red?style=for-the-badge)
![](https://img.shields.io/badge/Git_Hub-grey?style=for-the-badge&logo=github&logoColor=white)
![](https://img.shields.io/badge/PYTEST-blue?style=for-the-badge&logo=pytest&logoColor=white)
![](https://img.shields.io/badge/ALEMBIC-FFA500?style=for-the-badge)
![](https://img.shields.io/badge/uvicorn-FF00FF?style=for-the-badge)


---
### Архитектура проекта<a name="architecture"></a>

| Директория | Описание                     |
|------------|------------------------------|
| `alembic`  | Содержит миграции проекта    |
| `app`      | Файлы проекта  FastAPI       |
| `test`     | Директория с тестами проекта |                             
---
### Как развернуть проект локально?<a name="start_project"></a>

* Клонировать репозиторий и перейти в него в командной строке:

  ```
  git clone https://github.com/FakaFakaYeah/donation_project.git
  ```

  ```
  cd cat_charity_fund
  ```

* Cоздать и активировать виртуальное окружение:

  ```
  python3 -m venv venv
  ```

   Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```
   Если у вас windows

    ```
    source venv/scripts/activate
    ```
  
* Установить зависимости из файла requirements.txt:

  ```
  python3 -m pip install --upgrade pip
  ```

  ```
  pip install -r requirements.txt
  ```

* Наполнить env файл<br>
  В проекте создан шаблон env файла, добавьте вначале точку, заполните значения
  
  ```
  DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
  TITLE=Благотворительного фонда поддержки котиков QRKot
  DESCRIPTION=Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.
  SECRET= Ваш секретный ключ
  ```

* Выполнить миграции
  ```
  alembic upgrade head
  ```


* Запустить проект

  ```
  uvicorn app.main:app --reload
  ```

* Проект будет доступен по следующему адресу:

  ```
  http://127.0.0.1:8000 
  ```

* Документация проекта со всеми описаниями и эндпоинтами доступна по адресу:

  ```
  http://127.0.0.1:8000/docs
  ```

---
### Авторы проекта:<a name="author"></a>
Смирнов Степан
<div>
  <a href="https://github.com/FakaFakaYeah">
    <img src="https://github.com/FakaFakaYeah/FakaFakaYeah/blob/main/files/images/GitHub.png" title="GitHub" alt="Github" width="39" height="39"/>&nbsp
  </a>
  <a href="https://t.me/s_smirnov_work" target="_blank">
      <img src="https://github.com/FakaFakaYeah/FakaFakaYeah/blob/main/files/images/telegram.png" title="Telegram" alt="Telegram" width="40" height="40"/>&nbsp
  </a>
</div>