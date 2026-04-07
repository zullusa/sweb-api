# Домены / Доменные персоны

Доменные персоны
================

объект

описание

Операции с доменными персонами

применяемость

Домены

путь к объекту

POST https://api.sweb.rudomains/persons

требование к авторизации

да

список методов

*   index;
*   getinfo;
*   createFizIp;
*   createJur.

index
-----

метод

описание

Cписок доменных персон у пользователя

возвращаемые значения в свойствах элементов массива

'props\_filled' int Заполнены реквизиты

'persons' array Список доменных персон со свойствами:

'name' string Имя

'sweb\_handle' string Идентификатор

'str' string Идентификатор строкой

'id' int ID персоны

'type' string Тип

'resident' int Резидент РФ

'used' int Использовалась

'valid' int Валидная

тип данных в ответе

array

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"index"

"params":{}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"811077106951120.IDVLJwDrSg"

"result":\[

{

"props\_filled":

1

"persons":\[

{

"name":

"Иванов Иван Иванович"

"sweb\_handle":

"SWEB-FIZ-III-2168"

"str":

"\[SWEB-FIZ-III-2168\] Иванов Иван Иванович"

"id":

367684

"type":

"f"

"resident":

0

"used":

0

"valid":

1

}
```

```json
{

"name":

"ИП Иванов Иван Иванович"

"sweb\_handle":

"SWEB-IP-IIII-15"

"str":

"\[SWEB-IP-IIII-15\] ИП Иванов Иван Иванович"

"id":

368973

"type":

"ip"

"resident":

1

"used":

0

"valid":

1

}
```

```json
{

"name":

"ООО "Ромашка""

"sweb\_handle":

"SWEB-ORG-R-1424"

"str":

"\[SWEB-ORG-R-1424\] ООО "Ромашка""

"id":

368972

"type":

"u"

"resident":

0

"used":

0

"valid":

1

}
```

\]

}

\]

}

getinfo
-------

метод

описание

Подробная информация по ID персоны

возвращаемые значения в свойствах элементов массива

Для физ лица:

'name' string

'nameTrans' string

'resident' bool

'phones' string

'emails' string

'postIndex' string

'postCity' string

'postAddress' string

'birthdate' string

'passSeries' string

'passNum' string

'passDate' string

'passOrg' string

'inn' string|null

'type' string

'used' int

Для юр.лица:

'name' string

'nameTrans' string

'resident' bool

'phones' string

'faxes' string

'emails' string

'postIndex' string

'postCity' string

'postAddress' string

'jurIndex' string

'jurCity' string

'jurAddress' string

'inn' string|null

'kpp' string|null

'persName' string

'persNameTrans' string

'type' string

'used' int

параметры в запросе

id

integer

ID персоны

тип данных в ответе

array

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"getinfo"

"params":{

"id":

367684

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"355714030361797.FlkQSumwLF"

"result":\[

{

"name":

"Иванов Иван Иванович"

"nameTrans":

"Ivanov Ivan Ivanovich"

"resident":

false

"phones":\[

"+7 999 9999999"

\]

"emails":\[

"test@sweb.ru"

\]

"postIndex":

"197376"

"postCity":

"Санкт-Петербург"

"postAddress":

"наб. р. Карповки, д. 5, корп. 3"

"birthdate":

"1990-01-01"

"passSeries":

"4502"

"passNum":

"987432"

"passDate":

"2010-01-01"

"passOrg":

"ОВД района Южное Бутово города Москвы"

"inn":

NULL

"type":

"f"

"used":

0

}
```

\]

}

createFizIp
-----------

метод

описание

Создание доменной персоны физ. лица и ИП

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

name

string

Наименование организации (ФИО)

resident

boolean

Резидент РФ

phones

string

Телефон

emails

string

E-mail представителя

postIndex

string

Индекс

postCity

string

Город

postAddress

string

Адрес

birthdate

string

Дата рождения

passSeries

string

Серия паспорта

passNum

string

Номер паспорта

passDate

string

Дата выдачи

passOrg

string

Кем выдан

inn

string

ИНН

id

string

ID персоны (передается в случае редактирования)

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"createFizIp"

"params":{

"name":

"ИП Иванов Иван Иванович"

"resident":

true

"phones":

"+7 999 9999999"

"emails":

"test@sweb.ru"

"postIndex":

"197376"

"postCity":

"Санкт-Петербург"

"postAddress":

"наб. р. Карповки, д. 5, корп. 3"

"birthdate":

"1990-01-01"

"passSeries":

"4502"

"passNum":

"987432"

"passDate":

"2010-01-01"

"passOrg":

"ОВД района Южное Бутово города Москвы"

"inn":

"123456789123"

"id":

NULL

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"029425050175928.QniuqABATU"

"result":

1

}
```

createJur
---------

метод

описание

Создание доменной персоны юр. лица

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

name

string

Наименование организации

nameTrans

string

Наименование организации на латинице

resident

boolean

Резидент РФ

phones1

string

Телефон для уведомлений

phones2

string

Телефон

faxes

string

Факс

emails

string

E-mail представителя

postIndex

string

Индекс (почтовый адрес)

postCity

string

Город (почтовый адрес)

postAddress

string

Адрес (почтовый адрес)

jurIndex

string

Индекс (юридический адрес)

jurCity

string

Город (юридический адрес)

jurAddress

string

Адрес (юридический адрес)

inn

string

ИНН

kpp

string

КПП

persName

string

ФИО контактного представителя

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"createJur"

"params":{

"name":

"ООО Ромашка"

"nameTrans":

"ООО Romashka"

"resident":

true

"phones1":

"+7 930 7654323"

"phones2":

"+7 930 7654323"

"faxes":

"+7 930 7654323"

"emails":

"test@sweb.ru"

"postIndex":

"197376"

"postCity":

"Санкт-Петербург"

"postAddress":

"наб. р. Карповки, д. 5, корп. 3"

"jurIndex":

"197376"

"jurCity":

"Санкт-Петербург"

"jurAddress":

"наб. р. Карповки, д.5, корп.3"

"inn":

"3664069397"

"kpp":

"3664069397"

"persName":

"Иванов Иван Иванович"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"920152612082780.PUDNLNcaZz"

"result":

1

}
```