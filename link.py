# coding=utf-8
import sqlite3
import sys
import string
import random
import re
import requests
from model import Model
from post import Post
from somepic import Somepic
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup


class Link(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.dbPost=Post()
        self.cur.execute("""create table if not exists link(
        id integer primary key autoincrement,
        url text,
            shorturl text,
            div text,
            band_id text,
            user_id text,
            member_id text
                    );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from link")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from link where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def find_by_url(self,url="",user_id=""):
        self.cur.execute("select * from link where shorturl = ? and user_id = ?",(url,user_id))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        return row["div"]
    def getbyid(self,myid):
        self.cur.execute("select * from link where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def create(self,params):
        print("ok")
        myhash={}
        for x in params:
            if 'confirmation' in x:
                continue
            if 'envoyer' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                #print("my params",x,params[x])
                try:
                  myhash[x]=str(params[x].decode())
                except:
                  myhash[x]=str(params[x])
        print("M Y H A S H")
        print(myhash,myhash.keys())
        myid=None
        hey={}
        azerty={}
        try:
          self.cur.execute("insert into link (band_id,url,shorturl,div,user_id,member_id) values (:band_id,:url,:shorturl,:div,:user_id,:member_id)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
          #
          url = myhash["url"]
          req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

          webpage = urlopen(req).read()
          page_soup = soup(webpage, "html.parser")
          

          #

          div=""
          title=page_soup.find("title").get_text()
          print(title)
          if "#" in myhash["div"]:
            div = str(page_soup.find('div', id=myhash["div"].replace("#","")))
          elif "." in myhash["div"]:
            mydiv = page_soup.select(myhash["div"])
            for z in mydiv:
              div+=str(z)
          hey=Post().create({"title":title,"content":div,"band_id":myhash["band_id"],"user_id":myhash["user_id"]})
          azerty["post_id"]=hey["post_id"]
          images = page_soup.findAll('img')
          for image in images:
              src=image.attrs["src"]
              alt=""
              try:
                  alt=image.attrs["alt"]
              except:
                  alt=title
              if myhash["shorturl"] not in src:
                  src=myhash["shorturl"]+src
              N=10
              somename=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))+src.split("?")[0].split("/")[-1]
              print(somename)
              r = requests.get(src)
              fname="./uploads/"+somename
              open(fname , 'wb').write(r.content)
              newpic=Somepic().create({"title":alt,"post_id": hey["post_id"], "user_id": myhash["user_id"], "member_id":myhash["member_id"],"name":somename})
        except Exception as e:
          print("my error"+str(e))
        azerty["link_id"]=myid
        azerty["notice"]="votre link a été ajouté"
        return azerty
