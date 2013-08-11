title: Python3+Flaskでファイルを保存する
date: 2013-07-07
tags: python,flask

flask+Python3で画像をformタグから取得する方法を調べて解決できたのでメモ。

### html
      <form action = 'post_room' method='post' enctype='multipart/form-data'>
        <p>
          <h4>画像</h3>
          <input type='file' name='file'>
        </p>

        <input type='submit' value='投稿する' class='button'></input>
      </form>



### app.py 

    @app.route("post_room")
    def hoge():
        if request.method == "POST":
           _file = request.files['file']
           filename = secure_filename(_file.filename)

            path = os.path.join(app.config['UPLOAD_FOLDER'],filename)

            # save file to path
            _file.save(path)

<br>
Python3ってまだまだ使えないライブラリがたくさんある。でも、バッテリー内臓の感じがあるし、今の自分にとっては便利なライブラリーに頼リ過ぎない感じになっていくのも大事なことだと思う。
