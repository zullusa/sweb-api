# Виртуальный хостинг / Бэкапы

Бэкапы
======

объект

описание

Бэкапы для виртуального хостинга

применяемость

Виртуальный хостинг

путь к объекту

POST https://api.sweb.ruvh/backup

требование к авторизации

да

список методов

*   getList;
*   makeAccountCopy;
*   restoreFiles;
*   downloadFile;
*   getListFiles;
*   getListMysql;
*   receiveFiles;
*   receiveMysql;
*   restoreMysql.

getList
-------

метод

описание

Получение полного списка бэкапов (файлы и базы с группировкой по дням)

возвращаемые значения в свойствах элементов массива

'date' string Дата бэкапа

'mysql' int Если null, то значит идет подсчет баз

'files' int Если null, то значит идёт подсчет файлов

'backupFilesExists' bool

'warnQuota' bool Предупреждение о превышении квоты

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getList"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"983573784237674.sBohncmJbK"

"result":\[

{

"date":

"23.06.2023"

"mysql":

1

"files":

18

"backupFilesExists":

true

"warnQuota":

false

}

{

"date":

"22.06.2023"

"mysql":

1

"files":

18

"backupFilesExists":

true

"warnQuota":

false

}

{

"date":

"21.06.2023"

"mysql":

1

"files":

18

"backupFilesExists":

true

"warnQuota":

false

}

{

"date":

"20.06.2023"

"mysql":

1

"files":

18

"backupFilesExists":

true

"warnQuota":

false

}

{

"date":

"19.06.2023"

"mysql":

1

"files":

18

"backupFilesExists":

true

"warnQuota":

false

}

{

"date":

"18.06.2023"

"mysql":

1

"files":

18

"backupFilesExists":

true

"warnQuota":

false

}

{

"date":

"17.06.2023"

"mysql":

1

"files":

18

"backupFilesExists":

true

"warnQuota":

false

}

{

"date":

"01.06.2023"

"mysql":

0

"files":

NULL

"backupFilesExists":

true

"warnQuota":

false

}

{

"date":

"01.05.2023"

"mysql":

0

"files":

NULL

"backupFilesExists":

true

"warnQuota":

false

}

\]

}

makeAccountCopy
---------------

метод

описание

Ставит задание на создание копий всех баз и файлов домашней директории

возвращаемое значение

1 - успешно, 0 - ошибка

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"makeAccountCopy"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"106437688124080.TSBJcBGJTl"

"result":

1

}

restoreFiles
------------

метод

описание

Одиночные и массовые действия 'Восстановить' над файлами из бэкапа

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

date

string

Дата бэкапа (по сути это его папка на сервере, поэтому формат строгий)

files

array

Массив информации о файлах (в каждом элементе массив с 2мя значениями), которые нужно восстановить. files\[\]\[0\] - 0 или 1 (0 - файл; 1 - папка). Тип того, что требуется восстановить. files\[\]\[1\] - конкатенированные 'путь к директорию' и 'имя файла' (например, '/' и '.authfile'. Получится '/.authfile')

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"restoreFiles"

"params":{

"date":

"2023-02-27"

"files":\[

\[

0

"/test\_mysql57\_2023-06-07\_16-00.sql.gz"

\]

\]

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"234254631504176.TehDTtfptF"

"result":

1

}

downloadFile
------------

метод

описание

Скачивание одиночного файла из бэкапа

возвращаемые значения в свойствах элементов массива

'file':

'mimetype' string MIME-тип данных

'metadata' array Метаданные

'content' string Контент

'name' string Имя файла

параметры в запросе

date

string

Дата бэкапа (по сути это его папка на сервере, поэтому формат строгий)

files

array

Массив информации о файлах (в каждом элементе массив с 2мя значениями), которые нужно восстановить. files\[\]\[0\] - 0 или 1 (0 - файл; 1 - папка). Тип того, что требуется восстановить. files\[\]\[1\] - конкатенированные 'путь к директорию' и 'имя файла' (например, '/' и '.authfile'. Получится '/.authfile')

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"downloadFile"

"params":{

"date":

"2023-02-27"

"files":\[

\[

0

"/test\_mysql57\_2023-06-07\_16-00.sql.gz"

\]

\]

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"293633665527469.StHLFMChDX"

"result":\[

{

"file":{

"mimetype":

"application/gzip;base64"

"metadata":\[\]

"content":

"H4sICFd/gGQAA2xpbmExOTkzMDJfbXlzcWur/D1U9VJ6L377Gqp8KJUglL6Fql5J6uzOje3CFE+O4C++TqdBAwoAAA=="

"name":

"test\_mysql57\_2023-06-07\_16-00.sql.gz"

}

}

\]

}

getListFiles
------------

метод

описание

Метод для получения содержимого папки внутри бэкапа за конкретную дату

возвращаемые значения в свойствах элементов массива

'name' string Имя файла

'dir' bool

'size' string Размер

параметры в запросе

date

string

Дата бэкапа (по сути это его папка на сервере, поэтому формат строгий)

dir

string

Директория

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getListFiles"

"params":{

"date":

"2023-02-27"

"dir":

"/"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"983095020863527.hSRDcHiMYv"

"result":\[

{

"name":

".htaccess"

"dir":

false

"size":

"0 B"

}

{

"name":

"cgi-bin/"

"dir":

true

"size":

"4 KB"

}

{

"name":

"index.html"

"dir":

false

"size":

"309,89 KB"

}

\]

}

getListMysql
------------

метод

описание

Получение списка содержимого бэкапа баз данных за конкретный день

возвращаемые значения в свойствах элементов массива

'name' string Имя файла

'dir' bool

параметры в запросе

date

string

Дата бэкапа (по сути это его папка на сервере, поэтому формат строгий)

dir

string

Директория

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getListMysql"

"params":{

"date":

"2023-02-27"

"dir":

"/"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"014094846399709.xkVEogCXNF"

"result":\[

{

"name":

"test1234"

"dir":

true

}

\]

}

receiveFiles
------------

метод

описание

Одиночные и массовые действия 'Получить бэкап' над файлами из бэкапа

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

date

string

Дата бэкапа (по сути это его папка на сервере, поэтому формат строгий)

files

array

Массив информации о файлах (в каждом элементе массив с 2мя значениями), которые нужно восстановить. files\[\]\[0\] - 0 или 1 (0 - файл; 1 - папка). Тип того, что требуется восстановить. files\[\]\[1\] - конкатенированные 'путь к директорию' и 'имя файла' (например, '/' и '.authfile'. Получится '/.authfile')

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"receiveFiles"

"params":{

"date":

"2023-02-27"

"files":\[

\[

0

"/test\_mysql57\_2023-06-07\_16-00.sql.gz"

\]

\]

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"345992281852442.fMeOWgujMa"

"result":

1

}

receiveMysql
------------

метод

описание

Одиночные и массовые действия 'Получить бэкап' над одной или несколькими базами данных

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

date

string

Дата бэкапа (по сути это его папка на сервере, поэтому формат строгий)

databases

array

Массив с именами баз данных

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"receiveMysql"

"params":{

"date":

"2023-02-27"

"databases":\[

"test123"

\]

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"553530135046002.mluvgGNaRX"

"result":

1

}

restoreMysql
------------

метод

описание

Одиночные и массовые действия 'Восстановить' над таблицами и базами данных

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

date

string

Дата бэкапа (по сути это его папка на сервере, поэтому формат строгий)

databases

string

Имя базы данных

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"restoreMysql"

"params":{

"date":

"2023-02-27"

"databases":\[

"test123"

\]

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"186812255965976.zmoHKNoDBV"

"result":

1

}