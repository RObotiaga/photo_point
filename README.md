# Тестовое задание PhotoPoint

## Описание задания
Создан Django проект, который при переходе на страницу `/get-current-usd/` отображает в формате JSON актуальный курс доллара к рублю (запрос по API). Также показывает 10 последних запросов с интервалом не менее 10 секунд между запросами.

## Реализация функционала
Используется библиотека `freecurrencyapi` для получения актуального курса. Записывается время перед отправкой запроса. Реализовано ограничение на 1 запрос в 10 секунд для каждого пользователя с использованием декоратора `ratelimit` и ограничение списка последних 10 запросов.

## Используемые библиотеки
- `django_ratelimit` для управления частотой запросов
- `freecurrencyapi` для получения данных о курсах валют
- `decouple` для безопасного хранения конфигурационных переменных

## Запуск проекта
1. Установите необходимые библиотеки: `poetry install`
2. Укажите ваш ключ API для `freecurrencyapi` в файле конфигурации (`.env`): `FREECURRENCYAPI=ваш_ключ`
3. Запустите Django проект: `python manage.py runserver`

## API Endpoint
- `/get-current-usd/`: GET запрос для получения актуального курса доллара к рублю и истории последних 10 запросов.

## Примечание
Убедитесь, что проект запущен в среде с доступом к интернету для корректной работы с внешним API.
