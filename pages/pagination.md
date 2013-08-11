title: paginationというライブラリを作った
date: 2013-08-06
tags: python

<a href="https://github.com/okamurayasuyuki/pagination">pagination</a>というライブラリを作った。

複数の動画をペジネーションする際のアルゴリズムを考えなければならなかったので、
実装した。今までの自分だったら実装できていなかったと思うぐらいの難易度だけど、
無事に実装できてよかった。

paginationの使い方は簡単で、


使い方はREADME.mdを見てくれたらわかってくれると思う。

例えば、1000個のブログ記事があって、ページは10ページに分け,左端、右端に5つずつ表示させる。
この時の94ページ目のペジネーションの状態を求める。


出力はこんな感じ。

	[1, 2, 3, 4, 5, '..', 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, '..', 96, 97, 98, 99, 100]


上の状態を再現するためには以下の様なコードを書く。

	items = [item for item in range(0,1000)]

	pagination = Pagination(items,10)

	# 右、左端に５個表示
	pagination.limit = 5

	pagination.set_idx(94)


	if pagination.has_prev() and pagination.has_next():
	    print pagination.show_iter()
	else:
	    print "out of range"

次のページを表示させたい場合は,

	pagination.set_idx(95)

みたいにすればいいと思う。多分ちゃんと動いている。




