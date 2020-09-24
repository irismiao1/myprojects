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
                                fill=color,
                                outline ='grey')

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
        app.setActiveMode(app.gameMode)

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
        hLen = mode.app.height//12
        canvas.create_rectangle(0, 0, mode.app.width, mode.app.height, fill = 'lightblue')
        canvas.create_text(mode.app.width//2, mode.app.height//4, font = ssmFont, text = 'Welcome to Hextrix!')
        canvas.create_text(mode.app.width//2, 11*mode.app.height//16, font = helpFont, text = 'Press "s" to start.')
        canvas.create_text(mode.app.width//2, 6*mode.app.height//8, font = helpFont, text = 'Press "h" for help.')
        
        drawHex(canvas, mode.app.width//6 + offSet, mode.app.height//2, hLen, blue)
        drawHex(canvas, mode.app.width//3 + offSet, mode.app.height//2, hLen, red)
        drawHex(canvas, mode.app.width//2 + offSet, mode.app.height//2, hLen, yellow)
        drawHex(canvas, 2*mode.app.width//3 + offSet, mode.app.height//2, hLen, green)
        drawHex(canvas, 5*mode.app.width//6 + offSet, mode.app.height//2, hLen, orange)
        
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
        gameFont = 'Verdana 14'
        gameText = 'Game over!'
        gameText2 = 'Press "r" to restart.'
        gameText3 = 'Press any key to return'
        gameText4 = 'to the splash screen.'
        offSetX = 25
        offSetY = 20
        red = rgbString(255, 102, 102)
        blue = rgbString(102, 178, 255)
        yellow = rgbString(255, 255, 153)
        green = rgbString(153, 255, 153)
        orange = rgbString(255, 178, 102)
        hLen = mode.app.height//12

        canvas.create_rectangle(0, 0, mode.app.width, mode.app.height, fill = 'lightyellow')
        canvas.create_text(mode.app.width//2, mode.app.height//4, font = 'Verdana 22 bold italic', text = gameText)
        canvas.create_text(mode.app.width//2, 5*mode.app.height//12, font = gameFont, text = gameText2)
        canvas.create_text(mode.app.width//2, mode.app.height//2, font = gameFont, text = gameText3)
        canvas.create_text(mode.app.width//2, 7*mode.app.height//12, font = gameFont, text = gameText4)
        
        drawHex(canvas, mode.app.width//6 + offSetX, 3*mode.app.height//4 + offSetY, hLen, blue)
        drawHex(canvas, mode.app.width//3 + offSetX, 3*mode.app.height//4 + offSetY, hLen, red)
        drawHex(canvas, mode.app.width//2 + offSetX, 3*mode.app.height//4 + offSetY, hLen, yellow)
        drawHex(canvas, 2*mode.app.width//3 + offSetX, 3*mode.app.height//4 + offSetY, hLen, green)
        drawHex(canvas, 5*mode.app.width//6 + offSetX, 3*mode.app.height//4 + offSetY, hLen, orange)
        

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
        self.offSet = self.length * math.cos(22.5)
        self.gap = 5
    
    def distance(self, a, b):
        return ((self.x - a)**2 + (self.y - b)**2)**0.5

class oPiece(HextrixPieces):
    def __init__(self, x, y, length, color):
        super().__init__(x, y, length, color)
        self.piece = [
            [True]
        ]
    
    def draw(self, canvas):
        drawHex(canvas, self.x, self.y, self.length, 'red')

class cPiece(HextrixPieces):
    def __init__(self, x, y, length, color):
        super().__init__(x, y, length, color)
        self.piece = [
            [ False,  True,  True, False ],
            [ True,  False,  False, True ]
        ]
    
    def draw(self, canvas):
        drawHex(canvas, self.x, self.y, self.length, 'yellow')
        drawHex(canvas, self.x + (2*self.offSet), self.y, self.length, 'yellow')
        drawHex(canvas, self.x - self.offSet, self.y + (2*self.length) - self.gap, self.length, 'yellow')
        drawHex(canvas, self.x + (3*self.offSet), self.y + (2*self.length) - self.gap, self.length, 'yellow')

class iPiece(HextrixPieces):
    def __init__(self, x, y, length, color):
        super().__init__(x, y, length, color)
        self.piece = [
            [  True,  True,  True,  True ]
        ]
    
    def draw(self, canvas):
        drawHex(canvas, self.x, self.y, self.length, 'magenta')
        drawHex(canvas, self.x + (2*self.offSet), self.y, self.length, 'magenta')
        drawHex(canvas, self.x + (4*self.offSet), self.y, self.length, 'magenta')
        drawHex(canvas, self.x + (6*self.offSet), self.y, self.length, 'magenta')

class lPiece(HextrixPieces):
    def __init__(self, x, y, length, color):
        super().__init__(x, y, length, color)
        self.piece = [
            [  True, False, False, False ],
            [  False, True, False, False ],
            [  False, False, True, False ],
            [  False, False, False, True ]
        ]
    
    def draw(self, canvas):
        drawHex(canvas, self.x, self.y, self.length, 'pink')
        drawHex(canvas, self.x - self.offSet, self.y + (2*self.length) - self.gap, self.length, 'pink')
        drawHex(canvas, self.x - (2*self.offSet), self.y + (4*self.length) - 2*self.gap, self.length, 'pink')
        drawHex(canvas, self.x - (3*self.offSet), self.y + (6*self.length) - 3*self.gap, self.length, 'pink')

class sPiece(HextrixPieces):
    def __init__(self, x, y, length, color):
        super().__init__(x, y, length, color)
        self.piece =  [
            [ False, True,  True  ],
            [ True,  True,  False ]
        ]

    def draw(self, canvas):
        drawHex(canvas, self.x, self.y, self.length, 'cyan')
        drawHex(canvas, self.x + (2*self.offSet), self.y, self.length, 'cyan')
        drawHex(canvas, self.x + self.offSet, self.y + (2*self.length) - self.gap, self.length, 'cyan')
        drawHex(canvas, self.x + (3*self.offSet), self.y + (2*self.length) - self.gap, self.length, 'cyan')

class tPiece(HextrixPieces):
    def __init__(self, x, y, length, color):
        super().__init__(x, y, length, color)
        self.piece = [
            [ False,  True, False ],
            [  True,  True,  True ],
            [ False,  True, False ]
        ]
    
    def draw(self, canvas):
        drawHex(canvas, self.x, self.y, self.length, 'green')
        drawHex(canvas, self.x - self.offSet, self.y + (2*self.length) - self.gap, self.length, 'green')
        drawHex(canvas, self.x + self.offSet, self.y + (2*self.length) - self.gap, self.length, 'green')
        drawHex(canvas, self.x, self.y + (4*self.length) - (2*self.gap), self.length, 'green')

class vPiece(HextrixPieces):
    def __init__(self, x, y, length, color):
        super().__init__(x, y, length, color)
        self.piece = [
            [ True, False,  False ],
            [  True, False,  True ],
            [ False,  True, False ]
        ]
    
    def draw(self, canvas):
        drawHex(canvas, self.x, self.y, self.length, 'orange')
        drawHex(canvas, self.x - self.offSet, self.y + (2*self.length) - self.gap, self.length, 'orange')
        drawHex(canvas, self.x - (3*self.offSet), self.y + (2*self.length) - self.gap, self.length, 'orange')
        drawHex(canvas, self.x - (2*self.offSet), self.y + (3*self.length), self.length, 'orange')

class yPiece(HextrixPieces):
    def __init__(self, x, y, length, color):
        super().__init__(x, y, length, color)
        self.piece = [
            [ False,  True, False ],
            [  True, False,  True ],
            [ False, False,  True ]
        ]
    
    def draw(self, canvas):
        drawHex(canvas, self.x, self.y, self.length, 'blue')
        drawHex(canvas, self.x - self.offSet, self.y + (2*self.length) - self.gap, self.length, 'blue')
        drawHex(canvas, self.x + self.offSet, self.y + (2*self.length) - self.gap, self.length, 'blue')
        drawHex(canvas, self.x - (2*self.offSet), self.y + (4*self.length) - 2*self.gap, self.length, 'blue')

class GameMode(Mode):
    def appStarted(mode):
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
            [ False, True,  True  ],
            [ True,  True,  False ]
        ]

        tPiece = [
            [ False,  True, False ],
            [  True,  True,  True ],
            [ False,  True, False ]
        ]

        vPiece = [
            [ True, False,  False ],
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

        #hexagonal board
        mode.board = [
                    [None, None, None, 0, 0, 0, 0],
                    [None, None,    0, 0, 0, 0, 0],
                    [None,    0,    0, 0, 0, 0, 0],
                    [   0,    0,    0, 0, 0, 0, 0], 
                    [None,    0,    0, 0, 0, 0, 0],
                    [None, None,    0, 0, 0, 0, 0],
                    [None, None, None, 0, 0, 0, 0]
                    ]
        #initial 3 choices
        mode.choiceList = []
        mode.initializeChoices()

        #drag and drop
        mode.dragged = None
        mode.draggedCx, mode.draggedCy = 0, 0
        mode.draggedColor = None

    #draw hexagonal board
    def drawBoard(mode, canvas):
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
    
    #draw score box
    def drawScore(mode, canvas):
        scoreFont = 'Fixedsys 20 bold italic'
        color = rgbString(255,215,0)
        canvas.create_rectangle(3*mode.app.width//4, mode.app.height//16, 15*mode.app.width//16, mode.app.height//4, fill = color)
        canvas.create_text(27*mode.app.width//32, 3*mode.app.height//32, font = scoreFont, text = 'Score:')
        canvas.create_text(27*mode.app.width//32, 6*mode.app.height//32, font = scoreFont, text = f'{mode.score}')

    def drawNBM(mode, canvas):
        moveFont = 'Fixedsys 8 bold italic'
        moveText = 'Next Best Move:'
        color = rgbString(204, 229, 255)
        canvas.create_rectangle(3*mode.app.width//4, 10*mode.app.height//16, 15*mode.app.width//16, 15*mode.app.height//16, fill = color)
        canvas.create_text(27*mode.app.width//32, 21*mode.app.height//32, font = moveFont, text = moveText)

    #generate 3 random pieces
    def initializeChoices(mode):
        offSetX = 50
        length = mode.app.height//40
        for i in range(3):
            randomIndex = random.randint(1, len(mode.hextrixPieces) - 1)
            color = mode.hextrixPieceColors[randomIndex]
            if randomIndex == 1:
                oPieces = oPiece(i * (mode.app.width//6) + offSetX, 7*mode.app.height//8, length, color)
                mode.choiceList.append(oPieces)
            elif randomIndex == 2:
                cPieces = cPiece(i * (mode.app.width//6) + offSetX, 7*mode.app.height//8, length, color)
                mode.choiceList.append(cPieces)
            elif randomIndex == 3:
                iPieces = iPiece(i * (mode.app.width//6) + offSetX, 7*mode.app.height//8, length, color)
                mode.choiceList.append(iPieces)
            elif randomIndex == 4:
                lPieces = oPiece(i * (mode.app.width//6) + offSetX, 7*mode.app.height//8, length, color)
                mode.choiceList.append(lPieces)               
            elif randomIndex == 5:
                sPieces = sPiece(i * (mode.app.width//6) + offSetX, 7*mode.app.height//8, length, color)
                mode.choiceList.append(sPieces)
            elif randomIndex == 6:
                tPieces = tPiece(i * (mode.app.width//6) + offSetX, 7*mode.app.height//8, length, color)
                mode.choiceList.append(tPieces)
            elif randomIndex == 7:
                vPieces = vPiece(i * (mode.app.width//6) + offSetX, 7*mode.app.height//8, length, color)
                mode.choiceList.append(vPieces)
            elif randomIndex == 8:
                yPieces = yPiece(i * (mode.app.width//6) + offSetX, 7*mode.app.height//8, length, color)
                mode.choiceList.append(yPieces)
    
    def drawChoices(mode, canvas):
        for i in range(len(mode.choiceList)):
            mode.choiceList[i].draw(canvas)

    #drag and drop
    def mousePressed(mode, event):
        for elem in mode.choiceList:
            if elem.distance(event.x, event.y) < elem.length:
                mode.dragged = elem
                break

    def mouseDragged(mode, event):
        if not mode.dragged == None:
            mode.draggedCx, mode.draggedCy = event.x, event.y

    def mouseReleased(mode, event):
        mode.dragged = None

    def redrawAll(mode, canvas):
        #draw board
        mode.drawBoard(canvas)
        #draw scoreboard
        mode.drawScore(canvas)
        #draw initial choices
        mode.drawChoices(canvas)
        #draw next best move box
        mode.drawNBM(canvas)
 
def runHextrixGame():
    HextrixGame(width = 400, height = 400)

runHextrixGame()
