#!/bin/sh
if [ -z "$1" ]; then
  echo "Specify day number." >&2
  exit 1;
fi


DAY=$1
LDAY=$(echo "0${DAY}" | sed 's#^.*\(..\)$#\1#')
DIR="day${LDAY}"
if [ ! -d "${DIR}" ]; then
  mkdir "${DIR}"
fi;

COOKIE=$(cat cookie)
curl -v -b "session=${COOKIE}" "https://adventofcode.com/2020/day/${DAY}/input" -o "${DIR}/input"
