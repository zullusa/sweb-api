# VPS / IP-адреса

Ip
==

объект

описание

IP-адреса

применяемость

VPS

путь к объекту

POST https://api.sweb.ruvps/ip

требование к авторизации

да

список методов

*   index;
*   getAllIpList;
*   getOrderInfo;
*   addProtected;
*   removeProtected;
*   updateProtected;
*   moveProtected;
*   add;
*   addLocal;
*   removeLocal;
*   remove;
*   move;
*   editPtr;
*   getPtr.

index
-----

метод

описание

Получение информации о IP

возвращаемые значения в свойствах элементов массива

'ips' array

'ip' string IP-адрес

'gateway' string шлюз

'netmask' string маска подсети

'datacenter' int дата центр

'canBeDeclined' int можно ли отказаться от этого IP

'ptr' string обратная зона

'price' int стоимость платного доп. IP на VPSn

'protected\_ips' array

'ip' string IP-адрес

'gateway' string шлюзn

'netmask' string маска подсетиn

'canBeDeclined' int можно ли отказаться от этого IP

'ptr' string обратная зонаn

'price' int стоимость IP на VPSn

'planId' int ID тарифа

'limit' int Лимит канала (Mбит)

'vps' array информация об услуге VPS

'billingId' string идентификатор услуги VPS

'currentAction' string|null текущая операция над VPS

'isEmpty' string 0|1 Если 0, то услуга была проинициализирована, ОС установлена

'ordered\_ip\_count' string Количество адресов, заказанных на VPS

'local\_ip' array информация о локальном IP для услуги $billingId

'ip' string локальный IP-адрес 'mac' string MAC-адрес интерфейса 'mask' string маска подсети \]

параметры в запросе

billingId

string

идентификатор услуги (в формате login\_vps\_1)

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"index"

"params":{

"billingId":

"vhp\*\*\*\*\_vps\_1"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"613983368330015.HpfpHgcPIc"

"result":{

"ips":\[

{

"ip":

"192.168.122.70"

"gateway":

"192.168.122.1"

"netmask":

"192.168.122.0/24"

"datacenter":

1

"canBeDeclined":

1

"ptr":

"192-168-122-70.vps-ptr.clients.spaceweb.ru."

"price":

140

}

\]

"protected\_ips":\[

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

\]

"vps\_ip":\[\]

"local\_ip":\[\]

"vps":{

"billingId":

"dyasyuc384\_vps\_1"

"currentAction":

NULL

"isEmpty":

"0"

"ordered\_ip\_count":

2

}

}

}

getAllIpList
------------

метод

описание

Получение списка всех IP на аккаунте пользователя

возвращаемые значения в свойствах элементов массива

'ip' string IP

'name' string|null Имя VPS, может отсутствовать, если IP не привязан к услуге VPS

'billingId' string|null Идентификатор услуги 'login\_vps\_3'

'datacenter' int id дата-центра

'gateway' string шлюз

'netmask' string маска подсети

'isPrimary' bool является ли IP основным на услуге. false - дополнительные IP

'allowBeDecline' bool доступна ли функция Отказаться от IP (показать/скрыть элемент)

'canBeDecline' bool активна ли функция Отказаться от IP (доступность для использования)

'canBeMove' bool активна ли функция Перенести (доступность для использования)

'currentAction' string|null текущее действие с VPS (такое же, как current\_action у метода vps/ index() )

'acceptorBillingIds' array перечень realBillingId, на которые можно переместить данный IP

'name' => 'пользовательское имя vps'

'billingId' => 'user\_vps\_2'

'price' int может быть цена 0, если стоимость IP входит в тариф

'date' string дата окончания услуги в формате 01.07.2022

'planId' int|null ID тарифа защищенного IP

'limit' int|null Лимит канала защищенного IP (Mбит)

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getAllIpList"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"567245997454247.odCvHeVIdw"

"result":\[

{

"ip":

"192.168.122.70"

"name":

"dyasyuc384\_vps\_1"

"billingId":

"dyasyuc384\_vps\_1"

"datacenter":

1

"gateway":

"192.168.122.1"

"netmask":

"192.168.122.0/24"

"isPrimary":

false

"allowBeDecline":

true

"canBeDecline":

true

"canBeMove":

true

"currentAction":

NULL

"acceptorBillingIds":\[\]

"price":

140

"date":

"11.06.2025"

"limit":

NULL

"planId":

NULL

}

{

"ip":

"192.168.122.81"

"name":

NULL

"billingId":

NULL

"datacenter":

1

"gateway":

"192.168.122.1"

"netmask":

"192.168.122.0/24"

"isPrimary":

false

"allowBeDecline":

true

"canBeDecline":

true

"canBeMove":

true

"currentAction":

NULL

"acceptorBillingIds":\[

{

"name":

"dyasyuc384\_vps\_1"

"billingId":

"dyasyuc384\_vps\_1"

}

\]

"price":

140

"date":

"11.06.2025"

"limit":

NULL

"planId":

NULL

}

{

"ip":

"127.0.105.44"

"name":

"dyasyuc384\_vps\_1"

"billingId":

"dyasyuc384\_vps\_1"

"datacenter":

1

"gateway":

"127.0.105.1"

"netmask":

"127.0.105.0/24"

"isPrimary":

false

"allowBeDecline":

true

"canBeDecline":

true

"canBeMove":

true

"currentAction":

NULL

"acceptorBillingIds":\[\]

"price":

6000

"date":

NULL

"planId":

2

"limit":

50

}

\]

}

getOrderInfo
------------

метод

описание

Возвращает информацию по лимитам заказов ip

возвращаемое значение

'ipOrdersLastDay' int кол-во заказанных обычных IP-адресов за последние сутки

'dailyIpLimit' int кол-во разрешенных к заказу обычных IP-адресов за сутки

'protectedIpOrdersLastDay' int кол-во заказанных защищенных IP-адресов за последние сутки

'dailyProtectedIpLimit' int кол-во разрешенных к заказу защищенных IP-адресов за сутки

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getOrderInfo"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"285776202138203.fXkJxChvhA"

"result":{

"ipOrdersLastDay":

0

"dailyIpLimit":

7

"protectedIpOrdersLastDay":

0

"dailyProtectedIpLimit":

7

}

}

addProtected
------------

метод

описание

Добавляет защищенный IP на VPS

возвращаемое значение

true - если операция прошла успешно, ошибка 'Неврный тарифный план для защищенного IP' - ошибка в указании id тарифа

параметры в запросе

billingId

string

Идентификатор услуги (в формате login\_vps\_number)

planIds

array

ID тарифов защищенных IP

тип данных в ответе

boolean

пример запроса

{

"jsonrpc":

"2.0"

"method":

"addProtected"

"params":{

"billingId":

"dyasyuc584\_vps\_1"

"planIds":\[

2

3

\]

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"669222107696009.ovAotdMaWM"

"result":

true

}

removeProtected
---------------

метод

описание

Удаляет защищенный IP

возвращаемое значение

1 - успешно, 0 - не успешно

параметры в запросе

ip

string

Защищенный IP адрес

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"removeProtected"

"params":{

"removeProtected":

"127.0.105.54"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"492924172795286.PZJczfpgcB"

"result":

false

}

updateProtected
---------------

метод

описание

Изменяет тариф защищенного IP

возвращаемое значение

true - успешно, false - ошибка

параметры в запросе

ip

string

Защищенный IP адрес

planId

integer

ID нового тарифа защищенного IP

тип данных в ответе

boolean

пример запроса

{

"jsonrpc":

"2.0"

"method":

"updateProtected"

"params":{

"ip":

"127.0.105.44"

"planId":

1

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"014638797613332.dtyRPzHlVO"

"result":

true

}

moveProtected
-------------

метод

описание

Перемещает между VPS или открепляет/прикрепляет от/к VPS защищенный IP

возвращаемое значение

true - успешно, false - ошибка

параметры в запросе

ip

string

защищенный IP адрес

billingId

string

Идентификатор услуги, null - открепить услугу

тип данных в ответе

boolean

пример запроса

{

"jsonrpc":

"2.0"

"method":

"moveProtected"

"params":{

"ip":

"127.0.105.54"

"billingId":

"dyasyuc584\_vps\_1"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"202465971064708.BqNbobHhrQ"

"result":

true

}

add
---

метод

описание

Добавить необходимое количество доп. IP на VPS

возвращаемое значение

1 - успешно, 0 - не успешно

параметры в запросе

billingId

string

идентификатор услуги

number

integer

кол-во добавляемых адресов

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"add"

"params":{

"billingId":

"dyasyuc584\_vps\_1"

"number":

"1"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"102403020504298.XZQCCqONxr"

"result":

1

}

addLocal
--------

метод

описание

Подключение VPS к локальной сети

возвращаемое значение

1 - успешно, 0 - не успешно

параметры в запросе

billingId

string

идентификатор услуги

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"addLocal"

"params":{

"billingId":

"dyasyuc584\_vps\_1"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"877672240936515.OAjYkrARbW"

"result":

1

}

removeLocal
-----------

метод

описание

Удаление локального IP

возвращаемое значение

1 - успешно, 0 - не успешно

параметры в запросе

billingId

string

идентификатор услуги

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"removeLocal"

"params":{

"billingId":

"dyasyuc584\_vps\_1"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"634548838226901.kKPLPqxMsI"

"result":

1

}

remove
------

метод

описание

Удаление IP. Нельзя удалять связанный IP передавая при этом пустой $billingId.

возвращаемое значение

1 - успешно, 0 - не успешно

параметры в запросе

billingId

string

идентификатор услуги - для удаления несвязанных с услугой IP должна быть передана пустая строка

ip

string

ip адрес

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"remove"

"params":{

"billingId":

"dyasyuc584\_vps\_1"

"ip":

"127.0.105.54"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"817596183061558.tHjTqlXnRb"

"result":

1

}

move
----

метод

описание

Перемещение IP между услугами VPS и прикрепление/открепление IP от услуги VPS

возвращаемое значение

1 - успешно, 0 - не успешно

параметры в запросе

ip

string

ip адрес

billingId

string

идентификатор услуги, на которую нужно перенести данный IP. Если null, то IP будет откреплен от услуги

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"move"

"params":{

"ip":

"127.0.105.54"

"billingId":

"dyasyuc584\_vps\_1"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"628579445555355.uZnegJxyQX"

"result":

1

}

editPtr
-------

метод

описание

Редактирование PTR

возвращаемое значение

1 - успешно, 0 - не успешно

параметры в запросе

ip

string

ip адрес

ptr

string

обратная зона

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"editPtr"

"params":{

"ip":

"127.0.105.54"

"ptr":

"192-168-122-192.vps-ptr.clients.spacewb.ru."

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"244032886775533.qjjhYdCgfw"

"result":

1

}

getPtr
------

метод

описание

Получение обратной зоны для IP-адреса

возвращаемое значение

PTR-запись (обратная DNS-зона), null - если IP не привязан к услуге

параметры в запросе

ip

string

ip адрес

тип данных в ответе

string

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getPtr"

"params":{

"ip":

"127.0.105.54"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"610677025426640.QhjrSWfsgo"

"result":

"192-168-122-192.vps-ptr.clients.spacewb.ru."

}