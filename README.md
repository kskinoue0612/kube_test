# README

Minkube を使って、以下の方法について確認する。

* batch Job をいくつか流す

* Web API から Jobの一覧を、 labelなどで絞り込んで一覧表示する
* Python からJob の一覧を、label などで絞り込んで一覧表示する
* メモに従って、all mignty な権限を作ってその権限で Pod を起動し、 Pod の内側から Jobの一覧を表示する。

現在動いている Pod 一覧は以下で見られる

kubectl get pods --field-selector=status.phase=Running

# 高い権限の作成

