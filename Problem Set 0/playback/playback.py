#prompt user for input then replacing spacing with three periods

def playback():
    words = input("Say something: ")
    return '...'.join(words.split())

print(playback())

