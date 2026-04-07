# Инструкция

*   [Инструкция](/instructions)
*   [Примеры использования API](examples)
*   Виртуальный хостинг
    *   [Сайты](vh/sites)
        indexgetSiteInfoaddeditdelchangeDomainSitegetBackEndsListchangeBackEnd
    *   [Базы данных](vh/hosting)
        databaseGetListdatabaseMysqlChangePassdatabaseMysqlCreatedatabaseMysqlImportdatabaseMysqlMakeCopydatabaseMysqlAccessListdatabaseMysqlAccessCreatedatabaseMysqlAccessDeletedatabaseMysqlDeletedatabasePgsqlCreatedatabasePgsqlDeletedatabasePgsqlChangePassdatabaseEditCommentgetPmaUser
    *   [Бэкапы](vh/backup)
        getListmakeAccountCopyrestoreFilesdownloadFilegetListFilesgetListMysqlreceiveFilesreceiveMysqlrestoreMysql
    *   [Почта](vh/mail)
        getDomainsListgetMailboxesListgetMailQuotacreateMboxsendRequisitesToEmaildropMboxupdateAntispamStateupdateCommentgetAutoreplychangeAutoreplychangeMailboxSpfchangeDomainSpfgetForwardingEmailsListaddForwardingEmailremoveForwardingEmailisEnabledDeletingAfterForwardingchangeDeletingAfterForwardinggetDeliveryAddressesListgetDeliveryInfoaddDeliveryAddressdropDeliveryAddressgetMailsCollectorchangeMailsCollectorremoveMailsCollectorconfirmMailsCollectorEmailchangeSenderVerifychangeAutoDiscoverdeleteMailschangeMailboxPasswordgetWhitelistgetBlacklistaddToWhitelistaddToBlacklistdropFromWhitelistdropFromBlacklistenableDkimdisableDkim
    *   [SSL](vh/ssl)
        indexgetOrderListdownloadeditAutoprolongremoveCertificategetProlongInfoprolongCertificateinstallLetsEncrypt
    *   [Тариф](vh/tariff)
        indexserverInfo
    *   [Нагрузка](vh/load)
        indexgetLoadTable
    *   [SSH](vh/utils)
        sshOnsshOff
    *   [Квота](vh/disk-usage)
        indexgetTasksInfostartTaskgetEmailchangeEmail
    *   [Crontab](vh/cron)
        addTaskeditTaskremoveTaskgetTasks
    *   [DDG](vh/ddg)
        indexcountAllDomainsenabledisableenableInfopriceWidgetgetPrice
*   VPS
    *   [Управление VPS](vps/vps)
        indexgetFirstOrderInfocreateEnablegetAvailableConfigcopycreateFirstcreaterenameisRunningremoveremoveFirstloadgetConstructorPlanIdchangePlanpowerOnpowerOffrebootgetCurrentActionreinstallOslogs
    *   [Бэкапы](vps/backup)
        indexupdateIndexcreaterestoreattachdetachremovegetSettingssaveSettings
    *   [SSL](vps/ssl)
        indexgetOrderListdownloadeditAutoprolongremoveCertificategetProlongInfoorderSubmit
    *   [Локальная сеть](vps/ip)
        addLocalremoveLocal
    *   [IP-адреса](vps/protected-ip)
        indexgetAllIpListgetOrderInfoaddProtectedremoveProtectedupdateProtectedmoveProtectedaddaddLocalremoveLocalremovemoveeditPtrgetPtr
    *   [DBaaS](vps/dbaas)
        indexsetUpgradeAgreegetAvailableConfiggetConstructorPlanIdgetFirstOrderInforemoveFirstcreateInstanceeditInstanceremoveInstancedeleteDatabasevalidateUsers
    *   [Балансировщик](vps/balancer)
        indexisCreateEnablegetAvailableConfigcreateeditremove
    *   [Облачные бэкапы](vps/remote-backup)
        indexcreateeditCommentrestorerestoreIntoremove
    *   [Мониторинг](vps/monitoring)
        enabledisablechangeplans
    *   [Мониторинг. Проверки](vps/monitoring/checks)
        indexgetTypesgetIntervalsgetPortsgetKeywordModesgetInfogetFullCheckInfocreateeditactivateactivateListdeactivatedeactivateListremoveremoveListhistory
    *   [Мониторинг. Контакты](vps/monitoring/contacts)
        indexgetAllContactsaddContacteditContactaddEmaileditEmailaddPhoneeditPhonedeleteContactdeleteContactsaddTelegramrequestTelegramVerifyCodeisVerifiededitTelegramverifyContact
*   Домены
    *   [Домены](domains/domains)
        indexgetSubdomainsgetDomainInforegAvailablegetAvailablePackagesregListregmovemoveListchangeProlongchangeProlongListremoveremoveListprolongprolongListpriceForTrasferpriceForRegistrationremoveSubdomaincreateSubdomainsetRedirectVhgetRedirectVh
    *   [Доменные бонусы](domains/bonus)
        indexgetListbuy
    *   [Доменные персоны](domains/persons)
        indexgetinfocreateFizIpcreateJur
    *   [DNS](domains/dns)
        infoeditMxeditSrveditNSeditTxtgetFile

*   Оплата и финансы
    *   [Оплата и финансы](pay)
        indexisAutopaymentEnablegetPayRecommendationsgetRecommendationTotalCostgetUpcomingPaymentsVhchangeDefermentgetRemainsDategetRemainsDaysgetBalancegetActiveReserves

Инструкция по взаимодействию с API
==================================

актуальная версия используемой спецификации

JSON-RPC 2.0 [http://www.jsonrpc.org/specification](http://www.jsonrpc.org/specification)

Обращение к API метод
---------------------

Обращение к API происходит по протоколу HTTP/HTTPS и использует метод POST передачи данных в виде JSON. В самом запросе URI указывает на объект (класс), а тело запроса содержит метод этого класса и параметры вызова.  
  
Метод по умолчанию для всех объектов «index».

Получение токена для взаимодействия с API
-----------------------------------------

Для большинства запросов к API вам потребуется передавать токен, полученный после авторизации. Получить токен можно отправив следующий запрос на URL [https://api.sweb.ru/notAuthorized/](https://api.sweb.ru/notAuthorized/)

```json
{

"jsonrpc":

"2.0"

"method":

"getToken"

"params":{

"login":

"<ваш логин>"

"password":

"<ваш пароль>"

}
```

}

Где:

<ваш логин> — логин в Личный кабинет аккаунта

<ваш пароль> — пароль в Личный кабинет аккаунта

В ответе в параметре result придет токен, который нужно будет передавать при взаимодействии с API.

пример запроса

    curl -H 'Content-Type: application/json; charset=utf-8'
         -H 'Accept: application/json'
         --data '```json
{"jsonrpc":"2.0","method":"getToken","params":{"login":"LOGIN","password":"PASSWORD"}
```}'
         https://api.sweb.ru/notAuthorized/

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"20220505104244.40FxsQ16Ff"

"result":

"hdlhcdkd0bid6c29fhfu1s7123.202357ec-d5ca-4a0a-846c-2dabe0266ef4"

}
```

Пример формата запроса
----------------------

request URL

[https://api.sweb.rudomains/](https://api.sweb.rudomains/) (обращение к объекту класса Domains)

заголовки запроса

    Content-Type: application/json; charset=utf-8
    Accept: application/json
    Authorization: Bearer hdlhcdkd0bid6c29fhfu1s7123.202357ec-d5ca-4a0a-846c-2dabe0266ef4
    

Все запросы должны содержать заголовок с токеном авторизации (Autorization: Bearer <token>), кроме запросов к общедоступным методам [https://api.sweb.ru/notAuthorized/](https://api.sweb.ru/notAuthorized/)

POST данные в запросе

```json
{

"jsonrpc":

"2.0"

"method":

"move"

"params":{

"domain":

"vpstest.ru"

}
```

"id":

"20183994338.43VSEkfGFh"

"user":

"vhp\*\*\*\*"

}

описание параметров

jsonrpc — текущая версия JSON-RPC

version — текущая версия клиента приложения. Носит только информационный характер, используется в отчетах об ошибках

method — метод объекта Domains

params — объект параметров метода (ключ элемента объекта - имя параметра)

id — уникальный идентификатор запроса

user — логин пользователя, который отправляет запрос. Носит только информационный характер, сверяется со значением сессии токена и в случае расхождения приводит к ошибке авторизации

Параметр jsonrpc является обязательным. Если не передан id, то он будет сформирован на стороне API. Если не передан method будет вызван дефолтный метод для объекта.

Успешный ответ
--------------

В случае, если на стороне API не возникло ошибок возвращается результат работы вызванного метода в виде JSON.

пример ответа

```json
{

"jsonrpc":

"2.0"

"id":

"20183995523.MO4E9baKRr"

"result":{

"balance":{

"real\_balance":

500

"bonus\_balance":

0

}
```

}

}

описание параметров

jsonrpc — текущая версия JSON-RPC

version — текущая версия клиента

result — результат, который возвращает вызванный метод

id — уникальный идентификатор ответа, если был в запросе, то совпадает с ним

Все параметры в ответе являются обязательными.

Сообщение об ошибке
-------------------

В случае возникновения ошибок, ответ вместо параметра result будет содержать error с двумя значениями code и message.

пример ответа

```json
{

"jsonrpc":

"2.0"

"version":

"0.1"

"id":

"20183910121.UPNWsDxwmn"

"error":{

"code":

\-32601

"message":

"Object not found"

}
```

}

описание параметров

jsonrpc — текущая версия JSON-RPC

version — текущая версия клиента

error — объект ошибки, который содержит (code - код ошибки [http://xmlrpc-epi.sourceforge.net/specs/rfc.fault\_codes.php](http://xmlrpc-epi.sourceforge.net/specs/rfc.fault_codes.php) и message - текст ошибки)

id — уникальный идентификатор ответа, если был в запросе, то совпадает с ним

Все параметры в ответе являются обязательными.

Расширенное сообщение о результатах работы метода
-------------------------------------------------

Если метод кроме успешного или неуспешного результата должен передать клиенту какое-то кастомизированное сообщение или данные, то применяется общий тип ExtendedResult для таких ответов.

```json
{

"jsonrpc":

"2.0"

"id":

"20183995523.MO4E9baKRr"

"result":{

"extendedResult":{

"code":

1

"message":

"Заявка #180047823 принята в работу"

"data":\[\]

}
```

}

}

```json
{

"jsonrpc":

"2.0"

"id":

"20183995523.MO4E9baKRr"

"result":{

"extendedResult":{

"code":

0

"message":

"Зона .child не поддерживается для регистрации"

"data":\[\]

}
```

}

}

описание параметров extendedResult

code — 1 - успешное выполнение, 0 - ошибка

message — кастомизированное сообщение о результате

data — объект дополнительных данных (может быть пустым)