# Примеры использования API

Примеры использования API
=========================

*   PHP;
*   Python;
*   NodeJS.

PHP
---

Для запросов используется библиотека cURL.

    <?php
    
    $login = '<LOGIN>';
    $password = '<PASSWORD>';
    
    $headers = [
        'Content-Type: application/json; charset=utf-8',
        'Accept: application/json'
    ];
    
    // получение токена
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HEADER, false);
    curl_setopt($ch, CURLOPT_TIMEOUT, 15);
    curl_setopt($ch, CURLOPT_URL, "https://api.sweb.ru/notAuthorized/");
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode([
        'jsonrpc' => '2.0',
        'method' => 'getToken',
        'params' => [
            'login' => $login,
            'password' => $password
            ]
    ]));
    $result = json_decode(curl_exec($ch), true);
    curl_close($ch);
    $token = $result['result'];
    
    // пример вызова метода API с полученным токеном
    if ($token) {
        $headers[] = "Authorization: Bearer $token";
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HEADER, false);
        curl_setopt($ch, CURLOPT_TIMEOUT, 15);
        curl_setopt($ch, CURLOPT_URL, "https://api.sweb.rudomains/");
        curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode([
            'jsonrpc' => '2.0',
            'method' => 'move',
            'params' => [
                'domain' => 'mysite.ru',
                'prolongType' => 'no'
            ]
        ]));
        $result = json_decode(curl_exec($ch), true);
        curl_close($ch);
    }

Python
------

Для запросов используется библиотека requests.

    import requests
    import json
    
    # получение токена
    data = {
        'jsonrpc':'2.0',
        'method':'getToken',
        'params':{
            'login':'<LOGIN>',
            'password':'<PASSWORD>'
        }
    }
    headers = {
        'Content-Type':'application/json; charset=utf-8',
        'Accept':'application/json'
    }
    response = requests.post("https://api.sweb.ru/notAuthorized/", json=data, headers=headers)
    result = json.loads(response.text)
    
    # пример вызова метода API с полученным токеном
    if 'result' in result:
    
        headers['Authorization'] = 'Bearer ' + result.get('result')
        data = {
        'jsonrpc':'2.0',
        'method':'move',
        'params':{
                'domain':'mysite.ru',
                'prolongType':'no'
            }
        }
        response = requests.post("https://api.sweb.rudomains/", json=data, headers=headers)

NodeJS
------

Для запросов используется библиотека https.

    const https = require('https');
    
    let login = '<LOGIN>';
    let password = '<PASSWORD>';
    
    // получение токена
    let post_data = JSON.stringify({
        'jsonrpc':'2.0',
        'method':'getToken',
        'params':{
            'login': login,
            'password': password
        }
    });
    
    let post_options = {
        host: 'api.sweb.ru',
        port: 443,
        path: '/notAuthorized',
        method: 'POST',
        headers: {
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'application/json'
        }
    };
    let req = https.request(post_options, (res) => {
        let data = '';
        res.on('data', (chunk) => {
            data += chunk;
        });
    
        res.on('end', () => {
            let result = JSON.parse(data);
            // вызов метода API после получения токена
            result.result && move(result.result)
        });
    });
    req.write(post_data);
    req.end();
    
    // пример вызова метода API с полученным токеном
    const move = (token) => {
        let post_data = JSON.stringify({
            'jsonrpc':'2.0',
            'method':'move',
            'params':{
                'domain': 'mysite.ru',
                'prolongType': 'no'
            }
        });
    
        let post_options = {
            host: 'api.sweb.ru',
            port: 443,
            path: 'domains',
            method: 'POST',
            headers: {
                'Content-Type': 'application/json; charset=utf-8',
                'Accept': 'application/json',
                'Authorization': 'Bearer ' + token
            }
        };
        let req = https.request(post_options, (res) => {
            let data = '';
            res.on('data', (chunk) => {
                data += chunk;
            });
    
            res.on('end', () => {
                let result = JSON.parse(data);
            });
        });
        req.write(post_data);
        req.end();
    }