# VPS / Управление VPS

Vps
===

объект

описание

Объект VPS

применяемость

VPS

путь к объекту

POST https://api.sweb.ruvps

требование к авторизации

да

список методов

*   index;
*   getFirstOrderInfo;
*   createEnable;
*   getAvailableConfig;
*   copy;
*   createFirst;
*   create;
*   rename;
*   isRunning;
*   remove;
*   removeFirst;
*   load;
*   getConstructorPlanId;
*   changePlan;
*   powerOn;
*   powerOff;
*   reboot;
*   getCurrentAction;
*   reinstallOs;
*   logs.

index
-----

метод

описание

Список VPS

возвращаемые значения в свойствах элементов массива

'billingId' string ID сервиса

'name' string Имя VPS

'plan\_id' int ID плана

'plan\_name' string Название палана

'parent\_plan\_id' int ID родительского плана

'plan\_price' int Стоимость

'cpu' int Число процессоров

'ram' string Количество памяти

'disk' string Размер диска

'blockUi' int Заблокирована

'active' int Активна

'uid' string Идентификатор машины

'os\_distribution' string Название ОС

'os\_distr\_id' int ID Дистрибутива

'category' string Категория

'ts\_create' string Дата создания

'mac' string MAC-адрес

'ip' string IP

'local\_ip' string локальный IP

'local\_mac' string локальный MAC

'local\_mask' string локальная маска подсети

'current\_action' string Текущая операция

'is\_running' int Запущена

'isp' array Информация о панели управления:

'license\_type' string Название панели

'ip' string IP

'active\_until' string Активна до даты

'price' float Стоимость

'link' string Ссылка на вход в панель

'is\_blocked' int Заблокирована

'creation\_time' string Дата создания

'ext\_ips' array Информация о доп. IP:

'is\_test' int Тестовый период

'is\_new' bool Новая услуга

'datacenter' string Дата-центр

'ordered\_ip\_count' int Количество адресов, заказанных на VPS

'protected\_ips'

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

"720081569636118.LjJMsKaidf"

"result":\[

{

"billingId":

"inn\*\*\*\*\_vps\_4"

"name":

"inn\*\*\*\*\_vps\_4"

"plan\_id":

"4"

"plan\_name":

"KVM-10"

"parent\_plan\_id":

NULL

"plan\_price":

349

"cpu":

2

"ram":

"1024"

"disk":

"10 ГБ"

"blockUi":

1

"active":

0

"uid":

"a0a23dcee\*\*\*\*\*\*\*\*\*\*\*\*\*"

"os\_distribution":

"Ubuntu 22.04 LTS"

"os\_distr\_id":

102

"category":

"nvme"

"ts\_create":

"2023-06-26 15:38:20"

"mac":

"00:16:3e:77:a2:26"

"ip":

"77.222.43.225"

"local\_ip":

NULL

"local\_mac":

NULL

"local\_mask":

NULL

"current\_action":

""

"is\_running":

0

"isp":\[

{

"license\_type":

"LEMP"

"ip":

"77.222.43.225"

"active\_until":

""

"price":

0

"link":

""

"is\_blocked":

0

"creation\_time":

"10-15"

}
```

\]

"ext\_ips":\[\]

"is\_test":

0

"is\_new":

false

"datacenter":

"Москва"

"ordered\_ip\_count":

2

"protected\_ips":\[

"127.0.105.53"

\]

}

\]

}

getFirstOrderInfo
-----------------

метод

описание

Получение информации о первом заказе

возвращаемые значения в свойствах элементов массива

'plan' string Название плана

'os' string Название ОС

'panel' string Название ПУ

'cpu\_cores' string Количество процессоров

'ram' string Количество памяти

'volume\_disk' string Размер диска

'price\_per\_month' int Цена за месяц

'pay\_period' int Цена за период

'price\_for\_period\_with\_stock' int Цена за месяц со скидкой

'price\_per\_month\_with\_stock' int Цена за период со скидкой

'promocode' string|null Промо-код на скидку (не партнерский) введенный при регистрации

'clearAvailable' bool Доступна возможность очистки первого заказа

'plan\_is\_constructor' bool Флаг сконструированного тарифа

'ipCount' int Кол-во не защищенных IP в заказе

'protectedIps' int\[\] Массив ID тарифов защищенных IP для заказа (например, \[1, 3, 3\])

тип данных в ответе

array

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

"171633869878845.iBlzwvGSEL"

"result":\[

{

"jsonrpc":

"2.0"

"version":

"1.263.20250326113457"

"id":

"20250327104613.kmuG0Cu94B"

"result":{

"plan":

"CLOUD PROMO на год"

"os":

"Ubuntu 24.04 LTS"

"panel":

"Без ПО"

"cpu\_cores":

"1"

"ram":

"1024"

"volume\_disk":

"10 ГБ"

"price\_per\_month":

139

"pay\_period":

12

"price\_for\_period\_with\_stock":

1668

"price\_per\_month\_with\_stock":

139

"promocode":

NULL

"clearAvailable":

false

"plan\_is\_constructor":

false

"ipCount":

1

"protectedIps":\[

1

2

\]

}
```

}

\]

}

createEnable
------------

метод

описание

Проверка доступен ли заказ VPS

возвращаемое значение

1 - успешно, 0 - ошибка

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"createEnable"

"params":{}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"888990632800705.sNMzlIEKwE"

"result":

1

}
```

getAvailableConfig
------------------

метод

описание

Получение списка доступных дистрибутивов, ISP-лицензий, тарифных планов

возвращаемые значения в свойствах элементов массива

'vpsPlans' array Тарифные планы

Каждый тарифный план содержит массив значений:

'id' int id тарифного плана

'ts\_create' string дата и время создания в формате YYYY-MM-DD HH:MM:SS

'ts\_update' string дата и время обновления в формате YYYY-MM-DD HH:MM:SS

'billing\_id' string id услуги

'category\_id' string id категории тарифного плана

'name' string название тарифа

'price\_per\_month' int стоимость одного месяца при помесячной оплате

'parent\_plan\_id' int|null id родительского тарифного плана

'cpu\_cores' string кол-во ядер

'ram' string кол-во оперативной памяти

'disk\_type' string тип диска

'volume\_disk' string ёмкость диска

'units' string кол-во занимаемых юнитов

'is\_promo' string является ли промо-трифом (0 - не является)

'package\_duration' string длительность пакета в месяцах

'constructor' string относится ли тариф к категории Конструктор сайтов (N - не относится)

'year\_price\_per\_month' int стоимость одного месяца в годовом пакете

'category' string название категории тарифного плана

'datacenters' array массив из id дата-центров

'price\_per\_month\_promo' int стоимость месяца промо-версии тарифа при помесячной оплате

'year\_price\_per\_month\_promo' int стоимость месяца промо-версии тарифа в годовом пакете

'selectOs' array Операционные системы

Каждая ОС содержит массив значений:

'id' string id операционной системы

'name' string название ОС

'description' string более подробное название ОС

'order' string порядковый номер для сортировки в списке

'url' string|null ссылка на страницу с информацией об ОС

'full\_description' string|null полное подробное описание

'plan\_id' string id тарифного плана по умолчанию

'os\_distribution\_id' string id сборки

'panel\_type' array массив названий доступных панелей управления (empty - без ПУ)

'selectPanel' array Панели управления

Каждая панель управления содержит массив значений:

'id' string id панели управления

'name' string алиас названия

'description' string полное название

'order' string порядковый номер для сортировки в списке

'creation\_time' string|null диапазон времени(в минутах)

'url' string|null ссылка на страницу с информацией о панели управления

'full\_description' string|null полное подробне описание

'plan\_id' string id тарифного плана по умолчанию для данной панели

'os\_distribution\_id' string id сборки

'action' int действует ли акция на данную панель управления (0 - нет акции)

'price' int текущая стоимость панели управления в месяц с учетом активности акции (0 - бесплатно)

'old\_price' int базовая стоимость панели управления без акции

'osPanel' array Дистрибутивы (операционная система+панель). distributive передается в create

Каждый дистрибутив содержит массив значений:

'distributive' string id дистрибутива

'os' string id операционной системы

'panel' string id панели

'availablePlanIds' array массив из id тарифных планов доступных с этим дистрибутивом

'minRam' int минимальное кол-во ОЗУ (Гб)

'minStorage' int минимальный объем на диске

'datacenters' array Доступные дата-центры

Каждый дата-центр содержит массив значений:

'id' string id дата-центра

'name' string алиас названия (spb / msk)

'location' string название местоположения (Санкт-Петербург)

'site\_name' string название дата-центра для пользователей

'categories' array Категории тарифных планов

Каждая категория содержит массив значений:

'id' string id категории

'slug' string алиас категории

'name' string название категории для пользователей

'prior' string порядковый номер для сортировки в списке

'kit' array массив параметров для конфигуратора тарифов категории NVME:

'cpuCores' array параметры для установки кол-ва ядер:

'start' int минимальное значение

'end' int максимальное значение

'step' int размер шага при изменении кол-ва ядер

'price' int стоимость одного ядра

'ram' array параметры для установки кол-ва ОЗУ:

'values' array массив из доступных объемов в Гб:

'price' int стоимость одного Гб

'volumeDisk' array параметры для установки объема жесткого диск:

'start' int минимальное значение

'end' int максимальное значение

'step' int размер шага при изменении объема диска

'price' int стоимость одного Гб

'price\_backup' int стоимость одного Гб бэкапа

'categoryId' int id категории тарифного плана

'kit\_turbo' array массив параметров для конструктора тарифов категории Turbo:

'cpuCores' array параметры для установки кол-ва ядер:

'start' int минимальное значение

'end' int максимальное значение

'step' int размер шага при изменении кол-ва ядер

'price' int стоимость одного ядра

'ram' array параметры для установки кол-ва ОЗУ:

'start' int минимальное значение в Гб

'end' int максимальное значение в Гб

'step' int размер шага при изменении объема ОЗУ в Гб

'price' int стоимость одного Гб

'volumeDisk' array параметры для установки объема жесткого диска:

'start' int минимальное значение в Гб

'end' int максимальное значение в Гб

'step' int размер шага при изменении объема жесткого диска в Гб

'price' int стоимость одного Гб

'price\_backup' int стоимость одного Гб бэкапа

'categoryId' int id категории тарифного плана

'kit\_hdd' array массив параметров для конструктора тарифов категории HDD:

'cpuCores' array параметры для установки кол-ва ядер:

'start' int минимальное значение

'end' int максимальное значение

'step' int размер шага при изменении кол-ва ядер

'price' int стоимость одного ядра

'ram' array параметры для установки кол-ва ОЗУ:

'start' int минимальное значение в Гб

'end' int максимальное значение в Гб

'step' int размер шага при изменении объема ОЗУ в Гб

'price' int стоимость одного Гб

'volumeDisk' array параметры для установки объема жесткого диска:

'start' int минимальное значение в Гб

'end' int максимальное значение в Гб

'step' int размер шага при изменении объема жесткого диска в Гб

'price' int стоимость одного Гб

'categoryId' int id категории тарифного плана

тип данных в ответе

array

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

"795506945436770.AHWsEwMbad"

"result":{

"vpsPlans":\[

{

"id":

4

"ts\_create":

"2015-09-29 13:43:43"

"ts\_update":

"2021-09-22 11:48:03"

"billing\_id":

"597"

"category\_id":

"1"

"name":

"KVM-10"

"price\_per\_month":

349

"parent\_plan\_id":

NULL

"cpu\_cores":

"2"

"ram":

"1024"

"disk\_type":

"NVMe"

"volume\_disk":

"10 ГБ"

"units":

"1"

"is\_promo":

"0"

"package\_duration":

"1"

"constructor":

"N"

"year\_price\_per\_month":

299

"category":

"nvme"

"datacenters":\[

1

2

\]

"price\_per\_month\_promo":

239

"year\_price\_per\_month\_promo":

239

}
```

```json
{

"id":

5

"ts\_create":

"2015-09-29 13:43:43"

"ts\_update":

"2022-03-18 09:16:03"

"billing\_id":

"598"

"category\_id":

"1"

"name":

"KVM-20"

"price\_per\_month":

649

"parent\_plan\_id":

NULL

"cpu\_cores":

"2"

"ram":

"2048"

"disk\_type":

"NVMe"

"volume\_disk":

"20 ГБ"

"units":

"2"

"is\_promo":

"0"

"package\_duration":

"1"

"constructor":

"N"

"year\_price\_per\_month":

549

"category":

"nvme"

"datacenters":\[

1

2

\]

"price\_per\_month\_promo":

439

"year\_price\_per\_month\_promo":

439

}
```

```json
{

"id":

42

"ts\_create":

"2021-11-22 14:18:18"

"ts\_update":

NULL

"billing\_id":

"1606"

"category\_id":

"3"

"name":

"TURBO-160"

"price\_per\_month":

4099

"parent\_plan\_id":

NULL

"cpu\_cores":

"4"

"ram":

"8192"

"disk\_type":

"NVMe"

"volume\_disk":

"160 ГБ"

"units":

"16"

"is\_promo":

"0"

"package\_duration":

"1"

"constructor":

"N"

"year\_price\_per\_month":

3299

"category":

"turbo"

"datacenters":\[

1

2

\]

"price\_per\_month\_promo":

2639

"year\_price\_per\_month\_promo":

2639

}
```

\]

"selectOs":\[

```json
{

"id":

"20"

"name":

"ubuntu-20-04"

"description":

"Ubuntu 20.04 LTS"

"order":

"1"

"url":

NULL

"full\_description":

NULL

"plan\_id":

"4"

"os\_distribution\_id":

"32"

"panel\_type":\[

"empty"

"isp"

"docker"

"nodejs"

"rocket"

"gitlab"

"hestia"

"nextcloud"

"fastpanel"

"minecraft"

\]

}
```

```json
{

"id":

"13"

"name":

"debian-9"

"description":

"Debian 9"

"order":

"103"

"url":

NULL

"full\_description":

NULL

"plan\_id":

"4"

"os\_distribution\_id":

"22"

"panel\_type":\[

"empty"

"isp"

\]

}
```

```json
{

"id":

"19"

"name":

"bitrix-auto-centos-7"

"description":

"BitrixVM 7"

"order":

"104"

"url":

"https://sweb.ru/vds/bitrix/"

"full\_description":

"Готовое решение для продуктов на 1С-Битрикс"

"plan\_id":

"6"

"os\_distribution\_id":

"30"

"panel\_type":\[

"empty"

\]

}
```

\]

"selectPanel":\[

```json
{

"id":

"7"

"name":

"empty"

"description":

"Без ПО"

"order":

"0"

"creation\_time":

NULL

"url":

NULL

"full\_description":

NULL

"plan\_id":

"5"

"os\_distribution\_id":

"0"

"action":

0

"price":

0

"old\_price":

0

}
```

```json
{

"id":

"4"

"name":

"vps\_isp6\_lite"

"description":

"ISPmanager 6 Lite"

"order":

"2"

"creation\_time":

"20-30"

"url":

"https://help.sweb.ru/entry/728/"

"full\_description":

"Популярная панель управления сервером, 10 сайтов"

"plan\_id":

"5"

"os\_distribution\_id":

"77"

"action":

0

"price":

300

"old\_price":

300

}
```

```json
{

"id":

"9"

"name":

"nodejs"

"description":

"Node.js"

"order":

"8"

"creation\_time":

"10-15"

"url":

NULL

"full\_description":

"Серверная платформа для работы с JavaScript"

"plan\_id":

"5"

"os\_distribution\_id":

"62"

"action":

0

"price":

0

"old\_price":

0

}
```

```json
{

"id":

"10"

"name":

"rocket"

"description":

"Rocket.Chat"

"order":

"9"

"creation\_time":

"10-15"

"url":

NULL

"full\_description":

"Корпоративный мессенджер с открытым исходным кодом"

"plan\_id":

"5"

"os\_distribution\_id":

"63"

"action":

0

"price":

0

"old\_price":

0

}
```

```json
{

"id":

"11"

"name":

"gitlab"

"description":

"GitLab"

"order":

"10"

"creation\_time":

"15-30"

"url":

NULL

"full\_description":

"Система управления репозиториями программного кода для Git"

"plan\_id":

"6"

"os\_distribution\_id":

"64"

"action":

0

"price":

0

"old\_price":

0

}
```

```json
{

"id":

"15"

"name":

"minecraft"

"description":

"Minecraft JE Server"

"order":

"11"

"creation\_time":

"10-15"

"url":

"https://sweb.ru/vds/minecraft/"

"full\_description":

"Сервер игры Minecraft Java Edition"

"plan\_id":

"6"

"os\_distribution\_id":

"89"

"action":

0

"price":

0

"old\_price":

0

}
```

\]

"osPanel":\[

```json
{

"distributive":

"8"

"os":

"4"

"panel":

"7"

"availablePlanIds":\[

4

5

6

12

14

26

28

34

38

42

\]

"minRam":

0

"minStorage":

0

}
```

```json
{

"distributive":

"89"

"os":

"20"

"panel":

"15"

"availablePlanIds":\[

5

6

12

14

26

28

34

38

42

\]

"minRam":

2

"minStorage":

0

}
```

\]

"datacenters":\[

```json
{

"id":

"1"

"name":

"spb"

"location":

"Санкт-Петербург"

"site\_name":

"Дата-центр в СПБ"

}
```

```json
{

"id":

"2"

"name":

"msk"

"location":

"Москва"

"site\_name":

"Дата-центр в Москве"

}
```

\]

"categories":\[

```json
{

"id":

"1"

"slug":

"nvme"

"name":

"VPS/VDS на NVMe (быстрые)"

"prior":

"1"

}
```

```json
{

"id":

"3"

"slug":

"turbo"

"name":

"VPS/VDS HighCPU (турбо)"

"prior":

"2"

}
```

```json
{

"id":

"2"

"slug":

"hdd"

"name":

"VPS/VDS на HDD (большого объёма)"

"prior":

"3"

}
```

```json
{

"id":

"4"

"slug":

"kit"

"name":

"Конфигуратор VPS/VDS"

"prior":

"4"

}
```

\]

"kit":```json
{

"cpuCores":{

"start":

2

"end":

16

"step":

2

"price":

110

}
```

"ram":```json
{

"values":\[

1

2

3

4

6

8

10

12

14

16

18

20

22

24

26

28

30

32

\]

"price":

115

}
```

"volumeDisk":```json
{

"start":

10

"end":

320

"step":

10

"price":

15

"price\_backup":

1.5

}
```

"categoryId":

1

}

"kit\_turbo":```json
{

"cpuCores":{

"start":

1

"end":

4

"step":

1

"price":

530

}
```

"ram":```json
{

"start":

2

"end":

8

"step":

1

"price":

140

}
```

"volumeDisk":```json
{

"start":

40

"end":

160

"step":

10

"price":

9

"price\_backup":

3

}
```

"categoryId":

3

}

"kit\_hdd":```json
{

"cpuCores":{

"start":

1

"end":

2

"step":

1

"price":

530

}
```

"ram":```json
{

"start":

2

"end":

4

"step":

1

"price":

160

}
```

"volumeDisk":```json
{

"start":

500

"end":

1000

"step":

10

"price":

2

}
```

"categoryId":

2

}

}

}

copy
----

метод

описание

Клонирование VPS

возвращаемое значение

создание/клонирование VPS

параметры в запросе

billingId

string

идентификатор машины

vpsPlanId

integer

новый тарифный план

тип данных в ответе

string

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"copy"

"params":{

"billingId":

"vhp\*\*\*\*\_vps\_1"

"vpsPlanId":

4

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"539485902873327.lePGrCwkRE"

"result":

"vhp\*\*\*\*\_vps\_2"

}
```

createFirst
-----------

метод

описание

Создание первого заказа с VPS

возвращаемое значение

создание/клонирование VPS

параметры в запросе

distributiveId

integer

ID Дистрибутива

vpsPlanId

integer

ID Тарифного плана

datacenter

integer

Датацентр

alias

string

Название VPS

sshKey

string

Публичный SSH-ключ

sshKeyName

string

Имя ключа

privateIp

boolean

Подключить к локальной сети

period

integer

Период оплаты (1 или 12 мес.)

startTestPeriod

boolean

Начать тестовый период

monitoringPlanId

integer

ID плана мониторинга

monitoringContactId

integer

ID контакта мониторинга

ipCount

integer

Кол-во заказанных вместе с VPS IP-адресов (для 1ого заказа: 0 или 1)

protectedIps

array

Массив ID тарифов защищенных IP для заказа (например, \[1, 3, 3\])

тип данных в ответе

string

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"createFirst"

"params":{

"distributiveId":

32

"vpsPlanId":

4

"datacenter":

1

"period":

1

"startTestPeriod":

true

"ipCount":

1

"protectedIps":\[

1

2

3

\]

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"207117702707782.xXEErhZiJx"

"result":

"vhp\*\*\*\*\_vps\_1"

}
```

create
------

метод

описание

Создание VPS

возвращаемое значение

создание/клонирование VPS

параметры в запросе

distributiveId

integer

ID Дистрибутива

vpsPlanId

integer

ID Тарифного плана

datacenter

integer

датацентр

alias

string

название VPS

sshKey

string

публичный SSH-ключ

sshKeyName

string

имя ключа

privateIp

boolean

подключить к локальной сети

monitoringPlanId

integer

ID плана мониторинга

monitoringContactId

integer

ID контакта мониторинга

remoteBackupId

integer

ID бэкапа

ipCount

integer

кол-во заказанных вместе с VPS IP-адресов

protectedIps

integer

массив ID тарифов защищенных IP для заказа (например, \[1, 3, 3\])

тип данных в ответе

string

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"create"

"params":{

"distributiveId":

32

"vpsPlanId":

4

"datacenter":

1

"alias":

"hestiaVPS"

"sshKey":

"ssh-rsa ......."

"monitoringPlanId":

1

"monitoringContactId":

2642

"ipCount":

2

"protectedIps":\[

1

2

\]

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"921832275382655.QvWznXfvab"

"result":

"vhp\*\*\*\*\_vps\_2"

}
```

rename
------

метод

описание

Переименование VPS

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

billingId

string

идентификатор машины

alias

string

название VPS

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"rename"

"params":{

"billingId":

"vhp\*\*\*\*\_vps\_1"

"alias":

"hestiaVPS"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"534460260727581.ktleXhvmed"

"result":

1

}
```

isRunning
---------

метод

описание

Запущена ли VPS в данный момент

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

billingId

string

идентификатор машины

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"isRunning"

"params":{

"billingId":

"vhp\*\*\*\*\_vps\_1"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"998654563950036.aIgqVlSLwG"

"result":

1

}
```

remove
------

метод

описание

Удаление VPS

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

billingId

string

идентификатор машины

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"remove"

"params":{

"billingId":

"vhp\*\*\*\*\_vps\_1"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"669713065950971.vfsVDeDrel"

"result":

1

}
```

removeFirst
-----------

метод

описание

Удаление первого заказа.Доступно, если заказ ещё не был оплачен и услуга не стартовала

возвращаемое значение

1 - успешно, 0 - ошибка

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

"503723158316028.itBMJqOzOz"

"result":

1

}
```

load
----

метод

описание

Загрузка - возвращает картинку в Base64

возвращаемые значения в свойствах элементов массива

'mimetype' string MIME-тип данных (image/png;base64)

'metadata' array мета-данные

'content' string содержимое в base64

параметры в запросе

billingId

string

идентификатор машины

type

string

тип нагрузки ('cpu', 'hdd\_ops', 'net')

from

string

дата начала

to

string

дата окончания

width

integer

ширина графика

тип данных в ответе

array

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"load"

"params":{

"billingId":

"vhp\*\*\*\*\_vps\_1"

"type":

"hdd\_ops"

"from":

"08-03-2023"

"to":

"15-03-2023"

"width ":

640

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"734579342681177.QANhhrenec"

"result":{

"mimetype":

"image/png;base64"

"metadata":\[\]

"content":

"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"

}
```

}

getConstructorPlanId
--------------------

метод

описание

Возвращает id тарифного плана конструктора VPS по значениям кол-ва ядер, ОЗУ, объема диска и категории

возвращаемое значение

id тарифного плана конструктора VPS

параметры в запросе

cpu\_cores

integer

кол-во ядер CPU

ram

integer

ОЗУ в гигабайтах

volume\_disk

integer

жесткий диск в гигабайтах

category\_id

integer

id категории

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

"cpu\_cores":

4

"ram":

2

"volume\_disk":

20

"category\_id":

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

"215748354293096.RsEbKmyyev"

"result":

124

}
```

changePlan
----------

метод

описание

Изменение тарифного плана

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

billingId

string

идентификатор машины

planId

integer

ID Тарифного плана

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"changePlan"

"params":{

"billingId":

"vhp\*\*\*\*\_vps\_1"

"vpsPlanId":

4

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"851409313888159.HbxZlMeGbp"

"result":

1

}
```

powerOn
-------

метод

описание

Включение VPS

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

billingId

string

идентификатор машины

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"powerOn"

"params":{

"billingId":

"vhp\*\*\*\*\_vps\_1"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"528007144710978.bNOgcSCJoi"

"result":

1

}
```

powerOff
--------

метод

описание

Выключение VPS

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

billingId

string

идентификатор машины

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"powerOff"

"params":{

"billingId":

"vhp\*\*\*\*\_vps\_1"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"217824748450948.yQwudBniRK"

"result":

1

}
```

reboot
------

метод

описание

Перезагрузка VPS

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

billingId

string

идентификатор машины

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"reboot"

"params":{

"billingId":

"vhp\*\*\*\*\_vps\_1"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"339045769301497.hztDCuXaoZ"

"result":

1

}
```

getCurrentAction
----------------

метод

описание

Получение текущей операции по VPS

возвращаемое значение

получение текущей операции по VPS

параметры в запросе

billingId

string

идентификатор машины

тип данных в ответе

string

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"getCurrentAction"

"params":{

"billingId":

"vhp\*\*\*\*\_vps\_1"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"460594474260523.tDneBAxcGv"

"result":

"start"

}
```

reinstallOs
-----------

метод

описание

Переустановка образа VPS

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

billingId

string

идентификатор машины

distributiveId

integer

ID Дистрибутива

тип данных в ответе

integer

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"reinstallOs"

"params":{

"billingId":

"vhp\*\*\*\*\_vps\_1"

"distributiveId":

32

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"067069631845647.QceVobaWre"

"result":

1

}
```

logs
----

метод

описание

Получение логов операций

возвращаемые значения в свойствах элементов массива

'type' string тип операции

'status' string статус операции

'started\_at' string дата и время начала операции в формате YYYY-MM-DD HH:MM:SS

'ended\_at' string дата и время окончания операции в формате YYYY-MM-DD HH:MM:SS

параметры в запросе

billingId

string

идентификатор машины

тип данных в ответе

array

пример запроса

```json
{

"jsonrpc":

"2.0"

"method":

"logs"

"params":{

"billingId":

"vhp\*\*\*\*\_vps\_1"

}
```

}

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"064408096436268.ZppnSghsvf"

"result":\[

{

"type":

"Старт"

"status":

"Завершена"

"started\_at":

"2023-03-15 13:42:03"

"ended\_at":

"2023-03-15 13:43:03"

}
```

```json
{

"type":

"Стоп"

"status":

"Завершена"

"started\_at":

"2023-03-15 13:40:02"

"ended\_at":

"2023-03-15 13:41:03"

}
```

```json
{

"type":

"Создание бэкапа"

"status":

"Завершена"

"started\_at":

"2023-03-13 16:10:02"

"ended\_at":

"2023-03-13 16:11:03"

}
```

```json
{

"type":

"Удаление бэкапа"

"status":

"Завершена"

"started\_at":

"2023-03-13 16:04:02"

"ended\_at":

"2023-03-13 16:05:03"

}
```

```json
{

"type":

"Создание бэкапа"

"status":

"Завершена"

"started\_at":

"2023-03-13 15:49:02"

"ended\_at":

"2023-03-13 15:50:03"

}
```

```json
{

"type":

"Создание"

"status":

"Завершена"

"started\_at":

"2023-03-13 15:14:03"

"ended\_at":

"2023-03-13 15:15:05"

}
```

\]

}