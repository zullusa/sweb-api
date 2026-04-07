# VPS / DBaaS

DBaaS
=====

объект

описание

Работа с управляемыми базами данных

применяемость

VPS

путь к объекту

POST https://api.sweb.ru/dbaas

требование к авторизации

да

список методов

*   index;
*   setUpgradeAgree;
*   getAvailableConfig;
*   getConstructorPlanId;
*   getFirstOrderInfo;
*   removeFirst;
*   createInstance;
*   editInstance;
*   removeInstance;
*   deleteDatabase;
*   validateUsers.

index
-----

метод

описание

Возвращает объект управления DBaaS с элементами

возвращаемые значения в свойствах объекта

'id' int ID кластера

'billing\_id' string Cтроковый ID услуги (имеет вид (<customer\_id>\_dbaas\_<number>), где <customer\_id> - логин пользователя, <number> - порядковый номер кластера у пользователя)

'price' float Цена за услугу

'plan' array Информация о тарифе:

'id' int ID тарифа

'name' string Название тарифа

'cpu' int Количество CPU

'memory' int Количество ГБ памяти

'storage' int Количество ГБ диска

'active' boolean Активна ли услуга

'ts\_will\_be\_deleted' string|null Дата удаления бета-кластера

'blockUi' boolean Блокировано ли управление в ПУ

'currentAction' string|null Текущее выполняемое действие над услугой

'instance\_uuid' string UUID кластера

'name' string Отображаемое имя кластера (пользовательское, а если его нет, то billing\_id)

'display\_name' string Пользовательское имя кластера

'status' string|null Статус кластера в MPU DBaaS

'engine' string Тип и версия СУБД

'instances' int Количество экземпляров кластера (т.е. 1 + количество реплик), возможные значения 1,2,3

'sync\_replicas' int Количество синхронных реплик (возможные значения 1,2)

'read\_replicas' int Количество асинхронных реплик (возможные значения 1,2)

'replicas' int Количество реплик (возможные значения 1,2)

'is\_enabled' boolean Включен ли кластер в MPU

'ip' string Данные для подключения (ip:port)

'endpoints' array Данные подключения к репликам, может быть один или два элемента (в зависимости от типа реплик):

'port' int Порт

'type' string Доступ для чтения и записи

'ip' string IP

'users' array Список пользователей кластера:

'name' string Имя пользователя

'databases' array Список баз данных:

'name' string Техническое имя базы данных

'size' int Размер базы данных

'users' array Пользователи базы данных:

'name' string Имя пользователя

'display\_name' string Отоброжаемое имя базы данных

'total\_count' string Общее количество кластеров на бете

'max\_count' int Максимальное количество кластеров на бете

'can\_create' boolean Возможность создания кластера

'upgrade\_agree' boolean Cогласен ли пользователь с кластером на бете на переход на платную версию (true|false, если пользователь выбрал; null - если не выбирал)

тип данных в ответе

object

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

"191661267269076.LkNjEMREkC"

"result":{

"instances":\[

{

"id":

380

"billing\_id":

"testuser\_dbaas\_1"

"price":

398

"plan":{

"id":

"2"

"name":

"DBAAS-1/1/10"

"cpu":

"1"

"memory":

"1"

"storage":

"10"

}
```

"active":

true

"ts\_will\_be\_deleted":

NULL

"blockUi":

false

"currentAction":

NULL

"instance\_uuid":

"c000000-1111-222d-ns13-44444444b31d"

"name":

"testuser\_dbaas\_1"

"display\_name":

""

"status":

"ready"

"engine":

"MySQL 5.7"

"instances":

1

"sync\_replicas":

0

"read\_replicas":

0

"is\_enabled":

true

"replicas":

0

"ip":

"11.222.44.55:66666"

"endpoints":\[

```json
{

"ip":

"11.222.44.55"

"port":

66666

"type":

"rw"

}
```

\]

"users":\[

```json
{

"name":

"test"

}
```

\]

"databases":\[

```json
{

"name":

"test"

"size":

0

"users":\[\]

"display\_name":

""

}
```

\]

}

\]

"can\_create":

true

"total\_count":

"8"

"max\_count":

110

"upgrade\_agree":

NULL

}

}

setUpgradeAgree
---------------

метод

описание

Сохранение выбора пользователя о переходе на платную версию

возвращаемое значение

1 - при успехе, 0 - при невозможности сохранить выбор

параметры в запросе

upgradeAgree

boolean

выбор пользователя, переходить (true) или не переходить (false) на платную версию

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"setUpgradeAgree"

"params":{

"upgradeAgree":

true

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"778425186842844.izDszGaxuD"

"result":

1

}
```

getAvailableConfig
------------------

метод

описание

Возвращает данные для отображения страницы создания кластера: доступные тарифы и версии баз данных

возвращаемые значения в свойствах объекта

'plans' array Тарифы:

'id' int ID тарифа

'name' string Название тарифа

'cpu' int Количество CPU

'memory' int Количество ГБ памяти

'storage' int Количество ГБ диска

'engines' array Версии баз данных

'kit' object Данные конфигуратора DBaaS

тип данных в ответе

object

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

"833672158469849.fkCtXVWlWE"

"result":{

"plans":\[

{

"id":

"1"

"name":

"Тестовый"

"cpu":

"2"

"memory":

"2"

"storage":

"40"

}
```

\]

"engines":```json
{

"PostgreSQL":\[

{

"name":

"PostgreSQL 13"

"version":

"13"

}
```

```json
{

"name":

"PostgreSQL 14"

"version":

"14"

}
```

```json
{

"name":

"PostgreSQL 15"

"version":

"15"

}
```

\]

"MySQL":\[

```json
{

"name":

"MySQL 5.7"

"version":

"5.7"

}
```

```json
{

"name":

"MySQL 8.0"

"version":

"8.0"

}
```

\]

}

"kit":```json
{

"cpu":{

"start":

1

"end":

8

"step":

1

"price":

NULL

"prices":\[

{

"start":

1

"end":

2

"price":

131

}
```

```json
{

"start":

3

"end":

6

"price":

164

}
```

```json
{

"start":

7

"end":

NULL

"price":

157

}
```

\]

}

"memory":```json
{

"start":

1

"end":

16

"step":

1

"values":\[\]

"price":

NULL

"prices":\[

{

"start":

1

"end":

1

"price":

28

}
```

```json
{

"start":

2

"end":

2

"price":

34

}
```

```json
{

"start":

3

"end":

10

"price":

35

}
```

```json
{

"start":

11

"end":

NULL

"price":

34

}
```

\]

}

"storage":```json
{

"start":

10

"end":

160

"step":

10

"values":\[

15

\]

"price":

NULL

"prices":\[

{

"start":

10

"end":

19

"price":

7.5

}
```

```json
{

"start":

20

"end":

29

"price":

15

}
```

```json
{

"start":

30

"end":

50

"price":

9.5

}
```

```json
{

"start":

51

"end":

139

"price":

8.5

}
```

```json
{

"start":

140

"end":

150

"price":

9

}
```

```json
{

"start":

151

"end":

NULL

"price":

13.5

}
```

\]

"price\_backup":

NULL

"prices\_backup":\[

```json
{

"start":

10

"end":

19

"price":

0.5

}
```

```json
{

"start":

20

"end":

50

"price":

0.6

}
```

```json
{

"start":

51

"end":

120

"price":

0.65

}
```

```json
{

"start":

121

"end":

NULL

"price":

0.6

}
```

\]

}

"categoryId":

"dbaas"

}

}

}

getConstructorPlanId
--------------------

метод

описание

Возвращает id тарифного плана конфигуратора DBaaS по значениям кол-ва ядер, ОЗУ, объема диска и количеству реплик

возвращаемое значение

id тарифа конфигуратора DBaaS

параметры в запросе

cpu

integer

количество ядер CPU

memory

integer

ОЗУ в Гб

storage

integer

жесткий диск в Гб

replicas

integer

количество реплик (по умолчанию 0, т.к. только master-экземпляр)

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"getConstructorPlanId"

"params":{

"cpu":

1

"memory":

2

"storage":

160

"replicas":

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

"656953388872637.LnULyVAdAq"

"result":

96

}
```

getFirstOrderInfo
-----------------

метод

описание

Получение информации о первом заказе

возвращаемые значения в свойствах объекта

'plan' string|null Название плана

'engine' string|null Полное название типа и версии СУБД

'engine\_type' string|null Название типа СУБД - 'PostgreSQL' или 'MySQL'

'engine\_version' string|null Версия СУБД

'cpu' int Кол-во ядер CPU

'memory' int|null Количество памяти (ОЗУ) в Гб

'storage' int|null Размер жесткого диска в Гб

'sync\_replicas' int|null Количество синхронных реплик

'read\_replicas' int|null Количество асинхронных реплик

'replicas' int|null Общее количество реплик (= sync\_replicas + read\_replicas)

'instances' int|null Общее количество кластеров (= replicas + 1 (master))

'price\_per\_month' int|null Цена за месяц

'pay\_period' int|null Цена за период

'plan\_is\_constructor' boolean|null Флаг сконструированного тарифа

'clearAvailable' boolean|null Доступна возможность очистки первого заказа

'promocode' string|null Промо-код на скидку (не партнерский) введенный при регистрации

тип данных в ответе

object

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"getFirstOrderInfo"

"params":{}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"054376601657988.dtBtCiMvTs"

"result":{

"plan":

"DBAAS-1/1/10"

"engine":

"PostgreSQL 13"

"engine\_type":

"PostgreSQL"

"engine\_version":

"13"

"cpu":

"1"

"memory":

"1"

"storage":

"10"

"sync\_replicas":

"0"

"read\_replicas":

"0"

"replicas":

0

"instances":

1

"price\_per\_month":

398

"pay\_period":

1

"plan\_is\_constructor":

true

"clearAvailable":

true

"promocode":

NULL

}
```

}

removeFirst
-----------

метод

описание

Удаление первого заказа: доступно, если заказ ещё не был оплачен и услуга не стартовала

возвращаемое значение

1 - если операция прошла успешно, ошибка 'Доступ запрещен' - при отсутствии первого заказа

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"removeFirst"

"params":{}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"909318873869891.HDloSaVbFA"

"result":

1

}
```

createInstance
--------------

метод

описание

Создание кластера (инициирует создание кластера)

возвращаемые значения в свойствах объекта

объект Success ('Создание кластера баз данных запущено'), т.е. отображение сообщения

параметры в запросе

engineType

string

тип СУБД ('PostgreSQL', 'MySQL')

engineVersion

string

версия СУБД (PostgreSQL: '12', '13', '14', '15', '16'; MySQL: '5.7', '8.0')

users

array

массив пользователей: \[\['name': 'логин', 'password': 'пароль'\]\]

planId

integer

id тарифа DBaaS

displayName

string

отображаемое имя кластера

instanceOptions

array

массив настроек кластера (по умолчанию пустой массив \[\], который воспринимается как \['sync\_replicas': 0, 'read\_replicas': 0, 'is\_enabled': true\])

dbDisplayName

string

отображаемое имя первой базы данных (по умолчанию пустая строка)

dbOptions

array

массив настроек БД, сейчас можно указать список пользователей (поле 'users') для первой БД (по умолчанию: \['users': \[\]\]

databases

array

массив с данными дополнительных БД (по умолчанию пустой массив \[\]), можно указать следующие поля: name - имя БД, display\_name - отображаемое имя БД (аналогично параметру $dbDisplayName), users - список пользователей (аналогично параметру $dbOptions 'users')

тип данных в ответе

object

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"createInstance"

"params":{

"engineType":

"PostgreSQL"

"engineVersion":

"13"

"users":\[

{

"name":

"test1"

"password":

"Pass\_ByTest1"

}
```

\]

"planId":

3

"displayName":

"Тестовая управляемая база данных"

"instanceOptions":```json
{

"sync\_replicas":

1

"read\_replicas":

0

}
```

"dbDisplayName":

"тестовая база данных"

"dbOptions":```json
{

"users":\[

"test1"

\]

}
```

"databases":\[

```json
{

"name":

"testDB"

"users":\[

"test1"

\]

"display\_name":

"тест"

"recreate":

false

}
```

\]

}

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"966245419985561.zttzrVTYbP"

"result":{

"extendedResult":{

"code":

1

"message":

"Создание кластера баз данных запущено"

"data":\[\]

}
```

}

}

editInstance
------------

метод

описание

Редактирование кластера

возвращаемое значение

1 - при успехе, 0 - при неуспешном сохранении изменений

параметры в запросе

billingId

string

строка-идентификатор услуги

users

array

массив пользователей вида \[\['name': 'username1', 'password': 'password1'\],\['name': 'username2'\],...\] — при наличии поля password пользователь будет создан; — при отсутствии поля password существующий пользователь не будет удален; — отсутствующие в массиве пользователи, которые существуют в кластере, будут удалены

planId

integer

ID тарифа DBaaS (по умолчанию null)

displayName

string

отображаемое имя кластера (по умолчанию null)

instanceOptions

array

массив настроек кластера, доступны поля 'sync\_replicas' (количество синх. реплик) и 'read\_replicas' (количество асинх. реплик)

databases

array

список баз данных (по умолчанию null, базы не редактируются), можно указать следующие поля: name — имя БД, display\_name — отображаемое имя БД, users — список пользователей, owner — владелец базы из списка пользователей (только для Postgres), recreate — флаг удалить и создать заново)

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"editInstance"

"params":{

"billingId":

"testuser\_dbaas\_1"

"users":\[

{

"name":

"test1"

"password":

"Pass\_ByTest1"

}
```

\]

"planId":

3

"displayName":

"Тестовая управляемая база данных измененная"

"instanceOptions":```json
{

"sync\_replicas":

1

"read\_replicas":

0

}
```

"databases":\[

```json
{

"name":

"testDB"

"users":\[

"test1"

\]

"display\_name":

"тест"

"recreate":

false

}
```

\]

}

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"926244734567613.pluqIClTzN"

"result":

1

}
```

removeInstance
--------------

метод

описание

Удаление кластера

возвращаемое значение

1 - если операция прошла успешно

параметры в запросе

billingId

string

строка-идентификатор услуги

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"removeInstance"

"params":{

"billingId":

"testuser\_dbaas\_1"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"761395249170028.ZVihswBiuH"

"result":

1

}
```

deleteDatabase
--------------

метод

описание

Удаление отдельной базы данных из кластера

возвращаемые значения в свойствах объекта

объект Success ('База данных удалена'), т.е. отображение сообщения

параметры в запросе

billingId

string

строка-идентификатор услуги

dbName

string

техническое имя базы данных

тип данных в ответе

object

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"deleteDatabase"

"params":{

"billingId":

"testuser\_dbaas\_1"

"dbName":

"test1"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"041837601799476.mEaCAXxWQv"

"result":{

"extendedResult":{

"code":

1

"message":

"База данных удалена"

"data":\[\]

}
```

}

}

validateUsers
-------------

метод

описание

Проверяет список пользователей кластера БД

возвращаемое значение

если в списке пользователей ошибка, отображает ошибку, если нет - true

параметры в запросе

users

array

массив пользователей: \[\['name': 'логин', 'password': 'пароль'\]\]

тип данных в ответе

boolean

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"validateUsers"

"params":{

"users":\[

{

"name":

"test1"

"password":

"Pass\_ByTest1"

}
```

\]

}

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"934138840589012.uzMTKmpzcb"

"result":

true

}
```