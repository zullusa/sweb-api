# Домены / Доменные бонусы

Доменные бонусы
===============

объект

описание

Операции с доменными бонусами

применяемость

Домены

путь к объекту

POST https://api.sweb.rudomains/bonus

требование к авторизации

да

список методов

*   index;
*   getList;
*   buy.

index
-----

метод

описание

Получение информации о доменных бонусах

возвращаемые значения в свойствах элементов массива

'bonuses' array Информация о бонусах

'count' int Общее число бонусов

'unusedCount' int Число неиспользованных бонусов

параметры в запросе

page

integer

Страница

orderBy

string

Cортировка null, valid\_till, date\_used

orderType

string

Направление сортировки ASC, DESC

used

boolean

Фильтр по использованным null, true, false

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

"0"

"orderBy":

"valid\_till"

"orderType":

"DESC"

"used":

"false"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"094961732435485.rCPrxFiXhY"

"result":\[

{

"bonuses":\[

{

"id":

"106067"

"type":

"3"

"customer\_id":

"testvps123"

"use\_type":

NULL

"ts\_create":

"2023-01-30 16:53:49"

"valid\_till":

"2024-01-30 23:59:59"

"domain":

NULL

"payment\_id":

"4690785"

"bonus\_id":

"0"

"bonus\_title":

NULL

"type\_title":

"Доменный бонус .ONLINE"

"tld":

"online"

"used":

"n"

"ts\_close":

NULL

}
```

\]

"count":

1

"unusedCount":

1

}

\]

}

getList
-------

метод

описание

Получение доступных к покупке пакетов бонусов

возвращаемые значения в свойствах элементов массива

'id' int ID пакета бонусов

'title' string Название

'descr' string Описание

'price' int Цена без скидки

'price\_old' int Цена без скидки

'domains' int Колическтво доменов в пакете

'price\_for\_domain' string Цена за домен

тип данных в ответе

array

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"getList"

"params":{}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"946830953988279.KoPPLrScaS"

"result":\[

{

"id":

30

"title":

"100 доменных бонусов"

"descr":

"Приобретение 100 доменных бонусов"

"price":

17000

"price\_old":

40000

"domains":

100

"price\_for\_domain":

"170 ₽ за домен"

}
```

```json
{

"id":

5

"title":

"50 доменных бонусов"

"descr":

"Приобретение 50 доменных бонусов"

"price":

9000

"price\_old":

20000

"domains":

50

"price\_for\_domain":

"180 ₽ за домен"

}
```

```json
{

"id":

4

"title":

"25 доменных бонусов"

"descr":

"Приобретение 25 доменных бонусов"

"price":

5000

"price\_old":

10000

"domains":

25

"price\_for\_domain":

"200 ₽ за домен"

}
```

```json
{

"id":

3

"title":

"10 доменных бонусов"

"descr":

"Приобретение 10 доменных бонусов"

"price":

2600

"price\_old":

4000

"domains":

10

"price\_for\_domain":

"260 ₽ за домен"

}
```

```json
{

"id":

2

"title":

"5 доменных бонусов"

"descr":

"Приобретение 5 доменных бонусов"

"price":

1500

"price\_old":

2000

"domains":

5

"price\_for\_domain":

"300 ₽ за домен"

}
```

```json
{

"id":

1

"title":

"3 доменных бонуса"

"descr":

"Приобретение 3 доменных бонусов"

"price":

1050

"price\_old":

1200

"domains":

3

"price\_for\_domain":

"350 ₽ за домен"

}
```

\]

}

buy
---

метод

описание

Покупка бонусов

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

bonusId

integer

ID пакета бонусов

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"buy"

"params":{

"bonusId":

30

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"008652317074142.hFUbBSlFoZ"

"result":

1

}
```