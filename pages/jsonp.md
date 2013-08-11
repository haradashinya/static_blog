title: Flaskでjsonpを使う
date: 2013-03-21
tags: python


複数のサーバーを通信させるスクリプトを
作るときに、jsonpを使用しないといけない。


jsonpify というものを使うと簡単に実装できた。

  from flask.ext.jsonify import jsonify


  ...

  jsonify(user="hello")

