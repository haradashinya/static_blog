title: シェルスクリプトの返り値を受け取る
date: 2013-07-15


解決したのでメモ。



    import subprocess

    # curl -i でurlの情報を取得する場合
    proc = subprocess.Popen(['curl','-i',url],cwd='/',stdout =
        subprocess.PIPE)
    out,err = proc.communicate()

