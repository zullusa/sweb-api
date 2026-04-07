# Виртуальный хостинг / Почта

Mail
====

объект

описание

Объект для работы с почтовыми ящиками

применяемость

Виртуальный хостинг

путь к объекту

POST https://api.sweb.ruvh/mail

требование к авторизации

да

список методов

*   getDomainsList;
*   getMailboxesList;
*   getMailQuota;
*   createMbox;
*   sendRequisitesToEmail;
*   dropMbox;
*   updateAntispamState;
*   updateComment;
*   getAutoreply;
*   changeAutoreply;
*   changeMailboxSpf;
*   changeDomainSpf;
*   getForwardingEmailsList;
*   addForwardingEmail;
*   removeForwardingEmail;
*   isEnabledDeletingAfterForwarding;
*   changeDeletingAfterForwarding;
*   getDeliveryAddressesList;
*   getDeliveryInfo;
*   addDeliveryAddress;
*   dropDeliveryAddress;
*   getMailsCollector;
*   changeMailsCollector;
*   removeMailsCollector;
*   confirmMailsCollectorEmail;
*   changeSenderVerify;
*   changeAutoDiscover;
*   deleteMails;
*   changeMailboxPassword;
*   getWhitelist;
*   getBlacklist;
*   addToWhitelist;
*   addToBlacklist;
*   dropFromWhitelist;
*   dropFromBlacklist;
*   enableDkim;
*   disableDkim.

getDomainsList
--------------

метод

описание

Получение списка доменов клиента с почтовыми ящиками

возвращаемые значения в свойствах объекта

'list' array список доменов:

'fqdn\_readable' string домен

'mailboxesCnt' int кол-во ящиков

'spf' int SPF фильтрация (1 - включена, 0 - выключена)

'quota' int размер, MB

'senderVerify' int проверка существования адреса отправителя (1 - включена, 0 - выключена)

'autoDiscover' int автонастройка почтовых программ (1 - включена, 0 - выключена)

'emailCollector' string|null email сборщик писем

'dkim' string добавление цифровой подписи при отправке писем (on - включено, off - выключено)

'filterInfo' array информация о странице:

'page' int текущая страница

'limit' int кол-во не странице

'orderField' int поле сортировки

'orderDirect' string тип сортировки ('asc', 'desc')

'totalCount' int общее кол-во

параметры в запросе

page

integer

номер страницы

limit

integer

кол-во записей на странице

orderBy

integer

номер поля для сортировки

orderDirect

string

'asc' или 'desc'

тип данных в ответе

object

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getDomainsList"

"params":{

"page":

1

"searchMbox":

20

"orderBy":

0

"orderDirect":

"asc"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"280800839725764.MzzfUtlXRK"

"result":{

"list":\[

{

"fqdn\_readable":

"test.ru"

"mailboxesCnt":

4

"spf":

0

"quota":

0

"senderVerify":

0

"autoDiscover":

0

"emailCollector":

NULL

"dkim":

"on"

}

\]

"filterInfo":{

"page":

1

"limit":

20

"orderField":

0

"orderDirect":

"asc"

"totalCount":

1

}

}

}

getMailboxesList
----------------

метод

описание

Получение списка ящиков для домена

возвращаемые значения в свойствах объекта

'list' array список доменов:

'mbox' string название

'spf' int SPF фильтрация (1 - включена, 0 - выключена)

'quota' int размер, MB

'purpose' string назначение

'antispam' int настройка антиспам-фильтра (5 - жесткий, 8 - средний, 10 - мягкий, 0 - выключен)

'comment' string комментарий

'filterInfo' array информация о странице:

'page' int текущая страница

'limit' int кол-во не странице

'orderField' int поле сортировки

'orderDirect' string тип сортировки ('asc', 'desc')

'totalCount' int общее кол-во

параметры в запросе

domain

string

название домена

page

integer

номер страницы

limit

integer

кол-во записей на странице

orderBy

integer

номер поля для сортировки

orderDirect

string

'asc' или 'desc'

searchMbox

string

название ящика (для поиска по нему)

тип данных в ответе

object

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getMailboxesList"

"params":{

"domain":

"test.ru"

"page":

1

"searchMbox":

20

"orderBy":

0

"orderDirect":

"asc"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"915119587839201.zPZlOkyVMc"

"result":{

"list":\[

{

"mbox":

"test"

"quota":

0

"purpose":

"mail"

"spf":

1

"antispam":

10

"comment":

"тест"

}

{

"mbox":

"test1"

"quota":

0

"purpose":

"mail"

"spf":

1

"antispam":

0

"comment":

""

}

{

"mbox":

"test2"

"quota":

0

"purpose":

"mail"

"spf":

1

"antispam":

5

"comment":

""

}

\]

"filterInfo":{

"page":

1

"limit":

20

"orderField":

0

"orderDirect":

"asc"

"totalCount":

3

}

}

}

getMailQuota
------------

метод

описание

Возвращает общий размер (мб) почтовых ящиков клиента

возвращаемое значение

общий размер (мб) почтовых ящиков клиента

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getMailQuota"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"778583617391006.diOauMHUDz"

"result":

1

}

createMbox
----------

метод

описание

Создание почтового ящика

возвращаемые значения в свойствах объекта

'login' string почтовый ящик пример: example@test.ru

'password' string пароль

'webMail' string адрес веб-интерфейса для доступа к ящику

'mailProgramSettings' array настройка почтовых программ:

'name' string название сервера

'server' string адрес сервера

'port' string порт

'detailed' string адрес на страницу подробнее

'pdf' file pdf реквизиты

параметры в запросе

domain

string

название домена

mbox

string

название

password

string

пароль

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

"createMbox"

"params":{

"domain":

"test.ru"

"mbox":

"testmbox"

"password":

"Тест123!"

"comment":

"тест"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"252675911067503.HhTHZpKvFz"

"result":{

"login":

"testmbox@test.ru"

"password":

"Тест123!"

"webMail":

"https://webmail.sweb.ru"

"mailProgramSettings":\[

{

"name":

"IMAP"

"server":

"imap.spaceweb.ru"

"port":

"Порт 143 (Для SSL 993)"

}

{

"name":

"POP3"

"server":

"pop3.spaceweb.ru"

"port":

"Порт 110 (Для SSL 995)"

}

{

"name":

"SMTP"

"server":

"smtp.spaceweb.ru"

"port":

"Порт 25 или 2525 (Для SSL 465)"

}

\]

"detailed":

"https://help.sweb.ru/29/"

"pdf":{

"mimetype":

"application/pdf;base64"

"metadata":\[\]

"content":

"JVBERi0xLjQKJeLjz9MKMyAwIG9iago8PC9UeXBlIC9QYWdlCi9QYXJlbnQgMSAwI..."

"name":

"requisites.pdf"

}

}

}

sendRequisitesToEmail
---------------------

метод

описание

Отправка реквизитов созданного почтового ящика на почту

возвращаемое значение

1 - успешная отправка

параметры в запросе

email

string

email на который отправляются реквизиты

login

string

email реквизиты которого передаются на почту

password

string

пароль от ящика

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"sendRequisitesToEmail"

"params":{

"email":

"test@gmail.com"

"login":

"testmbox@test.ru"

"password":

"Тест123!"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"557025259335977.CWPmvbliXq"

"result":

1

}

dropMbox
--------

метод

описание

Удаление почтового ящика

возвращаемое значение

1 - успешное удаление

параметры в запросе

domain

string

название домена

mbox

string

название

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"dropMbox"

"params":{

"domain":

"test.ru"

"mbox":

"testmbox"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"649766456659468.dcBnHIwMMs"

"result":

1

}

updateAntispamState
-------------------

метод

описание

Изменяет состояние антиспам фильтра

возвращаемое значение

1 - успешно

параметры в запросе

domain

string

название домена

mbox

string

название

value

integer

состояние антиспам-фильтра (5 - жесткий, 8 - средний, 10 - мягкий, 0 - выключен)

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"updateAntispamState"

"params":{

"domain":

"test.ru"

"mbox":

"testmbox"

"value":

5

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"246228036001378.KjJXWLJpLc"

"result":

1

}

updateComment
-------------

метод

описание

Обновляет комментарий ящика

возвращаемое значение

1 - успешно

параметры в запросе

domain

string

название домена

mbox

string

название

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

"updateComment"

"params":{

"domain":

"test.ru"

"mbox":

"testmbox"

"comment":

"тест"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"859706075556154.dAHHEhMCPA"

"result":

1

}

getAutoreply
------------

метод

описание

Возвращает текст автоответчика

возвращаемое значение

текст автоответчика (ответного письма)

параметры в запросе

domain

string

название домена

mbox

string

название

тип данных в ответе

string

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getAutoreply"

"params":{

"domain":

"test.ru"

"mbox":

"testmbox"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"516616621691694.mqVaxYKseu"

"result":

"тест"

}

changeAutoreply
---------------

метод

описание

Изменяет текст автоответчика

возвращаемое значение

1 - успешно

параметры в запросе

domain

string

название домена

mbox

string

название

text

string

текст автоответчика

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"changeAutoreply"

"params":{

"domain":

"test.ru"

"mbox":

"testmbox"

"text":

"текст автоответчика"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"619583445386435.vhOkUMkZoN"

"result":

1

}

changeMailboxSpf
----------------

метод

описание

Вкл/выкл spf ящика

возвращаемое значение

1 - успешно

параметры в запросе

domain

string

название домена

mbox

string

название

turnOn

boolean

режим (true - включен, false - выключен)

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"changeMailboxSpf"

"params":{

"domain":

"test.ru"

"mbox":

"testmbox"

"turnOn":

true

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"918501915735914.sFkEQGOgtC"

"result":

1

}

changeDomainSpf
---------------

метод

описание

Вкл/выкл spf для всех почтовых ящиков домена

возвращаемое значение

1 - успешно

параметры в запросе

domain

string

название домена

turnOn

boolean

режим (true - включен, false - выключен)

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"changeDomainSpf"

"params":{

"domain":

"test.ru"

"turnOn":

true

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"085366305336602.ROrhZqTXvV"

"result":

1

}

getForwardingEmailsList
-----------------------

метод

описание

Возвращает список адресов для пересылки

возвращаемые значения в свойствах элементов массива

массив строк (адресов)

параметры в запросе

domain

string

название домена

mbox

string

название

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getForwardingEmailsList"

"params":{

"domain":

"test.ru"

"mbox":

"testmbox"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"316974623598815.dIINMSpRBJ"

"result":\[

"test1@test.ru"

\]

}

addForwardingEmail
------------------

метод

описание

Добавление адреса для пересылки

возвращаемое значение

1 - успешно

параметры в запросе

domain

string

название домена

mbox

string

название

email

string

email адрес

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"addForwardingEmail"

"params":{

"domain":

"test.ru"

"mbox":

"testmbox"

"email":

"test@gmail.com"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"240383992068707.zUrXAIolvi"

"result":

1

}

removeForwardingEmail
---------------------

метод

описание

Удаление адресов для пересылки

возвращаемое значение

1 - успешно

параметры в запросе

domain

string

название домена

mbox

string

название

email

string

email адрес

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"removeForwardingEmail"

"params":{

"domain":

"test.ru"

"mbox":

"testmbox"

"email":

"test@gmail.com"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"212418854378897.tYjwyIwbWu"

"result":

1

}

isEnabledDeletingAfterForwarding
--------------------------------

метод

описание

Проверяет, включено ли удаление писем из исходного ящика после пересылки

возвращаемое значение

1 - включено, 0 - выключено

параметры в запросе

domain

string

название домена

mbox

string

название

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"isEnabledDeletingAfterForwarding"

"params":{

"domain":

"test.ru"

"mbox":

"testmbox"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"395226707427380.XPbMeKaxnE"

"result":

0

}

changeDeletingAfterForwarding
-----------------------------

метод

описание

Вкл/выкл удаления из исходного ящика после пересылки

возвращаемое значение

1 - успешное вкл/выкл

параметры в запросе

domain

string

название домена

mbox

string

название

turnOn

boolean

режим (true - включен, false - выключен)

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"changeDeletingAfterForwarding"

"params":{

"domain":

"test.ru"

"mbox":

"testmbox"

"turnOn":

true

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"775350648940745.YykgqETAJi"

"result":

1

}

getDeliveryAddressesList
------------------------

метод

описание

Возвращает список адресов рассылки

возвращаемые значения в свойствах элементов массива

'list' array список адресов рассылки

'filterInfo' array информация о странице:

'page' int текущая страница

'limit' int кол-во не странице

'totalCount' int общее кол-во

параметры в запросе

domain

string

название домена

mbox

string

название

page

integer

страница

limit

integer

кол-во на странице

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getDeliveryAddressesList"

"params":{

"domain":

"test.ru"

"mbox":

"testmbox"

"page":

1

"searchMbox":

20

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"835063636574670.IAsCqKcaEm"

"result":{

"list":\[

"test1@test.ru"

\]

"filterInfo":{

"page":

1

"limit":

20

"totalCount":

"1"

}

}

}

getDeliveryInfo
---------------

метод

описание

Возвращает информацию о кол-ве списков и адресов рассылки

возвращаемые значения в свойствах объекта

'groups' array информация о списках:

'current' int текущее кол-во

'max' int максимальное кол-во

'addresses' array информация адресов рассылки

'current' int текущее кол-во

'max' int максимальное кол-во

параметры в запросе

domain

string

название домена

mbox

string

название

тип данных в ответе

object

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getDeliveryInfo"

"params":{

"domain":

"test.ru"

"mbox":

"testmbox"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"006869446031412.HuDuFTeDVm"

"result":{

"groups":{

"current":

0

"max":

10

}

"addresses":{

"current":

0

"max":

100

}

}

}

addDeliveryAddress
------------------

метод

описание

Добавить адрес рассылки

возвращаемое значение

1 - успешное добавление

параметры в запросе

domain

string

название домена

mbox

string

название

email

string

email адрес

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"addDeliveryAddress"

"params":{

"domain":

"test.ru"

"mbox":

"testmbox"

"email":

"test@gmail.com"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"951204504357775.jNgeyykNio"

"result":

1

}

dropDeliveryAddress
-------------------

метод

описание

Удалить адрес рассылки

возвращаемое значение

1 - успешное удаление

параметры в запросе

domain

string

название домена

mbox

string

название

email

string

email адрес

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"dropDeliveryAddress"

"params":{

"domain":

"test.ru"

"mbox":

"testmbox"

"email":

"test@gmail.com"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"047034444574222.FRfQBrzlnh"

"result":

1

}

getMailsCollector
-----------------

метод

описание

Возвращает адрес сборщика писем, если он добавлен

возвращаемое значение

email адрес сборщика писем

параметры в запросе

domain

string

название домена

тип данных в ответе

string

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getMailsCollector"

"params":{

"domain":

"test.ru"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"129169408468957.DearAOyIrD"

"result":

"test@gmail.com"

}

changeMailsCollector
--------------------

метод

описание

Изменяет адрес сборщика писем

возвращаемое значение

1 - успешно (домен на аккаунте); 2 - успешно (почта домена включается для адреса из домена, не пренадлежащего клиенту, требуется подтверждение)

параметры в запросе

domain

string

название домена

email

string

email адрес сборщика писем

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"changeMailsCollector"

"params":{

"domain":

"test.ru"

"email":

"test@gmail.com"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"405023605410677.NeHgnpAaiP"

"result":

1

}

removeMailsCollector
--------------------

метод

описание

Удаление адреса сборщика писем у домена

возвращаемое значение

1 - успешно

параметры в запросе

domain

string

название домена

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"removeMailsCollector"

"params":{

"domain":

"test.ru"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"742075556985587.bWLcvFMyeg"

"result":

1

}

confirmMailsCollectorEmail
--------------------------

метод

описание

Подтверждает ящик, который не находится на доменах аккаунта клиента

возвращаемое значение

1 - успешно, 0 - не успешно

параметры в запросе

domain

string

название домена

token

string

токен

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"confirmMailsCollectorEmail"

"params":{

"domain":

"test.ru"

"token":

"dhbvjwse97s8wh"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"237587320186914.kmEgsLrYbV"

"result":

1

}

changeSenderVerify
------------------

метод

описание

Вкл/выкл SenderVerify (проверку отправителя)

возвращаемое значение

1 - успешное изменение

параметры в запросе

domain

string

название домена

turnOn

boolean

вкл/выкл (true - включить, false - выключить)

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"changeSenderVerify"

"params":{

"domain":

"test.ru"

"turnOn":

true

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"451523942253650.wziWOCNRGO"

"result":

1

}

changeAutoDiscover
------------------

метод

описание

Вкл/выкл автонастройку почтовых программ

возвращаемое значение

1 - успешное изменение

параметры в запросе

domain

string

название домена

turnOn

boolean

вкл/выкл (true - включить, false - выключить)

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"changeAutoDiscover"

"params":{

"domain":

"test.ru"

"turnOn":

true

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"965619358096920.KRTSyhxbGz"

"result":

1

}

deleteMails
-----------

метод

описание

Удаляет письма ящика старше $days дней

возвращаемое значение

1 - успешное изменение

параметры в запросе

domain

string

название домена

mbox

string

название

days

integer

кол-во дней

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"deleteMails"

"params":{

"domain":

"test.ru"

"mbox":

"testmbox"

"days":

7

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"272968819845511.tosmUthFYw"

"result":

1

}

changeMailboxPassword
---------------------

метод

описание

Изменяет пароль почтового ящика

возвращаемое значение

1 - успешно

параметры в запросе

domain

string

название домена

mbox

string

название

password

string

пароль

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"changeMailboxPassword"

"params":{

"domain":

"test.ru"

"mbox":

"testmbox"

"password":

"Тест123!"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"366400398387936.dIfyhmelWA"

"result":

1

}

getWhitelist
------------

метод

описание

Возвращает белый список

возвращаемые значения в свойствах объекта

'list' array список адресов

'filterInfo' array информация о странице:

'page' int текущая страница

'limit' int кол-во не странице

'totalCount' int общее кол-во

параметры в запросе

domain

string

название домена

mbox

string

название

page

integer

номер страницы

limit

integer

кол-во на странице

тип данных в ответе

object

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getWhitelist"

"params":{

"domain":

"test.ru"

"mbox":

"testmbox"

"page":

1

"searchMbox":

20

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"342111403510807.oTzebAorhn"

"result":{

"list":\[

"test2@test.ru"

\]

"filterInfo":{

"page":

1

"limit":

20

"totalCount":

1

}

}

}

getBlacklist
------------

метод

описание

Возвращает черный список

возвращаемые значения в свойствах объекта

'list' array список адресов

'filterInfo' array информация о странице:

'page' int текущая страница

'limit' int кол-во не странице

'totalCount' int общее кол-во

параметры в запросе

domain

string

название домена

mbox

string

название

page

integer

номер страницы

limit

integer

кол-во на странице

тип данных в ответе

object

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getBlacklist"

"params":{

"domain":

"test.ru"

"mbox":

"testmbox"

"page":

1

"searchMbox":

20

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"186093064827112.hiUzMYeaLb"

"result":{

"list":\[

"test2@test.ru"

\]

"filterInfo":{

"page":

1

"limit":

20

"totalCount":

1

}

}

}

addToWhitelist
--------------

метод

описание

Добавляет исключение в белый список

возвращаемое значение

1 - успешно

параметры в запросе

domain

string

название домена

mbox

string

название

address

string

email адрес

all

boolean

применить ко всем ящикам домена

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"addToWhitelist"

"params":{

"domain":

"test.ru"

"mbox":

"testmbox"

"address":

"test@test.ru"

"all":

false

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"185900220038575.miSvfFaBlE"

"result":

1

}

addToBlacklist
--------------

метод

описание

Добавляет исключение в черный список

возвращаемое значение

1 - успешно

параметры в запросе

domain

string

название домена

mbox

string

название

email

string

email адрес

all

boolean

применить ко всем ящикам домена

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"addToBlacklist"

"params":{

"domain":

"test.ru"

"mbox":

"testmbox"

"email":

"test@gmail.com"

"all":

false

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"081713548269879.YWcPzPVrkR"

"result":

1

}

dropFromWhitelist
-----------------

метод

описание

Удаляет исключение из белого списка

возвращаемое значение

1 - успешно

параметры в запросе

domain

string

название домена

mbox

string

ящик клиента (часть адреса до @)

address

string

фильтруемый адрес

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"dropFromWhitelist"

"params":{

"domain":

"test.ru"

"mbox":

"testmbox"

"address":

"test@test.ru"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"307404139237882.GelRMdajsG"

"result":

1

}

dropFromBlacklist
-----------------

метод

описание

Удаляет исключение из черного списка

возвращаемое значение

1 - успешно

параметры в запросе

domain

string

название домена

mbox

string

ящик клиента (часть адреса до @)

email

string

фильтруемый адрес

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"dropFromBlacklist"

"params":{

"domain":

"test.ru"

"mbox":

"testmbox"

"email":

"test@gmail.com"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"516393820192679.NCgWGJyxvY"

"result":

1

}

enableDkim
----------

метод

описание

Включение DKIM

возвращаемое значение

1 - успешно

параметры в запросе

domain

string

название домена

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"enableDkim"

"params":{

"domain":

"test.ru"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"367719804161101.cUvXWAhHhF"

"result":

1

}

disableDkim
-----------

метод

описание

Выключение DKIM

возвращаемое значение

1 - успешно

параметры в запросе

domain

string

название домена

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"disableDkim"

"params":{

"domain":

"test.ru"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"694312937177583.PoGqqJfBqT"

"result":

1

}