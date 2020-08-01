import eyed3
from eyed3 import id3

#find directory of mp3 files 
directory = input("Enter mp3 directory: ")
print(directory)

tag = id3.Tag()
tag.parse("/home/benjamin/Music/AFI - Miss MurderLyrics.mp3")
print(tag.artist)