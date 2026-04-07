# VPS / Бэкапы

Бэкапы
======

объект

описание

Бэкапы для VPS

применяемость

VPS

путь к объекту

POST https://api.sweb.ruvps/backup

требование к авторизации

да

список методов

*   index;
*   updateIndex;
*   create;
*   restore;
*   attach;
*   detach;
*   remove;
*   getSettings;
*   saveSettings.

index
-----

метод

описание

Список бэкапов для VPS

возвращаемые значения в свойствах элементов массива

'name' string Имя бэкапа

'prettyName' string Понятное имя бэкапа

'unic\_id' string ID бэкапа

'attach\_btn' string Можно ли подключить

'restore\_btn' string Можно ли восстановить

'delete\_btn' string Можно ли удалить

'attach\_type' string Тип подключения

'updatedAt' string Дата создания

параметры в запросе

billingId

string

Идентификатор услуги

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

"billingId":

"lnpetrov93\_vps\_2"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"208416827268245.ypfViSJVAs"

"result":\[

{

"name":

"b67d4085c72cca7fa909e275b3fd6b52-2023-03-13-13-37"

"prettyName":

"13:37 13-03-2023"

"unic\_id":

"133713032023"

"attach\_btn":

"on"

"restore\_btn":

"on"

"delete\_btn":

"on"

"attach\_type":

"attach"

"updatedAt":

"2023-03-13 13:40:03"

}
```

\]

}

updateIndex
-----------

метод

описание

Обновление индекса бэкапов

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

billingId

string

Идентификатор услуги

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"updateIndex"

"params":{

"billingId":

"lnpetrov93\_vps\_2"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"654148542849931.ATNHIgAfBL"

"result":

1

}
```

create
------

метод

описание

Создание бэкапа VPS

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

billingId

string

Идентификатор услуги

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

"billingId":

"lnpetrov93\_vps\_2"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"978562935544556.nWpzsOpBib"

"result":

1

}
```

restore
-------

метод

описание

Восстановление из бэкапа

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

billingId

string

Идентификатор услуги

backupName

string

Название бэкапа

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"restore"

"params":{

"billingId":

"lnpetrov93\_vps\_2"

"backupName":

"b67d4085c72cca7fa909e275b3fd6b52-2023-03-13-13-37"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"936151563444713.JHirxilIXr"

"result":

1

}
```

attach
------

метод

описание

Подключение бэкапа как диска к VPS

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

billingId

string

Идентификатор услуги

backupName

string

Название бэкапа

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"attach"

"params":{

"billingId":

"lnpetrov93\_vps\_2"

"backupName":

"b67d4085c72cca7fa909e275b3fd6b52-2023-03-13-13-37"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"535031526387779.BRLlLcUGiM"

"result":

1

}
```

detach
------

метод

описание

Отключение бэкапа как диска

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

billingId

string

Идентификатор услуги

backupName

string

Название бэкапа

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"detach"

"params":{

"billingId":

"lnpetrov93\_vps\_2"

"backupName":

"b67d4085c72cca7fa909e275b3fd6b52-2023-03-13-13-37"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"354003953421055.MVXqCgqcTl"

"result":

1

}
```

remove
------

метод

описание

Удаление бэкапа

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

billingId

string

Идентификатор услуги

backupName

string

Название бэкапа

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

"lnpetrov93\_vps\_2"

"backupName":

"b67d4085c72cca7fa909e275b3fd6b52-2023-03-13-13-37"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"649013816836371.eEMBARWhos"

"result":

1

}
```

getSettings
-----------

метод

описание

Получение настроек создания бэкапов

возвращаемые значения в свойствах элементов массива

'mode' string Режим: 'manual' или 'auto'

'frequency' int|null Частота создания

'time' int|null Время создания

'next\_data\_backup' string Дата следующего бэкапа

параметры в запросе

billingId

string

Идентификатор услуги

тип данных в ответе

array

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"getSettings"

"params":{

"billingId":

"lnpetrov93\_vps\_2"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"692928995936803.edpLfZFDZl"

"result":\[

{

"mode":

"manual"

"frequency":

3

"time":

0

"next\_data\_backup":

""

}
```

\]

}

saveSettings
------------

метод

описание

Сохранение настроек бэкапа

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

billingId

string

Идентификатор услуги

mode

string

Режим: 'manual' или 'auto'

frequency

integer

Частота создания

time

integer

Время создания

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"saveSettings"

"params":{

"billingId":

"lnpetrov93\_vps\_2"

"mode":

"auto"

"frequency":

3

"time":

"16"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"021875439835396.xSUPCWeapD"

"result":

1

}
```