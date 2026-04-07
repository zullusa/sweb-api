# VPS / Локальная сеть

Локальная сеть
==============

объект

описание

IP для VPS

применяемость

VPS

путь к объекту

POST https://api.sweb.ruvps/ip

требование к авторизации

да

список методов

*   addLocal;
*   removeLocal.

addLocal
--------

метод

описание

Подключение VPS к локальной сети

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

billingId

string

Идентификатор услуги

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

"test\_vps\_1"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"306576218991870.LnwzhPuRHo"

"result":

1

}

removeLocal
-----------

метод

описание

Удаление локального IP

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

billingId

string

Идентификатор услуги

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

"test\_vps\_1"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"156324199985191.yXOAfqbOvk"

"result":

1

}