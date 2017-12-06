#!/bin/ash

set -e

docker run -p 80:80 -v /var/run/docker.sock:/var/run/docker.sock --name server --rm -d $@
function kill {
    docker container kill server
}
trap kill EXIT

IPAddress=""

while [ "$IPAddress" = "" ];
do
    sleep 0.5
    IPAddress=$(docker inspect server --format '{{ .NetworkSettings.IPAddress }}')
    echo $IPAddress
done

echo "Run tests"
python3 run.py http://"$IPAddress"
