import eyed3, os
from eyed3 import id3

#introductory and summary of script 
print("*************************************")
print("Running changeArtist script! \n This will change the metadata by setting an artist name")
print("*************************************")

print();

#step 1: gather user input
directory = input("Enter mp3 directory: ")
print(directory)
artistName = input("Enter artist name: ")
print(artistName)

print();

#step 2: run eyeD3 
mp3List = os.listdir(directory)
for song in mp3List:
	#initiate eyeD3 functionality 
	tag = id3.Tag()

	#find song path 
	songPath = directory + "/" + song
	print("running")
	print(songPath)

	#open song 
	tag.parse(songPath)
	
	#change artist metadata
	tag.artist = artistName

	#save song file 
	tag.save()

print()
print('*************************************')
print('DONE')