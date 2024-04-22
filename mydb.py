from band import Band 
from musician import Musician
from member import Member
from post import Post
from country import Country
from link import Link
from somepic import Somepic
from address import Address
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
