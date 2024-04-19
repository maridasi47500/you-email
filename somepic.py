# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Somepic(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists somepic(
        id integer primary key autoincrement,
        member_id integer,
            name text,
            title text,
            post_id integer,
            user_id integer
                    );""")
        self.con.commit()
        #self.con.close()
    def findallpicpost(self,wow):
        self.cur.execute("select * from somepic where post_id = ?",(wow,))

        row=self.cur.fetchall()
        return row
    def getall(self):
        self.cur.execute("select * from somepic")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from somepic where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from somepic where id = ?",(myid,))
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
        try:
          self.cur.execute("insert into somepic (title,member_id,name,post_id,user_id) values (:title,:member_id,:name,:post_id,:user_id)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["somepic_id"]=myid
        azerty["notice"]="votre somepic a été ajouté"
        return azerty




