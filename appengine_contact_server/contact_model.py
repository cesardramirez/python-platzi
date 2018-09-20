from google.appengine.ext import ndb  # ndb es un ORM.


class Contact(ndb.Model):  # La clase Contact extiende de ndb.Model
    name = ndb.StringProperty()
    phone = ndb.StringProperty()
    email = ndb.StringProperty()
