import json
import view
import webapp2


# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


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

  def GetResourceShort(self):
    return self.resource[0:2] if self.resource else "  "

  def GetTwoDigitNumber(self):
    return "%s%s" % (self.number_token if self.number_token else " ",
                     " " if self.number_token < 10 else "")

  def __str__(self):
    return """
         %s
         --
    %s / %s \ %s
    %s \ %s / %s
         --
         %s
    """ % (self.neighbor_n.GetResourceShort() if self.neighbor_n else "  ",
           self.neighbor_nw.GetResourceShort() if self.neighbor_nw else "  ",
           self.GetResourceShort(),
           self.neighbor_ne.GetResourceShort() if self.neighbor_ne else "  ",
           self.neighbor_sw.GetResourceShort() if self.neighbor_sw else "  ",
           self.GetTwoDigitNumber(),
           self.neighbor_se.GetResourceShort() if self.neighbor_se else "  ",
           self.neighbor_s.GetResourceShort() if self.neighbor_s else "  ")


class Board:
  root_tile = None
  tile_array = None

  def __init__(self):
    """Creates a skeleton of a board without any resources/ports/etc filled."""
    self.tile_array = []

    # Create all the tiles.
    for i in range(5):
      row = []
      for j in range(5 - abs(i - 2)):
        row.append(GraphTile())
      self.tile_array.append(row)

    # Set north the directions.
    for row in self.tile_array:
      prev_tile = None
      for tile in row:
        if prev_tile:
          prev_tile.neighbor_n = tile
          tile.neighbor_s = prev_tile

  def ToJson(self):
    tiles = []
    for row in self.tile_array:
      new_row = []
      for tile in row:
        new_row.append(
            {"resource": tile.resource,
             "number_token": tile.number_token if tile.number_token else ""})
      tiles.append(new_row)
    return json.dumps({"tiles": tiles})

  def __str__(self):
    template = """
                --
              / %s \ 
           --        --
         / %s \ %s / %s \ 
      --        --        --
    / %s \ %s / %s \ %s / %s \ 
           --        --
    \ %s / %s \ %s / %s \ %s /
      --        --        --
    / %s \ %s / %s \ %s / %s \ 
           --        --
    \ %s / %s \ %s / %s \ %s /
      --        --        --
    / %s \ %s / %s \ %s / %s \ 
           --        --
    \ %s / %s \ %s / %s \ %s /
      --        --        --
         \ %s / %s \ %s /
           --        --
              \ %s /
                --
    """
    return template % (
        self.tile_array[2][4].GetResourceShort(),

        self.tile_array[1][3].GetResourceShort(),
        self.tile_array[2][4].GetTwoDigitNumber(),
        self.tile_array[3][3].GetResourceShort(),

        self.tile_array[0][2].GetResourceShort(),
        self.tile_array[1][3].GetTwoDigitNumber(),
        self.tile_array[2][3].GetResourceShort(),
        self.tile_array[3][3].GetTwoDigitNumber(),
        self.tile_array[4][2].GetResourceShort(),

        self.tile_array[0][2].GetTwoDigitNumber(),
        self.tile_array[1][2].GetResourceShort(),
        self.tile_array[2][3].GetTwoDigitNumber(),
        self.tile_array[3][2].GetResourceShort(),
        self.tile_array[4][2].GetTwoDigitNumber(),

        self.tile_array[0][1].GetResourceShort(),
        self.tile_array[1][2].GetTwoDigitNumber(),
        self.tile_array[2][2].GetResourceShort(),
        self.tile_array[3][2].GetTwoDigitNumber(),
        self.tile_array[4][1].GetResourceShort(),

        self.tile_array[0][1].GetTwoDigitNumber(),
        self.tile_array[1][1].GetResourceShort(),
        self.tile_array[2][2].GetTwoDigitNumber(),
        self.tile_array[3][1].GetResourceShort(),
        self.tile_array[4][1].GetTwoDigitNumber(),

        self.tile_array[0][0].GetResourceShort(),
        self.tile_array[1][1].GetTwoDigitNumber(),
        self.tile_array[2][1].GetResourceShort(),
        self.tile_array[3][1].GetTwoDigitNumber(),
        self.tile_array[4][0].GetResourceShort(),

        self.tile_array[0][0].GetTwoDigitNumber(),
        self.tile_array[1][0].GetResourceShort(),
        self.tile_array[2][1].GetTwoDigitNumber(),
        self.tile_array[3][0].GetResourceShort(),
        self.tile_array[4][0].GetTwoDigitNumber(),

        self.tile_array[1][0].GetTwoDigitNumber(),
        self.tile_array[2][0].GetResourceShort(),
        self.tile_array[3][0].GetTwoDigitNumber(),

        self.tile_array[2][0].GetTwoDigitNumber())


def GenerateBoard():
  json_board = {"tiles": [[{"resource": "WHEAT", "number_token": 5},
                           {"resource": "SHEEP", "number_token": 2},
                           {"resource": "DESERT"}],
                          [{"resource": "WOOD", "number_token": 8},
                           {"resource": "STONE", "number_token": 10},
                           {"resource": "BRICK", "number_token": 9},
                           {"resource": "WOOD", "number_token": 6}],
                          [{"resource": "WHEAT", "number_token": 4},
                           {"resource": "BRICK", "number_token": 3},
                           {"resource": "SHEEP", "number_token": 11},
                           {"resource": "ORE", "number_token": 4},
                           {"resource": "WHEAT", "number_token": 3}],
                          [{"resource": "SHEEP", "number_token": 11},
                           {"resource": "ORE", "number_token": 6},
                           {"resource": "BRICK", "number_token": 5},
                           {"resource": "WOOD", "number_token": 8}],
                          [{"resource": "WOOD", "number_token": 12},
                           {"resource": "SHEEP", "number_token": 9},
                           {"resource": "WHEAT", "number_token": 10}]],
                "ports": ["ANY", "ANY", "BRICK", "WOOD", "ANY", "WHEAT", "STONE", "ANY", "SHEEP"],
                "id": 1234}
  graph_board = []
  for tile_row in json_board["tiles"]:
    graph_row = []
    for tile in tile_row:
      graph_tile = GraphTile()
      graph_tile.resource = tile["resource"]
      graph_tile.number_token = tile[
          "number_token"] if "number_token" in tile else None
      graph_row.append(graph_tile)
    graph_board.append(graph_row)

  row = 0
  col = 0
  # TODO do not hard code
  for row in range(len(graph_board)):
    # This denotes the shift of the adjacent row's column index based on
    # direction and location within the board (assuming a 5 row board).
    ne_shift = 1 if row < 2 else 0
    se_shift = 0 if row < 2 else -1
    nw_shift = 0 if row < 3 else 1
    sw_shift = -1 if row < 3 else 0
    for col in range(len(graph_board[row])):
      def GetTileOrNone(graph_board, row, col):
        if (row >= 0 and row < len(graph_board) and
                col >= 0 and col < len(graph_board[row])):
          return graph_board[row][col]
        else:
          return None

      curr = graph_board[row][col]
      curr.neighbor_n = GetTileOrNone(graph_board, row, col + 1)
      curr.neighbor_ne = GetTileOrNone(graph_board, row + 1, col + ne_shift)
      curr.neighbor_se = GetTileOrNone(graph_board, row + 1, col + se_shift)
      curr.neighbor_s = GetTileOrNone(graph_board, row, col - 1)
      curr.neighbor_nw = GetTileOrNone(graph_board, row - 1, col + nw_shift)
      curr.neighbor_sw = GetTileOrNone(graph_board, row - 1, col + sw_shift)

  return graph_board[0][0]


class GenerateJson(webapp2.RequestHandler):

  def get(self):
    board = Board()
    self.response.headers['Content-Type'] = 'application/json'
    self.response.write(board.ToJson())


class GenerateString(webapp2.RequestHandler):

  def get(self):
    board = Board()
    print board
    self.response.write("GAH")

app = webapp2.WSGIApplication([
    ('/generate_json', GenerateJson),
    ('/generate_string', GenerateString)
], debug=True)
