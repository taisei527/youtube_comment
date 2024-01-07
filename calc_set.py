from itertools import combinations


class set:
    def __init__(self, parnum):
        self.mainset = []
        self.parset = []
        self.allpar = []
        self.index = []
        self.parnum = parnum


    def calcparset(self, parlist):
        s = parlist
        self.parset = list(combinations(s, self.parnum))
        self.allpar.append(self.parset)
        for i in range(0, len(self.parset)): self.parset[i] = sorted(self.parset[i])


    @staticmethod
    def findIndex(l, x):
        if x in l:
            return l.index(x)
        else:
            return -1


    def findText(self, ltext, usr, ind, x):
        for i in range(len(ind)):
            d = self.findIndex(ind[i], x)
            if d != -1:
                return ltext[i][d], usr[i][d]
        else:
            return -1
    

    def addSerchPar(self, textNum):
        for i in self.parset:
            fI = self.findIndex(self.mainset, i)
            if fI != -1:

                #ソート追加処理
                if fI == 0: self.index[0].append(textNum)
                else:
                    j = 1
                    while fI-j >= 0 and len(self.index[fI-j]) == len(self.index[fI]): 
                        j += 1
                    else:
                        j -=1
                        #print(self.parnum, self.mainset[fI], fI, j)
                        self.index[fI].append(textNum)
                        self.mainset[fI], self.mainset[fI-j] = self.mainset[fI-j], self.mainset[fI]
                        self.index[fI], self.index[fI-j] = self.index[fI-j], self.index[fI]
                        #print(self.parnum, self.mainset[fI], fI, j)
            else:
                self.mainset.append(i)
                self.index.append([textNum])


    def subSerchPar(self):
        for i in self.allpar[0]:
            fI = self.findIndex(self.mainset, i)
            if len(self.index[fI])>1: 

                j = 1
                while fI+j < len(self.index) and len(self.index[fI+j]) == len(self.index[fI]): 
                    j += 1
                else:
                    j -=1
                    self.index[fI].pop(0)
                    self.mainset[fI], self.mainset[fI+j] = self.mainset[fI+j], self.mainset[fI]
                    self.index[fI], self.index[fI+j] = self.index[fI+j], self.index[fI]

            else:
                self.mainset.pop(fI)
                self.index.pop(fI)


    def addpar(self, parlist, textNum):
        self.calcparset(parlist)
        self.addSerchPar(textNum)

    #もっとも古いテキストのデータを消去
    def subpar(self):
        if len(self.allpar)!=0:
            self.subSerchPar()
            self.allpar.pop(0)
        else:
            print("古いデータが見つからず、テキストを消去できません。")