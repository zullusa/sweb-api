# Виртуальный хостинг / Квота

Квота
=====

объект

описание

Использование дискового пространства

применяемость

Виртуальный хостинг

путь к объекту

POST https://api.sweb.ruvh/utils/diskUsage

требование к авторизации

да

список методов

*   index;
*   getTasksInfo;
*   startTask;
*   getEmail;
*   changeEmail.

index
-----

метод

описание

Возвращаем информацию по используемому месту

возвращаемые значения в свойствах элементов массива

'tariffQuota' float Квора по тарифу Мб

'realQuota' float реальная квота Мб

'dbQuota' float базы Мб

'mailQuota' float почта Мб

'filesQuota' float файлы Мб

'filesNum' int кол-во файлов

тип данных в ответе

array

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

"769075036399155.aMWXjMwdvF"

"result":\[

{

"tariffQuota":

5000

"realQuota":

1

"dbQuota":

0

"mailQuota":

0

"filesQuota":

1

"filesNum":

36

}

\]

}

getTasksInfo
------------

метод

описание

Информация о задачах на подсчет занимаемого места

возвращаемые значения в свойствах объекта

'activeTasksCount' int Есть активные задачи сейчас

'lastDoneTaskDate' string Дата последнего обновления

тип данных в ответе

object

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getTasksInfo"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"376902100366009.noQYaPUYTU"

"result":{

"activeTasksCount":

"0"

"lastDoneTaskDate":

"2023-02-28 23:52:26"

}

}

startTask
---------

метод

описание

Создание задачи на подсчет данных

возвращаемое значение

1 - успешно, 0 - ошибка

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"startTask"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"874189314750787.ErxlnWUbyT"

"result":

1

}

getEmail
--------

метод

описание

Получение емейла для уведомлений о превышении занимаемого места

возвращаемое значение

емейл для уведомлений о превышении занимаемого места

тип данных в ответе

string

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getEmail"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"635751937958621.KbWVjUIzOs"

"result":

"test@gmail.com"

}

changeEmail
-----------

метод

описание

Смена емейла для уведомлений о занимаемом месте

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

email

string

новый емейл

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"changeEmail"

"params":{

"email":

"newtestemail@gmail.com"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"866198150044086.pZjYIGCZok"

"result":

1

}