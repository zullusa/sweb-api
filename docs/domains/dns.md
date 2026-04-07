# Домены / DNS

Dns
===

объект

описание

Объект управления DNS записями

применяемость

Домены

путь к объекту

POST https://api.sweb.rudomains/dns

требование к авторизации

да

список методов

*   info;
*   editMx;
*   editSrv;
*   editNS;
*   editTxt;
*   getFile.

info
----

метод

описание

Получение текущих записей зоны DNS

возвращаемые значения в свойствах элементов массива

'service' string Идентификатор сервиса для записей

'protocol' string Протокол для записей

'ttl' string Время жизни записи

'priority' string Приоритет записи

'weight' string Вес записи

'port' string Номер порта TCP/UDP для записей

'target' string Целевой хост или IP-адрес, на который указывает запись

'index' string Идентификатор записи для редактирования/удаления

'category' string Тип сервиса или группа записей

'type' string Идентификатор, определяющий вид записи

'name' string Доменное имя, к которому применяется запись

'domain' string Основное доменное имя

'flag' string Числовой или строковый параметр, определяющий поведение записи

'tag' string Тип или категория записи

'value' string Значение параметра

параметры в запросе

domain

string

Основное доменное имя

тип данных в ответе

array

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"info"

"params":{

"domain":

"test32132.ru"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"935747963988238.tIUXXnetdK"

"result":{

"ips":\[

\[

{

"name":

""

"value":

"10.18.5.59"

"index":

0

"canChange":

"true"

"sel":

"A"

"type":

"A"

"category":

"zoneMain"

}
```

```json
{

"name":

"www"

"value":

"10.18.5.59"

"index":

1

"canChange":

"false"

"sel":

"A"

"type":

"A"

"category":

"zoneMain"

}
```

```json
{

"name":

"autoconfig"

"value":

"autoconfig.spaceweb.ru."

"type":

"CNAME"

"index":

2

"category":

"subdom"

}
```

```json
{

"name":

"autodiscover"

"value":

"autodiscover.spaceweb.ru."

"type":

"CNAME"

"index":

3

"category":

"subdom"

}
```

```json
{

"value":

"mx1.spaceweb.ru."

"priority":

"10"

"name":

""

"index":

0

"category":

"mx"

"type":

"MX"

}
```

```json
{

"value":

"mx2.spaceweb.ru."

"priority":

"20"

"name":

""

"index":

1

"category":

"mx"

"type":

"MX"

}
```

```json
{

"service":

"autodiscover"

"protocol":

"tcp"

"ttl":

"86400"

"priority":

"5"

"weight":

"0"

"port":

"443"

"target":

"autodiscover.spaceweb.ru."

"index":

0

"category":

"srv"

"type":

"SRV"

"name":

""

}
```

```json
{

"domain":

"@"

"ttl":

"600"

"value":

"v=spf1 include:\_spf.spaceweb.ru ~all"

"index":

0

"main":

1

"category":

"mainTxt"

"type":

"TXT"

}
```

\]

\]

"protected\_ips":\[

```json
{

"ip":

"127.0.105.44"

"gateway":

"127.0.105.1"

"netmask":

"127.0.105.0/24"

"canBeDeclined":

1

"ptr":

"44.105.0.127.in-addr.arpa."

"price":

6000

"planId":

2

"limit":

50

}
```

\]

"vps\_ip":\[\]

"local\_ip":\[\]

"vps":```json
{

"billingId":

"dyasyuc384\_vps\_1"

"currentAction":

NULL

"isEmpty":

"0"

"ordered\_ip\_count":

2

}
```

}

}

editMx
------

метод

описание

Редактирование МХ записи

возвращаемое значение

1 - успешно, ошибка - при некорректных параметрах

параметры в запросе

domain

string

Основное доменное имя

action

string

Тип операции с записью

index

integer

Идентификатор записи для редактирования/удаления

priority

integer

Приоритет записи

value

string

Сервер обработки почты

subDomain

string

Поддомен, если запись не для основного домена

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"editMx"

"params":{

"domain":

"test32132.ru"

"action":

"edit"

"index":

0

"priority":

11

"value":

"mx1.speweb.ru."

"subDomain":

"teess11.ru.retesttt.ru"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"768186299634860.DGWdhHYdwd"

"result":

1

}
```

editSrv
-------

метод

описание

Редактирование SRV записи

возвращаемое значение

true - успешно, ошибка - при некорректных параметрах

параметры в запросе

domain

string

Основное доменное имя

action

string

Тип операции с записью

index

integer

Идентификатор записи для редактирования/удаления

priority

integer

Приоритет записи

ttl

integer

Время жизни записи

weight

integer

Вес записи

target

string

Целевой хост или IP-адрес, на который указывает запись

service

string

Идентификатор сервиса для записей

protocol

string

Протокол для записей

port

integer

Номер порта TCP/UDP для записей

subDomain

string

Поддомен, если запись не для основного домена

тип данных в ответе

boolean

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"editSrv"

"params":{

"domain":

"test32132.ru"

"action":

"edit"

"index":

0

"priority":

11

"ttl":

"86400"

"weight":

"0"

"target":

"autodiscover.spaceweb.ru."

"service":

"autodiscove"

"protocol":

"tcp"

"port":

"443"

"subDomain":

"teess11.ru.retesttt.ru"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"197830267185970.CPpXCGrOiY"

"result":

true

}
```

editNS
------

метод

описание

Редактирование NS записи

возвращаемое значение

true - успешно, ошибка - при некорректных параметрах

параметры в запросе

domain

string

Основное доменное имя

action

string

Тип операции с аписью

index

integer

Идентификатор записи для редактирования/удаления

subDomain

string

Поддомен

value

string

Значение параметра

тип данных в ответе

boolean

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"editNS"

"params":{

"domain":

"test32132.ru"

"action":

"edit"

"index":

0

"subDomain":

"teess11.ru.retesttt.ru"

"value":

"111"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"189940035892239.dzdXBMKhfa"

"result":

true

}
```

editTxt
-------

метод

описание

Редактирование Txt записи

возвращаемое значение

true - успешно, ошибка - при некорректных параметрах

параметры в запросе

domain

string

Основное доменное имя

action

string

Тип операции с записью

index

integer

Идентификатор записи для редактирования/удаления

subDomain

string

Поддомен

value

string

Значение параметра

тип данных в ответе

boolean

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"editTxt"

"params":{

"domain":

"test32132.ru"

"action":

"edit"

"index":

0

"subDomain":

"teess11.ru.retesttt.ru"

"value":

"111"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"752720392854108.pGkEUFKHOr"

"result":

true

}
```

getFile
-------

метод

описание

Получение содержимого файла зоны

возвращаемые значения в свойствах элементов массива

содержимое файла зоны

параметры в запросе

domain

string

Основное доменное имя

тип данных в ответе

array

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"getFile"

"params":{

"domain":

"test32132.ru"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"301749244828894.ZcXadDnCXi"

"result":{

"mimetype":

"text/plain"

"metadata":\[\]

"content":

"@ IN SOA ns1.spaceweb.ru. dns1.sweb.ru. ( 2025043040 8H 2H 2W 10m ) IN A 10.18.5.59 IN NS ns1.spaceweb.ru. IN NS ns2.spaceweb.ru. IN NS ns3.spaceweb.pro. IN NS ns4.spaceweb.pro. IN MX 111 mx1.speweb.ru. IN MX 20 mx2.spaceweb.ru. www IN A 10.18.5.59 autoconfig IN CNAME autoconfig.spaceweb.ru. autodiscover IN CNAME autodiscover.spaceweb.ru. teess11.ru IN A 10.18.5.59 www.teess11.ru IN A 10.18.5.59 \_autodiscove.\_tcp 86400 IN SRV 5 0 443 autodiscover.spaceweb.ru. @ 600 IN TXT "v=spf1 include:\_spf.spaceweb.ru ~all/" teess11.ru.retesttt.ru IN NS 111."

"name":

"retesttt.ru.zone.txt"

}
```

}