from . import lexicalParser
from . import syntacticParser
from . import getLetterList
from .modifyLetterVal import letters

# 语义分析接口类
class SeA:
    def __init__(self, path):
        self.s = ''
        with open(path, 'r') as f:
            self.s = f.read()
            f.close()
        self.Lparser = lexicalParser.lexicalParser()
        self.tokens,_ = self.Lparser.parser(expression=self.s)
        # print(tokens)
        # print(tokens[0].value, tokens[0].type)
    def gettoken(self):
        return self.tokens
    # 获取变量列表
    def getvar(self):
        self.letterList = getLetterList.getLetterList().getList(tokens=self.tokens)
        #print(letterList)
        return self.letterList
    # 输入变量取值
    def inputvalue(self, varvalue):
        letters.modifyLetterList(letters=self.letterList,vals=varvalue)
    # 获取语法分析结果
    def getres(self):
        Sparser = syntacticParser.syntacticParser()
        result = Sparser.getValue(self.s)
        print("res:"+str(result))
        return result

if __name__=="__main__":
    SeAma = SeA("test/test.txt")
    print("token:")
    print(SeAma.gettoken())
    
    varlist = SeAma.getvar()
    print("varlist:")
    print(varlist)
    x = 4
    valuelist = []
    for i in range(x,x+len(varlist)):
        valuelist.append(i)
    
    SeAma.inputvalue(valuelist)

    print("res:"+str(SeAma.getres()))

