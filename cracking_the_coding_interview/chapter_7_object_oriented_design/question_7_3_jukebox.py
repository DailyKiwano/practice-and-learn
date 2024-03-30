# Jukebox: Design a musical jukebox using object-oriented principles

# I don't exactly know how a jukebox works, but I'm going to imagine a really old school version that isn't digital.
# This Jukebox has physical trays or racks that cassete tapes? or vinyl records? are stored on. So the Jukebox has maybe
# 5 "racks" or "rows" of physical media storage. Each rack can hold X number of media, maybe 5. So 5 racks of 5 cassette
# tapes. This makes a matrix, and each position in the matrix has a coordinate.

# The user interface of the Jukebox has buttons that you can press say the letter A and number 3 and you'll play
# whatever media is in position A,3 in the matrix.

# This will need a Jukebox class which will have a property that is a list of MediaRack classes
# A MediaRack class that will have a property that is a list of songs. These songs will be classes with a simple title
# property, but they could have another property pointing to the actual .mp3 file or whatever to  actually play it.
# The Jukebox will have a user_interface method that prompts the user for input and validates it, and calls a
# play_song method that retrieves the song in the coordinates provided.


class Media:
    def __init__(self, title: str):
        self.title = title
        self.digital_file_location = ""


class MediaRack:
    def __init__(self):
        self.media = []
        self.max_media = 5

    def add_media(self, media: Media):
        if len(self.media) < self.max_media:
            self.media.append(media)
        else:
            raise Exception("MediaRack is full.")

    def remove_media(self, media: Media):
        if self.media and media in self.media:
            self.media.remove(media)


class JukeBox:
    def __init__(self):
        self.library = []
        self.max_racks = 5

    def add_rack(self, media_rack: MediaRack):
        if len(self.library) < self.max_racks:
            self.library.append(media_rack)

    def remove_rack(self, media_rack: MediaRack):
        if self.library and media_rack in self.library:
            self.library.remove(media_rack)

    def select_song(self) -> str:
        valid_selection_list = []
        for media_rack in self.library:
            for song in media_rack.media:
                selection_option = f"{self.library.index(media_rack)}{media_rack.media.index(song)}"
                valid_selection_list.append(selection_option)
                print(f"{selection_option}: {song.title}")
        selection = None
        while selection not in valid_selection_list:
            selection = str(input("Please enter a song code: "))
        return self.play_song(selection)

    def play_song(self, selection: str) -> str:
        media_rack_index = int(selection[0])
        media_index = int(selection[1])
        song = self.library[media_rack_index].media[media_index]
        musical_note_1 = 9834
        musical_note_2 = 9835
        return f"Now Playing: {chr(musical_note_2)} {song.title} {chr(musical_note_1)}"
