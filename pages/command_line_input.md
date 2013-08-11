title: シェルスクリプトの返り値を受け取る
date: 2013-07-15
tags: python,dev

解決したのでメモ。



    import subprocess

    proc = subprocess.Popen(['curl','-i',url],cwd='/',stdout =
        subprocess.PIPE)

    # outに出力結果が表示される。

    out,err = proc.communicate()

Pythonは標準ライブラリを使ったサンプルが簡単に見つかるのがいいところだと思う。



