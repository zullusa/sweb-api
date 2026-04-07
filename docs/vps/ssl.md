# VPS / SSL

SSL
===

объект

описание

SSL для VPS

применяемость

VPS

путь к объекту

POST https://api.sweb.ruvps/ssl

требование к авторизации

да

список методов

*   index;
*   getOrderList;
*   download;
*   editAutoprolong;
*   removeCertificate;
*   getProlongInfo;
*   orderSubmit.

index
-----

метод

описание

Возвращает список сертификатов пользователя

возвращаемые значения в свойствах элементов массива

'list' array Список сертификатов, со следующими свойствами:

'id' int ID сертификата

'status' string Статус

'ip' string|null IP (только для VH)

'domain' string Домен

'name' string Название

'valid\_to' string Дата действия

'prolong\_available' int Доступно продление

'autoprolong' bool Включено автопродление

'autoprolongAllowed' bool Доступно автопродление

'autoprolongAddition' array Дополнительная информация по автопродлению

'filterInfo' array Информация о странице

параметры в запросе

page

integer

Начиная с 1

perPage

integer

Кол-во записей на странице

orderField

string

Поле для сортировки: 'id', 'valid\_to', 'fqdn', 'status', 'ip'

orderDirect

string

Направление сортировки: 'asc' или 'desc'

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

"id"

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

"393763068970756.qomSfCqesC"

"result":\[

{

"list":\[

{

"id":

622297

"status":

"Заказ в обработке"

"ip":

NULL

"domain":

"www.kommersant.ru"

"name":

"GlobalSign AlphaSSL"

"valid\_to":

NULL

"prolong\_available":

0

"autoprolong":

true

"autoprolongAllowed":

false

"autoprolongAddition":{

"id":

"35"

"name":

"GlobalSign AlphaSSL"

"full\_name":

"GlobalSign AlphaSSL на 1 год"

"price":

1900

}
```

"isFree":

true

}

```json
{

"id":

620567

"status":

"Заказ в обработке"

"ip":

NULL

"domain":

"www.mail.ru"

"name":

"GlobalSign AlphaSSL"

"valid\_to":

NULL

"prolong\_available":

0

"autoprolong":

true

"autoprolongAllowed":

false

"autoprolongAddition":{

"id":

"36"

"name":

"GlobalSign AlphaSSL"

"full\_name":

"GlobalSign AlphaSSL на 1 год"

"price":

1900

}
```

"isFree":

true

}

\]

"filterInfo":```json
{

"page":

1

"perPage":

20

"orderField":

"id"

"orderDirect":

"desc"

"totalCount":

8

}
```

}

\]

}

getOrderList
------------

метод

описание

Получение списка сертификатов доступных для заказа

возвращаемые значения в свойствах элементов массива

'id' int ID сертификата

'name' string Название

'type' string Тип

'advantage\_text' string Описание

'persons' array Для каких доменных персон

'advantages' string\[\] Описание по-строчно

'periods' array Периоды

'prices' array|null Цены

'prices\_old' array|null Старые цены

тип данных в ответе

array

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"getOrderList"

"params":{}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"705473275075129.oAgilucaBc"

"result":\[

{

"id":

"12"

"name":

"GlobalSign AlphaSSL"

"type":

"dv"

"advantage\_text":

"Подтверждает домен"

"persons":\[

"u"

"f"

"ip"

\]

"advantages":\[

"для <b>юр.</b>/<b>физ.</b> <b>лиц</b> и <b>ИП</b>"

"количество доменов <b>1d + www</b>"

"гарантия <b>$10K</b>"

\]

"periods":\[

"12"

\]

"prices":{

"12":

"1900.00"

}
```

"prices\_old":

NULL

"autoprolongAddition":

NULL

}

```json
{

"id":

"7"

"name":

"GlobalSign DomainSSL"

"type":

"dv"

"advantage\_text":

"Подтверждает домен"

"persons":\[

"u"

"f"

"ip"

\]

"advantages":\[

"для <b>юр.</b>/<b>физ.</b> <b>лиц</b> и <b>ИП</b>"

"количество доменов <b>1d + www</b>"

"гарантия <b>$10K</b>"

\]

"periods":\[

"12"

\]

"prices":{

"12":

"4100.00"

}
```

"prices\_old":

NULL

"autoprolongAddition":

NULL

}

```json
{

"id":

"9"

"name":

"GlobalSign OrganizationSSL"

"type":

"ov"

"advantage\_text":

"Подтверждает организацию"

"persons":\[

"u"

\]

"advantages":\[

"для <b>юр.</b> <b>лиц</b>"

"количество доменов <b>1d + www</b>"

"гарантия <b>$1,25M</b>"

\]

"periods":\[

"12"

\]

"prices":{

"12":

"6750.00"

}
```

"prices\_old":

NULL

"autoprolongAddition":

NULL

}

```json
{

"id":

"8"

"name":

"GlobalSign DomainSSL WildCard"

"type":

"dv"

"advantage\_text":

"Домен и все поддомены"

"persons":\[

"u"

"f"

"ip"

\]

"advantages":\[

"для <b>юр.</b>/<b>физ.</b> <b>лиц</b> и <b>ИП</b>"

"<b>wildcard</b>"

"гарантия <b>$10K</b>"

\]

"periods":\[

"12"

\]

"prices":{

"12":

"11450.00"

}
```

"prices\_old":

NULL

"autoprolongAddition":

NULL

}

```json
{

"id":

"10"

"name":

"GlobalSign OrganizationSSL WildCard"

"type":

"ov"

"advantage\_text":

"Домен и все поддомены"

"persons":\[

"u"

\]

"advantages":\[

"для <b>юр.</b> <b>лиц</b>"

"<b>wildcard</b>"

"гарантия <b>$1,25M</b>"

\]

"periods":\[

"12"

\]

"prices":{

"12":

"17520.00"

}
```

"prices\_old":

NULL

"autoprolongAddition":

NULL

}

```json
{

"id":

"11"

"name":

"GlobalSign ExtendedSSL"

"type":

"ev"

"advantage\_text":

"Имя компании в строке браузера"

"persons":\[

"u"

\]

"advantages":\[

"для <b>юр.</b> <b>лиц</b>"

"количество доменов <b>1d + www</b>"

"гарантия <b>$1,5M</b>"

\]

"periods":\[

"12"

\]

"prices":{

"12":

"17550.00"

}
```

"prices\_old":

NULL

"autoprolongAddition":

NULL

}

\]

}

download
--------

метод

описание

Возвращает архив с файлами сертификата

возвращаемые значения в свойствах элементов массива

'mimetype' string MIME-тип данных

'metadata' array Метаданные

'content' string Контент

'name' string Название файла

параметры в запросе

id

integer

Идентификатор сертификата

password

string

Пароль от аккаунта

тип данных в ответе

array

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"download"

"params":{

"id":

348533

"password":

"........"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"214012085710833.WXjnOvrTaa"

"result":\[

{

"mimetype":

"application/zip;base64"

"metadata":\[\]

"content":

"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"

"name":

"test.ru.2023.348533.zip"

}
```

\]

}

editAutoprolong
---------------

метод

описание

Изменение режима автопродления сертификата

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

certificateId

integer

Идентификатор сертификата

autoprolong

integer

Автопроделние (0 или 1)

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"editAutoprolong"

"params":{

"certificateId":

348533

"autoprolong":

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

"354006597998340.YEGOKQidcW"

"result":

1

}
```

removeCertificate
-----------------

метод

описание

Удаляет сертификат

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

certificateId

integer

Идентификатор сертификата

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"removeCertificate"

"params":{

"certificateId":

348533

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"901259335743928.SvwkzlZaJx"

"result":

1

}
```

getProlongInfo
--------------

метод

описание

Получение информации о вариантах продления сертификата

возвращаемые значения в свойствах элементов массива

'currentCertificateId' int Идентификатор сертификата

'orderData' array Информация для заказа

'prices' array Цены

'ids' array ID сертификатов

'title' string Название

'isFreeCertificate' bool Флаг бесплатного сертификата

параметры в запросе

certificateId

integer

Идентификатор сертификата

тип данных в ответе

array

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"getProlongInfo"

"params":{

"certificateId":

348533

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"692585369079219.cmlLeITWGV"

"result":\[

{

"currentCertificateId":

348533

"orderData":{

"domain":

"test.ru"

"sub\_domain":

NULL

"person\_id":

"360120"

"mailbox":

"admin@test.ru"

"company\_link":

""

"nic\_customer\_id":

"777"

"auth\_type":

NULL

"nic\_order\_id":

NULL

"is\_machine":

"N"

}
```

"prices":```json
{

"12":

"1900.00"

}
```

"ids":```json
{

"12":

"35"

}
```

"title":

"GlobalSign AlphaSSL"

"isFreeCertificate":

false

}

\]

}

orderSubmit
-----------

метод

описание

Отправка заказа

возвращаемое значение

1 - успешно, 0 - ошибка, 2 - заказ ушел на ручную обработку

параметры в запросе

domain

string

Домен

certificateId

integer

Идентификатор сертификата

certificateConfirmMail

string

Email для подтверждения сертификата

personId

integer

ID доменной персоны

companyPageLink

string

Ссылка на страницу о компании

subdomain

string

Поддомен

autoprolong

integer

Автопродление

oldCertificateId

integer

Старый id доменной персоны

fromProlongation

boolean

Отметка, что заказ сделан из конфирмации продления

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"orderSubmit"

"params":{

"domain":

"test.ru"

"certificateId":

348533

"certificateConfirmMail":

"admin@test.ru"

"personId":

360129

"companyPageLink":

NULL

"subdomain":

NULL

"autoprolong":

1

"oldCertificateId":

NULL

"fromProlongation":

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

"673938482960289.yOnaqmVpMw"

"result":

1

}
```