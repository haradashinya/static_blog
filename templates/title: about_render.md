title: jinja2_tips1
date: 2013-07-


#問題

子供のテンプレートから、親のテンプレートに引数を渡したい時の対処法。


#解決策

	{% with <tit></tit>le= page.title %}
	{% include "base.html" %}
	{% endwith %}




