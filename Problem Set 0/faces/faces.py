#function that takes str parametre
def convert(emoticon):
    #replace all occurance of emticon with emooji equivalent
    convertedText=emoticon.replace(":)","🙂").replace(":(","🙁")
    return convertedText

#main function
def main():
    converted=input("enter text: ")
    print(convert(converted))

main()
