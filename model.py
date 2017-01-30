import ndb.model

class Resource(messages.Enum):
  UNKNOWN = 0
  ANY = 1
  BRICK = 2
  DESERT = 3
  GRAIN = 4
  SHEEP = 5
  STONE = 6
  WHEAT = 7
  WOOD = 8

class Rating(messages.Enum):
  UNKNOWN = 0
  BAD = 100
  NEUTRAL = 500
  GOOD = 900

class Tile(ndb.Model):
  resource = ndb.EnumProperty(Resource, required=True)
  number_token = ndb.IntegerProperty()
  position_x = ndb.IntegerProperty()
  position_y = ndb.IntegerProperty()

class Port(ndb.Model):
  resource = ndb.EnumProperty(Resource, repeated=True)
  # If the port is a 3:1 port, then ratio_numerator is 3.
  ratio_numerator = ndb.IntegerProperty(required=True)

class PlayerFeedback(ndb.Model):
  score = ndb.IntegerProperty(required=True)
  overall_rating = ndb.EnumProperty(Rating, required=True)
  comment = ndb.TextProperty()
 
class Board(ndb.Model):
  created = ndb.DateTimeProperty(auto_now_add=True, required=True)
  size = ndb.IntegerProperty(required=True)
  tiles = ndb.KeyProperty(Tile, repeated=True)
  port = ndb.KeyProperty(Port, repeated=True)
  feedback = ndb.KeyProperty(PlayerFeedback, repeated=True)

