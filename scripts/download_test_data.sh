#!/usr/bash
cwd="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
datapath="$cwd/../dataset/test/"
mkdir -p $datapath

echo -n "Download data [y/N]?"
read yesorno
case $yesorno in 
  y | Y ) 
    echo '[INFO] Downloading ...';
    scp chuan@miaopdv.ipe.kit.edu:/home/chuan/DATA/kitcube_test/*tar.gz $datapath;;
  n | N | '' ) 
    echo '[INFO] No data downloaded';;
  * )
    echo '[ERRO] What? Exiting...';
    exit;;
esac

for file in $datapath/*tar.gz; do
  if [[ -f $file ]]; then
    tar xzf $file -C $datapath
  fi
done
