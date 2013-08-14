date: 2013-08-15
title: Flask-SQLAlchemyを使ってモデルを複数ファイルに分ける方法
tags: python,flask,sqlalchemy

Flask-SQLAlchemyはとても便利なものだと思うけど,どのサンプルもmodels.pyに複数のclassを書いていて、
ちょっとでも太ったモデルを書こうとしたら、すぐに破綻してしまう。これを克服するために色々と調べてみたら、
SQLAlchemy()オブジェクトをシェアするようなモジュールを作るといいみたい。


##例

models/shared.py
models/user.py
models/video.py

みたいにする。shared.pyの中には、


	from flask.ext.sqlalchemy import SQLAlchemy
	from app import app

	app = app
	db = SQLAlchemy()

と書いて、user.pyの中には

	from models.shared import base,db,app

	class User(db.Model):
	    __tablename__ = "users"
	    id = db.Column(db.Integer,primary_key=True)
	    name = db.Column(db.String,unique=True)
	    tags = db.relationship("Tag",backref="user")
	    def __init__(self,name):
	        self.name = name

同じように,video.pyの中には

	from models.shared import base,db,app

	class Video(db.Model):
		__tablename__ = "videos"
	...


と書けば問題が解決した。これでだいぶスッキリした。












