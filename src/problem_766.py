# Problem 766: https://projecteuler.net/problem=766

from urllib.request import urlopen

from PIL import Image, ImageChops, ImageDraw


def read_pieces(url, width, height):
    with urlopen(url) as response:
        picture = Image.open(response).convert("RGB")
    centers = {}
    for y in range(height):
        for x in range(width):
            px = (2 * x + 1) * picture.width // (2 * width)
            py = (2 * y + 1) * picture.height // (2 * height)
            centers[(x, y)] = (px, py)

    red, green, blue = picture.split()
    bright = ImageChops.lighter(ImageChops.lighter(red, green), blue)
    cutoff = min(bright.getpixel(p) for p in centers.values()) / 2
    interior = bright.point(lambda v: 255 if v > cutoff else 0)
    pieces = []
    for cell, point in centers.items():
        if not interior.getpixel(point) or picture.getpixel(point) == (255, 255, 255):
            continue
        ImageDraw.floodfill(interior, point, 1)
        piece = [c for c, p in centers.items() if interior.getpixel(p) == 1]
        pieces.append(piece)
        ImageDraw.floodfill(interior, point, 0)
    return pieces


def reachable(width, height, pieces):
    stride = width + 2
    board = bytearray([1]) * (stride * (height + 2))
    for y in range(height):
        start = (y + 1) * stride + 1
        board[start:start + width] = bytes(width)

    tiles = {}
    moves = {}
    next_tile = 2
    for piece in pieces:
        cells = sorted((y + 1) * stride + x + 1 for x, y in piece)
        shape = tuple(p - cells[0] for p in cells)
        if shape not in tiles:
            tiles[shape] = range(next_tile, next_tile + len(shape))
            next_tile += len(shape)
            for step in (-stride, -1, 1, stride):
                entering = [p + step for p in shape if p + step not in shape]
                edge = entering[0] - step
                tile = tiles[shape][shape.index(edge)]
                needed = [p - edge for p in entering[1:]]
                edits = [(p - edge, 0) for p in shape if p - step not in shape]
                for p, value in zip(shape, tiles[shape]):
                    edits.append((p + step - edge, value))
                moves[tile, step] = needed, edits
        for cell, tile in zip(cells, tiles[shape]):
            board[cell] = tile

    initial = bytes(board)
    seen = {initial}
    pending = [initial]
    while pending:
        state = pending.pop()
        hole = state.find(b"\x00")
        while hole >= 0:
            for step in (-stride, -1, 1, stride):
                source = hole - step
                move = moves.get((state[source], step))
                if move is None:
                    continue
                needed, edits = move
                if any(state[source + offset] for offset in needed):
                    continue
                after = bytearray(state)
                for offset, value in edits:
                    after[source + offset] = value
                neighbor = bytes(after)
                if neighbor not in seen:
                    seen.add(neighbor)
                    pending.append(neighbor)
            hole = state.find(b"\x00", hole + 1)
    return len(seen)


def solve():
    url = "https://projecteuler.net/resources/images/0766_SlidingBlock2.jpg"
    width, height = 6, 5
    return reachable(width, height, read_pieces(url, width, height))


if __name__ == "__main__":
    print(solve())
