from PIL import Image, ImageFont, ImageDraw
from bing_image_downloader import downloader
import random
from random import randrange
import os
from os import path

#Animal stuck in weird places
query_string = "Animal stuck in weird places"

def getRandomFile():
    randomFile = getAllFiles()[randrange(len(getAllFiles()))]
    return randomFile

def getAllFiles():
    files = os.listdir('\\'.join(__file__.split('\\')[0:-1]) + "\\ImgRAW\\" + query_string)
    return files

def downloadImages(query):
    downloader.download(query, limit=30,  output_dir="ImgRAW", 
    adult_filter_off=True, force_replace=False, timeout=60)
    
def getRandomName():
    lines = open('\\'.join(__file__.split('\\')[0:-1]) + "\\names.txt").read().splitlines()
    return random.choice(lines)

def saveFile(image, name):
    path = input(r"Enter the path of the folder (Ex: C:\Users\username\Desktop ): ")
    image.save(path + "\\" + name + ".jpg")
    print("Image saved!")

def showImage(image):
    image.show()

def final(image, name):
    while True:
        command = input("Do you want to save the image or just show it? (save/show): ")

        if command.upper() == "SAVE":
            saveFile(image, name)
            redo()
            break

        elif command.upper() == "SHOW":
            showImage(image)
            redo()
            break

        else:
            print("\n Wrong command, try again.\n")
            continue

def renderImage():

    my_image = Image.open('\\'.join(__file__.split('\\')[0:-1]) + "\\ImgRAW\\" + query_string + "\\" + getRandomFile())
    width, eight = my_image.size
    title_font = ImageFont.truetype('arial.ttf', int(width/10))
    my_name = getRandomName()
    title_text = my_name
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((((width/2) - int(width/10)),eight - (eight / 4)), title_text, (255, 255, 255), font=title_font)
    final(my_image, my_name)

def checkFiles():
    
    for i in range(len(getAllFiles())):
        correctName = "Image_" + str(i + 1)
        if getAllFiles()[i] == correctName:
            continue
        
        else:
            getAllFiles()[i] = correctName


def checkForDownload():

    if path.exists('\\'.join(__file__.split('\\')[0:-1]) + "\\ImgRAW\\" + query_string) == True:      

        allFiles = os.listdir('\\'.join(__file__.split('\\')[0:-1]) + "\\ImgRAW\\" + query_string)
        if len(allFiles) < 10:
            return True 

        else:
            return False    


    else:
        return True


def main():

    if checkForDownload() == True:
        downloadImages(query_string)
        checkFiles()
        renderImage()

    else:
        checkFiles()
        renderImage()


def redo():

    while True:
        command = input("\nDo you want to create another meme? (y/n): ")
        
        if command.upper() == "Y":
            main()

        elif command.upper() == "N":
            exit()
        
        else:
            print("\nWrong command, try again!")


print("Welcome to Juan Meme Generator v1.0 made by Federico Rasi")
print("This app can make a weird image similar to the horse 'Juan Meme'")
main()
