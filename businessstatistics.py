import math
from math import sqrt
from math import pow


class BUSINESSstatistics:
    def __init__(self):
        pass

    def showModels():
        listOfModels = ['PEARSONmodels', '', '']
        return

    def showDescription():
        return """
        -- Statistics for Business Analysis.
           This module will help the beginners to predict business situations by processing unprocessed data.
        -- Rules to use this module is shown here...
            1. First you need to install the module.
            >>> pip install businessstatistics
            2. Import the module in several ways...
            >>> import businessstatistics
            >>> from businessstatistics import *
            >>> import businessstatistics.CLASSNAME functionName
            >>> from businessstatistics import CLASSNAME
            >>> from businessstatistics import functionName
            3. Basics...
                 The module is for the beginners who possess some knowledge in statistics. 
                 Use proper name for the module, class, methods and attributes.
        
        """

class CORRELATIONanalysis:
    def __init__(self):
        pass

    class PEARSONmodel:
        def __init__(self):
            pass

        def pearson(self, x_list, y_list):

            def getSumProductXY(self, passXList, passYList):
                avgXList = sum(passXList) / len(passXList)
                avgYList = sum(passYList) / len(passYList)
                sumXYList = 0
                for index in range(len(passXList)):
                    sumXYList += (passXList[index]-avgXList) * (passYList[index]-avgYList)

                return sumXYList

            sum_product_xy = getSumProductXY(self, x_list, y_list)

            def getStdOfList(passList):
                avgList = sum(passList) / len(passList)
                sumStd = 0
                for value in passList:
                    sumStd += math.pow((value-avgList), 2)

                return sumStd

            stdOfX = sqrt(getStdOfList(x_list))
            stdOfY = sqrt(getStdOfList(y_list))
            stdProductXY = stdOfX * stdOfY
            correlationXY = sum_product_xy / stdProductXY

            return correlationXY

        def getProduct(self, passXList, passYList):
            avgXList = sum(passXList) / len(passXList)
            avgYList = sum(passYList) / len(passYList)
            productList = []
            for index in range(len(passXList)):
                product = (passXList[index] - avgXList) * (passYList[index] - avgYList)
                productList.append(product)
            return productList

        def getSumValuesNotSquared(self, passList):
            avgList = sum(passList) / len(passList)

            sumList = 0
            sumListValues = []
            for index in range(len(passList)):
                sumList = (passList[index] - avgList)
                sumListValues.append(sumList)

            return sumListValues

        def getSumValuesSquare(self, passList):
            avgList = sum(passList) / len(passList)

            sumList = 0
            sumListValuesSq = []
            for index in range(len(passList)):
                sumList = (passList[index] - avgList) * (passList[index] - avgList)
                sumListValuesSq.append(sumList)

            return sumListValuesSq



