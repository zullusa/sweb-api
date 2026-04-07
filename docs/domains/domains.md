# Домены / Домены

Domains
=======

объект

описание

Операции с доменами и поддоменами

применяемость

Домены

путь к объекту

POST https://api.sweb.rudomains

требование к авторизации

да

список методов

*   index;
*   getSubdomains;
*   getDomainInfo;
*   regAvailable;
*   getAvailablePackages;
*   regList;
*   reg;
*   move;
*   moveList;
*   changeProlong;
*   changeProlongList;
*   remove;
*   removeList;
*   prolong;
*   prolongList;
*   priceForTrasfer;
*   priceForRegistration;
*   removeSubdomain;
*   createSubdomain;
*   setRedirectVh;
*   getRedirectVh.

index
-----

метод

описание

Информация о доменах пользователя

возвращаемые значения в свойствах элементов массива

'fqdn' string Закодированное название домена

'fqdn\_readable' string Читаемое название домена

'fqdnList' string Закодированные названия доменов из пакета доменов

'fqdnReadableList' string Читаемые названия доменов из пакета доменов

'docroot' string Домашняя директория

'fqdn\_tech' string Технический домен

'fqdnTechList' string Список технических доменов для пакета доменов

'is\_available' int 1, если пакет доменов доступен для регистрации

'in\_queue' int 1, если идет операция над доменом

'order\_package\_id' int Номер заказа для пакета доменов

'subdomains' array Поддомены:

'docroot' string Домашняя директория поддомена

'machine' string Закодированное название поддомена

'machine\_readable' string Читаемое название поддомена

'siteAlias' string Название сайта в ПУ

'fqdn' string Полное закодированное название поддомена с доменом

'fqdn\_readable' string Читаемое полное название поддомена с доменом

'parent\_fqdn' string Закодированное название домена, совпадает с 'fqdn'

'parent\_fqdn\_readable' string Читаемое название домена, совпадает с 'fqdn\_readable'

'reg\_price' float Цена регистрации

'bonus\_available' int 1, если можно зарегистрировать за бонусы

'siteAlias' string Название сайта в ПУ

параметры в запросе

orderField

string

тип сортировки

orderDirect

string

направление сортировки

type

string

тип доменов ('all' - все домены; 'sweb' - только sweb; 'free' - свободные; 'other' - все остальные)

filter

string

фильтр по названию домена

page

integer

страница

perPage

integer

количество на странице

showPackages

boolean

выводить или нет пакеты доменов на аккаунте

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"index"

"params":{

"orderField":

"fqdn\_readable"

"orderDirect":

"ASC"

"type":

"all"

"filter":

"test"

"page":

1

"perPage":

20

"showPackages":

false

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"491089979812587.PQSTsZttcF"

"result":\[

{

"fqdn":

"test549849.ru"

"fqdn\_readable":

"test549849.ru"

"siteAlias":

"default"

"docroot":

"/home/i/innamaly76"

"fqdn\_tech":

"test549849.ru.swtest.ru"

"subdomains":\[

{

"docroot":

"/home/i/innamaly76"

"machine":

"\*"

"machine\_readable":

"\*"

"siteAlias":

"default"

"fqdn":

"\*.test549849.ru"

"fqdn\_readable":

"\*.test549849.ru"

"parent\_fqdn":

"test549849.ru"

"parent\_fqdn\_readable":

"test549849.ru"

}

\]

"reg\_price":

199

"bonus\_available":

false

}

\]

}

getSubdomains
-------------

метод

описание

Список поддоменов домена

возвращаемые значения в свойствах элементов массива

'value' string Закодированное название поддомена

'name' string Читаемое название поддомена

параметры в запросе

domain

string

домен

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getSubdomains"

"params":{

"domain":

"test549849.ru"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"992040264410254.MTMIWKlJmb"

"result":\[

{

"value":

"\*.test549849.ru"

"name":

"\*.test549849.ru"

}

\]

}

getDomainInfo
-------------

метод

описание

Полная информация о домене

возвращаемые значения в свойствах объекта

'is\_active\_task' int Выполняется операция над доменом

'autoreg' int Включена авторегистрация

'is\_taken' int Занят

'registrar' string Регистратор

'is\_our' int Под нашим управлением

'expired' string Дата окончания регистрации

'can\_prolong' int Можно продить сейчас

'prolong\_price' int Стоимость продления

'prolong\_by\_bonus' bool Можно ли продлить за бонусы

'prolong\_confirm' null|array Информация о продлении:

'domain' string Читаемое название домена

'confirm' bool Выводить или нет диалог с подтверждением операции продления

'price' int Стоимость продления

'link' string|null URL для ссылки на страницу с дополнительной информацией

'reg\_price' int Стоимость регистрации

'transfer\_price' int Стоимость трансфера

'autoprolong' string Тип автопродления

'docRoot' int Домашняя директория

'siteAlias' string Название сайта

'bonus\_available' bool Можно ли зарегистрировать за бонусы

'transferLink' string Ссылка на трансфер

'redirectUrl' string Адрес установленного редиректа

параметры в запросе

domain

string

домен

тип данных в ответе

object

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getDomainInfo"

"params":{

"domain":

"test549849.ru"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"803224957885741.ynEMPTSweh"

"result":{

"is\_active\_task":

0

"autoreg":

0

"is\_taken":

0

"registrar":

NULL

"is\_our":

0

"expired":

""

"can\_prolong":

0

"prolong\_price":

0

"prolong\_by\_bonus":

true

"prolong\_confirm":{

"domain":

"test549849.ru"

"confirm":

false

"price":

399

"link":

NULL

}

"reg\_price":

199

"transfer\_price":

\-1

"autoprolong":

"no"

"docRoot":

"/home/i/innamaly76"

"siteAlias":

"default"

"bonus\_available":

true

"transferLink":

NULL

"redirectUrl":

NULL

}

}

regAvailable
------------

метод

описание

Предварительная проверка на возможность регистрации домена

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

domain

string

домен

payType

string

тип оплаты

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"regAvailable"

"params":{

"domain":

"test549849.ru"

"payType":

"balance"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"383753711398377.OlPXjVilgk"

"result":

1

}

getAvailablePackages
--------------------

метод

описание

Проверяет возможность регистрации пакета для доменов, если пакет доступен, то добавляет его на аккаунт и возвращает объект с order\_package\_id - ID по которому его можно зарегистрировать

возвращаемые значения в свойствах элементов массива

'id' int ID пакета

'name\_readable' string Название пакета

'price' int Акционная цена

'price2' int Обычная цена

'priority' int Приоритет для отображения

'available' bool Доступен или нет для заказа

'domains' Домены из пакета:

'name' string Закодированное имя

'name\_readable' string Читаемое имя

'order\_package\_id' int Номер заказа пакета

параметры в запросе

domains

array

домены

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getAvailablePackages"

"params":{

"domains":

"testswebinnna.ru, testswebinnna.shop"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"470716726270567.QEDuEngRGO"

"result":\[

{

"id":

"3"

"name\_readable":

".ru+.shop"

"price":

"249"

"price2":

"398"

"priority":

"20"

"available":

true

"domains":\[

{

"name":

"testswebinnna.ru"

"name\_readable":

"testswebinnna.ru"

}

{

"name":

"testswebinnna.shop"

"name\_readable":

"testswebinnna.shop"

}

\]

"order\_package\_id":

696

}

\]

}

regList
-------

метод

описание

Зарегистрировать список доменов

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

domains

array

домены

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"regList"

"params":{

"domains":

"testswebinnna.ru, testswebinnna.shop"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"677379065314241.jrzDGiqfmr"

"result":

1

}

reg
---

метод

описание

Регистрация домена на аккаунте

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

domain

string

домен

payType

string

тип как будет оплачен домен ('balance' - деньги, 'bonus' - бонусы)

domPerson

integer

ID доменной персоны

prolongType

string

тип продления ('none', 'bonus\_money', 'manual')

autoReg

integer

авторегистрация

dir

string

относительная директория сайта

idShield

boolean

сокрытие Whois

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"reg"

"params":{

"domain":

"test549849.ru"

"payType":

"balance"

"domPerson":

359687

"prolongType":

"bonus\_money"

"autoReg":

0

"dir":

"/тест"

"idShield":

false

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"830955652135525.vEvJrzoITM"

"result":

1

}

move
----

метод

описание

Добавление домена на аккаунт

возвращаемое значение

1 - успешно, ExtendedResult (содержащий в data массив ошибок в формате \[fqdn: string, error: string\]) - ошибка

параметры в запросе

domain

string

домен

prolongType

string

тип продления ('no', 'bonus\_money', 'manual')

dir

string

домашняя директория (не обязательное поле)

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"move"

"params":{

"domain":

"test549849.ru"

"prolongType":

"bonus\_money"

"dir":

"/тест"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"474745760145700.ovlCIqQWbi"

"result":

1

}

moveList
--------

метод

описание

Добавление существующих доменов на аккаунт

возвращаемое значение

1 - успешно, ExtendedResult (содержащий в data массив ошибок в формате \[fqdn: string, error: string\]) - ошибка

параметры в запросе

domains

array

массив доменов: \[\['fqdn' : 'имя домена', 'prolongType' : 'тип продления ('no', 'manual', 'bonus\_money')', 'dir' : 'домашняя директория (не обязательное поле)'\]\]

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"moveList"

"params":{

"domains":\[

{

"fqdn":

"example.com"

"prolongType":

"manual"

"dir":

"/home/example"

}

{

"fqdn":

"test.com"

"prolongType":

"bonus\_money"

"dir":

"/home/test"

}

\]

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"374476651597292.WczElYjMHa"

"result":

1

}

changeProlong
-------------

метод

описание

Изменение настроек автопродления

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

domain

string

домен

prolongType

string

тип продления ('none', 'bonus\_money', 'manual')

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"changeProlong"

"params":{

"domain":

"test549849.ru"

"prolongType":

"bonus\_money"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"031522578269093.YzsmIShfec"

"result":

1

}

changeProlongList
-----------------

метод

описание

Массовая смена типа автопродления

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

domains

array

массив массивов: \[\['domain' : 'имя домена', 'prolongType' : 'тип продления ('no' - не продлевать, 'manual' - вручную клиентом, 'bonus\_money' - продлевать за ДБ)'\]\]

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"changeProlongList"

"params":{

"domains":\[

{

"domain":

"example.com"

"prolongType":

"bonus\_money"

}

{

"domain":

"test.com"

"prolongType":

"bonus\_money"

}

\]

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"464445276827990.EgCzWnKBFu"

"result":

1

}

remove
------

метод

описание

Удаление домена

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

domain

string

домен

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"remove"

"params":{

"domain":

"test549849.ru"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"625229330839441.MolMxiCWlv"

"result":

1

}

removeList
----------

метод

описание

Массовое удаление доменов

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

domains

array

домены

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"removeList"

"params":{

"domains":

"testswebinnna.ru, testswebinnna.shop"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"107398046591109.MaNdboHcPI"

"result":

1

}

prolong
-------

метод

описание

Продление домена

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

domain

string

домен

payType

string

тип оплаты

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"prolong"

"params":{

"domain":

"test549849.ru"

"payType":

"balance"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"140002864957485.HJzMEYiMTS"

"result":

1

}

prolongList
-----------

метод

описание

Массовое продление доменов

возвращаемые значения в свойствах объекта

'code' int индентификатор

'message' сообщение об успешном продлении

'data' date дата отправки заявки

параметры в запросе

domains

array

домены

тип данных в ответе

object

пример запроса

{

"jsonrpc":

"2.0"

"method":

"prolongList"

"params":{

"domains":

"testswebinnna.ru, testswebinnna.shop"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"834813228821363.dizzKMEKKT"

"result":{

"extendedResult":{

"code":

1

"message":

"Выбранные домены успешно продлены"

"data":\[\]

}

}

}

priceForTrasfer
---------------

метод

описание

Можно ли сделать трансфер домена

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

domain

string

домен

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"priceForTrasfer"

"params":{

"domain":

"test549849.ru"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"919533188039507.qlIwKRaooF"

"result":

1

}

priceForRegistration
--------------------

метод

описание

Стоимость регистрации домена

возвращаемое значение

стоимость регистрации домена

параметры в запросе

domain

string

домен

тип данных в ответе

string

пример запроса

{

"jsonrpc":

"2.0"

"method":

"priceForRegistration"

"params":{

"domain":

"test549849.ru"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"051670330215084.pNOXYbgvhm"

"result":

199

}

removeSubdomain
---------------

метод

описание

Удаление поддомена

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

domain

string

домен

machine

string

поддомен

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"removeSubdomain"

"params":{

"domain":

"test549849.ru"

"machine":

"test1"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"605362157080283.QOCkYsBISW"

"result":

1

}

createSubdomain
---------------

метод

описание

Добавление поддомена

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

domain

string

домен

machine

string

поддомен

dir

string

директория сайта

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"createSubdomain"

"params":{

"domain":

"test549849.ru"

"machine":

"test1"

"dir":

"/тест"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"656585730644531.SjobSNbPjX"

"result":

1

}

setRedirectVh
-------------

метод

описание

Установка переадресации для домена

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

domain

string

домен

redirect

string

URL редиректа

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"setRedirectVh"

"params":{

"domain":

"test549849.ru"

"setRedirectVh":

"https://testredirect.ru"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"604151400956609.iUJfrVyRQr"

"result":

1

}

getRedirectVh
-------------

метод

описание

Возвращает переадресацию для домена

возвращаемое значение

возвращает переадресацию для домена (URL редиректа)

параметры в запросе

domain

string

домен

тип данных в ответе

string

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getRedirectVh"

"params":{

"domain":

"test549849.ru"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"253323049301185.RrAuefzKEX"

"result":

"https://testgetredirect.ru"

}