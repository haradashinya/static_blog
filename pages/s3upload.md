title: Flaskを使ってクライアントサイドから直接Amazon S3にアップロード
date: 2013-09-12
tags: python,flask,s3

<a href="https://devcenter.heroku.com/articles/s3-upload-python">このリンクを読むのが手っ取り早い。かなり丁寧に説明されてる。</a>
ざっくりと手順を説明してみる。

### S3のサイトに行って、投げたいバケットのプロパティの箇所でCORSを編集する。

    <?xml version="1.0" encoding="UTF-8"?>
    <CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <CORSRule>
    <AllowedOrigin>yourdomain.com</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <AllowedMethod>POST</AllowedMethod>
    <AllowedMethod>PUT</AllowedMethod>
    <AllowedHeader>*</AllowedHeader>
    </CORSRule>
    </CORSConfiguration>

### s3-upload.jsを使う。


<a href="https://github.com/tadruj/s3upload-coffee-javascript">ここからダウンロード</a>


### HTML側はこんな感じ。

    <input type="file" id="file" onchange="s3_upload();"/>
    <p id="progress">Please select a file```</p>




### JS側はこんな感じ。

      $("#file").change(function(){
          var s3upload = new S3Upload({
            file_dom_selector: '#file',

            //put_s3のサーバーにリクエストを投げる。

            s3_sign_put_url:  'http://your_domain/put_s3',
            s3_object_name: '保存されるファイル名',
            onProgress: function(percent, message) {
              console.log("progress");
            },
            onFinishS3Put: function(url) {
              console.log("finish");
            },
            onError: function(status) {
              console.log(status);
            }
          });
      });

### Python側はこんな感じ。

    @bp.route("/put_s3")
        def sign_s3():
        AWS_ACCESS_KEY = "your access key"
        AWS_SECRET_KEY = "your secret key"
        S3_BUCKET = "your bucket name"
        object_name = request.args.get('s3_object_name')
        mime_type = request.args.get('s3_object_type')
        ext = mime_type.split("/")[1]

        myhash = random.getrandbits(128)
        hash_str = "%032x" % myhash
        f_name = "{0}_{1}.mp4".format(hash_str,object_name)

        # request が　タイムアウトすると動画をアップロードするのに失敗する。
        expires = int(time.time()+100*10000)

        amz_headers = "x-amz-acl:public-read"

        put_request = "PUT\n\n%s\n%d\n%s\n/%s/%s" % (mime_type, expires, amz_headers, S3_BUCKET, object_name)

        signature = base64.encodestring(hmac.new(AWS_SECRET_KEY,put_request, sha).digest())
        signature = urllib.quote_plus(signature.strip())

        url = 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET, object_name)

        return json.dumps({
        'signed_request': '%s?AWSAccessKeyId=%s&Expires=%d&Signature=%s' % (url, AWS_ACCESS_KEY, expires, signature),
        'url': url
        })


