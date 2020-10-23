Установка Coturn Amazon Linux OS:

Приложение развернуто за путем `/opt/turn/`
Конфигурационный файл сервиса рассположена за путем `/etc/coturn/`

*Установка в ручную*:

__Системные пакеты:__

- `yum update -y`
- `yum install -y gcc make openssl-devel libhiredis-devel libevent-devel`

__Сбор исходников:__

- скачать исходный код пакета (https://coturn.net/turnserver/v4.5.1.3/turnserver-4.5.1.3.tar.gz)
- `mkdir -p /opt/turn && cd /opt/turn`
- `tar -xzf turnserver-4.5.1.3.tar.gz`
- `cd turnserver-4.5.1.3`
- `./configure`
- `make && make install`

После успешного установления появить исполняемый файл сервера за путем `/opt/turn/turnserver-4.5.1.3/bin/turnserver`
`/opt/turn/turnserver-4.5.1.3/bin/turnserver -c /etc/coturn/turnserver.conf`


_Установка с помощью ansible_:

__Системные пакеты:__

- `yum update -y`
- `yum install -y python3-pip git`
- `pip3 install ansible==2.9.11`
- `git clone https://github.com/sasha-kantoriz/coturn.git`
- `cd coturn`

- В файле _hosts.ini_ указываем нужные хосты
- Темплейт конфига находится за путем _roles/coturn/templates/turnserver.conf_
- В файле _roles/coturn/defaults/main.yml_ устанавливаем значение переменных конфига сервиса
- Также переменные можно задавать безпосредственно в файле playbook'a `coturn.yml`
- `ansible-playbook coturn.yml`


 __Работа с сервисом:__

- Установка вручную (1-й способ) имеет результатом выполняемый файл сервиса
- Установка ansible (2-й способ) имеет результатом системный сервис TURN/STUN server'a `coturn`
- После успешного выполнения установки вторым из указаных способо проверяем работу сервиса:
`sudo systemctl status coturn`
- Выполняем команду в случае обновления конфига или неполадок сервиса `sudo systemctl restart coturn`
- `sudo systemctl start/stop coturn` - для вкл/выкл сервиса TURN/STUN 
