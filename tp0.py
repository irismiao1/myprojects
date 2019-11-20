import math, copy, random

from cmu_112_graphics import *
from tkinter import *

#draw board which consists of hexagon pieces
#from: https://github.com/noobien/pytk-hexagon-grid
def drawHex(canvas, x, y, length, color):
    start_x = x
    start_y = y
    angle = 60
    coords = []
    for i in range(6):
        end_x = start_x + length * math.cos(math.radians(angle * i + 150))
        end_y = start_y + length * math.sin(math.radians(angle * i + 150))
        coords.append([start_x, start_y])
        start_x = end_x
        start_y = end_y
    canvas.create_polygon(coords[0][0],
                                coords[0][1], 
                                coords[1][0], 
                                coords[1][1],
                                coords[2][0],
                                coords[2][1],
                                coords[3][0],
                                coords[3][1],
                                coords[4][0],
                                coords[4][1], 
                                coords[5][0],
                                coords[5][1], 
                                fill=color)

#custom colors
def rgbString(red, green, blue):
    # Don't worry about how this code works yet.
    return "#%02x%02x%02x" % (red, green, blue)

class HextrixGame(ModalApp):
    def appStarted(app):
        app.SSM = SplashScreenMode()
        app.gameMode = GameMode()
        app.helpMode = HelpMode()
        app.gameOver = GameOver()
        app.setActiveMode(app.SSM)

class SplashScreenMode(Mode):
    def redrawAll(mode, canvas):
        ssmFont = 'Verdana 20 bold'
        helpFont = 'Verdana 16 bold italic'
        offSet = 25
        red = rgbString(255, 102, 102)
        blue = rgbString(102, 178, 255)
        yellow = rgbString(255, 255, 153)
        green = rgbString(153, 255, 153)
        orange = rgbString(255, 178, 102)
        canvas.create_rectangle(0, 0, mode.app.width, mode.app.height, fill = 'lightblue')
        canvas.create_text(mode.app.width//2, mode.app.height//4, font = ssmFont, text = 'Welcome to Hextrix!')
        canvas.create_text(mode.app.width//2, 11*mode.app.height//16, font = helpFont, text = 'Press "s" to start.')
        canvas.create_text(mode.app.width//2, 6*mode.app.height//8, font = helpFont, text = 'Press "h" for help.')
        
        drawHex(canvas, mode.app.width//6 + offSet, mode.app.height//2, 35, blue)
        drawHex(canvas, mode.app.width//3 + offSet, mode.app.height//2, 35, red)
        drawHex(canvas, mode.app.width//2 + offSet, mode.app.height//2, 35, yellow)
        drawHex(canvas, 2*mode.app.width//3 + offSet, mode.app.height//2, 35, green)
        drawHex(canvas, 5*mode.app.width//6 + offSet, mode.app.height//2, 35, orange)
        
    def keyPressed(mode, event):
        if event.key == 's':
            mode.app.setActiveMode(mode.app.gameMode)
        elif event.key == 'h':
            mode.app.setActiveMode(mode.app.helpMode)

class HelpMode(Mode):
    def redrawAll(mode, canvas):
        helpFont = 'Verdana 18'
        helpText = 'Select one of the 3 pieces given to'
        helpText2 = 'you and drag it to the board.'
        helpText3 = 'Fill up as many rows as you can'
        helpText4 = 'to get a high score!'
        canvas.create_rectangle(0, 0, mode.app.width, mode.app.height, fill = 'lightpink')
        canvas.create_text(mode.app.width//2, mode.app.height//4, font = helpFont, text = helpText)
        canvas.create_text(mode.app.width//2, mode.app.height//3, font = helpFont, text = helpText2)
        canvas.create_text(mode.app.width//2, 5*mode.app.height//12, font = helpFont, text = helpText3)
        canvas.create_text(mode.app.width//2, mode.app.height//2, font = helpFont, text = helpText4)

        canvas.create_text(mode.app.width//2, 3*mode.app.height//4, font = helpFont, text = 'Press "s" to start.')

    def keyPressed(mode, event):
        if event.key == 's':
            mode.app.setActiveMode(mode.app.gameMode)
        else:
            mode.app.setActiveMode(mode.app.SSM)

class GameOver(Mode):
    def redrawAll(mode, canvas):
        canvas.create_text(mode.app.width//2, mode.app.height//2, \
                        text = 'Game Over! Press "r" to restart.')

    def keyPressed(mode, event):
        if event.key == 'r':
            mode.app.setActiveMode(mode.app.gameMode)
        else:
            mode.app.setActiveMode(mode.app.SSM)

class HextrixPieces(object): 
    def __init__(self, x, y, length, color):
        self.x = x
        self.y = y
        self.length = length
        self.color = color
        self.hLen = app.height / 20
        self.offSet = self.hLen * math.cos(22.5)

class oPiece(HextrixPieces):
    def __init__(self, x, y, length, color):
        super().__init__(x, y, length, color)
        self.piece = [
            [True]
        ]
    
    def draw(self, canvas, x, y, length):
        drawHex(canvas, x, y, self.hLen, 'red')

class cPiece(HextrixPieces):
    def __init__(self, x, y, length, color):
        super().__init__(x, y, length, color)
        self.piece = [
            [ False,  True,  True, False ],
            [ True,  False,  False, True ]
        ]
    
    def draw(self, canvas, x, y, length):
        drawHex(canvas, x, y, self.hLen, 'yellow')
        drawHex(canvas, x + (2*self.offSet), y, self.hLen, 'yellow')
        drawHex(canvas, x - self.offSet, y + (2*self.hLen), self.hLen, 'yellow')
        drawHex(canvas, x + (3*self.offSet), y + (2*self.hLen), self.hLen, 'yellow')

class iPiece(HextrixPieces):
    def __init__(self, x, y, length, color):
        super().__init__(x, y, length, color)
        self.piece = [
            [  True,  True,  True,  True ]
        ]
    
    def draw(self, canvas, x, y, length):
        drawHex(canvas, x, y, self.hLen, 'magenta')
        drawHex(canvas, x + (2*self.offSet), y, self.hLen, 'magenta')
        drawHex(canvas, x + (4*self.offSet), y, self.hLen, 'magenta')
        drawHex(canvas, x + (6*self.offSet), y, self.hLen, 'magenta')

class lPiece(HextrixPieces):
    def __init__(self, x, y, length, color):
        super().__init__(x, y, length, color)
        self.piece = [
            [  True, False, False, False ],
            [  False, True, False, False ],
            [  False, False, True, False ],
            [  False, False, False, True ]
        ]
    
    def draw(self, canvas, x, y, length):
        drawHex(canvas, x, y, self.hLen, 'pink')
        drawHex(canvas, x + self.offSet, y + (2*hLen), hLen, 'pink')
        drawHex(canvas, x + (2*self.offSet), y + (4*hLen), hLen, 'pink')
        drawHex(canvas, x + (3*self.offSet), y + (6*hLen), hLen, 'pink')

class sPiece(HextrixPieces):
    def __init__(self, x, y, length, color):
        super().__init__(x, y, length, color)
        self.piece =  [
            [  True,  True, False ],
            [ False,  True,  True ]
        ]

    def draw(self, canvas, x, y, length):
        drawHex(canvas, x, y, self.hLen, 'cyan')
        drawHex(canvas, x + (2*self.offSet), y, self.hLen, 'cyan')
        drawHex(canvas, x + self.offSet, y + (2*self.hLen), self.hLen, 'cyan')
        drawHex(canvas, x + (2*self.offSet), y + (2*self.hLen), self.hLen, 'cyan')

class tPiece(HextrixPieces):
    def __init__(self, x, y, length, color):
        super().__init__(x, y, length, color)
        self.piece = [
            [ False,  True, False ],
            [  True,  True,  True ],
            [ False,  True, False ]
        ]
    
    def draw(self, canvas, x, y, length):
        drawHex(canvas, x, y, self.hLen, 'green')
        drawHex(canvas, x - self.offSet, y + (2*self.hLen), self.hLen, 'green')
        drawHex(canvas, x + self.offSet, y + (2*self.hLen), self.hLen, 'green')
        drawHex(canvas, x, y + (4*self.hLen), self.hLen, 'green')

class vPiece(HextrixPieces):
    def __init__(self, x, y, length, color):
        super().__init__(x, y, length, color)
        self.piece = [
            [ False, False,  True ],
            [  True, False,  True ],
            [ False,  True, False ]
        ]
    
    def draw(self, canvas, x, y, length):
        drawHex(canvas, x, y, self.hLen, 'orange')
        drawHex(canvas, x + self.offSet, y - (2*self.hLen), self.hLen, 'orange')
        drawHex(canvas, x + (3*self.offSet), y - (2*self.hLen), self.hLen, 'orange')
        drawHex(canvas, x + (2*self.offSet), y - (3*self.hLen), self.hLen, 'orange')

class yPiece(HextrixPieces):
    def __init__(self, x, y, length, color):
        super().__init__(x, y, length, color)
        self.piece = [
            [ False,  True, False ],
            [  True, False,  True ],
            [ False, False,  True ]
        ]
    
    def draw(self, canvas, x, y, length):
        drawHex(canvas, x, y, self.hLen, 'blue')
        drawHex(canvas, x - self.offSet, y + (2*self.hLen), self.hLen, 'blue')
        drawHex(canvas, x + self.offSet, y + (2*self.hLen), self.hLen, 'blue')
        drawHex(canvas, x + (2*self.offSet), y + (4*self.hLen), self.hLen, 'blue')

class GameMode(Mode):
    def appStarted(mode):
        mode.Piece = 0
        mode.PieceColor = None
        mode.score = 0
        #hextrix pieces
        oPiece = [
            [True]
        ]
        
        cPiece = [
            [ False,  True,  True, False ],
            [ True,  False,  False, True ]
        ]

        iPiece = [
            [  True,  True,  True,  True ]
        ]

        lPiece = [
            [  False, False, False, True ],
            [  False, False, True, False ],
            [  False, True, False, False ],
            [  True, False, False, False ]
        ]

        sPiece = [
            [  True,  True, False ],
            [ False,  True,  True ]
        ]

        tPiece = [
            [ False,  True, False ],
            [  True,  True,  True ],
            [ False,  True, False ]
        ]

        vPiece = [
            [ False, False,  True ],
            [  True, False,  True ],
            [ False,  True, False ]
        ]

        yPiece = [
            [ False,  True, False ],
            [  True, False,  True ],
            [ False, False,  True ]
        ]
        mode.hextrixPieces = [None, oPiece, cPiece, iPiece, lPiece, 
                            sPiece, tPiece, vPiece, yPiece ]
        mode.hextrixPieceColors = ["grey", "red", "yellow", "magenta", "pink", "cyan", 
                            "green", "orange", "blue" ]
        mode.choiceList = []
        mode.board = [
                    [None, None, None, 1, 0, 0, 0],
                    [None, None,    1, 0, 0, 0, 0],
                    [None,    1,    0, 0, 0, 0, 0],
                    [   1,    0,    0, 0, 0, 0, 0], 
                    [None,    0,    0, 0, 0, 0, 0],
                    [None, None,    1, 1, 0, 0, 0],
                    [None, None, None, 1, 1, 0, 0]
                    ]
        mode.initializeChoices()

    #generate 3 random pieces
    def initializeChoices(mode):
        for i in range(3):
            randomIndex = random.randint(1, len(mode.hextrixPieces) - 1)
            mode.choiceList.append(mode.hextrixPieces[randomIndex])

    def drawChoices(mode, canvas):
        for i in range(len(mode.choiceList)):
            if mode.choiceList[i] == mode.sPiece:
                drawSPiece(canvas, )
            #elif 
    
    #drag and drop
    def mousePressed(mode, event):
        #update piece cx, cy with event
        pass

    def redrawAll(mode, canvas):
        #draw board
        hLen = mode.app.height / 20
        offSet = hLen * math.cos(22.5)
        r = mode.app.height / 8
        l = mode.app.width / 20
        for row in range(len(mode.board)):
            for col in range(len(mode.board[0])):
                if mode.board[row][col] == None:
                    continue
                idx = mode.board[row][col]
                if mode.board[row][col] is not None:
                    if row == 0 or row == 6:
                        drawHex(canvas, l + (2 * hLen) * col + offSet, r + (2 * hLen) * row, hLen, mode.hextrixPieceColors[idx])
                    if row == 1 or row == 5:
                        drawHex(canvas, l + (2 * hLen) * col, r + (2 * hLen) * row, hLen, mode.hextrixPieceColors[idx])
                    if row == 2 or row == 4:
                        drawHex(canvas, l + (2 * hLen) * col - offSet, r + (2 * hLen) * row, hLen, mode.hextrixPieceColors[idx])
                    if row == 3: 
                        drawHex(canvas, l + (2 * hLen) * col - 2 * offSet, r + (2 * hLen) * row, hLen, mode.hextrixPieceColors[idx])
       
        #draw scoreboard
        scoreFont = 'Fixedsys 20 bold'
        color = rgbString(255,215,0)
        canvas.create_rectangle(3*mode.app.width//4, mode.app.height//16, 15*mode.app.width//16, mode.app.height//4, fill = color)
        canvas.create_text(27*mode.app.width//32, 3*mode.app.height//32, font = scoreFont, text = 'Score:')
        canvas.create_text(27*mode.app.width//32, 6*mode.app.height//32, font = scoreFont, text = f'{mode.score}')


def runHextrixGame():
    HextrixGame(width = 400, height = 400)

runHextrixGame()