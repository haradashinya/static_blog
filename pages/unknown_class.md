title: Unknown class ModalViewController in Interface Builder file の解決
date: 2013-04-27

Storyboardを使ってViewControllerのSubClassしたModalViewControllerを
紐付けた時にタイトルのメッセージが表示されたのでメモ。


Build Phases -> Compile Sourcesに追加したViewControllerを追加
すると解決した。

