title: Amazon S3を簡単に扱えるようにするプログラムを書いた
tags: python,s3
date: 2013-09-27

Amazon S3はすごい便利なものだと思う。Dropboxだと容量の制限もあったりして
いつもいつも便利なわけではない。一方でS3はDropboxみたいに容量を気にせずに使えるのですごい便利。

今回はコマンドラインで自分のローカルのファイルをS3に投げたり、消したり、一覧を見たりするプログラムを書いた。
とはいっても、botoというすごいライブラリの上に乗りまくっていて、実際はちょっと整形しただけなんだけど。
でも、<a href="https://github.com/okamurayasuyuki/s3">僕がスタバで書いたライブラリ</a>を使うとすごく簡単にs3周りを操作できる。



使い方はとても簡単。

##使い方

最初に

    git clone https://github.com/okamurayasuyuki/s3
    cd /path/to/s3
    python gen.py

をタイプして、config.jsonを作ってあげる。すると、config.jsonの中にAWS_SECRET_KEY,AWS_ACCESS_KEY,BUCKET_NAMEの項目をを入力する。

あとは、

    python s3.py put|clone|delete filename
    python s3.py show

とかしたら便利。


