from band import Band 
from musician import Musician
from member import Member
from post import Post
from country import Country
from link import Link
from somepic import Somepic
from user import User
from address import Address
from message import Message 
class Mydb():
  def __init__(self):
    self.Link=Link()
    self.Address=Address()
    self.Member=Member()
    self.Post=Post()
    self.Country=Country()
    self.Musician=Musician()
    self.Band=Band()
    self.Somepic=Somepic()
    self.User=User()
    self.Message=Message()
