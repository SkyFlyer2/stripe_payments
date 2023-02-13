# stripe_payments
# Платежи Stripe

Stripe - американская компания, разрабатывающая решения для приема и обработки электронных платежей.
Проект "Платежи Stripe" реализует основные возможности этой системы и показывает её работу.

## Автор
Ковалев Владислав (SkyFlyer), telegram: @skyflyer1

## Ссылка на сайт
Сервис запущен по [адресу](http://158.160.4.20/).

## Технологии:
* Python 3.8
* Django 4.6
* Django-Money
* Python DotEnv
* Docker & DockerHub
* Gunicorn
* Nginx

## Порядок действий для развертывания и запуска:

#### Локально (dev-сервер VS-Code)

* Клонируйте репозиторий и перейдите в него в командной строке:
```
git clone git@github.com:SkyFlyer2/stripe_payments.git
cd stripe_payments
```
* Cоздайте и активируйте виртуальное окружение:

```
python -m venv venv
source venv/Scripts/activate
```
* Установите зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Создайте аккаунт на [сайте](https://dashboard.stripe.com/register) платежной системы.
В разделе Developers/Api keys находятся ключи для тестового доступа к API системы. Скопируйте их.
В директории "stripepay" из шаблона ".env.template" создайте файл ".env" и пропишите в него полученные ранее ключи для доступа к API платежной системы (STRIPE_PUBLISHABLE_KEY и STRIPE_SECRET_KEY).
Также задайте значение ключа для Django (SECRET_KEY).
#### Важно! Кавычки в значениях ключей не требуются!

* Выполните миграции:
```
python manage.py migrate
```
* Создайте суперпользователя:
```
python manage.py createsuperuser
```
* Запустите проект:
```
python manage.py runserver
```

По адресу [http://127.0.0.1:8000] расположена главная страница со списком доступных товаров для покупки. Добавить новые товары можно через админ-панель Django: [http://127.0.0.1:8000/admin]

При клике на товар вызывается метод API *"/item/{id}"*, результатом работы которого является html-страница с кнопкой "Купить". По её нажатию происходит запрос на эндпоинт *"/buy/{id}"*, получение session_id и далее редирект на форму Checkout платежной системы.

Для "покупки" и "оплаты" введите тестовые данные карты:
```
Номер: 4242 4242 4242 4242
Дата действия: любая
Код CVC: любой
```

В личном кабинете Stripe вы можете посмотреть данные платежа.
##
#### Развертывание на удаленном сервере

Для удобства и быстрого запуска проекта был подготовлен образ Docker и загружен на DockerHub.

* Выполните вход на удаленный сервер

* Из каталога infra скопируйте на удаленный сервер файлы docker-compose.yml и nginx/default.conf.
```
scp docker-compose.yml <username>@<host>:/home/<username>/docker-compose.yml
scp -r nginx/default.conf <username>@<host>:/home/<username>/nginx/default.conf
```
```
/home/имя_пользователя/nginx/default.conf
/home/имя_пользователя/nginx/docker-compose.yml
```

* В файле infra/default.conf пропишите IP-адрес сервера:

```
server_name xxx.xxx.xxx.xxx;
```

* Cоздайте файл ```.env```:

```bash 
touch stripepay/.env
```

* Заполните ```.env``` файл переменными окружения по примеру:
```bash 
echo SECRET_KEY=<уникальный токен> >> .env
echo STRIPE_PUBLISHABLE_KEY=<публичный ключ stripe> >> .env
echo STRIPE_SECRET_KEY=<секретный ключ stripe> >> .env
```

* Теперь можно установить и запустить приложение в контейнерах (контейнеры web, nginx и python загружаются из DockerHub):
```bash 
sudo docker-compose up -d --build
```

* Запуск миграций, создание суперюзера, сбор статики и заполнение БД:
```
docker-compose exec infra_web_1 python manage.py migrate
docker-compose exec infra_web_1 python manage.py createsuperuser
docker-compose exec infra_web_1 python manage.py collectstatic --no-input 
```
* Проект доступен по адресу http://<IP адрес сервера>/

**Доступные адреса проекта:**

    -  http://<IP адрес сервера>/ - главная страница;
    -  http://<IP адрес сервера>/admin/ - панель администрирования;
    -  http://<IP адрес сервера>/item/{id}/ - метод API, возвращающий страницу html с кнопкой "Купить".
    -  http://<IP адрес сервера>/buy/{id} - метод API, получает Stripe Session Id для оплаты выбранного товара.

