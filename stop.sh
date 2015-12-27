#!/bin/sh

PIDFILE=kippo.pid

cd $(dirname $0)

PID=$(cat $PIDFILE 2>/dev/null)

if [ -n "$PID" ]; then
  echo "Stopping kippo...\n"
  kill -TERM $PID
fi

PIDFILE2=http.pid

cd $(dirname $0)

PID=$(cat $PIDFILE2 2>/dev/null)

if [ -n "$PID" ]; then
  echo "Stopping webUI...\n"
  kill -TERM $PID
fi
