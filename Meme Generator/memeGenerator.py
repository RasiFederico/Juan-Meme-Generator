from PIL import Image, ImageFont, ImageDraw
from bing_image_downloader import downloader
import random
from random import randrange
import os

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
            break

        elif command.upper() == "SHOW":
            showImage(image)
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

while True:
    print("Welcome to Juan Meme Generator v1.0 made by Federico Rasi")
    print("This app can make a weird image similar to the horse 'Juan Meme'")
    command = input("\nDo you want to download the images? ! CHOOSE 'YES' ONLY IF YOU DON'T HAVE THE 'ImgRAW' FOLDER ANYMORE ! (y/n): ")

    if command.upper() == "Y":
        downloadImages(query_string)
        renderImage()
        break

    elif command.upper() == "N":
        renderImage()
        break

    else:
        print("\n Wrong command, try again.\n")
        continue