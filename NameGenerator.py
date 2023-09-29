# Simple name generator program based on databases;
# This project was done as a way to learn GUI creation with Tkinter,
# aswell as file manipulation in Python and program distribution with pyinstaller,
# it is not good or a particularly useful program, but it is a functional one.
import csv
import os
import random
import tkinter

## Variables Base Values
pickedAmount = 2  # Amount of nicks being picked from pool
nickInherits = 3  # Amount of letters from each parent to inherit
baseNamesFile = "internal/brazilianLeagueNames.csv" # Default database
trashIconFile = "internal/trashResized.png"
brazilFlag = "internal/brazilFlag.png"
usaFlag = "internal/usaFlag.png"
programVersion = ".1"

# Language transcripts for translation
english = [
    "Nick Generator",
    "Random start position",
    "Two names",
    "Your new nickname is",
    "Get nickname",
    "Pick a database to use!"
]
portuguese = [
    "Gerador de Nick",
    "Posição inicial aleatória",
    "Nome composto",
    "    Seu novo nome é",
    "Gerar nome",
    "Escolha database a usar!"
]
defaultLanguage = english

englishHover = [
    "The X variable is the amount\n\
of nicks being picked from the\n\
available pool on database.\
\nDefault value: 2.",

    "The Y variable is the amount\n\
of letters your generated nick is\n\
gonna inherit from each parent\n\
previously picked on X.\n\
Default value: 3.",

    "By default the letters your generated\n\
nick inherit start counting from the first\n\
letter of parents' name.\n\
By checking 'Random start position' this\n\
start position is randomized, starting from\n\
any valid point.",

    "'Two names' places a random space in\n\
your generated nick, giving the impression\n\
that you are receiving 'First Second' names.",

    "This program uses databases based on\n\
existing proplayer's names, this dropdown menu\n\
allows you to choose which database to pick from\n\
to form your generated name. Also there's an\n\
example database called 'baseNames' that contains\n\
fruit names.",

    "Click to generate a new nickname.",

    "Click to clean the nickname box."
]
portugueseHover = [
    "A variável X é a quantidade\n\
de nicks que serão escolhidos da\n\
lista de nicks disponíveis na\n\
base de dados.\n\
Valor padrão: 2.",

    "A variável Y é a quantidade\n\
de letras que o nome gerado vai\n\
herdar de cada pai que foi\n\
previamente escolhido no X.\n\
Valor padrão: 3.",

    "Por padrão, as letras do nick gerado\n\
começam a contar a partir da primeira\n\
letra do nick previamente escolhido.\n\
Ao marcar 'Posição inicial aleatória' essa\n\
posição é aleatorizada, começando por\n\
qualquer ponto válido encontrado.",

    "'Nome composto' adiciona um espaço\n\
aleatório no meio do nome gerado, dando\n\
a impressão que você está recebendo\n\
'Nome Sobrenome'.",

    "Esse program utiliza de bases de dados\n\
baseadas em nomes de jogadores profissionais\n\
que existem, esse menu dropdown lhe permite\n\
escolher de qual base de dados os nomes que\n\
serão escolhidos para formar seu nick gerado virão.\n\
Também tem uma database exemplo chamada\n\
'baseNames', ela contém nomes de frutas.",

    "Clique para gerar seu nome.",

    "Clique para limpar a lista de nomes."
]

# Find file folder
bundle_dir = os.path.abspath(os.path.dirname(__file__))

def main():
    # Create window
    mainWindow = tkinter.Tk()
    mainWindow.title("")
    mainWindow.resizable(0, 0)

    # Calculations for windows
    w = 182 # width for window
    h = 344 # height for window

    # get screen width and height
    ws = mainWindow.winfo_screenwidth() # width of the screen
    hs = mainWindow.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # TKinter Variables
    global pickedAmountTK
    pickedAmountTK = tkinter.IntVar()
    pickedAmountTK.set(pickedAmount)
    global nickInheritsTK
    nickInheritsTK = tkinter.IntVar()
    nickInheritsTK.set(nickInherits)
    global varCheckA
    varCheckA = tkinter.IntVar()
    global varCheckB
    varCheckB = tkinter.IntVar()
    global dropdownVariable
    dropdownVariable = tkinter.StringVar()
    dropdownVariable.set(f"{defaultLanguage[5]}")
    dropdownOptions = [
        "baseNames",
        "brazilianLeagueNames"
    ]

    # Widgets create and config
    labelTitle = tkinter.Label(text=f"{defaultLanguage[0]}", font=("Papyrus", 17))
    labelVersion = tkinter.Label(text=f"v{programVersion}", font=("Arial", 8))

    # Brazil language flag
    file_path2 = os.path.join(bundle_dir, brazilFlag)
    iconPT = tkinter.PhotoImage(file=rf"{file_path2}", width=20, height=20)
    languagePT = tkinter.Button(image=iconPT, border=0, command=lambda: languageButtons(portuguese, portugueseHover, labelTitle, labelCheckA, labelCheckB, dropdownVariable, labelNick, generateButton, labelX, labelY, dropdownMenu, cleanButton))
    # English language flag
    file_path3 = os.path.join(bundle_dir, usaFlag)
    iconEN = tkinter.PhotoImage(file=rf"{file_path3}", width=20, height=20)
    languageEN = tkinter.Button(image=iconEN, border=0, command=lambda: languageButtons(english, englishHover, labelTitle, labelCheckA, labelCheckB, dropdownVariable, labelNick, generateButton, labelX, labelY, dropdownMenu, cleanButton))

    labelX = tkinter.Label(text="X")
    varX = tkinter.Scale(orient="horizontal", length=120, from_=1, to=20, width=15, sliderlength=25, variable=pickedAmountTK)
    labelY = tkinter.Label(text="Y")
    varY = tkinter.Scale(orient="horizontal", length=120, from_=1, to=20, width=15, sliderlength=25, variable=nickInheritsTK)

    checkA = tkinter.Checkbutton(variable=varCheckA)
    labelCheckA = tkinter.Label(text=f"{defaultLanguage[1]}")
    checkB = tkinter.Checkbutton(variable=varCheckB)
    labelCheckB = tkinter.Label(text=f"{defaultLanguage[2]}")
    dropdownMenu = tkinter.OptionMenu(mainWindow, dropdownVariable, *dropdownOptions)

    labelNick = tkinter.Label(text=f"{defaultLanguage[3]}", font=("Arial", 11))
    nickList = tkinter.Listbox(width=26, height=4)

    generateButton = tkinter.Button(mainWindow, width=12,  text=f"{defaultLanguage[4]}", command=lambda: clickButton(nickList))

    # Get trash icon path
    file_path = os.path.join(bundle_dir, trashIconFile)
    iconTrash = tkinter.PhotoImage(file=rf"{file_path}")
    cleanButton = tkinter.Button(image=iconTrash, command=lambda: nickList.delete(0, 999))

    # Widgets placement
    labelTitle.place(x=4, y=10)
    languagePT.place(x=157, y=1)
    languageEN.place(x=134, y=1)

    labelX.place(x=20, y=60)
    varX.place(x=36, y=41)
    labelY.place(x=20, y=100)
    varY.place(x=36, y=81)

    checkA.place(x=20, y=125)
    labelCheckA.place(x=40, y=126)
    checkB.place(x=20, y=150)
    labelCheckB.place(x=40,y=151)
    dropdownMenu.place(x=10, y=174)

    labelNick.place(x=15, y=205)
    nickList.place(x=11, y=225)
    labelVersion.place(x=156 ,y=325)
    generateButton.place(x=21, y=305)
    cleanButton.place(x=128, y=305)

    # Widgets hover default
    CreateToolTip(labelX, text=f"{englishHover[0]}")
    CreateToolTip(labelY, text=f"{englishHover[1]}")
    CreateToolTip(labelCheckA, text=f"{englishHover[2]}")
    CreateToolTip(labelCheckB, text=f"{englishHover[3]}")
    CreateToolTip(dropdownMenu, text=f"{englishHover[4]}")
    CreateToolTip(generateButton, text=f"{englishHover[5]}")
    CreateToolTip(cleanButton, text=f"{englishHover[6]}")

    # Set window config and display window
    mainWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # Change window icon when open
    file_path1 = os.path.join(bundle_dir, "internal/letraN.png")
    iconProgram = tkinter.PhotoImage(file=rf"{file_path1}")
    mainWindow.iconphoto(False, iconProgram)

    mainWindow.mainloop()


def clickButton(nickList):
    # When button clicked call function generateNick passing default database
    generatedNick = generateNick(baseNamesFile)
    nickList.insert(0, generatedNick) # Insert generated nick in listbox


def languageButtons(language, languageHover, labelTitle, labelCheckA, labelCheckB, dropdownVariable, labelNick, generateButton, labelX, labelY, dropdownMenu, cleanButton):
    # Receive widgets and apply relative translation to them
    labelTitle.config(text= f"{language[0]}")
    labelCheckA.config(text= f"{language[1]}")
    labelCheckB.config(text= f"{language[2]}")
    dropdownVariable.set(f"{language[5]}")
    labelNick.config(text= f"{language[3]}")
    generateButton.config(text= f"{language[4]}")
    defaultLanguage[5] = language[5]
    CreateToolTip(labelX, text=f"{languageHover[0]}")
    CreateToolTip(labelY, text=f"{languageHover[1]}")
    CreateToolTip(labelCheckA, text=f"{languageHover[2]}")
    CreateToolTip(labelCheckB, text=f"{languageHover[3]}")
    CreateToolTip(dropdownMenu, text=f"{languageHover[4]}")
    CreateToolTip(generateButton, text=f"{languageHover[5]}")
    CreateToolTip(cleanButton, text=f"{languageHover[6]}")


def generateNick(baseNamesFile):
    # Check if user picked new database from dropdown menu, if not, go with default
    if dropdownVariable.get() != defaultLanguage[5]:
        baseNamesFile = "internal/" + dropdownVariable.get() + ".csv"

    # Get database path and open file
    file_path = os.path.join(bundle_dir, baseNamesFile)
    file = open(file_path, "r", encoding="utf-8")

    # Load rows(nicks in database) on buffer, store buffer in nickList
    buffer = csv.reader(file)
    nickList = []
    for row in buffer:
        nickList.append(row)
    # print(nickList) # DEBUG
    # Call pickNicks with nickList stored database
    # Then call shuffleNicks with result
    generatedName = shuffleNicks(pickNicks(nickList))
    return generatedName # Return generatedName to clickButton to be added to Listbox


def pickNicks(nickList):
    nickGeneratedList = []
    for i in range(pickedAmountTK.get()): # Retirate over pickedAmountTK
        x = random.randint(0, (len(nickList) - 1))
        # Store picked nicks from nickList to nickGeneratedList
        nickGeneratedList.append(nickList[x])
    # print(nickGeneratedList) # DEBUG
    return nickGeneratedList


def shuffleNicks(nickGeneratedList):
    # print(nickGeneratedList) # DEBUG
    shuffledGenerated = ""
    if varCheckB.get() == 1: # Two Names checkbox
        twonameSpace = random.randint(1, pickedAmountTK.get() - 1)

    for i in range(pickedAmountTK.get()): # Reiterate over pickerAmountTK
        # Store nickInheritsTK amount of letters on previously picked nicks to new nickname
        string = "".join(nickGeneratedList[i])
        if varCheckB.get() == 1 and twonameSpace == i:
            shuffledGenerated += " "        
        if varCheckA.get() == 1: # Random start position checkbox
            stringRandomized = randomLetters(string)
            shuffledGenerated += stringRandomized
        else: # By default, start position is first letter
            stringRandomized = string[0:nickInheritsTK.get()]
            shuffledGenerated += stringRandomized
    generatedName = shuffledGenerated.title()
    return generatedName


def randomLetters(string):
    # Make sure that random letters inherit don't go longer
    # than Parents nick length. Example: Y = 3, Parent name = Zuao,
    # randomizer should only pick start in 0(Zua) or 1(uao).

    # Randomize where to start couting based on last valid letter
    lastValid = len(string) - (nickInheritsTK.get() - 1)
    startCount = random.randint(0, lastValid - 1) # Account for 0 indexed

    # Get nickInherits amount of randomized letters starting on startCount
    name = ""
    for i in range(nickInheritsTK.get()):
        name += string[startCount]
        startCount += 1
    return name # Return to shuffleNicks function


# Code below is entirely grabbed from stackoverflow: Question <20399243>
# Display description on widget hover with cursor
class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = tkinter.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tkinter.Label(tw, text=self.text, justify=tkinter.LEFT,
                      background="#ffffe0", relief=tkinter.SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


main()
