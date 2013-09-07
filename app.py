#coding: utf-8
import os
from flask import Flask,render_template,redirect,url_for
from flask_flatpages import FlatPages,pygments_style_defs
from flask import g
import feedformatter,time
import feedgenerator
import datetime




DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = ".md"

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)

def title(title = None):
	if title is None:
		return 'none'
	return title

@app.route("/sitemap")
def sitemap():
    return render_template("sitemap.xml",pages=pages)

@app.route("/memo/detail/")
def memo():
    sorted_pages = sorted(pages,reverse=True,
    key = lambda p: p.meta["date"] )
    for page in sorted_pages:
        if page.meta.get("memo"):
            print "exists"
    memo_pages = [page for page in sorted_pages if page.meta.get("memo")]
    return render_template("all.html",pages=memo_pages)

@app.route("/rss")
def rss():
    feed = feedgenerator.Rss201rev2Feed(
            title = u"Pickalize",
            link = u"http://pickalize.info",
            feed_url = u"http://pickalize.info/rss",
            description = u"",
            author_name = u"pickalize",
            pubdate = datetime.datetime.utcnow()
            )
    for e in sorted(pages,reverse = True,key = lambda p: p.meta["date"]):
        feed.add_item(
                title = u'%s' % e.meta['title'],
                link = u'http://pickalize.info/' + e.path,
                description =  e.body.encode('utf-8'),
                pubdate = e.meta['date']
                )

    return feed.writeString('utf-8')
@app.route("/tags/<name>")
def tags(name):
    tag_page = [page for page in pages if page.meta.get("tags") is not None]
    res = []
    for page in tag_page:
        if name in page.meta.get("tags").split(","):
            res.append(page)


    sorted_pages = sorted(res,reverse=True,
    key = lambda p: p.meta["date"] )
    return render_template("all.html",pages=sorted_pages)


@app.route("/archive")
def archive():

    sorted_pages = sorted(pages,reverse=True,

    key = lambda p: p.meta["date"] )
    return render_template("all.html",pages=sorted_pages)


app.jinja_env.globals['title'] = title

@app.route("/")
def index():

	sorted_pages = sorted(pages,reverse=True,
		key = lambda p: p.meta["date"] )

	return render_template("hello.html",pages=sorted_pages[0:20],page = None)
    # http://pickalize.info/sublime_setting/detail/

# render detail view
@app.route("/<path:path>/detail/")
def d(path):
	page = pages.get_or_404(path)
	title = u"%s" % page.meta["title"]
	app.jinja_env.globals['title'] = title
	page.meta["path"] = path
	return render_template('page.html', page=page,title=title)

@app.route("/<path:path>/")
def detail(path):
    page = pages.get_or_404(path)
    page.meta["path"] = path
    return render_template('page.html', page=page)

@app.route("/apps")
def apps():
    return render_template("apps.html")

@app.route("/product")
def product():
    return render_template("product.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

# show other scripts
@app.route("/scripts")
def scripts():
    return render_template("scripts.html")



