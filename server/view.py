import json


def RenderJsonBoard(root_tile):
  ordered_tiles = []
  # First grab the tile for the beginning of each row.
  curr = root_tile
  while (curr != None):
    ordered_tiles.append([curr])
    # We always go east, but choose the non-null one.
    curr = curr.neighbor_ne if curr.neighbor_ne != None else curr.neighbor_se

  for row in ordered_tiles:
    curr = row[0].neighbor_n
    while (curr != None):
      row.append(curr)
      curr = curr.neighbor_n

  print "num_ordered_tiles: %s" % len(ordered_tiles)

  tiles = []
  for row in ordered_tiles:
    new_row = []
    for tile in row:
      new_row.append(
          {"resource": tile.resource,
           "number_token": tile.number_token if tile.number_token else ""})
    tiles.append(new_row)

  return json.dumps({
      "tiles": tiles})
