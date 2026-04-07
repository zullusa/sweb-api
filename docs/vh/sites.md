# Виртуальный хостинг / Сайты

Сайты
=====

объект

описание

Работа с сайтами

применяемость

Виртуальный хостинг

путь к объекту

POST https://api.sweb.ru/sites

требование к авторизации

да

список методов

*   index;
*   getSiteInfo;
*   add;
*   edit;
*   del;
*   changeDomainSite;
*   getBackEndsList;
*   changeBackEnd.

index
-----

метод

описание

Список всех сайтов на аккаунте пользователя

возвращаемые значения в свойствах элементов массива

'id' int ID сайта

'docRoot' string Домашняя директория

'docRootFull' string Домашняя директория полная

'alias' string Название сайта

'domainTech' string Технический домен

'antivirusExpired' string Дата окончания антивируса

'antivirusAvailable' bool Доступен заказ антивируса

'antivirusActive' int 1 - антивирус активен, 0 - антивирус неактивен

'antivirusPrice' int Стоимость антивируса

'redisSessionSelected' bool Добавлен ли этот сайт в список сайтов, сессии которых хранятся в Redis

'redisSessionEnabled' bool включено ли сейчас хранение сессий этого сайта в Redis

параметры в запросе

page

integer

страница (с 1-й)

perPage

integer

количество на странице

filter

string

фильтр по названию сайта или домену

тип данных в ответе

array

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"index"

"params":{

"page":

1

"perPage":

20

"filter":

"САЙТ"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"799981940731949.LsBeIlUWvd"

"result":\[

{

"id":

"105394"

"docRoot":

"/test"

"docRootFull":

"/home/i/imalysheva/test"

"alias":

"Сайт 3"

"domainTech":

NULL

"antivirusExpired":

NULL

"antivirusAvailable":

true

"antivirusActive":

0

"antivirusPrice":

199

"redisSessionSelected":

false

"redisSessionEnabled":

false

}
```

```json
{

"id":

"105417"

"docRoot":

"/тест567"

"docRootFull":

"/home/i/imalysheva/тест567"

"alias":

"Сайт 10"

"domainTech":

NULL

"antivirusExpired":

NULL

"antivirusAvailable":

true

"antivirusActive":

0

"antivirusPrice":

199

"redisSessionSelected":

false

"redisSessionEnabled":

false

}
```

\]

}

getSiteInfo
-----------

метод

описание

Получение подробной информации о сайте

возвращаемые значения в свойствах объекта

'backEnd' string Тип бэкэнда

'backEndId' int ID бэкэнда

'viewFiles' bool Показывать файлы

'runScripts' bool Запуск скриптов

'redisAvailable' bool Доступен ли Redis для подключения (определяется по тарифу и серверу)

'redisNeedTransfer' bool True, если Redis можно подключить на другом сервере, т.е. нужен перенос (при этом redisAvailable будет false)

'redisEnabled' bool Возможно ли подключение Redis (определяется по доступности (redisAvailable) и отсутствию текущих операций подключения/отключения)

'redisBackendAvailable' bool Доступен ли Redis для текущего бэкенда данного сайта (сейчас Redis доступен только для php7.\*, php8)

'redisSessionEnabled' bool Включено ли сейчас хранение сессий этого сайта в Redis

'redisCanEnableSession' bool Возможно ли включение хранений сессий в Redis (определяется по доступности (redisAvailable) и отсутствию текущих операций подключения/отключения)

'redisSessionSelected' bool Добавлен ли этот сайт в список сайтов, сессии которых хранятся в Redis

'encoding' string Кодировка

'domains' array Домены

'program' array Установленные программы

параметры в запросе

docRoot

string

директория сайта

тип данных в ответе

object

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"getSiteInfo"

"params":{

"docRoot":

"/dir"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"926893537795730.SvvrZzqtAP"

"result":{

"backEnd":

"Apache 2.2 + PHP 7.1 (Актуальная версия)"

"backEndId":

"8"

"viewFiles":

false

"runScripts":

true

"redisAvailable":

true

"redisBackendAvailable":

true

"redisNeedTransfer":

false

"redisEnabled":

true

"redisSessionEnabled":

false

"redisCanEnableSession":

true

"redisSessionSelected":

false

"encoding":

"UTF-8"

"domains":\[

"тестовыйдомен.рф"

\]

"program":\[\]

}
```

}

add
---

метод

описание

Метод для добавления сайта

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

alias

string

название сайта

docRoot

string

домашняя директория

domain

string

домен

machine

string

поддомен

enableRedisSession

boolean

включить запись сессий в Redis

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"add"

"params":{

"alias":

"Мой сайт"

"docRoot":

"/dir"

"domain":

"mysite.ru"

"machine":

"subdomain"

"enableRedisSession":

true

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"488621980049283.XNPPUXAvgw"

"result":

1

}
```

edit
----

метод

описание

Редактирование названия сайта и директории для docroot

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

docRoot

string

текущая директория сайта

alias

string

название сайта

docRootNew

string

новая директория

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"edit"

"params":{

"docRoot":

"/dir"

"alias":

"Мой сайт"

"docRootNew":

"newDir"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"871660881231220.hlZdzvbICW"

"result":

1

}
```

del
---

метод

описание

Удаление сайта

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

docRoot

string

директория сайта

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"del"

"params":{

"docRoot":

"/dir"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"782391120461516.KpAJQwxetu"

"result":

1

}
```

changeDomainSite
----------------

метод

описание

Cмена сайта для домена

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

domain

string

домен сайта

docRoot

string

директория сайта

machine

string

поддомен

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"changeDomainSite"

"params":{

"domain":

"mysite.ru"

"docRoot":

"/dir"

"machine":

"subdomain"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"188571902128815.xacYYQggiD"

"result":

1

}
```

getBackEndsList
---------------

метод

описание

Получение cписка доступных бэкэндов

возвращаемые значения в свойствах элементов массива

'id' int ID бэкэнда

'name' string Описание бэкэнда

тип данных в ответе

array

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"getBackEndsList"

"params":{}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"076508020902342.jwRAepisEW"

"result":\[

{

"id":

32

"name":

"Apache 2.4 + PHP 8.0 Bitrix (Актуальная версия)"

}
```

```json
{

"id":

23

"name":

"Apache 2.4 + PHP 8.1 opcache (Актуальная версия)"

}
```

```json
{

"id":

22

"name":

"Apache 2.4 + PHP 8 opcache + mod\_wsgi python3.8 (Актуальная версия)"

}
```

```json
{

"id":

21

"name":

"Apache 2.4 + PHP 7.4 Bitrix (Актуальная версия)"

}
```

```json
{

"id":

16

"name":

"Apache 2.2 + mod\_passenger + mod\_wsgi (Актуальная версия)"

}
```

```json
{

"id":

12

"name":

"Apache 2.4 + PHP 7.4 opcache (Актуальная версия)"

}
```

```json
{

"id":

11

"name":

"Apache 2.2 + PHP 7.1 opcache (Актуальная версия)"

}
```

```json
{

"id":

10

"name":

"Apache 2.2 + PHP 7.3 (Актуальная версия)"

}
```

```json
{

"id":

9

"name":

"Apache 2.2 + PHP 7.2 (Актуальная версия)"

}
```

```json
{

"id":

8

"name":

"Apache 2.2 + PHP 7.1 (Актуальная версия)"

}
```

```json
{

"id":

7

"name":

"Apache 2.2 + PHP 7 (Актуальная версия)"

}
```

```json
{

"id":

6

"name":

"Apache 2.2 + PHP 5.6 (Актуальная версия)"

}
```

```json
{

"id":

5

"name":

"Apache 2.2 + PHP 5.5 (Стабильная версия)"

}
```

```json
{

"id":

4

"name":

"Apache 2.2 + PHP 5.4 (Стабильная версия)"

}
```

```json
{

"id":

2

"name":

"Apache 2.2 + PHP 5.3 (Устаревшая версия)"

}
```

```json
{

"id":

1

"name":

"Apache 2.2 + PHP 5.2 (Устаревшая версия)"

}
```

\]

}

changeBackEnd
-------------

метод

описание

Смена типа бэкэнда для сайта

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

docRoot

string

директория сайта

backEndId

integer

ID Back-End из списка доступных

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"changeBackEnd"

"params":{

"docRoot":

"/dir"

"idBackEnd":

1

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"511222161064398.oZZKJMXYRh"

"result":

1

}
```