title: AndroidでHTTP通信するとき
date: 2013-03-21


メインスレッドでHTTP通信を行うと、その間メインスレッドをぶろっきんぐしてしまうので、Async を継承したクラスを作成して,doInBackgroundメソッドの中で処理をする。
またUIに結果を反映する時は、onPostExecuteメソッド内で返さないといけない。


iPhoneアプリ開発と事情が違ってかなりハマった。。。


