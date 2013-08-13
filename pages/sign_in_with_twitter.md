date: 2013-08-13
title: How to Sign in with Twitter using Flask
tags: python

Twitter でログイン認証をする必要性が出てきたので、最小限のコードを書いてみた。便利なので使いまわす。

		#!/usr/bin/env/python
		#coding: utf-8


		from flask import Flask,render_template,session
		from flask.ext.sqlalchemy import SQLAlchemy
		import flask
		from flask_oauth import OAuth
		from flask import redirect,request,url_for,flash
		from flask import redirect, url_for, session, request, flash, Blueprint, current_app
		from rauth.service import OAuth1Service
		from rauth.utils import parse_utf8_qsl

		twitter = OAuth1Service(
		    name='twitter',
		    base_url='https://api.twitter.com/1/',
		    request_token_url='https://api.twitter.com/oauth/request_token',
		    access_token_url='https://api.twitter.com/oauth/access_token',
		    authorize_url='https://api.twitter.com/oauth/authorize',
		    consumer_key='CONSUMER_KEY',
		    consumer_secret='CONSUMER_SECRET'
		    )

		request_token, request_token_secret = twitter.get_request_token(method='GET')
		app = Flask(__name__)

		@app.route("/index")
		def index():
		    return "hello world"



		@app.route('/login')
		def login():
		    token = request.args.get('oauth_token',None)
		    verifier = request.args.get('oauth_verifier', None)

		    if (token and verifier):
		        print 'TOKEN: ', token
		        print 'VERIFIER: ', verifier

		        resp =  twitter.get_access_token(
		            'POST',
		            request_token = request_token,
		            request_token_secret = request_token_secret,
		            data = {'oauth_verifier': verifier}
		        )

		        data = resp.content

		        access_token = data['oauth_token']
		        access_token_secret = data['oauth_token_secret']
		        return 'ACCESS_TOKEN: ' + access_token + ' | ACCESS_TOKEN_SECRET: ' + access_token_secret
		    else:
		        return redirect(url_for('progress'))


		@app.route('/progress')
		def progress():
		    authorize_url = twitter.get_authorize_url(request_token)
		    return redirect(authorize_url)
