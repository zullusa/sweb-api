# VPS / Мониторинг. Проверки

Monitoring
==========

объект

описание

Объект управления проверками сервиса Мониторинг

применяемость

VPS

путь к объекту

POST https://api.sweb.ru/monitoring/checks

требование к авторизации

да

список методов

*   index;
*   getTypes;
*   getIntervals;
*   getPorts;
*   getKeywordModes;
*   getInfo;
*   getFullCheckInfo;
*   create;
*   edit;
*   activate;
*   activateList;
*   deactivate;
*   deactivateList;
*   remove;
*   removeList;
*   history.

index
-----

метод

описание

Получение списка проверок

возвращаемые значения в свойствах объекта

'list' array список контактов со следующими свойствами:

'id' string ID проверки

'name' string Название проверки

'type' int Тип проверки (1 - Ping; 2 - Http; 3 - Port)

'status' boolean Cтатус проверки: true - активна; false - отключена

'disabled' boolean Блокировка: true - заблокирована; false - не заблокирована

'lastResult' boolean|null Результат последней проверки: null - проверки ещё не было; true - OK; false - проверка не прошла (неуспех)

'tsLastResult' string|null Разница времени между tsLastResult и текущим временем по МСК в формате 'ЧЧЧЧЧ:ММ:СС' кол.-во часов может быть любое, в зависимости от того, сколько суток разница

'tsDeltaResult' array список контактов со следующими свойствами:

'filterInfo' array массив информация для пагинации:

page - текущий номер страницы (начиная с 1) с данными в объекте list

perPage - текущее выбранное кол-во записей на одну страницу

otalCount - всего кол-во записей

параметры в запросе

page

integer

номер страницы. если задан, то используется пагинация

perPage

integer

кол-во единиц на странице, не больше 20

тип данных в ответе

object

пример запроса

{

"jsonrpc":

"2.0"

"method":

"index"

"params":{

"page":

1

"perPage":

2

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"219771940943748.iopQYLMibc"

"result":{

"list":\[

{

"id":

"339"

"name":

"sweb.ru"

"type":

"1"

"status":

true

"disabled":

false

"lastResult":

true

"tsLastResult":

NULL

"tsDeltaResult":

NULL

}

\]

"filterInfo":{

"page":

1

"perPage":

2

"totalCount":

1

}

}

}

getTypes
--------

метод

описание

Получение всех доступных типов проверок

возвращаемые значения в свойствах элементов массива

'id' string ID типа проверки

'code' string Алиас типа проверки (например, 'ping' или 'http' или 'port')

'name' string Название типа проверки (например, 'Ping')

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getTypes"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"906553281924430.JqUNuXGrQy"

"result":\[

{

"id":

"1"

"code":

"ping"

"name":

"Ping"

}

{

"id":

"2"

"code":

"http"

"name":

"HTTP"

}

{

"id":

"3"

"code":

"port"

"name":

"Порт"

}

\]

}

getIntervals
------------

метод

описание

Получение всех доступных интервалов проверок

возвращаемые значения в свойствах элементов массива

'id' string ID интервала проверки

'name' string Название интервала проверки

'time' string Длительность интервала проверки в минутах

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getIntervals"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"715943542422148.FBCaOBWwrM"

"result":\[

{

"id":

"1"

"name":

"1 мин"

"time":

"1"

}

{

"id":

"2"

"name":

"2 мин"

"time":

"2"

}

{

"id":

"3"

"name":

"5 мин"

"time":

"5"

}

{

"id":

"4"

"name":

"10 мин"

"time":

"10"

}

{

"id":

"5"

"name":

"15 мин"

"time":

"15"

}

{

"id":

"6"

"name":

"30 мин"

"time":

"30"

}

{

"id":

"7"

"name":

"1 час"

"time":

"60"

}

{

"id":

"8"

"name":

"2 часа"

"time":

"120"

}

{

"id":

"9"

"name":

"6 часов"

"time":

"360"

}

{

"id":

"10"

"name":

"12 часов"

"time":

"720"

}

{

"id":

"11"

"name":

"1 день"

"time":

"1440"

}

{

"id":

"12"

"name":

"7 дней"

"time":

"10080"

}

\]

}

getPorts
--------

метод

описание

Получение рекомендуемых портов для проверки

возвращаемые значения в свойствах элементов массива

'name' string Сокращенное название порта

'nameFull' string Полное название порта

'value' string Значение порта

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getPorts"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"809323424842563.pcnZePwLxN"

"result":\[

{

"name":

"FTP"

"nameFull":

"File Transfer Protocol"

"value":

"21"

}

{

"name":

"SSH"

"nameFull":

"Secure Shell"

"value":

"22"

}

{

"name":

"TELNET"

"nameFull":

"TELecommunication NETwork"

"value":

"23"

}

{

"name":

"SMTP"

"nameFull":

"Simple Mail Transfer Protocol"

"value":

"25"

}

{

"name":

"DNS"

"nameFull":

"Domain Name System"

"value":

"53"

}

{

"name":

"Finger"

"nameFull":

"Finger"

"value":

"79"

}

{

"name":

"WWW"

"nameFull":

"Web-сервер"

"value":

"80"

}

{

"name":

"POP3"

"nameFull":

"Post Office Protocol Version 3"

"value":

"110"

}

{

"name":

"Sun RPC"

"nameFull":

"Sun RPC"

"value":

"111"

}

{

"name":

"NNTP"

"nameFull":

"Network News Transfer Protocol"

"value":

"119"

}

{

"name":

"NetBIOS"

"nameFull":

"Network Basic Input/Output System"

"value":

"139"

}

{

"name":

"HTTPS"

"nameFull":

"Hypertext Transfer Protocol Secure"

"value":

"443"

}

{

"name":

"rLogin"

"nameFull":

"Remote LOGIN"

"value":

"513"

}

\]

}

getKeywordModes
---------------

метод

описание

Получение всех доступных режимов проверки ключевых слов

возвращаемые значения в свойствах элементов массива

'id' string ID режима

'name' string Название режима

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getKeywordModes"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"323187195084581.EtoQEJpUKB"

"result":\[

{

"id":

"1"

"name":

"на странице должны быть все слова"

}

{

"id":

"2"

"name":

"на странице должно быть хотя бы одно слово"

}

{

"id":

"3"

"name":

"на странице не должно быть всех слов"

}

{

"id":

"4"

"name":

"на странице не должно быть хотя бы одного слова"

}

\]

}

getInfo
-------

метод

описание

Общая информация для отображения настроек проверками

возвращаемые значения в свойствах объекта

'types' array Все доступные типы проверок (см. описание метода getTypes())

'intervals' array Доступные интервалы проверок (см. описание метода getIntervals())

'keywordModes' array Доступные режимы проверки ключевых слов (см. описание метода getKeywordModes())

'ports' array Список портов с названиями (см. описание метода getPorts())

'availableSms' int Кол-во оставшихся sms в периоде

'currentSms' int Кол-во отправленных sms в периоде

'totalSms' int Кол-во sms по тарифу в периоде

'availableChecks' int Кол-во доступных проверок по тарифу

'currentChecks' int Кол-во активных проверок

'totalChecks' int Кол-во проверок

'active' boolean Активна ли услуга

'expired' string|null Дата окончания услуги

'tariff' array|null Информация о тарифе

тип данных в ответе

object

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getInfo"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"404936988154220.rQPuQGhtSd"

"result":{

"types":\[

{

"id":

"1"

"code":

"ping"

"name":

"Ping "

}

{

"id":

"2"

"code":

"http"

"name":

"HTTP"

}

{

"id":

"3"

"code":

"port"

"name":

"Порт"

}

\]

"intervals":\[

{

"id":

"1"

"name":

"1 мин"

"time":

"1"

}

{

"id":

"2"

"name":

"2 мин"

"time":

"2"

}

{

"id":

"3"

"name":

"5 мин"

"time":

"5"

}

{

"id":

"4"

"name":

"10 мин"

"time":

"10"

}

{

"id":

"5"

"name":

"15 мин"

"time":

"15"

}

{

"id":

"6"

"name":

"30 мин"

"time":

"30"

}

{

"id":

"7"

"name":

"1 час"

"time":

"60"

}

{

"id":

"8"

"name":

"2 часа"

"time":

"120"

}

{

"id":

"9"

"name":

"6 часов"

"time":

"360"

}

{

"id":

"10"

"name":

"12 часов"

"time":

"720"

}

{

"id":

"11"

"name":

"1 день"

"time":

"1440"

}

{

"id":

"12"

"name":

"7 дней"

"time":

"10080"

}

\]

"keywordModes":\[

{

"id":

"1"

"name":

"на странице должны быть все слова"

}

{

"id":

"2"

"name":

"на странице должно быть хотя бы одно слово"

}

{

"id":

"3"

"name":

"на странице не должно быть всех слов"

}

{

"id":

"4"

"name":

"на странице не должно быть хотя бы одного слова"

}

\]

"ports":\[

{

"name":

"FTP"

"nameFull":

"File Transfer Protocol"

"value":

"21"

}

{

"name":

"SSH"

"nameFull":

"Secure Shell"

"value":

"22"

}

{

"name":

"TELNET"

"nameFull":

"TELecommunication NETwork"

"value":

"23"

}

{

"name":

"SMTP"

"nameFull":

"Simple Mail Transfer Protocol"

"value":

"25"

}

{

"name":

"DNS"

"nameFull":

"Domain Name System"

"value":

"53"

}

{

"name":

"Finger"

"nameFull":

"Finger"

"value":

"79"

}

{

"name":

"WWW"

"nameFull":

"Web-сервер"

"value":

"80"

}

{

"name":

"POP3"

"nameFull":

"Post Office Protocol Version 3"

"value":

"110"

}

{

"name":

"Sun RPC"

"nameFull":

"Sun RPC"

"value":

"111"

}

{

"name":

"NNTP"

"nameFull":

"Network News Transfer Protocol"

"value":

"119"

}

{

"name":

"NetBIOS"

"nameFull":

"Network Basic Input/Output System"

"value":

"139"

}

{

"name":

"HTTPS"

"nameFull":

"Hypertext Transfer Protocol Secure"

"value":

"443"

}

{

"name":

"rLogin"

"nameFull":

"Remote LOGIN"

"value":

"513"

}

\]

"availableSms":

6

"currentSms":

0

"totalSms":

6

"availableChecks":

0

"currentChecks":

1

"totalChecks":

1

"active":

true

"disabled":

false

"expired":

"29.10.2025"

"tariff":{

"id":

1

"name":

"Базовый"

"checks":

1

"sms":

6

}

}

}

getFullCheckInfo
----------------

метод

описание

Получение подробной информации о проверке

возвращаемые значения в свойствах объекта

'id' int ID проверки

'type' int ID типа проверки

'name' string Название проверки

'status' boolean Cтатус проверки: true - активна; false - отключена

'lastResult' boolean Результат последней проверки: null - проверки ещё не было; true - OK, false - проверка не прошла (неуспех)

'settings' array Массив настроек проверки:

'type' string Алиас типа настройки

'value' string Значение настройки

'contacts' array Массив контактов проверки(описание элементов см. в методе index API monitoring/contacts):

'id' int ID контакта

'type' string Алиас типа контакта

'name' string Имя контакта

'value' string Значение

'verified' boolean Подтвержден или нет контакт

Возможные значения settings\[\].type алиасов настроек:

'target' - цель проверки (URL или IP), есть у всех проверок

'interval' - интервал проверки (есть у всех проверок)

'keyword' - ключевое слово (может быть несколько ключевых слов)

'keyword\_mode' - режим проверки ключевых слов (один режим для всех ключевых слов)

'port' - порт (может быть только у типа проверки Порт)

'ssl' - использовать SSL (настройка либо отсутствует, что означает выключена, либо присутствует со значением 1)

параметры в запросе

id

integer

id проверки

тип данных в ответе

object

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getFullCheckInfo"

"params":{

"id":

1

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"805304617965136.pQQJYuphWA"

"result":{

"id":

1

"type":

1

"name":

"sweb.ru"

"status":

true

"lastResult":

true

"settings":\[

{

"type":

"target"

"value":

"192.168.122.75"

}

{

"type":

"interval"

"value":

"4"

}

\]

"contacts":\[

{

"id":

3205

"type":

"email"

"name":

"Малышева Инна Александровна"

"value":

"imalysheva@sweb.ru"

"verified":

true

}

\]

}

}

create
------

метод

описание

Создание проверки

возвращаемое значение

1 - успешное создание, 0 - не успешное создание

параметры в запросе

type

integer

id типа проверки (одно из возвращаемых методом getTypes)

target

string

значение цели проверки (URL или IP)

name

string

название проверки, не должно совпадать с другими

interval

integer

id интервала проверки (одно из возвращаемых методом getIntervals)

contactIds

array

массив id подтвержденных контактов для уведомлений

port

integer

порт (только для типа проверки id=3 'Порт')

ssl

boolean

использовать ssl (только для типа проверки id=3 'Порт')

keywords

array

массив ключевых слов (только для типа проверки id=2 'Http')

keywordMode

integer

режим проверки ключевых слов (только для типа проверки id=2 'Http')

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"create"

"params":{

"type":

1

"target":

"ip"

"name":

"тест"

"interval":

1

"contactIds":\[

1

2

\]

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"270687361480284.vHRqMurROY"

"result":

1

}

edit
----

метод

описание

Редактирование проверки

возвращаемое значение

1 - успешное редактирование, 0 - не успешное редактирование

параметры в запросе

id

integer

id редактируемой проверки

target

string

значение цели проверки (URL или IP)

name

string

название проверки, не должно совпадать с другими

interval

integer

id интервала проверки (одно из возвращаемых методом getIntervals)

contactIds

array

массив id подтвержденных контактов для уведомлений

port

integer

порт (только для типа проверки id=3 'Порт')

ssl

boolean

использовать ssl (только для типа проверки id=3 'Порт')

keywords

array

массив ключевых слов (только для типа проверки id=2 'Http')

keywordMode

integer

режим проверки ключевых слов (только для типа проверки id=2 'Http')

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"edit"

"params":{

"id":

1

"target":

"ip"

"name":

"тест"

"interval":

1

"contactIds":\[

1

2

\]

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"177373275454770.QHFsXpvZmg"

"result":

1

}

activate
--------

метод

описание

Включение одной проверки

возвращаемое значение

1 - проверка включена

параметры в запросе

id

integer

id проверки

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"activate"

"params":{

"id":

1

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"552838279031371.eWMRCmVMDe"

"result":

1

}

activateList
------------

метод

описание

Включение списка проверок

возвращаемое значение

1 - проверки включены

параметры в запросе

ids

array

id проверок

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"activateList"

"params":{

"ids":\[

1

2

\]

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"341389772049816.BvqOhNTKob"

"result":

1

}

deactivate
----------

метод

описание

Отключение одной проверки

возвращаемое значение

1 - проверка отключена

параметры в запросе

id

integer

id проверки

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"deactivate"

"params":{

"id":

1

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"177381240592919.YLwEPfuuqD"

"result":

1

}

deactivateList
--------------

метод

описание

Отключение списка проверок

возвращаемое значение

1 - проверки отключены

параметры в запросе

ids

array

id проверок

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"deactivateList"

"params":{

"ids":\[

1

2

\]

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"542419504230408.oQGsUQhUzb"

"result":

1

}

remove
------

метод

описание

Удаление проверки

возвращаемое значение

1 - проверка удалена

параметры в запросе

id

integer

id проверки

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"remove"

"params":{

"id":

1

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"603195037873229.oiuZqgVBMm"

"result":

1

}

removeList
----------

метод

описание

Удаление списка проверок

возвращаемое значение

1 - проверки удалены

параметры в запросе

ids

array

id проверок

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"removeList"

"params":{

"ids":\[

1

2

\]

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"808353151685743.eNMbSPKahy"

"result":

1

}

history
-------

метод

описание

История проверок

возвращаемые значения в свойствах объекта

'list' array Список событий:

id string - id события

check\_id string - id проверки

ts string дата события

success string y - успешно, n - не успешно

'filterInfo' array Массив информация для пагинации:

page - текущий номер страницы (начиная с 1) с данными в объекте list

perPage - текущее выбранное кол.-во записей на одну страницу

totalCount - всего кол-во записей

параметры в запросе

id

integer

id проверки

startDate

string

история с даты

finishDate

string

история по дату

page

integer

номер страницы. если задан, то используется пагинация

perPage

integer

кол-во единиц на странице, не больше 20

тип данных в ответе

object

пример запроса

{

"jsonrpc":

"2.0"

"method":

"history"

"params":{

"id":

1

"startDate":

"29-08-2025"

"finishDate":

"29-09-2025"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"086757776783687.WeKhstzRKG"

"result":{

"list":\[\]

"filterInfo":{

"page":

1

"perPage":

20

"totalCount":

0

}

}

}