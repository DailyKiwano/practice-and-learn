from unittest import mock
import unittest
from question_7_3_jukebox import Media
from question_7_3_jukebox import MediaRack
from question_7_3_jukebox import JukeBox


class TestJukebox(unittest.TestCase):

    song01 = Media("Hell is Forever")
    song02 = Media("Twinkle Twinkle Little Star")
    song03 = Media("Don't Stop Me Now")
    song04 = Media("Yellow Submarine")
    song05 = Media("Beethoven's 5th")
    song06 = Media("Happy Birthday")
    media_rack_01 = MediaRack()
    media_rack_02 = MediaRack()
    media_rack_01.add_media(song01)
    media_rack_01.add_media(song02)
    media_rack_01.add_media(song03)
    media_rack_01.add_media(song04)
    media_rack_01.add_media(song05)
    media_rack_02.add_media(song06)
    my_jukebox = JukeBox()
    my_jukebox.add_rack(media_rack_01)
    my_jukebox.add_rack(media_rack_02)

    def test_media(self):
        self.assertTrue(type(self.song01.title) is str)

    def test_jukebox_library(self):
        self.assertEqual(self.my_jukebox.library, [self.media_rack_01, self.media_rack_02])

    @mock.patch('question_7_3_jukebox.input', create=True)
    def test_select_song(self, mocked_input):
        mocked_input.side_effect = ["10"]
        result = self.my_jukebox.select_song()
        self.assertEqual(result, 'Now Playing: ♫ Happy Birthday ♪')


if __name__ == '__main__':
    unittest.main()
