date: 2013-06-18
title: Sign in with Facebook by Python3
tags: python


FlaskがPython3に対応したので、早速アップグレードした。

Facebookで認証させる必要のアプリがあったので、便利な認証系のライブラリを探していたんだけど、
見つからなかったので、oauthの仕組み（まだよくわかっていない)を学んでとりあえず無事に動いたのでメモ。

まず、手順として、

1.Facebookアプリに登録して、アプリケーションIDを手に入れる。

2.アプリケーションID(client_id)、リダイレクト先のURLを書いたurl(http://localhost:5000/posted)にリダイレクト。

  http://www.facebook.com/dialog/oauth/?client_id=%s&redirect_uri=http://localhost:5000/posted&scope=email&state=RANDOM_NUMBER_PREVENT_CSRC&response_type=code

3.リダイレクト先で,手に入ったcodeの文字列を使用してユーザー情報を手に入れる。

client_id,http://localhost:5000/posted,secret_keyをhttps://graph.facebook.com/oauth/access_tokenにクエリーとして渡してGETアクセスすると、
json形式でログインしたユーザー情報が手に入る。


模擬コードはこんな感じ。
<script src="https://gist.github.com/okamurayasuyuki/5805672.js"></script>







