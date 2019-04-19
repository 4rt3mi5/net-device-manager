#!/usr/bin/env bash

function start_celery() {
    `cd ../ && celery multi start worker -A website -c 10 -l info --pidfile=/var/www/ndm/celery.pid --logfile=/var/www/ndm/celery.log`
    echo -e "\033[31m celery 开启成功 \033[0m"
}
function start_beat() {
    `cd ../ && celery beat -A website --pidfile=/var/www/ndm/beat.pid --logfile=/var/www/ndm/beat.log --detach`
    echo -e "\033[31m beat 开启成功 \033[0m"
}
function stop_celery() {
    `cd ../ && celery multi stop worker --pidfile=/var/www/ndm/celery.pid`
    echo -e "\033[31m celery 已停止 \033[0m"
}
function stop_beat() {
    `kill -9 $(cat /var/www/ndm/beat.pid)`
    echo -e "\033[31m beat 已停止 \033[0m"
}
case $1 in
  "start")
    start_celery
    start_beat
    ;;
  "stop")
    stop_celery
    stop_beat
    ;;
  *)
    echo "Usage $0 {start|stop}"
    ;;
esac
