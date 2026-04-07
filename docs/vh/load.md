# Виртуальный хостинг / Нагрузка

Нагрузка
========

объект

описание

Данные по нагрузке виртуального хостинга

применяемость

Виртуальный хостинг

путь к объекту

POST https://api.sweb.ruvh/load

требование к авторизации

да

список методов

*   index;
*   getLoadTable.

index
-----

метод

описание

Список доступных периодов статистики

возвращаемые значения в свойствах элементов массива

'year' string

'month' string

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

"186370438079080.BStXTAAmMB"

"result":\[

{

"year":

"2022"

"month":

"11"

}
```

```json
{

"year":

"2022"

"month":

"12"

}
```

```json
{

"year":

"2023"

"month":

"1"

}
```

```json
{

"year":

"2023"

"month":

"2"

}
```

```json
{

"year":

"2023"

"month":

"3"

}
```

\]

}

getLoadTable
------------

метод

описание

Получение данных в виде таблицы

возвращаемые значения в свойствах элементов массива

'list' string\[\]

'hostingLevels' int\[\]

'dbLevels' int\[\]

'csv' string\[\]

параметры в запросе

year

integer

Год

month

integer

Месяц

type

string

Тип (cpu, mysql)

тип данных в ответе

array

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"getLoadTable"

"params":{

"year":

"2023"

"month":

"3"

"type":

"null"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"272056517334535.hdCsOGKCrZ"

"result":\[

{

"list":\[

{

"date":

"2023-06-01"

"cpu":

"0.00"

"mysql":

0

}
```

```json
{

"date":

"2023-06-02"

"cpu":

"0.00"

"mysql":

0

}
```

```json
{

"date":

"2023-06-03"

"cpu":

"0.00"

"mysql":

0

}
```

```json
{

"date":

"2023-06-04"

"cpu":

"0.00"

"mysql":

0

}
```

```json
{

"date":

"2023-06-05"

"cpu":

"0.00"

"mysql":

0

}
```

```json
{

"date":

"2023-06-06"

"cpu":

"0.00"

"mysql":

0

}
```

```json
{

"date":

"2023-06-07"

"cpu":

"0.00"

"mysql":

0

}
```

```json
{

"date":

"2023-06-08"

"cpu":

"0.00"

"mysql":

0

}
```

```json
{

"date":

"2023-06-09"

"cpu":

"0.00"

"mysql":

0

}
```

```json
{

"date":

"2023-06-10"

"cpu":

"0.00"

"mysql":

0

}
```

```json
{

"date":

"2023-06-11"

"cpu":

"0.00"

"mysql":

0

}
```

```json
{

"date":

"2023-06-12"

"cpu":

"0.00"

"mysql":

0

}
```

```json
{

"date":

"2023-06-13"

"cpu":

"0.00"

"mysql":

0

}
```

```json
{

"date":

"2023-06-14"

"cpu":

"0.00"

"mysql":

0

}
```

```json
{

"date":

"2023-06-15"

"cpu":

"0.00"

"mysql":

0

}
```

```json
{

"date":

"2023-06-16"

"cpu":

"0.00"

"mysql":

0

}
```

```json
{

"date":

"2023-06-17"

"cpu":

"0.00"

"mysql":

0

}
```

```json
{

"date":

"2023-06-18"

"cpu":

"0.00"

"mysql":

0

}
```

```json
{

"date":

"2023-06-19"

"cpu":

"0.00"

"mysql":

0

}
```

```json
{

"date":

"2023-06-20"

"cpu":

"0.00"

"mysql":

0

}
```

```json
{

"date":

"2023-06-21"

"cpu":

"0.00"

"mysql":

0

}
```

```json
{

"date":

"2023-06-22"

"cpu":

"0.00"

"mysql":

0

}
```

```json
{

"date":

"2023-06-23"

"cpu":

"0.00"

"mysql":

0

}
```

```json
{

"date":

"2023-06-24"

"cpu":

"0.00"

"mysql":

0

}
```

```json
{

"date":

"2023-06-25"

"cpu":

"0.00"

"mysql":

0

}
```

```json
{

"date":

"2023-06-26"

"cpu":

"0.00"

"mysql":

0

}
```

```json
{

"date":

"2023-06-27"

"cpu":

"0.00"

"mysql":

0

}
```

\]

"hostingLevels":\[

120

260

500

1000

\]

"dbLevels":\[

2000

3000

6000

12000

\]

"csv":```json
{

"mimetype":

"application/csv;base64"

"metadata":\[\]

"content":

"MjAyMy0wNi0wMTswLjAwCjIwMjMtMDYtMDI7MC4wMAoyMDIzLTA2LTAzOzAuMDAKMjAyMy0wNi0wNDswLjAwCjIwMjMtMDYtMDU7MC4wMAoyMDIzLTA2LTA2OzAuMDAKMjAyMy0wNi0wNzswLjAwCjIwMjMtMDYtMDg7MC4wMAoyMDIzLTA2LTA5OzAuMDAKMjAyMy0wNi0xMDswLjAwCjIwMjMtMDYtMTE7MC4wMAoyMDIzLTA2LTEyOzAuMDAKMjAyMy0wNi0xMzswLjAwCjIwMjMtMDYtMTQ7MC4wMAoyMDIzLTA2LTE1OzAuMDAKMjAyMy0wNi0xNjswLjAwCjIwMjMtMDYtMTc7MC4wMAoyMDIzLTA2LTE4OzAuMDAKMjAyMy0wNi0xOTswLjAwCjIwMjMtMDYtMjA7MC4wMAoyMDIzLTA2LTIxOzAuMDAKMjAyMy0wNi0yMjswLjAwCjIwMjMtMDYtMjM7MC4wMAoyMDIzLTA2LTI0OzAuMDAKMjAyMy0wNi0yNTswLjAwCjIwMjMtMDYtMjY7MC4wMAoyMDIzLTA2LTI3OzAuMDAK"

"name":

"loading\_lina199302\_6.csv"

}
```

}

\]

}