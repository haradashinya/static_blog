title: jinja templateのescapeを無効化
date: 2013-07-13
tags: python

最近は<a href="http://jinja.pocoo.org/">Jinjaテンプレート</a>にお世話になっているのだけど、auto escape絡みでいつもハマるのでメモ。



  {{page.body|safe }



でhtmlを埋め込むことが安心して出来ます。

