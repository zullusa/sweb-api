# Виртуальный хостинг / SSL

SSL
===

объект

описание

SSL для виртуального хостинга

применяемость

Виртуальный хостинг

путь к объекту

POST https://api.sweb.ruvh/ssl

требование к авторизации

да

список методов

*   index;
*   getOrderList;
*   download;
*   editAutoprolong;
*   removeCertificate;
*   getProlongInfo;
*   prolongCertificate;
*   installLetsEncrypt.

index
-----

метод

описание

Возвращает список сертификатов пользователя

возвращаемые значения в свойствах объекта

'list' array список сертификатов, со следующими свойствами:

'id' int ID сертификата

'status' string Статус

'ip' string|null IP (только для VH)

'domain' string Домен

'name' string Название

'valid\_to' string Дата действия

'prolong\_available' int Доступно продление

'autoprolong' bool Включено автопродление

'autoprolongAllowed' bool Доступно автопродление

'autoprolongAddition' array Дополнительная информация по автопродлению:

'id' int ID сертификата

'name' string Сокращенное название сертификата

'full\_name' string Полное название сертификата

'price' int Стоимость продления

'filterInfo' array Информация о странице

'page' int номер текущей страницы

'perPage' int кол-во элементов на странице (20 по умолчанию)

'orderField' string название поля для сортировки ('id', 'valid\_to', 'fqdn', 'status', 'ip')

'orderDirect' string тип сортировки (asc - прямая; desc - обратная)

'totalCount' int общее кол-во

параметры в запросе

page

integer

страница (с 1-й)

perPage

integer

количество записей на странице

orderField

string

поле для сортировки: 'id', 'valid\_to', 'fqdn', 'status', 'ip'

orderDirect

string

направление сортировки: 'asc' или 'desc'

тип данных в ответе

object

пример запроса

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

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"762817724111069.fLqhIAAgBi"

"result":{

"list":\[

{

"id":

"525686"

"status":

"waiting"

"ip":

"sni"

"domain":

"mysite.ru"

"name":

NULL

"valid\_to":

NULL

"prolong\_available":

0

"autoprolong":

false

"autoprolongAllowed":

false

"autoprolongAddition":

NULL

}

{

"id":

"466893"

"status":

"issued"

"ip":

"sni"

"domain":

"mysite.ru"

"name":

"Let's Encrypt"

"valid\_to":

"2023-01-23"

"prolong\_available":

0

"autoprolong":

true

"autoprolongAllowed":

false

"autoprolongAddition":

NULL

}

\]

"filterInfo":{

"page":

1

"perPage":

20

"orderField":

"id"

"orderDirect":

"desc"

"totalCount":

6

}

}

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

'autoprolongAddition' array|null Дополнительная информация по автопродлению

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getOrderList"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"301198927631810.hNkxUavFCI"

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

0

}

"prices\_old":

NULL

"autoprolongAddition":

NULL

}

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

'mimetype' string MIME-тип данных (application/zip;base64)

'metadata' array мета-данные

'content' string содержимое в base64

'name' string название файла

параметры в запросе

id

integer

идентификатор сертификата

password

string

пароль от аккаунта

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"download"

"params":{

"id":

466893

"password":

"......."

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"284939793632386.wzYdRhMiAF"

"result":{

"mimetype":

"application/zip;base64"

"metadata":\[\]

"content":

"......"

"name":

"my\_cert.zip"

}

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

идентификатор сертификата

autoprolong

boolean

автопроделние

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"editAutoprolong"

"params":{

"id":

466893

"autoprolong":

true

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"706267465629678.LTXEfhFXEg"

"result":

1

}

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

идентификатор сертификата

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"removeCertificate"

"params":{

"id":

466893

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"719144789994256.uwXtIRPIle"

"result":

1

}

getProlongInfo
--------------

метод

описание

Получение информации о вариантах продления сертификата

возвращаемые значения в свойствах объекта

'currentCertificateId' int Идентификатор сертификата

'orderData' array Информация для заказа:

'domain' string Домен

'sub\_domain' string|null Доддомен

'person\_id' string ID персоны

'mailbox' string Почтовый ящик

'company\_link' string Ссылка на компанию

'nic\_customer\_id' string ID клиента

'auth\_type' string Тип аутентификации

'nic\_order\_id' string|null ID заказа

'is\_machine' string Поддомен (N - если отсутствует)

'prices' array Цены:

'12' string стоимость за год

'ids' array ID сертификатов

'title' string Название

'isFreeCertificate' bool Флаг бесплатного сертификата

параметры в запросе

certificateId

integer

идентификатор сертификата

тип данных в ответе

object

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getProlongInfo"

"params":{

"id":

466893

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"390876526920702.BSalJELdxU"

"result":{

"currentCertificateId":

348397

"orderData":{

"domain":

"testetste.com"

"sub\_domain":

NULL

"person\_id":

"359688"

"mailbox":

"admin@dfhbvjd.org.ru"

"company\_link":

""

"nic\_customer\_id":

"777"

"auth\_type":

"dns"

"nic\_order\_id":

NULL

"is\_machine":

"N"

}

"prices":{

"12":

"4100.00"

}

"ids":{

"12":

"27"

}

"title":

"GlobalSign DomainSSL"

"isFreeCertificate":

false

}

}

prolongCertificate
------------------

метод

описание

Продлевает сертификат

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

currentCertificateId

integer

текущий сертификат

certificateProlongId

integer

новый сертификат

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"prolongCertificate"

"params":{

"id":

466893

"certificateProlongId":

987234

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"058242250838769.OulgJFmibf"

"result":

1

}

installLetsEncrypt
------------------

метод

описание

Установка сертификата LetsEncrypt

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

domain

string

домен

virtdom

string

поддомен

ip

string

ip

wildcard

integer

wildcard-сертификат или нет

challenge

string

тип подтверждения ('acme' , 'dns')

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"installLetsEncrypt"

"params":{

"domain":

"mysite.ru"

"virtdom":

"poddomen.mysite.ru"

"ip":

"sni"

"wildcard":

0

"challenge":

"dns"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"702315915569124.zQZNCOkrST"

"result":

1

}