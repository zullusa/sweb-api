# Оплата и финансы / Оплата и финансы

Pay
===

объект

описание

Оплата

применяемость

Оплата и финансы

путь к объекту

POST https://api.sweb.rupay

требование к авторизации

да

список методов

*   index;
*   isAutopaymentEnable;
*   getPayRecommendations;
*   getRecommendationTotalCost;
*   getUpcomingPaymentsVh;
*   changeDeferment;
*   getRemainsDate;
*   getRemainsDays;
*   getBalance;
*   getActiveReserves.

index
-----

метод

описание

Информация о балансе

возвращаемые значения в свойствах элементов массива

'real\_balance' float Реальные деньги

'bonus\_balance' float Бонусные деньги

'cloud\_balance' float Деньги на услуги cloud

'other\_balance' float Деньги на другие услуги

'cloud\_balance\_view' float Сумма для отображения для баланса cloud

'other\_balance\_vew' float Сумма для отображения для баланса на другие услуги

'credit\_balance' float Общий долг

'credit\_cloud\_balance' float Долг по услугам cloud

'credit\_other\_balance' float Долг услугам other

'type' int Тип биллинга

'multiple\_balance\_enabled' bool Режим нескольких балансов (true - включен)

'auto\_payment\_enable' int Подключен ли автоплатеж

'isAutopaymentEnable' int Доступны ли автоплатежи

'domainBonuses' int Количество доменных бонусов

'status' string Статус аккаунта

'blockInfo' string Причина блокировки аккаунта

'blockedMoney' float Заблокированные деньги

'deferment' ('show' показывать отсрочку, 'value' дней отсрочки)

'edgeDate' string Дата с которой доступны документы

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

"038390914330916.UVswNWdPVx"

"result":\[

{

"balance":{

"real\_balance":

11886

"bonus\_balance":

0

"vat\_balance":{

"2":

"11886.0000"

}

"credit\_balance":

0

"type":

1

"cloud\_balance":

11886

"other\_balance":

11886

"cloud\_balance\_view":

11886

"other\_balance\_view":

0

}

"auto\_payment\_enable":

0

"isAutopaymentEnable":

1

"domainBonuses":

7

"status":

"active"

"blockInfo":{

"days\_date":

"25.04.2032"

"days":

2274

"days\_word":

"дня"

}

"blockedMoney":

36033

"deferment":{

"show":

false

"value":

0

}

"edgeDate":

"2024-08-30"

}

\]

}

isAutopaymentEnable
-------------------

метод

описание

Включен или нет автоплатеж на аккаунте

возвращаемое значение

true - включен, false - выключен

тип данных в ответе

boolean

пример запроса

{

"jsonrpc":

"2.0"

"method":

"isAutopaymentEnable"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"636726627008079.JHKHzWxTwk"

"result":

false

}

getPayRecommendations
---------------------

метод

описание

Получение рекомендаций к оплате

возвращаемые значения в свойствах элементов массива

'recommended\_for\_pay' array Массив рекомендаций

'recommended\_for\_pay\_balance' массив рекомендаций по балансу

'exist\_domain\_bonus' int Количество доменных бонусов

'total\_frp\_balance' int Реальный баланс

'tariff\_domain\_bonus' int Бонусы за оплату тарифа

'tariff\_domain\_bonus\_tld' int Бонусы на конкретные зоны

'domain\_bonuses\_by\_tld' array Детализация по бонусам на конкретные зоны

параметры в запросе

addBalanceRecommendations

boolean

true - отображать рекомендации по пополнению баланса, false - не отображать

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getPayRecommendations"

"params":{

"addBalanceRecommendations":

"false"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"430918453629924.PdhsCNVaqu"

"result":\[

{

"recommended\_for\_pay":\[

{

"id":

1

"name":

"Домен test32132.ru (1 год)"

"date":

"не зарегистрирован"

"cost":

175

}

\]

"recommended\_for\_pay\_balance":\[\]

"exist\_domain\_bonus":

0

"total\_frp\_balance":

2800

"tariff\_domain\_bonus":

0

"tariff\_domain\_bonus\_tld":

0

"domain\_bonuses\_by\_tld":{

"any":

0

}

}

\]

}

getRecommendationTotalCost
--------------------------

метод

описание

Возвращает полную сумму, рекомендованную к оплате

возвращаемое значение

Полная сумма, рекомендованная к оплате

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getRecommendationTotalCost"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"477918812019909.FyydUOWoaY"

"result":

949

}

getUpcomingPaymentsVh
---------------------

метод

описание

Возвращает информацию о предстоящих платежах для пользователей VH

возвращаемые значения в свойствах элементов массива

'name' string Название услуги

'cost' int Стоимость

'cost\_str' string Стоимость строчкой

'action' int (1 - если доступна регистрация за бонус, 0 - недоступна)

Для не новых аккаунтов или новых с измененным первым заказов выводим рекомендации

Возвращаемые значения в элементах массива

'id' int Идентификатор рекомендации

'name' string Название

'date' string Дата

'cost' int Цена

'cost\_str' string Цена в виде 100 р.

'entity\_type' string Тип услуги

'action' int (по умолчанию 0)

'checkbox\_available' int Доступен ли чекбокс выбора (1 - доступен, 0 - не доступен)

'service\_id' string Идентификатор услуги

'vat\_type' string Тип налога

'vat\_name' string НДС

'vat\_value' int Ставка НДС

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getUpcomingPaymentsVh"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"143368602500896.joVninWTcf"

"result":\[

{

"id":

1

"name":

"Домен test526.ru (1 год)"

"date":

"не зарегистрирован"

"cost":

0

"cost\_str":

"0 руб. (по акции)"

"entity\_type":

"domain"

"action":

0

"checkbox\_available":

0

"service\_id":

"dyasyuc794\_domain\_1"

"vat\_type":

"other"

"vat\_name":

"НДС 22%"

"vat\_value":

"22"

"ready\_for\_bonus":

1

"base\_cost":

"175"

"base\_cost\_str":

"175 руб."

"bonus\_cost":

0

"bonus\_cost\_str":

"0 руб. (по акции)"

"tld":

"ru"

}

{

"id":

2

"name":

"Домен test865.ru (1 год)"

"date":

"не зарегистрирован"

"cost":

175

"cost\_str":

"175 руб."

"entity\_type":

"domain"

"action":

0

"checkbox\_available":

1

"service\_id":

"dyasyuc794\_domain\_2"

"vat\_type":

"other"

"vat\_name":

"НДС 22%"

"vat\_value":

"22"

"ready\_for\_bonus":

1

"base\_cost":

"175"

"base\_cost\_str":

"175 руб."

"bonus\_cost":

0

"bonus\_cost\_str":

"0 руб. (по акции)"

"tld":

"ru"

}

{

"id":

3

"name":

"Лечение антивирусом сайта dyasyuc794 (1 мес.)"

"date":

"19.02.2026"

"cost":

199

"cost\_str":

"199 р."

"entity\_type":

"antivirus"

"action":

0

"checkbox\_available":

0

"type":

"antivirus"

"service\_id":

"dyasyuc794\_antivirus\_dyasyuc794"

"vat\_type":

"other"

"vat\_name":

"НДС 22%"

"vat\_value":

"22"

}

{

"id":

4

"name":

"Лечение антивирусом сайта Сайт 2 (1 мес.)"

"date":

"19.02.2026"

"cost":

199

"cost\_str":

"199 р."

"entity\_type":

"antivirus"

"action":

0

"checkbox\_available":

0

"type":

"antivirus"

"service\_id":

"dyasyuc794\_antivirus\_105875"

"vat\_type":

"other"

"vat\_name":

"НДС 22%"

"vat\_value":

"22"

}

{

"id":

5

"name":

"SEO и реклама: test526.ru"

"date":

"остановлена"

"cost":

5510

"cost\_str":

"5510 р."

"entity\_type":

"seo"

"action":

0

"checkbox\_available":

1

"service\_id":

"dyasyuc794\_seo\_5"

"vat\_type":

"other"

"vat\_name":

"НДС 22%"

"vat\_value":

"22"

}

\]

}

changeDeferment
---------------

метод

описание

Включить/выключить отсрочку

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

turnOn

boolean

true - включить, false - выключить

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"changeDeferment"

"params":{

"turnOn":

"false"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"640878664494288.mnOeKUguDM"

"result":

1

}

getRemainsDate
--------------

метод

описание

Дата, до которой хватит денег на счету

возвращаемое значение

'd.m.Y'

тип данных в ответе

string

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getRemainsDate"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"826599988468567.CeYwrGHARE"

"result":

"01.10.2023"

}

getRemainsDays
--------------

метод

описание

Количество дней до блокировки

возвращаемое значение

Количество дней до блокировки

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getRemainsDays"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"915803143575533.WZnnbIxkOk"

"result":

15

}

getBalance
----------

метод

описание

Информация о балансе

возвращаемые значения в свойствах элементов массива

'real\_balance' float Реальные деньги

'bonus\_balance' float Бонусные деньги

'cloud\_balance' float Деньги на услуги cloud

'other\_balance' float Деньги на другие услуги

'cloud\_balance\_view' float Сумма для отображения для баланса cloud

'other\_balance\_vew' float Сумма для отображения для баланса на другие услуги

'credit\_balance' float Общий долг

'credit\_cloud\_balance' float Долг по услугам cloud

'credit\_other\_balance' float Долг услугам other

'type' int Тип биллинга

'multiple\_balance\_enabled' bool Режим нескольких балансов (true - включен)

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getBalance"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"150985699655551.jPmpPXkePF"

"result":\[

{

"real\_balance":

1544

"bonus\_balance":

0

"vat\_balance":{

"4":

"1492.0000"

"5":

"52.0000"

}

"credit\_balance":

0

"type":

1

"multiple\_balance\_enabled":

true

"cloud\_balance":

1492

"other\_balance":

52

"cloud\_balance\_view":

1492

"other\_balance\_view":

52

}

\]

}

getActiveReserves
-----------------

метод

описание

Детальная информация о заблокированных средствах

возвращаемые значения в свойствах элементов массива

'charge' float Остаток заблокированных средств

'type' string Тип услуги

'balance\_type' string Тип налога баланса

'info' Информация о блокировке

'title' string Название услуги

'endDate' string Дата окончания блокировки

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getActiveReserves"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"566865116732700.jsyKFuOoRb"

"result":\[

{

"charge":

2368.74

"info":{

"title":

"Тариф «‎Взлёт на 1 год»"

"endDate":

"2027-01-20"

}

"type":

"tariff"

"balance\_type":

"cloud"

}

{

"charge":

"3120.00"

"info":{

"title":

"Другое"

"endDate":

NULL

}

"type":

"other"

"balance\_type":

"other"

}

\]

}