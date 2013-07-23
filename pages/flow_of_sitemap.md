title: サイトマップの送信方法
date: 2013-07-24

このブログをGoogle Web Master Toolsを利用してサイトマップを送信してみた。

流れとしては

+ <a href="http://www.sitemapxml.jp/">サイトマップ自動生成ツール</a>利用して、sitemap.xmlを生成する。

+ flask でsitemap.xml　を返すようなプログラムを書く。

    @app.route("sitemap")
    def sitemap():
      return render_template("sitemmap.xml")

+ ウェブマスターツール -> クロール -> サイトマップの追加を行う。


以上でできた。簡単にできてよかった。
でも、render_template で xmlを返すことができるの知らなかったので勉強になった。

