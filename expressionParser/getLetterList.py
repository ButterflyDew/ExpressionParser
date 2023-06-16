class getLetterList:
    def __init__(self) -> None:
        pass
    
    def getList(self, tokens):
        ret = []
        for i in tokens:
            if i.type == 'LETTER' and (i.value not in ret):
                ret.append(i.value)
        
        return ret