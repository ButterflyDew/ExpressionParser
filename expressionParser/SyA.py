from . import lexicalParser
from . import syntacticParser
from . import getLetterList
from .modifyLetterVal import letters
# 语义分析接口类
class SyA:
    def __init__(self, path):
        s = ''
        with open(path, 'r') as f:
            s = f.read()
            f.close()
        Lparser = lexicalParser.lexicalParser()
        #tokens = Lparser.parser(expression=s)
        
        # letterList = getLetterList.getLetterList().getList(tokens=tokens)
        
        # letters.modifyLetterList(letters=letterList, vals=[2,3])
        
        self.Sparser = syntacticParser.syntacticParser()
        result = self.Sparser.parse(expression=s)
        self.Sparser.genePic(expression=s)

    # 获取是否发生错误
    def geterr(self):
        return self.Sparser.issynerr()