# Diplom_3
# Diplom_3 — UI-тесты для Stellar Burgers

Проект содержит автоматизированные UI-тесты для веб-приложения [Stellar Burgers](https://stellarburgers.education-services.ru). Тесты написаны на Python с использованием `pytest`, `Selenium` и `allure-pytest`. Реализован паттерн Page Object Model.

## Структура проекта

```
Diplom_3/
├── tests/
│   ├── test_base_functions.py   # Тесты основной функциональности
│   └── test_feed_page.py        # Тесты страницы «Лента заказов»
├── pages/
│   ├── base_page.py             # Базовый класс с общими методами
│   ├── main_page.py             # Страница «Конструктор»
│   ├── feed_page.py             # Страница «Лента заказов»
│   ├── login_page.py            # Страница авторизации
│   └── register_page.py         # Страница регистрации
├── locators/
│   ├── base_page_locators.py    # Локаторы шапки (навигация)
│   ├── main_page_locators.py    # Локаторы конструктора
│   ├── feed_page_locators.py    # Локаторы ленты заказов
│   ├── login_page_locators.py   # Локаторы страницы логина
│   └── register_page_locators.py # Локаторы страницы регистрации
├── conftest.py                  # Фикстуры (driver, page-объекты)
├── data.py                      # Вспомогательные функции
├── urls.py                      # URL-константы
├── pytest.ini                   # Конфигурация pytest
├── requirements.txt             # Зависимости
└── allure-report/               # Сгенерированный Allure-отчёт
```

## Тестовое покрытие

### Основная функциональность (`test_base_functions.py`)
- Переход на страницу «Конструктор» по клику на кнопку в навигации
- Переход на страницу «Лента заказов» по клику на кнопку в навигации
- Появление всплывающего окна с деталями ингредиента при клике на ингредиент
- Закрытие всплывающего окна кликом по крестику
- Увеличение счётчика ингредиента при добавлении его в заказ

### Лента заказов (`test_feed_page.py`)
- Увеличение счётчика «Выполнено за всё время» после оформления заказа
- Увеличение счётчика «Выполнено за сегодня» после оформления заказа
- Появление номера оформленного заказа в разделе «В работе»

## Установка

Установить зависимости:
```bash
pip install -r requirements.txt
```

## Запуск тестов

```bash
pytest --alluredir=allure-results
```

Тесты автоматически запускаются в двух браузерах: Google Chrome и Mozilla Firefox.

## Генерация и просмотр Allure-отчёта

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

## Стек

- Python 3
- pytest 9.0.2
- Selenium 4.41.0
- allure-pytest 2.15.3