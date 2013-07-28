title: 子供のテンプレートから、親のテンプレートに引数を渡したい時の対処法。
date: 2013-07-28

ブログ記事に使用されていた"page.html"のタイトルを"base.html"のtitleタグに入れたかったのでメモ。

##解決策
----

	{% with <tit></tit>le= page.title %}
	{% include "base.html" %}
	{% endwith %}


----

今までブログの記事が全然引っかかってこなかったので、これで少しは引っかかるように
なるはず。