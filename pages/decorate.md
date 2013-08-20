title: Pythonのdecoratorを使う。
date: 2013-08-20
tags: python,flask

ケースとしてログインしたユーザーにだけ、見せたい情報があって、それ以外の人が訪れた場合は、ログインしてくださいみたいなメッセージを表示する時にdecoratorは便利。


##Code

	def login_required(func):
	    def inner(*args,**kwargs):
	        if request.method == "GET":
	            if session.get("current_user") is None:
	                flash(u"ログインしてください")
	                return redirect("/")
	            else:
	                return func(*args,**kwargs)
	        else:
	            return func(*args,**kwargs)
	    return inner


##How to Use

	# if user hasn't logined yet, then redirect("/").

	@app.route("/secret")
	@login_required
	def secret():
		return "your password!!"