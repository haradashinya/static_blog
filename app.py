from flask import Flask,render_template,redirect,url_for
from flask_flatpages import FlatPages,pygments_style_defs
import feedformatter,time
import feedgenerator
import datetime

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = ".md"

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)


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










@app.route("/")
def index():
    sorted_pages = sorted(pages,reverse=True,
    key = lambda p: p.meta["date"] )

    return render_template("hello.html",pages=sorted_pages[0:20])

@app.route("/<path:path>/")
def page(path):
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





if __name__ == "__main__":
    app.debug=True
    app.run(port=5000)

