date: 2013-07-27
title: Sublime Text3を導入してみた
memo: true
tags: sublime

今までVimを使っていたけど、思い切ってSublime Text3を導入してみた。理由はもう歳なのでVimのプラグインを入れてコンフリクトしたりするのを修正するような細かい環境構築の作業が面倒だと思うようになってきたから。




Sublime なら、環境構築が簡単で結構なんとでもなりそう。
とりあえず現段階のカスタマイズしたキーマップはこんな感じ。

	[
	{ "keys": ["super+shift+r"], "command": "goto_symbol_in_project" },
	{ "keys": ["super+alt+up"], "command": "jump_back" },
	{ "keys": ["super+alt+n"], "command": "toggle_side_bar" },

		{ "keys": ["super+right"], "command": "focus_neighboring_group" },
		{ "keys": ["super+left"], "command": "focus_neighboring_group", "args": {"forward": false} },


		]


***
## よく使うショートカットキー達
***

###サイドバーの切り替え
cmd + alt + n

###定義元にジャンプ
cmd + alt + down


###定義もとに戻る
cmd + alt + up



###プロジェクト内の関数を探す。
cmd + shift + r



### 分割画面

cmd + -> : 次の画面

cmd + -> : 前の画面

cmd + alt + 1 : １画面に分割

cmd + alt + 2 : 1行2列に分割


これだけで随分使いやすくなったし、だいたいは不満ないと思う。

