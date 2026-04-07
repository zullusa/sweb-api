# Виртуальный хостинг / Базы данных

Базы данных
===========

объект

описание

Управление базами данных хостинга

применяемость

Виртуальный хостинг

путь к объекту

POST https://api.sweb.ruvh/hosting

требование к авторизации

да

список методов

*   databaseGetList;
*   databaseMysqlChangePass;
*   databaseMysqlCreate;
*   databaseMysqlImport;
*   databaseMysqlMakeCopy;
*   databaseMysqlAccessList;
*   databaseMysqlAccessCreate;
*   databaseMysqlAccessDelete;
*   databaseMysqlDelete;
*   databasePgsqlCreate;
*   databasePgsqlDelete;
*   databasePgsqlChangePass;
*   databaseEditComment;
*   getPmaUser.

databaseGetList
---------------

метод

описание

Получение списка баз данных

возвращаемые значения в свойствах объекта

'params' array Параметры:

'server' string имя сервера (например, vh1.devel.sweb.ru)

'mysqlCount' int количество баз MySql на акк.

'mysqlMaxCount' int максимально разрешенное количество баз MySql

'mysqlCanCreate' int может ли этот пользователь создать ещё одну БД Mysql

'pgsqlCount' int количество баз PgSql на акк.

'pgsqlMaxCount' int максимально разрешенное количество баз PgSql

'pgsqlCanCreate' int может ли этот пользователь создать ещё одну БД Mysql

'redisAvailable' bool Доступен ли Redis для подключения (по тарифу, серверу, ...)

'redisNeedTransfer' bool True, если Redis можно подключить на другом сервере, т.е. нужен перенос (при этом redisAvailable будет false)

'redisEnabled' bool Подключен ли Redis

'redisCanEnable' bool Возможно ли подключение Redis (определяется по доступности (redisAvailable) и отсутствию текущих операций подключения/отключения)

'redisCanDisable' bool Возможно ли отключение Redis (определяется по доступности (redisAvailable) и отсутствию текущих операций подключения/отключения)

'redisSessionEnabled' bool Включено ли хранение сессий сайтов в Redis

'redisInfo' array Данные об использовании Redis: 'sites' array of string Cписок сайтов (docRoot), для которых включено хранение сессий в Redis 'size' int Размер оперативной памяти процесса Redis 'ip' string|null IP-адрес для подключения, сейчас он статичный - 127.0.0.79 (null вернется, если Redis не подключен) 'protocol' string|null Протокол для подключения, сейчас только TCP (null вернется, если Redis не подключен) 'port' int|null Порт для подключения, определяется uid пользователя на сервере (null вернется, если Redis не подключен)

'page' int текущая страница, на front-end нумерация с 1

'perPage' int количество строк на странице

'totalPages' int количество страниц, сколько займет пагинация

'totalCount' int количество строк всего

'sortingType' string тип сортировки

'directOrder' string направление сортировки (true - по возрастанию, false - по убыванию)\]

'list' array Список баз данных:

'type' string тип базы данных mysql/pgsql

'version' string версия mysql. Поле присутствует, если 'type'=mysql

'name' string название базы данных

'login' string логин базы данных

'countTables' int кол-во таблиц

'sizeTables' float размер в Мб

'charset' string кодировка

'comment' string комментарий

'pgAdminUrl' string url для входа в PgMyAdmin, зависитот версии Postgre. Поле присутствует, если 'type'= pgsql

параметры в запросе

page

integer

страница, начиная с 1

sortingType

string

тип сортировки (по какому параметру)

directOrder

boolean

направление сортировки

filter

string

фильтр для списка по доменам

тип данных в ответе

object

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"databaseGetList"

"params":{

"page":

1

"sortingType":

"default"

"directOrder":

true

"filter":

"inn"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"329015428550951.DrybgGyHXg"

"result":{

"params":{

"server":

"VH297"

"mysqlCount":

1

"mysqlMaxCount":

512

"mysqlCanCreate":

true

"pgsqlCount":

0

"pgsqlMaxCount":

512

"pgsqlCanCreate":

true

"redisAvailable":

true

"redisNeedTransfer":

false

"redisEnabled":

true

"redisCanEnable":

false

"redisCanDisable":

true

"redisSessionEnabled":

true

"redisInfo":{

"sites":\[

{

"docRoot":

"/тест"

"alias":

"Сайт 1"

"redisBackendAvailable":

true

"redisSessionSelected":

true

"redisSessionEnabled":

true

}
```

```json
{

"docRoot":

""

"alias":

"inn\*\*\*\*"

"redisBackendAvailable":

true

"redisSessionSelected":

true

"redisSessionEnabled":

true

}
```

\]

"size":

649496

"ip":

"127.0.0.79"

"protocol":

"TCP"

"port":

15121

}

"page":

1

"perPage":

20

"totalPages":

1

"totalCount":

1

"sortingType":

"default"

"directOrder":

true

}

"list":\[

```json
{

"type":

"mysql"

"version":

"5.7"

"name":

"in\*\*\*\*"

"login":

"in\*\*\*\*"

"countTables":

0

"sizeTables":

0.01

"charset":

""

"comment":

"тест"

}
```

\]

}

}

databaseMysqlChangePass
-----------------------

метод

описание

Изменение пароля к БД mysql

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

dbName

string

название БД

dbPassword

string

новый пароль для БД

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"databaseMysqlChangePass"

"params":{

"dbName":

"mydb"

"dbPassword":

"......"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"431257497251225.PWtHPgSATQ"

"result":

1

}
```

databaseMysqlCreate
-------------------

метод

описание

Создание БД MySQL

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

dbName

string

название БД

dbPassword

string

пароль для БД

dbComment

string

комментарий к БД

dbVersion

string

версия БД

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"databaseMysqlCreate"

"params":{

"dbName":

"mydb"

"dbPassword":

"......"

"dbComment":

"тестовая БД"

"dbVersion":

"8"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"466742467487524.vJTAAskXvn"

"result":

1

}
```

databaseMysqlImport
-------------------

метод

описание

Импорт базы данных MySql из файла

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

dbName

string

название уже имеющейся на акк. БД mysql

filePatch

string

путь к файлу в папке пользователя

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"databaseMysqlImport"

"params":{

"dbName":

"mydb"

"filePatch":

"/mydb\_mysql\_2019-09-11\_backup.sql.gz"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"592737992128729.TSreAsTVrw"

"result":

1

}
```

databaseMysqlMakeCopy
---------------------

метод

описание

Создает задание в очереди на создание архива базы данных MySql

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

dbName

string

полное название БД

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"databaseMysqlMakeCopy"

"params":{

"dbName":

"mydb"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"124798915494315.yfqeNnuNqT"

"result":

1

}
```

databaseMysqlAccessList
-----------------------

метод

описание

Вывод списка правил удаленного доступа к БД MySql

возвращаемые значения в свойствах объекта

'params' array параметры удаленного доступа:

'server' string имя сервера

'canCreate' bool можно ли создать ещё одно правило. Если максимальное количество записей об удаленном доступе к БД MySql не превышено, то можно.

'list' array массив значений string прав доступа к БД:

'localhost', IP-адрес или подсеть

параметры в запросе

dbName

string

полное название БД mysql

тип данных в ответе

object

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"databaseMysqlAccessList"

"params":{

"dbName":

"mydb"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"548369127163219.pvluupYoqr"

"result":{

"params":{

"server":

"VH297"

"canCreate":

true

}
```

"list":\[

"localhost"

\]

}

}

databaseMysqlAccessCreate
-------------------------

метод

описание

Добавление нового правила удаленного доступа к БД MySql

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

dbName

string

полное название БД

rule

string

правило удаленного доступа к БД MySQL

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"databaseMysqlAccessCreate"

"params":{

"dbName":

"mydb"

"rule":

"127.0.0.2"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"914302587762172.iZdottCcAR"

"result":

1

}
```

databaseMysqlAccessDelete
-------------------------

метод

описание

Удаление правила удаленного доступа к БД MySql

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

dbName

string

полное название БД

rule

string

правило удаленного доступа к БД MySQL

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"databaseMysqlAccessDelete"

"params":{

"dbName":

"mydb"

"rule":

"127.0.0.2"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"005491828358275.EHuEPRniEW"

"result":

1

}
```

databaseMysqlDelete
-------------------

метод

описание

Удаление БД MySQL

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

dbName

string

название БД

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"databaseMysqlDelete"

"params":{

"dbName":

"mydb"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"060697460600608.fgcHXcXNpj"

"result":

1

}
```

databasePgsqlCreate
-------------------

метод

описание

Создание БД PostgreSQL

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

dbName

string

название БД

dbPassword

string

пароль для БД

dbCharset

string

вид кодировки

dbComment

string

комментарий к БД

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"databasePgsqlCreate"

"params":{

"dbName":

"mydb"

"dbPassword":

"......"

"dbCharset":

"unicode"

"dbComment":

"тестовая БД"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"097581110935654.zzNhPwHnYm"

"result":

1

}
```

databasePgsqlDelete
-------------------

метод

описание

Удаление базы данных Pgsql

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

dbName

string

название БД

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"databasePgsqlDelete"

"params":{

"dbName":

"mydb"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"433011593333389.HVejMIpUPe"

"result":

1

}
```

databasePgsqlChangePass
-----------------------

метод

описание

Изменение пароля к БД PostgreSQL

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

dbName

string

название БД

dbPassword

string

новый пароль для БД

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"databasePgsqlChangePass"

"params":{

"dbName":

"mydb"

"dbPassword":

"......"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"054602243557832.fQezBWNYun"

"result":

1

}
```

databaseEditComment
-------------------

метод

описание

Добавление/редактирование комментария в БД. Если его не было, то запись создается

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

dbType

string

тип БД (mysql или pgsql)

dbName

string

полное название БД

dbComment

string

комментарий, который необходимо сохранить

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"databaseEditComment"

"params":{

"dbType":

"pgsql"

"dbName":

"mydb"

"dbComment":

"тестовая БД"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"266792683677172.QCOLTvfdEg"

"result":

1

}
```

getPmaUser
----------

метод

описание

Создание временного пользователя

возвращаемые значения в свойствах объекта

'url' string Ссылка для входа в PhpMyAdmin

'db' string База данных

'user' string Пользователь

'pass' string Пароль

параметры в запросе

dbName

string

название базы данных

тип данных в ответе

object

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"getPmaUser"

"params":{

"dbName":

"mydb"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"609869211268443.emZhlyWHKs"

"result":{

"url":

"qlnpd02knh8ogot21u5iie0gqj.75902b85-c966-4bd9-875c-8bfc06ff3377"

"db":

"mydb"

"user":

"\_pma\_3610018962"

"pass":

"....."

}
```

}