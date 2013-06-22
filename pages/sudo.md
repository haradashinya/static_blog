title: Python のスクリプトをどこでも実行する
date: 2013-02-17

こんなふうに書いて、
<pre>export PATH=/usr/local/bin:/usr/local/sbin:$PATH</pre>

こんなふうにしたらいけた。
<pre>
chmod +x /path/to/great.py

sudo ln -s /path/to/great.py /usr/local/sbin/great.py

</pre>



