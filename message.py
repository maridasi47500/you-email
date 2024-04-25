# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Message(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists message(
        id integer primary key autoincrement,
        'from' text,
            'sent' integer,
            envoyeremail string,
            'to' text,
            'object' text,
            content text
                    );""")
        self.con.commit()
        #self.con.close()
    def search(self,search,user_id):
        s="%"+search.replace(" ","%")+"%"
        t=search.split(" ")[0]
        self.cur.execute("select m.*, (address.name || ' &lt;' || address.email || '&gt;') myaddress,  m.content as mycontent, INSTR(lower(m.content), ?) position1, user.id as user_id, INSTR(lower(m.object),?) position2 from message m left join user on user.email = m.[from] or user.email = m.[to] left join address on address.email = m.[to] where lower(m.object) like ? or lower(m.content) like ? or lower(address.name) like ? or m.[from] like ? or m.[to] like ? and user.id = ?", (t,t,s,s,s,s,s,user_id))
        row=self.cur.fetchall()
        return row
    def getallrecu(self,hey):
        self.cur.execute("select * from message where [to] = (select email from user where user.id = ?) and envoyeremail = 'envoyer' and sent = 1", (hey,))

        row=self.cur.fetchall()
        return row
    def getallenvoye(self,hey):
        self.cur.execute("select * from message where [from] = (select email from user where user.id = ?) and envoyeremail = '1' and sent = 1", (hey,))

        row=self.cur.fetchall()
        return row
    def getallbrouillon(self,hey):
        self.cur.execute("select * from message where [from] = (select email from user where user.id = ?) and envoyeremail = '1' and sent = 0", (hey,))

        row=self.cur.fetchall()
        return row
    def getallsupprime(self,hey):
        self.cur.execute("select * from message where [from] = (select email from user where user.id = ?) and envoyeremail = '0'", (hey,))

        row=self.cur.fetchall()
        return row
    def getall(self):
        self.cur.execute("select * from message")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from message where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select message.*, (address.name || ' &lt;' || address.email || '&gt;') myaddress from message left join address on address.email = message.[to] where message.id = ? ",(myid,))
        row=dict(self.cur.fetchone())
        return row
    def create(self,params):
        print("ok PARMS=>>>>>",params)
        myhash={}
        for x in params:
            if 'confirmation' in x:
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
          self.cur.execute("insert into message (envoyeremail,sent,[from], [to],object,content) values (:envoyeremail,:sent,:from,:to,:object,:content)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["sent"]=params["sent"]
        azerty["envoyeremail"]=params["envoyeremail"]
        azerty["message_id"]=myid
        azerty["notice"]="votre message a été ajouté"
        return azerty
    def update(self,params):
        print("ok PARMS=>>>>>",params)
        myhash={}
        for x in params:
            if 'confirmation' in x:
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
          self.cur.execute("update message set envoyeremail = :envoyeremail,sent=:sent,[from]=:from, [to]=:to,object=:object,content=:content where id = :id",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["sent"]=params["sent"]
        azerty["envoyeremail"]=params["envoyeremail"]
        azerty["message_id"]=myid
        azerty["notice"]="votre message a été envoyé"
        return azerty





