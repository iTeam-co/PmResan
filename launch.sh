THIS_DIR=$(cd $(dirname $0); pwd)
cd $THIS_DIR

update() {
  git pull
  git submodule update --init --recursive
}
install() {
  apt-get install python3-pip
  pip3 install pytelegrambotapi
  pip3 install pytelegrambotapi --upgrade
  pip3 install redis
}
iteam () {
f=3 b=4
for j in f b; do
  for i in {0..7}; do
    printf -v $j$i %b "\e[${!j}${i}m"
  done
done
bld=$'\e[1m'
rst=$'\e[0m'
clear
cat << EOF
 $bld$f1▄ ▀▄   ▄▀ ▄   $f2 ▄▄▄████▄▄▄    $f3  ▄██▄     $f4▄ ▀▄   ▄▀ ▄$rst
 $bld$f1█▄█▀███▀█▄█   $f2███▀▀██▀▀███   $f3▄█▀██▀█▄   $f4█▄█▀███▀█▄█$rst
 $bld$f1▀█████████▀   $f2▀▀▀██▀▀██▀▀▀   $f3▀▀█▀▀█▀▀   $f4▀█████████▀$rst
 $bld$f1 ▄▀     ▀▄    $f2▄▄▀▀ ▀▀ ▀▀▄▄   $f3▄▀▄▀▀▄▀▄   $f4 ▄▀     ▀▄ $rst
EOF
echo "______________________________________________________________"
echo -e "\e[0;36m _ _____\e[0m"
echo -e "\e[1;37m(_)_   _|__  __ _ _ __ ___\e[0m"
echo -e "\e[0;33m| | | |/ _ \/ _| | '_ _ _ \\"
echo -e "\e[0;32m| | | |  __/ (_| | | | | | |\e[0m"
echo -e "\e[0;35m|_| |_|\___|\__,_|_| |_| |_|\e[0m"
echo "______________________________________________________________"
cat << EOF
 $bld$f1▄ ▀▄   ▄▀ ▄   $f2 ▄▄▄████▄▄▄    $f3  ▄██▄     $f4▄ ▀▄   ▄▀ ▄$rst
 $bld$f1█▄█▀███▀█▄█   $f2███▀▀██▀▀███   $f3▄█▀██▀█▄   $f4█▄█▀███▀█▄█$rst
 $bld$f1▀█████████▀   $f2▀▀▀██▀▀██▀▀▀   $f3▀▀█▀▀█▀▀   $f4▀█████████▀$rst
 $bld$f1 ▄▀     ▀▄    $f2▄▄▀▀ ▀▀ ▀▀▄▄   $f3▄▀▄▀▀▄▀▄   $f4 ▄▀     ▀▄ $rst
EOF
}
if [ "$1" = "install" ]; then
  iteam
  install
elif [ "$1" = "update" ]; then
  iteam
  update
else
  iteam
  if [ ! -f ./bot.py ]; then
    echo -e "\e[0;36msource not found\e[0m"
    exit 1
  fi
  while true; do
   python3.4 bot.py
   sleep 3
  done
fi
