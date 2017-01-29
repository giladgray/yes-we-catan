import webapp2
# from flask import Flask
# app = Flask(__name__)
# app.config['DEBUG'] = True

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

app = webapp2.WSGIApplication([
    ('/', Hello),
    ], debug=True)

# @app.errorhandler(404)
# def page_not_found(e):
#     """Return a custom 404 error."""
#     return 'Sorry, nothing at this URL.', 404
