import view
import webapp2

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

class Hello(webapp2.RequestHandler):
  def get(self):
    """Return a friendly HTTP greeting."""
    return_val = """
{ "tiles": [ [ {"resource": "WHEAT", "number_token": 5},
           {"resource": "SHEEP", "number_token": 2},
           {"resource": "DESERT"} ],
         [ {"resource": "WOOD", "number_token": 8},
           {"resource": "STONE", "number_token": 10},
           {"resource": "BRICK", "number_token": 9},
     {"resource": "WOOD", "number_token": 6} ],
   [ {"resource": "WHEAT", "number_token": 4},
     {"resource": "BRICK", "number_token": 3},
     {"resource": "SHEEP", "number_token": 11},
     {"resource": "ORE", "number_token": 4},
     {"resource": "WHEAT", "number_token": 3} ],
   [ {"resource": "SHEEP", "number_token": 11},
           {"resource": "ORE", "number_token": 6},
           {"resource": "BRICK", "number_token": 5},
           {"resource": "WOOD", "number_token": 8} ],
         [ {"resource": "WOOD", "number_token": 12},
           {"resource": "SHEEP", "number_token": 9},
           {"resource": "WHEAT", "number_token": 10} ] ],
  "ports": [ "ANY", "ANY", "BRICK", "WOOD", "ANY", "WHEAT", "STONE", "ANY", "SHEEP" ],
  "id": 1234
}"""
    self.response.headers['Content-Type'] = 'application/json'
    self.response.write(return_val)

class GraphTile(object):
  neighbor_n = None
  neighbor_ne = None
  neighbor_se = None
  neighbor_s = None
  neighbor_sw = None
  neighbor_nw = None

  resource = None
  number_token = None
  is_port = None

class Generate(webapp2.RequestHandler):
  def get(self):
    board = self.GenerateBoard()
    self.response.headers['Content-Type'] = 'application/json'
    self.response.write(view.RenderBoard(board))

app = webapp2.WSGIApplication([
    ('/', Hello),
    ('/generate', Generate),
    ], debug=True)
