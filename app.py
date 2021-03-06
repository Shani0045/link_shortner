from flask import*
from pyshorteners import Shortener
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/short_link",methods=["POST"])
def short_link():
    
    try:
        x=request.form['a']
        link=request.form['b']
        if link=="nullpointer":
            s=Shortener()
            q=s.nullpointer.short(x)
            return render_template("index.html",c=q)
        elif link=="tinyurl":
            s=Shortener()
            q=s.tinyurl.short(x)
            return render_template("index.html",c=q)
        elif link=="dagd":
            s=Shortener()
            q=s.dagd.short(x)
            return render_template("index.html",c=q)
        elif link=="isgd":
            s=Shortener()
            q=s.isgd.short(x)
            return render_template("index.html",c=q)
        elif link=="chilpit":
            s=Shortener()
            q=s.chilpit.short(x)
            return render_template("index.html",c=q)
        elif link=="osdb":
            s=Shortener()
            q=s.osdb.short(x)
            return render_template("index.html",c=q)
        elif link=="qpsru":
            s=Shortener()
            q=s.qpsru.short(x)
            return render_template("index.html",c=q)
        elif link=="bitly":
            s=Shortener(api_key="5b0366c4f79b0b7d1b1ca6e9aaf89c57fb0b115e")
            q=s.bitly.short(x)
            return render_template("index.html",c=q)

        elif link=="none":
            return render_template("index.html")
                     
    except:
        return render_template("index.html")

if __name__=="__main__":
    app.run()
