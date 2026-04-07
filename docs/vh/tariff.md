# Виртуальный хостинг / Тариф

Тариф
=====

объект

описание

Тариф

применяемость

Виртуальный хостинг

путь к объекту

POST https://api.sweb.ru/tariff

требование к авторизации

да

список методов

*   index;
*   serverInfo.

index
-----

метод

описание

Текущая информация о тарифе и реальном использовании ресурсов

возвращаемые значения в свойствах элементов массива

'info' array Информация о текущем тарифе:

'plan\_id' int ID плана

'name' string Название плана

'category' string Категория плана

'quota' int Доступная квота

'mail\_quota' int Доступная почтовая квота

'mysql' int Число баз MySQL

'site' int Число сайтов

'postgresql' int Число баз PostgeSQL

'price' int Цена за месяц

'price\_6' int Цена за полгода

'price\_12' int Цена за год

'duration' int Период автопродления

'real' array Информация о реально используемых ресурсах:

'quota' float Текущая квота

'mail\_quota' float Текущая почтовая квота

'mysql' int Число баз MySQL

'site' int Число сайтов

'postgresql' int Число баз PostgeSQL

'firebird' int Число баз Firebird

'mailbox' int Число почтовых ящиков

'realPrice' int Текущая стоимость

'realDuration' int Текущая настройка автопродления

'prolongPrice' int Текущая цена автопродления

'prolongDuration' int Значение настройки продления для тарифа автопродления

'noHosting' int 1, если не хостинговый тариф

'prolongChangeDisable' bool Запрещена смена настроек автопродления

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

"698400854768120.GwNysSXbUQ"

"result":\[

{

"info":{

"plan\_id":

7112

"name":

"Ракета"

"category":

"standart"

"quota":

10000

"mail\_quota":

0

"mysql":

512

"site":

10

"postgresql":

512

"price":

339

"price\_6":

0

"price\_12":

3348

"duration":

12

}

"real":{

"quota":

"0,00"

"mail\_quota":

"0,00"

"mysql":

"0"

"site":

1

"postgresql":

"0"

"firebird":

"0"

"mailbox":

"1"

"realPrice":

339

"realDuration":

1

"prolongPrice":

3348

"prolongDuration":

12

"noHosting":

0

"prolongChangeDisable":

false

}

}

\]

}

serverInfo
----------

метод

описание

Информация о сервере, на котором находится аккаунт пользователя

возвращаемые значения в свойствах элементов массива

'os' string Версия ОС

'apache' string Версия Apache

'perl' string Версия Perl

'mysql' string Версия MySQL

'ip' string IP

'name' string Название

'backend' string Версия бэкэнд

'ruby' string Версия Ruby

'python' string Версия Python

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"serverInfo"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"115603528178768.aogtWVSFId"

"result":\[

{

"os":

"Linux 3.10"

"apache":

"2.2.29"

"perl":

"5.20.2"

"mysql":

"5.7.27"

"ip":

"77.222.40.224"

"name":

"VH293"

"backend":\[

{

"type":

"php8.0bitrix"

"port":

"8094"

"descr":

"Apache 2.4 + PHP 8.0 Bitrix (Актуальная версия)"

"release\_version":

"3.0gamma"

"php\_info":

"https:/vh293.spaceweb.ru/phpinfo.php80bitrix"

"id":

32

}

{

"type":

"php8.1"

"port":

"8093"

"descr":

"Apache 2.4 + PHP 8.1 opcache (Актуальная версия)"

"release\_version":

"3.0gamma"

"php\_info":

"https:/vh293.spaceweb.ru/phpinfo.php81"

"id":

23

}

{

"type":

"php8"

"port":

"8092"

"descr":

"Apache 2.4 + PHP 8 opcache + mod\_wsgi python3.8 (Актуальная версия)"

"release\_version":

"3.0gamma"

"php\_info":

"https:/vh293.spaceweb.ru/phpinfo.php8"

"id":

22

}

{

"type":

"php7.4bitrix"

"port":

"8091"

"descr":

"Apache 2.4 + PHP 7.4 Bitrix (Актуальная версия)"

"release\_version":

"3.0gamma"

"php\_info":

"https:/vh293.spaceweb.ru/phpinfo.php74bitrix"

"id":

21

}

{

"type":

"php7.4"

"port":

"8090"

"descr":

"Apache 2.4 + PHP 7.4 opcache (Актуальная версия)"

"release\_version":

"3.0gamma"

"php\_info":

"https:/vh293.spaceweb.ru/phpinfo.php74"

"id":

12

}

{

"type":

"php7.1opc"

"port":

"8089"

"descr":

"Apache 2.2 + PHP 7.1 opcache (Актуальная версия)"

"release\_version":

"3.0gamma"

"php\_info":

"https:/vh293.spaceweb.ru/phpinfo.php71opc"

"id":

11

}

{

"type":

"php7.3"

"port":

"8088"

"descr":

"Apache 2.2 + PHP 7.3 (Актуальная версия)"

"release\_version":

"3.0gamma"

"php\_info":

"https:/vh293.spaceweb.ru/phpinfo.php73"

"id":

10

}

{

"type":

"php7.2"

"port":

"8087"

"descr":

"Apache 2.2 + PHP 7.2 (Актуальная версия)"

"release\_version":

"3.0gamma"

"php\_info":

"https:/vh293.spaceweb.ru/phpinfo.php72"

"id":

9

}

{

"type":

"php7.1"

"port":

"8086"

"descr":

"Apache 2.2 + PHP 7.1 (Актуальная версия)"

"release\_version":

"3.0gamma"

"php\_info":

"https:/vh293.spaceweb.ru/phpinfo.php71"

"id":

8

}

{

"type":

"php7"

"port":

"8085"

"descr":

"Apache 2.2 + PHP 7 (Актуальная версия)"

"release\_version":

"3.0gamma"

"php\_info":

"https:/vh293.spaceweb.ru/phpinfo.php7"

"id":

7

}

{

"type":

"php5.6"

"port":

"8084"

"descr":

"Apache 2.2 + PHP 5.6 (Актуальная версия)"

"release\_version":

"2.1"

"php\_info":

"https:/vh293.spaceweb.ru/phpinfo.php56"

"id":

6

}

{

"type":

"php5.5"

"port":

"8083"

"descr":

"Apache 2.2 + PHP 5.5 (Стабильная версия)"

"release\_version":

"2.0"

"php\_info":

"https:/vh293.spaceweb.ru/phpinfo.php55"

"id":

5

}

{

"type":

"php5.4"

"port":

"8082"

"descr":

"Apache 2.2 + PHP 5.4 (Стабильная версия)"

"release\_version":

"2.0"

"php\_info":

"https:/vh293.spaceweb.ru/phpinfo.php54"

"id":

4

}

{

"type":

"php5.3"

"port":

"8081"

"descr":

"Apache 2.2 + PHP 5.3 (Устаревшая версия)"

"php\_info":

"https:/vh293.spaceweb.ru/phpinfo.php53"

"id":

2

}

{

"type":

"php5.2"

"port":

"8080"

"descr":

"Apache 2.2 + PHP 5.2 (Устаревшая версия)"

"php\_info":

"https:/vh293.spaceweb.ru/phpinfo.php52"

"id":

1

}

\]

"ruby":

""

"python":

""

}

\]

}