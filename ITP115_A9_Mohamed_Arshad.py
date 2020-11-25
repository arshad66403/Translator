# Jakub Nogalski, jnogalsk@usc.edu
# ITP 115, Spring 2020
# Assignment 9
# Description:
# The program will read a csv file, ask the user to select a language and read the file to create a list of words in tha language
# we will ask the user for a word and then translate that word


def getLanguages(fileName):
    fileIn = open(fileName, "r")
    line = fileIn.readline()
    line.strip()
    data = line.split(",")
    fileIn.close()
    return data

def getSecondLanguage(langList):
    joinedList = ", ".join(langList)
    print("Language Translator\nTranslate English words to one of the following Languages:", joinedList)
    userLang = input("Enter a language: ")
    while userLang.capitalize() not in langList:
        userLang = input("This program does not support this language \nEnter a language: ")
    return userLang.capitalize()

def readFile(langList, langStr, fileName):
    fileIn = open(fileName, "r")
    indexOf = langList.index(langStr)
    newList = []
    fileIn.readline()
    for line in fileIn:
        line = line.strip()
        dataList = line.split(",")
        numStr = dataList[indexOf]
        newList.append(numStr)
    fileIn.close()
    return newList

def createResultsFile(language, resultsFile):
    resultsFile = open(resultsFile, "w")
    resultsFile.write("Words translated from English to %s \n" %(language))
    resultsFile.close()

def translateWords(englishList, secondList, resultsFile):
    fileOut = open(resultsFile, "a")
    run = True
    while run:
        wordToTranslate = input("Enter your word to translate: ")
        if wordToTranslate not in englishList:
            print("%s is not in the English List" %(wordToTranslate))
            again = input("Another word (y or n)? ")
            while again.lower() != "y" and again.lower() != "n":
                again = input("Another word (y or n)? ")
            if again == "n":
                print("Translated words have been saved to %s" % (resultsFile))
                run = False
        else:
            location = englishList.index(wordToTranslate)
            translation = secondList[location]
            if translation == "-":
                print("Your word has no translation")
            else:
                print("%s is translated to %s" % (wordToTranslate, translation))
                print(wordToTranslate, "=",  translation, file=fileOut)
            again = input("Another word (y or n)? ")
            while again.lower() != "y" and again.lower() != "n":
                again = input("Another word (y or n)? ")
            if again == "n":
                print("Translated words have been saved to %s" %(resultsFile))
                run = False

def main():
    fileName = ("languages.csv")
    langList = getLanguages(fileName)
    langStr = getSecondLanguage(langList)
    englishList = readFile(langList, "English", fileName)
    secondLanguage = readFile(langList, langStr, fileName)
    nameOfFile = input("Enter a name for the results file (%s.txt): " % (langStr))
    createResultsFile(langStr, nameOfFile)
    translateWords(englishList, secondLanguage, nameOfFile)


main()