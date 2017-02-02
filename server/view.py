import json


def _GetTileMatrix(root_tile):
  ordered_tiles = []
  # First grab the tile for the beginning of each row.
  curr = root_tile
  while (curr != None):
    ordered_tiles.append([curr])
    # We always go east, but choose the non-null one.
    curr = curr.neighbor_se if curr.neighbor_se != None else curr.neighbor_ne

  i = 0
  for row in ordered_tiles:
    i += 1
    curr = row[0].neighbor_n
    while (curr != None):
      row.append(curr)
      curr = curr.neighbor_n
  return ordered_tiles


def RenderJsonBoard(root_tile):
  ordered_tiles = _GetTileMatrix(root_tile)

  tiles = []
  for row in ordered_tiles:
    new_row = []
    for tile in row:
      new_row.append(
          {"resource": tile.resource,
           "number_token": tile.number_token if tile.number_token else ""})
    tiles.append(new_row)

  return json.dumps({"tiles": tiles})


def RenderStringBoard(root_tile):
  template = """
_                --<br>
_              / %s \<br>
_           --        --<br>
_         / %s \ %s / %s \<br>
_      --        --        --<br>
_    / %s \ %s / %s \ %s / %s \<br>
_           --        --<br>
_    \ %s / %s \ %s / %s \ %s /<br>
_      --        --        --<br>
_    / %s \ %s / %s \ %s / %s \<br>
_           --        --<br>
_    \ %s / %s \ %s / %s \ %s /<br>
_      --        --        --<br>
_    / %s \ %s / %s \ %s / %s \<br>
_           --        --<br>
_    \ %s / %s \ %s / %s \ %s /<br>
_      --        --        --<br>
_         \ %s / %s \ %s /<br>
_           --        --<br>
_              \ %s /<br>
_                --<br>
  """
  ordered_tiles = _GetTileMatrix(root_tile)
  s = ""
  for row in ordered_tiles:
    print["%s-%s" % (tile.GetResourceShort(), tile.GetTwoDigitNumber()) for tile in row]

  return template % (
      ordered_tiles[2][4].GetResourceShort(),

      ordered_tiles[1][3].GetResourceShort(),
      ordered_tiles[2][4].GetTwoDigitNumber(),
      ordered_tiles[3][3].GetResourceShort(),

      ordered_tiles[0][2].GetResourceShort(),
      ordered_tiles[1][3].GetTwoDigitNumber(),
      ordered_tiles[2][3].GetResourceShort(),
      ordered_tiles[3][3].GetTwoDigitNumber(),
      ordered_tiles[4][2].GetResourceShort(),

      ordered_tiles[0][2].GetTwoDigitNumber(),
      ordered_tiles[1][2].GetResourceShort(),
      ordered_tiles[2][3].GetTwoDigitNumber(),
      ordered_tiles[3][2].GetResourceShort(),
      ordered_tiles[4][2].GetTwoDigitNumber(),

      ordered_tiles[0][1].GetResourceShort(),
      ordered_tiles[1][2].GetTwoDigitNumber(),
      ordered_tiles[2][2].GetResourceShort(),
      ordered_tiles[3][2].GetTwoDigitNumber(),
      ordered_tiles[4][1].GetResourceShort(),

      ordered_tiles[0][1].GetTwoDigitNumber(),
      ordered_tiles[1][1].GetResourceShort(),
      ordered_tiles[2][2].GetTwoDigitNumber(),
      ordered_tiles[3][1].GetResourceShort(),
      ordered_tiles[4][1].GetTwoDigitNumber(),

      ordered_tiles[0][0].GetResourceShort(),
      ordered_tiles[1][1].GetTwoDigitNumber(),
      ordered_tiles[2][1].GetResourceShort(),
      ordered_tiles[3][1].GetTwoDigitNumber(),
      ordered_tiles[4][0].GetResourceShort(),

      ordered_tiles[0][0].GetTwoDigitNumber(),
      ordered_tiles[1][0].GetResourceShort(),
      ordered_tiles[2][1].GetTwoDigitNumber(),
      ordered_tiles[3][0].GetResourceShort(),
      ordered_tiles[4][0].GetTwoDigitNumber(),

      ordered_tiles[1][0].GetTwoDigitNumber(),
      ordered_tiles[2][0].GetResourceShort(),
      ordered_tiles[3][0].GetTwoDigitNumber(),

      ordered_tiles[2][0].GetTwoDigitNumber())
