# SwebClient - Python клиент для API Sweb.ru

Python-клиент для работы с API Sweb.ru через протокол JSON-RPC 2.0.

## Установка

```bash
pip install sweb-api
```

## Быстрый старт

```python
from sweb_api import SwebClient

# Создание клиента с авторизацией
client = SwebClient("ваш_логин", "ваш_пароль")

# Теперь можно использовать доступные методы
domains = client.domains.index()
```

## Конструктор

```python
SwebClient(login: str, password: str, timeout: int = 30)
```

Параметры:
- `login` - логин от личного кабинета Sweb.ru
- `password` - пароль от личного кабинета Sweb.ru
- `timeout` - таймаут запросов в секундах (по умолчанию 30)

## Доступные методы

### Виртуальный хостинг

| Свойство | Описание | API раздел |
|----------|----------|------------|
| `client.domains` | Управление доменами | domains |
| `client.domains_bonus` | Доменные бонусы | domains/bonus |
| `client.domains_persons` | Доменные персоны | domains/persons |
| `client.domains_dns` | Управление DNS | domains/dns |
| `client.sites` | Управление сайтами | sites |
| `client.hosting` | Базы данных (MySQL/PostgreSQL) | vh/hosting |
| `client.backup` | Резервные копии | vh/backup |
| `client.mail` | Почтовый сервис | vh/mail |
| `client.ssl` | SSL-сертификаты | vh/ssl |
| `client.tariff` | Информация о тарифе | tariff |
| `client.load` | Нагрузка на сервер | vh/load |
| `client.utils` | SSH-доступ | vh/utils |
| `client.cron` | Планировщик задач | vh/cron |
| `client.disk_usage` | Использование диска | vh/utils/diskUsage |
| `client.ddg` | Защита от DDOS | vh/ddg |

### VPS

| Свойство | Описание | API раздел |
|----------|----------|------------|
| `client.vps` | Управление VPS | vps |
| `client.vps_backup` | Резервные копии VPS | vps/backup |
| `client.vps_ssl` | SSL-сертификаты для VPS | vps/ssl |
| `client.vps_ip` | Локальная сеть | vps/ip |
| `client.vps_protected_ip` | Защищённые IP-адреса | vps/protected-ip |
| `client.vps_dbaas` | DBaaS ( Managed PostgreSQL) | vps/dbaas |
| `client.vps_balancer` | Балансировщик | vps/balancer |
| `client.vps_remote_backup` | Облачные бэкапы | vps/remote-backup |
| `client.vps_monitoring` | Мониторинг | vps/monitoring |
| `client.vps_monitoring_checks` | Проверки мониторинга | vps/monitoring/checks |
| `client.vps_monitoring_contacts` | Контакты мониторинга | vps/monitoring/contacts |

### Оплата и финансы

| Свойство | Описание | API раздел |
|----------|----------|------------|
| `client.pay` | Баланс и платежи | pay |

## Примеры использования

### Получение списка доменов

```python
from sweb_api import SwebClient

client = SwebClient("логин", "пароль")
domains = client.domains.index()
print(domains)
```

### Информация о тарифе

```python
client = SwebClient("логин", "пароль")
tariff_info = client.tariff.serverInfo()
print(tariff_info)
```

### Управление VPS

```python
client = SwebClient("логин", "пароль")

# Получить список VPS
vps_list = client.vps.index()

# Включить VPS
client.vps.powerOn(vps_id=123)

# Выключить VPS
client.vps.powerOff(vps_id=123)
```

### Работа с базами данных

```python
client = SwebClient("логин", "пароль")

# Список баз данных
databases = client.hosting.databaseGetList()

# Создать базу данных
client.hosting.databaseMysqlCreatedbname="new_db", user="user", password="pass")
```

### Работа с почтой

```python
client = SwebClient("логин", "пароль")

# Список почтовых ящиков
mailboxes = client.mail.getMailboxesList()

# Создать почтовый ящик
client.mail.createMbox(name="info", domain="example.ru", password="secret")
```

## Обработка ошибок

```python
from sweb_api import SwebClient
from sweb_api.exceptions import AuthenticationError

try:
    client = SwebClient("логин", "пароль")
except AuthenticationError as e:
    print(f"Ошибка авторизации: {e}")
```

## Требования

- Python 3.8+
- requests >= 2.28.0
- urllib3 >= 1.26.0