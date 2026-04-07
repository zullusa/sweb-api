# VPS / Облачные бэкапы

RemoteBackup
============

объект

описание

Работа с облачными бэкапами VPS

применяемость

VPS

путь к объекту

POST https://api.sweb.ruvps/remoteBackup

требование к авторизации

да

список методов

*   index;
*   create;
*   editComment;
*   restore;
*   restoreInto;
*   remove.

index
-----

метод

описание

Получение данных по бэкапам

возвращаемые значения в свойствах объекта

'id' int ID

'billing\_id' string ID VPS

'disk\_size' int Размер диска VPS

'size' int Размер

'status' string Статус

'os\_distribution\_id' string ID дистрибутива VPS

'price' int Цена

'name' string Название

'comment' string Комментарий

'ts\_create' string Дата создания

'can\_perform\_actions' bool Флаг есть ли доступ на выполнения действий

'can\_delete' bool Флаг возможности удаления

'can\_restore\_self' bool Флаг самостоятельного восстановления

'is\_isp' bool Флаг, что на VPS установлен ispmanager

'process\_statuses' array:

'billing\_id' string Название VPS

'status' string Статус

тип данных в ответе

object

пример запроса

{

"jsonrpc":

"2.0"

"method":

"index"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"012665572939242.GAOtoJYaXy"

"result":{

"id":

123

"billing\_id":

NULL

"disk\_size":

10240

"size":

1706

"status":

"ready"

"os\_distribution\_id":

"122"

"price":

10

"name":

"backup\_test\_vps\_1"

"comment":

""

"ts\_create":

"2024-07-01 16:02:32"

"can\_perform\_actions":

true

"can\_delete":

true

"can\_restore\_self":

false

"process\_statuses":\[\]

"is\_isp":

false

}

}

create
------

метод

описание

Создание бэкапа VPS

возвращаемые значения в свойствах объекта

'code' int Код

'message' string Сообщение

'data' array Данные

параметры в запросе

billingId

string

ID VPS

name

string

название

comment

string

комментарий

тип данных в ответе

object

пример запроса

{

"jsonrpc":

"2.0"

"method":

"create"

"params":{

"billingId":

"test\_vps\_1"

"name":

"backup\_test\_vps\_1"

"comment":

"тестовый бэкап vps"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"424646885490739.VRCndbeqwq"

"result":{

"extendedResult":{

"code":

1

"message":

"Создание облачного бэкапа backup\_test\_vps\_1 запущено"

"data":\[\]

}

}

}

editComment
-----------

метод

описание

Редактирование комментария к бэкапу

возвращаемое значение

1 - при успехе, 0 - при неуспешном сохранении изменений

параметры в запросе

remoteBackupId

integer

ID бэкапа

comment

string

комментарий

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"editComment"

"params":{

"remoteBackupId":

1

"comment":

"тестовый бэкап vps"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"794092673621595.nQKdARZFeu"

"result":

1

}

restore
-------

метод

описание

Восстановление из бэкапа в ту VPS, из которой бэкап создан

возвращаемые значения в свойствах объекта

'code' int Код

'message' string Сообщение

'data' array Данные

параметры в запросе

remoteBackupId

integer

ID бэкапа

тип данных в ответе

object

пример запроса

{

"jsonrpc":

"2.0"

"method":

"restore"

"params":{

"remoteBackupId":

1

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"762683876745508.DsLFsxtyrF"

"result":{

"extendedResult":{

"code":

1

"message":

"Восстановление облачного бэкапа backup\_test\_vps\_1 на виртуальную машину test\_vps\_1 запущено"

"data":\[\]

}

}

}

restoreInto
-----------

метод

описание

Восстановление из бэкапа в существующую VPS

возвращаемые значения в свойствах объекта

'code' int Код

'message' string Сообщение

'data' array Данные

параметры в запросе

remoteBackupId

integer

ID бэкапа

billingId

string

ID VPS, в которую будет восстановление

тип данных в ответе

object

пример запроса

{

"jsonrpc":

"2.0"

"method":

"restoreInto"

"params":{

"remoteBackupId":

1

"billingId":

"test\_vps\_2"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"874767431460998.WWKddVKFly"

"result":{

"extendedResult":{

"code":

1

"message":

"Восстановление облачного бэкапа backup\_test\_vps\_1 на виртуальную машину test\_vps\_2 запущено"

"data":\[\]

}

}

}

remove
------

метод

описание

Удаление бэкапа

возвращаемые значения в свойствах объекта

'code' int Код

'message' string Сообщение

'data' array Данные

параметры в запросе

remoteBackupId

integer

ID бэкапа

тип данных в ответе

object

пример запроса

{

"jsonrpc":

"2.0"

"method":

"remove"

"params":{

"remoteBackupId":

1

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"088855187442109.xFknQmHoQr"

"result":{

"extendedResult":{

"code":

1

"message":

"Удаление облачного бэкапа backup\_test\_vps\_1 запущено"

"data":\[\]

}

}

}