#!/bin/bash
#
# chkconfig: - 85 15
# Description: Creates a swapfile
  
# source function library
. /etc/rc.d/init.d/functions

DEVICE=sdc
SWAPFILE=/mnt/${DEVICE}/root/swapfile.swp
MEMORY=$(grep MemTotal /proc/meminfo | awk '{ print $2 }')
SWAP=$(grep SwapTotal /proc/meminfo | awk '{ print $2 }')

[ -b /dev/${DEVICE} ] && INCREASE=$((${MEMORY} * 2)) || INCREASE=2097152

start() {
  echo -n $"Checking for existing swap"
  RETVAL=0
  success
  echo
  [ ${SWAP} -ne 0 ] && exit 0
 
  echo -n $"Checking for existing swapfile"
  [ ! -f ${SWAPFILE} ] && CREATE=1
  RETVAL=0
  success
  echo

  if [ ${CREATE} ]
  then
    echo -n $"Creating swapfile"
    mkdir -p ${SWAPFILE%/*}
    dd if=/dev/zero of=${SWAPFILE} bs=1kB count=${INCREASE} >/dev/null 2>&1
    RETVAL=$?
    [ ${RETVAL} -eq 0 ] && success && echo
    [ ${RETVAL} -eq 1 ] && failure && echo && exit 1
    
    echo -n $"Executing mkswap"
    mkswap ${SWAPFILE} >/dev/null 2>&1
    RETVAL=$?
    [ ${RETVAL} -eq 0 ] && success && echo 
    [ ${RETVAL} -eq 1 ] && failure && echo && exit 1
  fi

  echo -n $"Enabling swapfile"
  swapon ${SWAPFILE} >/dev/null 2>&1
  RETVAL=$?
  [ $RETVAL -eq 0 ] && success || failure
  echo
}

stop() {
  echo -n $"Disabling swapfile"
  if [ ${SWAP} -eq 0 ]
  then
    RETVAL=0
    success
    echo
  else
    if [ -f ${SWAPFILE} ]
    then
      swapoff $SWAPFILE
      RETVAL=$?
    else
      RETVAL=0
    fi
    [ $RETVAL -eq 0 ] && success || failure
    echo
  fi
}

case "$1" in
  start)
    start
    ;;
  stop)
    stop
    ;;
  restart)
    stop
    start
    ;;
  *)
    echo "Usage: /etc/init.d/swapfile {start|stop|restart}"
    exit 1
    ;;
esac

exit 0

