# VPS / Мониторинг. Контакты

Monitoring
==========

объект

описание

Объект управления контактами сервиса Мониторинг

применяемость

VPS

путь к объекту

POST https://api.sweb.ru/monitoring/contacts

требование к авторизации

да

список методов

*   index;
*   getAllContacts;
*   addContact;
*   editContact;
*   addEmail;
*   editEmail;
*   addPhone;
*   editPhone;
*   deleteContact;
*   deleteContacts;
*   addTelegram;
*   requestTelegramVerifyCode;
*   isVerified;
*   editTelegram;
*   verifyContact.

index
-----

метод

описание

Возвращает список контактов мониторинга для текущего пользователя для отображения в ПУ. Не отображаются удаленные и неподтвержденные контакты.

возвращаемые значения в свойствах объекта

'list' array список контактов со следующими свойствами:

'id' int ID контакта

'type' string Тип контакта: email - электронная почта, phone - телефон, telegram - телеграм

'name' string Имя контакта

'value' string Значение контакта

'verified' bool Подтвержден ли контакт

'filterInfo' array массив информация для пагинации:

page - текущий номер страницы (начиная с 1) с данными в объекте list

perPage - текущее выбранное кол-во записей на одну страницу

orderField - поле для сортировки

orderDirect - направление для сортировки

totalCount - всего кол-во записей

параметры в запросе

page

integer

текущий номер страницы (начиная с 1)

perPage

integer

текущее выбранное кол.-во записей на одну страницу

orderField

string

поле сортировки, по умолчанию id

orderDirect

string

тип сортировки, по умолчанию asc

тип данных в ответе

object

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

2

"orderField":

"type"

"orderDirect":

"desc"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"185594759327922.XqUAKJxpAZ"

"result":{

"list":\[

{

"id":

"4320"

"type":

"phone"

"name":

"тест"

"value":

"+7 921 8990681"

"verified":

true

}
```

```json
{

"id":

"3205"

"type":

"email"

"name":

"Иванов Иван Иванович"

"value":

"test@gmail.ru"

"verified":

true

}
```

\]

"filterInfo":```json
{

"page":

1

"perPage":

2

"orderField":

"type"

"orderDirect":

"desc"

"totalCount":

2

}
```

}

}

getAllContacts
--------------

метод

описание

Возвращает список всех контактов мониторинга для текущего пользователя

возвращаемые значения в свойствах элементов массива

'list' array список контактов со следующими свойствами:

'id' int ID контакта

'type' string Тип контакта: email - электронная почта, phone - телефон, telegram - телеграм

'name' string Имя контакта

'value' string Значение контакта

'verified' bool Подтвержден ли контакт

'admin' bool Является ли административным контактом пользователя

тип данных в ответе

array

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"getAllContacts"

"params":{}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"354226792930327.jCGDTVvjwH"

"result":\[

{

"id":

"3204"

"type":

"phone"

"name":

"Иванов Иван Иванович"

"value":

"+7 949 8469541"

"verified":

false

"admin":

true

}
```

```json
{

"id":

"3205"

"type":

"email"

"name":

"Иванов Иван Иванович"

"value":

"test@gmail.ru"

"verified":

true

"admin":

true

}
```

```json
{

"id":

"4320"

"type":

"phone"

"name":

"тест"

"value":

"+7 921 8990681"

"verified":

true

"admin":

false

}
```

\]

}

addContact
----------

метод

описание

Добавление контакта

возвращаемое значение

id контакта, если контакт добавлен

параметры в запросе

type

string

тип контакта: 1 - электронная почта, 2 - телефон, 3 - ID телеграм-аккаунта

value

string

значение контакта: электронная почта, телефон или ID телеграм-аккаунта

name

string

имя контакта

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"addContact"

"params":{

"type":

"phone"

"value":

"+7 921 5556699"

"name":

"тест"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"849459893206910.igcLvIhjzo"

"result":

1

}
```

editContact
-----------

метод

описание

Редактирование контакта

возвращаемое значение

1, если контакт изменен

параметры в запросе

contactId

string

id контакта

value

string

значение контакта: электронная почта, телефон или ID телеграм-аккаунта

name

string

имя контакта

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"editContact"

"params":{

"contactId":

"1"

"value":

"+7 921 5556699"

"name":

"тест"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"608902333870402.oSdBEwHIea"

"result":

1

}
```

addEmail
--------

метод

описание

Добавление контакта - адреса электронной почты

возвращаемое значение

id контакта, если контакт добавлен

параметры в запросе

email

string

адрес электронной почты

name

string

имя контакта

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"addEmail"

"params":{

"email":

"test@gmail.ru"

"name":

"тест"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"367167883418955.MSNXvfQgsX"

"result":

1

}
```

editEmail
---------

метод

описание

Редактирование контакта - адреса электронной почты

возвращаемое значение

1, если контакт изменен

параметры в запросе

contactId

string

id контакта

email

string

адрес электронной почты

name

string

имя контакта

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"editEmail"

"params":{

"contactId":

"1"

"email":

"test@gmail.ru"

"name":

"тест"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"946227769579358.eTpmcyhWYz"

"result":

1

}
```

addPhone
--------

метод

описание

Добавление контакта - телефона

возвращаемое значение

id контакта, если контакт добавлен

параметры в запросе

phone

string

номер телефона

name

string

имя контакта

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"addPhone"

"params":{

"phone":

"+7 921 5556699"

"name":

"тест"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"903207785928744.SaZHpCOhgg"

"result":

1

}
```

editPhone
---------

метод

описание

Редактирование контакта - телефона

возвращаемое значение

1, если контакт изменен

параметры в запросе

contactId

string

id контакта

phone

string

новый телефон

name

string

новое имя контакта

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"editPhone"

"params":{

"contactId":

"1"

"phone":

"+7 921 5556699"

"name":

"тест"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"556585635768872.FrrpbuaPCO"

"result":

1

}
```

deleteContact
-------------

метод

описание

Удаление контакта

возвращаемое значение

1, если контакт удален

параметры в запросе

contactId

string

id контакта

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"deleteContact"

"params":{

"contactId":

"1"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"403222482488876.dkInfwnceZ"

"result":

1

}
```

deleteContacts
--------------

метод

описание

Удаление нескольких контактов

возвращаемые значения в свойствах элементов массива

1, если все контакты удалены

параметры в запросе

contactIds

array

список id контактов

тип данных в ответе

array

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"deleteContacts"

"params":{

"contactIds":\[

"1"

"2"

\]

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"886697639824492.ZMAfFLTXIg"

"result":

1

}
```

addTelegram
-----------

метод

описание

Добавление контакта - телеграма

возвращаемое значение

ID контакта, если контакт добавлен

параметры в запросе

name

string

имя контакта

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"addTelegram"

"params":{

"name":

"тест"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"423826595551765.WdbiezSuAm"

"result":

1

}
```

requestTelegramVerifyCode
-------------------------

метод

описание

Получить верификационный код для контакта Телеграм

возвращаемое значение

верификационный код

параметры в запросе

contactId

string

id контакта

тип данных в ответе

string

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"requestTelegramVerifyCode"

"params":{

"contactId":

"1"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"592919346649552.zdoQtNIbFW"

"result":

"611021"

}
```

isVerified
----------

метод

описание

Получить признак, подтвержден ли контакт

возвращаемое значение

true, если подтвержден; false, если неподтвержден

параметры в запросе

contactId

string

id контакта

тип данных в ответе

boolean

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"isVerified"

"params":{

"contactId":

"1"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"894782391622248.HGpHFtbvcG"

"result":

true

}
```

editTelegram
------------

метод

описание

Редактирование контакта - телеграма

возвращаемое значение

1, если контакт изменен

параметры в запросе

contactId

string

id контакта

name

string

новое имя контакта

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"editTelegram"

"params":{

"contactId":

"1"

"name":

"тест"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"936005465083051.BGYQNTYYWD"

"result":

1

}
```

verifyContact
-------------

метод

описание

Подтверждение контакта

возвращаемое значение

1, если контакт подтвержден

параметры в запросе

contactId

string

id контакта

code

string

код подтверждения

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"verifyContact"

"params":{

"contactId":

"1"

"code":

"611021"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"683944613350148.LgwxGPxEIj"

"result":

1

}
```