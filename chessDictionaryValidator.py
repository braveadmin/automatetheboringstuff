#Chess Dictionary Validator

chessboard = {'1h': 'bpawn', '6c': 'wqueen', '2g': 'wbishop', '5h': 'bqueen', '3e': 'wking'}


#chessboard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking','1a':'bpawn','1b':'bpawn','3d':'bpawn','4b':'bpawn','3g':'bpawn','5h':'bpawn','2d':'bpawn','6d':'bpawn'}

def isValidChessBoard(position):

    #check if there is 1 king of each color

    if ('bking' and 'wking') not in position.values():

        print('Broken.')

    #check that there is not more than 16 pieces in the chessboard

    if len(chessboard) > 15:

        print('Broken.')

    #check that each player has maximum 8 pawns

    count = {}

    for pawns in position.values():

        count.setdefault(pawns, 0)

        count[pawns] = count[pawns] + 1

    # next step: check if bpawn and wpawn are in the dictionary

    if ( ('bpawn' or 'wpawn') in count.keys() ) and ( (count['bpawn'] or count['wpawn']) > 7 ):

        print('Broken.')

    # valid space position 1a to 8h

    x=['a','b','c','d','e','f','g','h']

    y=['1','2','3','4','5','6','7','8']

    for i in position.keys():

        if (i[0] not in y) or (i[1] not in x):

            print('Broken.')

    # all pieces start with 'b' or 'w'

    pieceColour = ('b','w')

    for i in position.values():

        if i[0] not in pieceColour:

            print('Broken.')

    # piece name is valid

    valid_pieces=['pawn','king','queen','bishop','knight','rook']

    for i in position.values():

        if i[1:] not in valid_pieces:

           print('Broken.')


isValidChessBoard(chessboard)



