# from PIL import Image
#
# im = Image.open("husky.png")
#
# print(dir(im))

class Song:
    def __init__(self, artist, genre, length, album):
        self.artist = artist
        self.genre = genre
        self.length = length
        self.album = album

Love = Song("DEAN", "kpop??", "180 sec", "Single")
Cereal = Song("Crush", "kpop again??", "120 sec", "wonderlost")
IkaretaBaby = Song("Mizuki Ohira", "Jpop now!?", "240 sec", "Single")
DuHast = Song("Rammstein", "German Metal what!?!?", "120 sec", "Sensucht")

print(Love.artist)
print(Cereal.genre)
print(IkaretaBaby.length)
print(DuHast.album)
