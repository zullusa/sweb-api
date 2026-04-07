# Виртуальный хостинг / Crontab

Crontab
=======

объект

описание

Планировщик заданий

применяемость

Виртуальный хостинг

путь к объекту

POST https://api.sweb.ruvh/cron

требование к авторизации

да

список методов

*   addTask;
*   editTask;
*   removeTask;
*   getTasks.

addTask
-------

метод

описание

Добавляет задание

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

minute

integer

Минута (диапазон от 0 до 59)

hour

integer

Час (диапазон от 0 до 23)

day

integer

День (диапазон от 1 до 31)

month

integer

Месяц (диапазон от 0 до 12)

weekday

integer

День недели (диапазон от 0 до 7, где воскресенье соответствует 0 или 7)

command

string

Команда для запуска

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"addTask"

"params":{

"minute":

"30"

"hour":

"12"

"day":

"1"

"month":

"12"

"weekday":

"7"

"command":

"test"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"293925508972027.kiIPcTEnVF"

"result":

1

}

editTask
--------

метод

описание

Изменяет задание в кроне

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

oldTask

integer

ID старого задания

minute

integer

Минута (диапазон от 0 до 59)

hour

integer

Час (диапазон от 0 до 23)

day

integer

День (диапазон от 1 до 31)

month

integer

Месяц (диапазон от 0 до 12)

weekday

integer

День недели (диапазон от 0 до 7, где воскресенье соответствует 0 или 7)

command

string

Команда для запуска

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"editTask"

"params":{

"oldTask":

"30 12 1 12 7 test"

"minute":

"30"

"hour":

"12"

"day":

"1"

"month":

"12"

"weekday":

"7"

"command":

"test"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"608723769708942.SQuSiDVGTz"

"result":

1

}

removeTask
----------

метод

описание

Удаляет задание из крона

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

task

integer

ID задания

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"removeTask"

"params":{

"task":

"30 0 31 1 1 test"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"745962996205252.unxaBoyIpa"

"result":

1

}

getTasks
--------

метод

описание

Возвращает список заданий в кроне

возвращаемые значения в свойствах элементов массива

'minute' int Минута (диапазон от 0 до 59),

'hour' int Час (диапазон от 0 до 23)

'day' int День (диапазон от 1 до 31)

'month' int Месяц (диапазон от 0 до 12)

'weekday' int День недели (Диапазон от 0 до 7, где воскресенье соответствует 0 или 7)

'command' string Команда для запуска

'task' int ID задания

'task\_escaped' string Значение 'task' только для корректного отображения спецсимволов

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getTasks"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"856392427559856.kStTYHEEcl"

"result":\[

{

"minute":

"30"

"hour":

"12"

"day":

"1"

"month":

"12"

"weekday":

"7"

"command":

"test"

"task":

"30 12 1 12 7 test"

"task\_escaped":

"30%2012%201%2012%207%20test"

}

\]

}