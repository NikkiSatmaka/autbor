theBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

def isValidChessBoard(board):

    spaces = ['1a', '1b', '1c', '1d', '1e', '1f', '1g', '1h',
              '2a', '2b', '2c', '2d', '2e', '2f', '2g', '2h',
              '3a', '3b', '3c', '3d', '3e', '3f', '3g', '3h',
              '4a', '4b', '4c', '4d', '4e', '4f', '4g', '4h',
              '5a', '5b', '5c', '5d', '5e', '5f', '5g', '5h',
              '6a', '6b', '6c', '6d', '6e', '6f', '6g', '6h',
              '7a', '7b', '7c', '7d', '7e', '7f', '7g', '7h',
              '8a', '8b', '8c', '8d', '8e', '8f', '8g', '8h']

    pieces = ['wpawn', 'wknight', 'wbishop', 'wrook', 'wqueen', 'wking',
              'bpawn', 'bknight', 'bbishop', 'brook', 'bqueen', 'bking']

    # Check if there is invalid spaces
    for space in board:
        if space not in spaces:
            return False

    # Check if there is invalid pieces
    for piece in board.values():
        if piece not in pieces:
            return False

    # Count the number of pieces
    count = {}
    for piece in board.values():
        count.setdefault(piece, 0)
        count[piece] += 1

    # Check to see if there's 1 white king and black king
    if 'wking' not in count or 'bking' not in count:
        return False
    elif count['wking'] != 1 or count['bking'] != 1:
        return False

    # Check to see if the pawns don't exceed 8
    if 'wpawn' in count and count['wpawn'] > 8:
        return False
    if 'bpawn' in count and count['bpawn'] > 8:
        return False

    return True

print(isValidChessBoard(theBoard))