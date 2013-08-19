title: 日付順に要素を並べる
date: 2013-08-19
tags: "python"

複数のデータが入っている中で、データのキー順に並べることがしたかったのでメモ。

	sorted(items,key = lambda item: item[key])

で並べれることがわかった。


	users = []

	user0 = {
	        "name":"foo",
	        "date":"2013-08-04"
	        }

	user1 = {
	        "name":"foo",
	        "date":"2013-08-01"
	        }

	user2 = {
	        "name":"foo",
	        "date":"2013-08-03"
	        }

	names = "user0 user1 user2".split()

	for name in names:
	    user = locals().get(name)
	    users.append(user)


	print sorted(users,key = lambda user: user["date"])


ちなみに locals()でローカル変数をdict形式で取得できる。なので、

	locals().get("foo")　

みたいにすると、ローカル変数にアクセスできる。これを使って文字列から変数にアクセスできて便利。

