import lexicalParser
import syntacticParser
import getLetterList
from .modifyLetterVal import letters


def main():
    path = 'test/test.txt'
    s = ''
    with open(path, 'r') as f:
        s = f.read()
        f.close()
    Lparser = lexicalParser.lexicalParser()
    tokens = Lparser.parser(expression=s)
    print(tokens)
    # print(tokens[0].value, tokens[0].type)
    
    letterList = getLetterList.getLetterList().getList(tokens=tokens)
    print(letterList)
    
    letters.modifyLetterList(letters=letterList, vals=[4])
    for i in letterList:
        print(letters.getMap(i))
    
    Sparser = syntacticParser.syntacticParser()
    result = Sparser.parse(expression=s)
    print(result)
    

if __name__ == '__main__':
    main()