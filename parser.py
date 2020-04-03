import tokenizer

token = []  # List that holds all the LexKind and value pairs.  token[0] holds the position of the line
cSymbol = ''


# function to take the list and goes to teh next system
def nextSymbol():
    global token
    global cSymbol

    pos = token[0] + 1

    if pos == len(token):
        cSymbol = 'EOL'
    else:
        token[0] = pos
        cSymbol = token[pos][1]
        if token[pos][0] == 'end-of-text':
            return


# syntax for expression
def expr():
    booleanExpr()


# syntax for boolean expression
def booleanExpr():
    booleanTerm()
    if cSymbol == "EOL":
        return

    while cSymbol == "or":
        nextSymbol()
        if cSymbol == "EOL":
            return
        booleanTerm()


# syntax for boolean term
def booleanTerm():
    booleanFactor()
    if cSymbol == "EOL":
        return

    while cSymbol == "and":
        nextSymbol()
        if cSymbol == "EOL":
            return
        booleanFactor()


# syntax for boolean factor
def booleanFactor():
    if cSymbol == "not":
        nextSymbol()
        if cSymbol == "EOL":
            return

    arithmeticExpr()
    if cSymbol == "EOL":
        return

    if cSymbol == "=" or cSymbol == "<":
        nextSymbol()
        if cSymbol == "EOL":
            return
        arithmeticExpr()


# syntax for arithmetic expression
def arithmeticExpr():
    term()
    if cSymbol == "EOL":
        return
    while cSymbol == "+" or cSymbol == "-":
        nextSymbol()
        if cSymbol == "EOL":
            return
        term()


# syntax for term
def term():
    factor()
    if cSymbol == "EOL":
        return
    while cSymbol == "*" or cSymbol == "/":
        nextSymbol()
        if cSymbol == "EOL":
            return
        factor()


# syntax for factor
def factor():
    lexKind = token[token[0]][0]

    if cSymbol in ["True", "False", tokenizer.digits]:
        literal()

    elif lexKind == "ID":
        nextSymbol()
        if cSymbol == "EOL":
            return

    elif lexKind == 'NUM':
        nextSymbol()
        if cSymbol == "EOL":
            return

    elif cSymbol in tokenizer.identifier:
        nextSymbol()
        if cSymbol == "EOL":
            return
    # if their is a left parenthesis, their is a right one as well
    elif cSymbol == "(":
        nextSymbol()
        if cSymbol == "EOL":
            return

        expr()
        accept(")")
    # Error Checking
    else:
        expected()
        quit()


# syntax for literal
def literal():
    if cSymbol in tokenizer.digits:
        nextSymbol()
        if cSymbol == "EOL":
            return
    else:
        booleanLiteral()


# syntax for boolean literal
def booleanLiteral():
    if cSymbol == "True" or cSymbol == "False":
        nextSymbol()
        if cSymbol == "EOL":
            return


# makes sure their is a symbol in the language, if teh symbol is not then displays
# an error message
def accept(symbol):
    if cSymbol == symbol:
        nextSymbol()
        if cSymbol == "EOL":
            return
    # error checking
    else:
        print("SYNTAX ERROR")
        quit()


# if a symbol is not in the grammar, an error message is displayed telling which symbol
# is not in the grammar
def expected():
    if cSymbol not in (tokenizer.identifier, tokenizer.keywords, tokenizer.symbols):
        print("Error! ", cSymbol, " is not a accepted symbol")
        return


# driver function
def main():
    global token
    # calling the program that used in Project 1 and print out the table
    dSymbol = tokenizer.main()

    print('-' * 40)
    # goes through the file and reads teh symcols line by line
    for v in dSymbol.values():
        token = v
        nextSymbol()
        if cSymbol == "EOL":
            return
        expr()
    # output for completing the table
    print("Parsing Completed with with no errors.")


if __name__ == "__main__":
    main()
