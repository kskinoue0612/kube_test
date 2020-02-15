# README

以下を参考にした。

https://qiita.com/rsakao/items/617f54579278173d3c20

方針を変更。Minikube では Docker build が直接できることを利用。

https://qiita.com/ocadaruma/items/efe720e46ae7ecb9ec25

1. minikube docker-envを実行

```
SET DOCKER_TLS_VERIFY=1
SET DOCKER_HOST=tcp://192.168.99.100:2376
SET DOCKER_CERT_PATH=C:\Users\Keisuke Inoue\.minikube\certs
REM Run this command to configure your shell:
REM @FOR /f "tokens=*" %i IN ('minikube docker-env') DO @%i
```

Linux マシンに、.minikube\certs 以下をコピー
Linux マシンに Docker インストール

```
export DOCKER_TLS_VERIFY=1
export DOCKER_HOST=tcp://192.168.99.100:2376
export DOCKER_CERT_PATH=/home/kinoue/docker_certs
```

mkdir docker-test
cd docket-test
echo "FROM nginx" >> Dockerfile
docker build -t bri/nginx:v1.0 .

ビルドは成功した。
これで、実際に bri/nginx:v1.0 が使えるか試した。



