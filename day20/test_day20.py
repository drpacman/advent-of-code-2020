import unittest
import day20

class TestDay20(unittest.TestCase):

    test_tile = [
        [ '.', '.', '#' ],
        [ '#', '.', '#' ],
        [ '#', '#', '.' ]
    ]
    def test_flip_horizontal(self):
        t = day20.Tile('test', self.test_tile)
        t.flip_horizontal()
        result = [
            [ '#', '.', '.' ],
            [ '#', '.', '#' ],
            [ '.', '#', '#' ]
        ]
        self.assertEquals( t.contents, result )
    
    def test_flip_vertical(self):
        t = day20.Tile('test', self.test_tile)
        t.flip_vertical()
        result = [
            [ '#', '#', '.' ],
            [ '#', '.', '#' ],
            [ '.', '.', '#' ]            
        ]
        self.assertEquals( t.contents, result )
    
    def test_rotate_right(self):
        t = day20.Tile('test', self.test_tile)
        t.rotate_right()
        result = [
            [ '#', '#', '.' ],
            [ '#', '.', '.' ],
            [ '.', '#', '#' ]            
        ]
        self.assertEquals( t.contents, result )

        
if __name__ == '__main__':

    unittest.main()