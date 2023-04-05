# 0x0E. SQL - More queries

## General
* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* What’s a PRIMARY KEY
* What’s a FOREIGN KEY
* How to use NOT NULL and UNIQUE constraints
* How to retrieve datas from multiple tables in one request
* What are subqueries
* What are JOIN and UNION

## Comments for your SQL file:
```sh
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

## Install MySQL 5.7 on Ubuntu 14.04 LTS
```sh
$ echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
$ sudo apt-get update
$ sudo apt-get install mysql-server-5.7
...
$ mysql --version
mysql  Ver 14.14 Distrib 5.7.8-rc, for Linux (x86_64) using  EditLine wrapper
$
```

Don’t forget your root password

If you had before MySQL 5.5 installed, please run these 2 commands after the installation of the version 5.7:

```sh
$ mysql_upgrade -u root -p
Password: 
$ sudo service mysql restart
```

If you have some issues to upgrade to 5.7, don’t hesitate to cleanup your server of any MySQL packages:
```sudo apt-get remove --purge mysql-server mysql-client mysql-common```