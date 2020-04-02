# all global variables for the functions to call on
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letters = ["a", "b", "c", "d", "e", "f", "g", 'h', "i", "j", "k", "l", "m", "n", "o", "p", "q", "u", "r", "s", "t", "u",
           "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
           "U", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
identifier = digits + letters + ['_']
keywords = ['begin', 'end', 'bool', 'int', 'if', 'then', 'else', 'fi', 'while', 'do', 'od', 'print', 'or', 'and', 'not',
            'true', 'false']
symbols = ['=', '<', '+', '-', '*', '(', ')', ':=', ';', ':', '/']


# reads the next lexeme
def next(f, counter, EOL, lineNumber):
    lex = ''
    char = ''
    EOF = False
    EOL = False

    while True:
        # f.read looks ahead for anything in the file
        char = f.read(1)
        # error checking
        if char not in identifier and char not in symbols and char not in ['\n', ' ', '/', '']:
            print("error in line", lineNumber, "position", counter, 'Character ', char)
            quit()
        counter += 1
        # seeing if it is at the end of file
        if char == '':
            EOF = True
        # seeing if its end of line
        elif char == '\n':
            EOL = True
        # add the char variable to the lex variable
        elif char != ' ':
            lex += char
        # resets the  lex, counter and char variable and increments the line number
        if lex == '//':
            f.readline()
            lex = ''
            counter = 0
            char = ''
            lineNumber += 1
        # breaks the loops after lexeme is found
        if EOF or (EOL and lex != '') or (lex != '' and char == ' '):
            break

    return lex, counter, EOL, lineNumber


# reads the lex variable  and returns the kinds of  lex
def kind(lex):
    if lex == '':
        return "end-of-text"
    elif lex.isnumeric():
        return "NUM"
    elif lex.lower() in keywords or lex[0] in symbols:
        return lex
    elif lex[0].lower() in identifier:
        return "ID"
    return


# reads the  kind if the lexeme and assigns the lexeme a variable
#returns the value of the lexeme (if it is an “ID” or a “NUM”).
def value(lex, lexkind):
    if lexkind == 'NUM':
        return int(lex)
    elif lexkind =="ID":
        return lex
    else: 
        return lex    


# finds out the  position of the lexeme
def postion(lex, counter):
    return counter - len(lex)


def main():
    # initialize variables
    EOL = False
    counter = 0
    lexkind = ''
    lineNumber = 1
    linePosition = 0
    # opens file
    
    dSymbol={}
    f = open("input.txt", "r")
    print("{0:5}{1:10}{2:15}{3:15}".format('Line', 'Position', 'Kind', 'Value'))
    print("-" * 40)
    # calls on all functions
    while lexkind != "end-of-text":
        lex, counter, EOL, lineNumber = next(f, counter, EOL, lineNumber)

        lexkind = kind(lex)
        lexval = value(lex, lexkind)
        linePosition = postion(lex, counter)
        print("{0:<5}{1:<10}{2:15}{3:<15}".format(lineNumber, linePosition, lexkind, lexval))
        #lSymbol.append([lineNumber,lexkind,lexval])
        if lineNumber not in dSymbol:
            dSymbol[lineNumber] = [0,(lexkind,lexval)]
        else: 
             dSymbol[lineNumber].extend([(lexkind,lexval)])

        if EOL:
            counter = 0
            lex = ''
            lineNumber += 1
    
    return dSymbol


if __name__ == "__main__":
    main()
