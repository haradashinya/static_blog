# Static Blog


*  このウェブサイトを走らせるにはPython,Flaskが必要です。

## Motibation
I want to make a simple blogging system for me which  following the functonality ...


- It can edit my favorite editor by markdwn syntax.
- Syntax highlight.
-  Auto deployment .
- Hosted on static files to maintain it easily.



## This blog is powerd by
- Flask 
- Frozen-Flask
- Flask-FlatPages

## How to write a new post
+ Touch pages/hello.md
+ Edit it like this.

``` yaml
title: My Title 
date: 2013-01-03

body is here.
```

+ Highlight it.

```python
<pre><code data-language="python">
	def hello():
		print "hello"
</code></pre>
```


## Deploy it to the ec2-instance  via fabric
```
	fab push
```







