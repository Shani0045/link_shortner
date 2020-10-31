#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import*
from pyshorteners import Shortener
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/short_link",methods=["GET","POST"])
def short_link():
    s=Shortener()
    x=request.form['a']
    y=request.form['b']
    q=s.nullpointer.short(x)
    return render_template("index.html",c=q)
if __name__=="__main__":
	app.run()
