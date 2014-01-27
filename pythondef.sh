#!/bin/bash
for i in $(sudo find -type f -iname '*.py')
do
  echo "*****************" "$i"
  sudo cat "$i" | sed -n '/def /p' | sed -e "s/^ *//g" | sed -r "s/\t//ig"
done
