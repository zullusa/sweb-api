# VPS / Балансировщик

Balancer
========

объект

описание

Объект операций с сервисом «Балансировщик нагрузки»

применяемость

VPS

путь к объекту

POST https://api.sweb.ru/balancer

требование к авторизации

да

список методов

*   index;
*   isCreateEnable;
*   getAvailableConfig;
*   create;
*   edit;
*   remove.

index
-----

метод

описание

Получение списка услуг «Балансировщик нагрузки»

возвращаемые значения в свойствах элементов массива

'billingId' string ID сервиса (Балансировщик нагрузки)

'name' string Название балансировщика

'type' string Тип алгоритма балансировщика (Значения: 'roundrobin' или 'leastconn')

'plan\_id' int ID плана

'plan\_name' string Название плана

'price' int Стоимость услуги

'active' bool Услуга активна

'removeAllowed' bool Разрешено или нет инициировать удаление услуги

'blockUi' bool Управление услугой заблокировано. Блокировка может быть из-за неуплаты, может быть из-за обработки изменений в настройках балансировщика, либо первого старта услуги

'currentAction' string|null Текущее действие, которое выполняется с услугой, значения (null не выполняется никакой операции, 'create' создание услуги, 'edit' изменение параметров услуги, 'remove' удаление услуги)

'tsCreate' string Дата и время создания услуги

'ipBalancer' string IP балансировщика

'datacenter' string Дата-центр, в котором находится IP балансировщика

'healthCheck' bool Проверка доступности серверов

'proxyProto' bool Перенаправлять или нет данные о подключении (IP-адрес и порт) на конечный сервер. Работает для всех правил, которые имеют целевой протокол HTTP или HTTPS

'keepalive' bool Поддерживать режим постоянного соединения для всех правил с целевым протоколом HTTP или HTTPS

'saveSession' bool Запоминать сессию или нет

'rules' array Правила переадресации, их может быть несколько. Каждое правило - массив параметров ('protocolBalancer' string Протокол начального узла, 'portBalancer' string Порт начального узла, 'protocolServer' float Протокол конечного узла, 'portServer' string Порт конечного узла)

'servers' array Серверы для балансировки. Не более 20 серверов. Каждый сервер - массив параметров ('ip' string IP адрес сервера, 'weight' int Приоритет, вес сервера для балансировки. Значения от 1 до 5. Параметр присутствует при 'type' = 'roundrobin', 'vpsName' string|null Название виртуального сервера)

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

"816969108687412.fHyQTrMYQN"

"result":{

"ips":\[

{

"billingId":

"dyasyuc578\_balancer\_1"

"name":

"Балансировщик 1"

"type":

"leastconn"

"plan\_id":

"4298"

"plan\_name":

"Стандартный"

"price":

375

"active":

true

"removeAllowed":

false

"blockUi":

false

"currentAction":

NULL

"tsCreate":

"2025-09-25 10:53:24"

"ipBalancer":

"192.168.122.66"

"datacenter":

1

"healthCheck":

false

"proxyProto":

false

"keepalive":

false

"saveSession":

false

"rules":\[

{

"protocolBalancer":

"https"

"portBalancer":

"443"

"protocolServer":

"https"

"portServer":

"443"

}
```

\]

"servers":\[

```json
{

"ip":

"1.1.1.1"

"vpsName":

NULL

}
```

\]

}

\]

}

}

isCreateEnable
--------------

метод

описание

Проверка доступен ли заказ услуги «Балансировщик нагрузки»

возвращаемое значение

1 - доступен или 0 - не доступен

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"isCreateEnable"

"params":{}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"757488281199525.aQcfVKrqtT"

"result":

1

}
```

getAvailableConfig
------------------

метод

описание

Получение списка услуг «Балансировщик нагрузки»

возвращаемые значения в свойствах элементов массива

'plans' array Тарифы ('id' string Id тарифа, 'tag' string Текстовый идентификатор, 'title' string Название, 'price' string Цена

'protocols' array Протоколы ('id' string id протокола, 'name' string Название, 'restrictions' array Доступные варианты \['HTTP', 'HTTPS'\])

'descriptions' array Описание ('service\_plan\_id': string Id тарифа, 'service\_id': string Id услуги, 'description': string Описание)

тип данных в ответе

array

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"getAvailableConfig"

"params":{}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"850380324369390.ihJrTIedfN"

"result":{

"plans":\[

{

"id":

"1815"

"tag":

"balancer\_1"

"title":

"Отказоустойчивый"

"price":

"750.0000"

}
```

```json
{

"id":

"4298"

"tag":

"balancer\_2"

"title":

"Стандартный"

"price":

"375.0000"

}
```

\]

"protocols":\[

```json
{

"id":

"1"

"name":

"HTTP"

"restrictions":\[

"HTTP"

"HTTPS"

\]

}
```

```json
{

"id":

"2"

"name":

"HTTP2"

"restrictions":\[

"HTTP"

"HTTP2"

\]

}
```

```json
{

"id":

"3"

"name":

"HTTPS"

"restrictions":\[

"HTTP"

"HTTPS"

\]

}
```

```json
{

"id":

"4"

"name":

"TCP"

"restrictions":\[

"TCP"

\]

}
```

\]

"descriptions":\[

```json
{

"service\_plan\_id":

"1815"

"service\_id":

"balancer\_1"

"description":

"Балансировщик автоматически переключается на резервный сервер при сбоях, обеспечивая непрерывную работу."

}
```

```json
{

"service\_plan\_id":

"4298"

"service\_id":

"balancer\_2"

"description":

"Балансировщик размещает правила на одном из двух серверов в выбранном дата-центре, но не имеет встроенной отказоустойчивости."

}
```

\]

}

}

create
------

метод

описание

Создание услуги «Балансировщик нагрузки»

возвращаемое значение

1 - успешно стартовала процедура создания балансировщика

параметры в запросе

datacenter

integer

id дата-центра

type

string

Тип алгоритма балансировки 'roundrobin' или 'leastconn'

servers

array

Серверы для балансировки

rules

array

Правила переадресации

planId

integer

ID плана

healthCheck

boolean

Проверка доступности серверов

proxyProto

boolean

Перенаправлять или нет данные о подключении (IP-адрес и порт) на конечный сервер

keepalive

boolean

Поддерживать режим постоянного соединения для всех правил с целевым протоколом HTTP или HTTPS

saveSession

boolean

Запоминать сессию или нет

alias

string

Название услуги

isFirstOrder

boolean

Первый заказ

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"create"

"params":{

"datacenter":

"1"

"type":

"leastconn"

"servers":

"ip: 1.1.1.1"

"rules":

"protocolBalancer"

"planId":

"4298"

"healthCheck":

"false"

"proxyProto":

"false"

"keepalive":

"false"

"saveSession":

"false"

"alias":

"Балансировщик 3"

"isFirstOrder":

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

"627757699261266.hOPGmoolCO"

"result":

1

}
```

edit
----

метод

описание

Редактирование услуги «Балансировщик нагрузки»

возвращаемое значение

1 - успешное выполнение операции

параметры в запросе

billingId

string

Идентификатор балансировщика

type

string

Тип алгоритма балансировки 'roundrobin' или 'leastconn'

servers

array

Серверы для балансировки

rules

array

Правила переадресации

healthCheck

boolean

Проверка доступности серверов

proxyProto

boolean

Перенаправлять или нет данные о подключении (IP-адрес и порт) на конечный сервер

keepalive

boolean

Поддерживать режим постоянного соединения для всех правил с целевым протоколом HTTP или HTTPS

saveSession

boolean

Запоминать сессию или нет

alias

string

Название услуги

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

"billingId":

"dyasyuc578\_balancer\_1"

"type":

"leastconn"

"servers":

"ip: 1.1.1.1"

"rules":

"protocolBalancer"

"healthCheck":

"false"

"proxyProto":

"false"

"keepalive":

"false"

"saveSession":

"false"

"alias":

"Балансировщик 3"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"783268505159950.fsFnULGBte"

"result":

1

}
```

remove
------

метод

описание

Удаление балансировщика

возвращаемое значение

1 - если операция прошла успешно, 0 - в случае не успешной операции

параметры в запросе

billingId

string

Идентификатор балансировщика

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"remove"

"params":{

"billingId":

"dyasyuc578\_balancer\_1"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"519547491824887.AQVxuuCrLP"

"result":

1

}
```