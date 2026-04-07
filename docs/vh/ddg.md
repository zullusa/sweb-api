# Виртуальный хостинг / DDG

DDG
===

объект

описание

Объект услуги 'Защита от DDoS'

применяемость

Виртуальный хостинг

путь к объекту

POST https://api.sweb.ruvh/ddg

требование к авторизации

да

список методов

*   index;
*   countAllDomains;
*   enable;
*   disable;
*   enableInfo;
*   priceWidget;
*   getPrice.

index
-----

метод

описание

Получение списка доменов с информацией о подключенных услугах

возвращаемые значения в свойствах элементов массива

'fqdn' string название домена в Punycode

'fqdnReadable' string читабельное название домена

'ip' string|null IP адрес или null если услуга не подключена

'expired' string|null дата истечения оплаты в формате yyyy-mm-dd или null если услуга не подключена

'blocked' string|null дата блокировки услуги в формате yyyy-mm-dd или null если услуга не подключена

'status' string статус слуги (disabled - не подключена, active - подключена, active\_blocked - заблокирована клиентом, blocked - заблокирована за неуплату)

параметры в запросе

page

integer

текущая страница (начиная с 1)

perPage

integer

кол-во доменов на странице

orderField

string

поле сортировки: по статусу 'status' (по умолчанию) или по названию домена 'fqdn'

orderDirect

string

'ASC' (по умолчанию) или 'DESC'

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

"orderField":

"status"

"orderDirect":

"ASC"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"404708916625591.XkiVMevLwP"

"result":\[

{

"fqdn":

"testdomen.shop"

"fqdnReadable":

"testdomen.shop"

"ip":

"77.222.44.5"

"expired":

"2024-07-10"

"blocked":

"2024-06-10"

"status":

"active\_blocked"

}
```

```json
{

"fqdn":

"domentest.ru"

"fqdnReadable":

"domentest.ru"

"ip":

"77.222.44.3"

"expired":

"2024-06-29"

"blocked":

NULL

"status":

"active"

}
```

```json
{

"fqdn":

"itomen.ru"

"fqdnReadable":

"itomen.ru"

"ip":

NULL

"expired":

NULL

"blocked":

NULL

"status":

"disabled"

}
```

\]

}

countAllDomains
---------------

метод

описание

Возвращает кол-во доменов клиента (за исключением технических). Используется для пагинации на главной

возвращаемое значение

кол-во доменов клиента (за исключением технических)

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"countAllDomains"

"params":{}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"408032970789982.eAhXfyPlfX"

"result":

21

}
```

enable
------

метод

описание

Подключить/разблокировать услугу для домена

возвращаемые значения в свойствах объекта

'fqdn' string название домена в Punycode

'fqdnReadable' string читабельное название домена

'isOnOurNs' bool домен на NS Spaceweb

'ip' string новый IP адрес

параметры в запросе

domain

string

название домена

тип данных в ответе

object

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"enable"

"params":{

"domain":

"test.ru"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"533279166390618.TfkDDAxGVa"

"result":{

"fqdn":

"test.ru"

"fqdnReadable":

"test.ru"

"isOnOurNs":

false

"ip":

"77.222.44.8"

}
```

}

disable
-------

метод

описание

Отключить/заблокировать услугу для домена

возвращаемые значения в свойствах объекта

'fqdn' string название домена в Punycode

'fqdnReadable' string читабельное название домена

'isOnOurNs' bool домен на NS Spaceweb

'expire' string дата истечения оплаты в формате dd.mm.yy

параметры в запросе

domain

string

название домена

тип данных в ответе

object

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"disable"

"params":{

"domain":

"test.ru"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"546049978839969.zJoYRDQknk"

"result":{

"fqdn":

"test.ru"

"fqdnReadable":

"test.ru"

"isOnOurNs":

false

"expire":

"10.07.24"

}
```

}

enableInfo
----------

метод

описание

Возвращает данные для страницы подключения услуги

возвращаемые значения в свойствах объекта

'domains' array массив доменов доступных для подключения услуги c элементами:

'fqdn' string FQDN в Punycode,

'fqdnReadable' string читабельный FQDN,

'ssl' array|null информация по SSL сертификату домена или null при его отсутствии,

'isOnOurNs' bool сомен на NS Spaceweb

'price' float|int стоимость подключения услуги

тип данных в ответе

object

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"enableInfo"

"params":{}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"284439005676153.rXZIRdGDDN"

"result":{

"domains":\[

{

"fqdn":

"test1.ru"

"fqdnReadable":

"test1.ru"

"ssl":{

"isOur":

true

"isFilled":

true

}
```

"isOnOurNs":

true

}

```json
{

"fqdn":

"test2.com"

"fqdnReadable":

"test2.com"

"ssl":

NULL

"isOnOurNs":

false

}
```

\]

"price":

290

}

}

priceWidget
-----------

метод

описание

Цены на услугу для виджета 'Смена тарифа'

возвращаемые значения в свойствах объекта

'current' float|int стоимость услуги на текущем тарифе

'new' float|int стоимость услуги при переходе на тариф другой линейки

тип данных в ответе

object

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"priceWidget"

"params":{}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"191358370639405.tgxanVBKUG"

"result":{

"current":

"290"

"new":

"990"

}
```

}

getPrice
--------

метод

описание

Возвращает стоимость услуги для текущего тарифного плана пользователя

возвращаемое значение

стоимость услуги для текущего тарифного плана пользователя

тип данных в ответе

number

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"getPrice"

"params":{}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"407807895584919.pmeKSLLZNy"

"result":

290

}
```