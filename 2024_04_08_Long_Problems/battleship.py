import sys

def in_range(values):
    """
    This helper function checks if all values in a given list are within the 
    range of 0 to 10, and returns True if they are, and False if any value is 
    outside of that range.
    Args:
        values
    Returns:
        the boolean representing whether the values are in range.
    """
    for value in values:
        if value not in range(0,10):
            return False
    return True

class GridPos:
    """
    This class represents a position on a 10x10 battleship board. It has x, y,
    ship, and prev_guessed attributes. x and y are the positions, the ship is 
    the type of ship at the spot, and prev_guessed is a boolean to check if the
    user had already guessed that x and y.
    """
    def __init__(self, x, y):
        """
        This function initializes a GridPos object with the given x and y 
        coordinates, and sets the ship and prev_guessed values to default 
        values of None.
        Parameters:
            x: the x-coord
            y: the y-coord:
        Returns:
            None
        """
        self._x = x
        self._y = y
        self._ship = None
        self._prev_guessed = False

    def __str__(self):
        guessed_str = "❌"
        if self._prev_guessed:
            guessed_str = "✅"
        return f"P({self._x},{self._y}) = {self._ship}\nGuessed: {guessed_str}"

class Board:
    """
    This class represents a 10x10 battleship board. It has a grid attribute and
    a ships attribute, which are both lists.
    """
    def __init__(self):
        """
        This function initializes the Battleship Board by creating a grid and a
        list of ships. It sets the grid attribute to [], then using a loop 
        turns it into a 2D list with a length of 10. Each inner list also has
        a length of 10.
        Parameters:
            None
        Returns:
            None
        """
        self._grid = []
        for i in range(10):
            row = []
            for j in range(10):
                # swap j and i to go row by row rather than column by column
                row.append(GridPos(j,i))
            self._grid.append(row)
        self._ships = []

    def add_ship(self, ship, x, y):
        """
        This function adds a ship to a grid at a specified location, checking
        for any overlapping ships and printing an error if found and exits the 
        program. If there's no overlap, the ship is added to a list and 
        assigned to the grid at the specified location.
        Parameters:
            ship: the Ship object at the specified x and y
            x: the x-coord
            y: the y-coord
        Returns:
            None
        """
        if self._grid[x][y]._ship != None:
            print("ERROR: overlapping ship: " + ship._raw_line)
            sys.exit(0)
        self._ships.append(ship)
        self._grid[x][y]._ship = ship

    def process_guess(self, x, y):
        """
        This method takes in two coordinates and first checks if they are 
        within the range of the game grid. If they are not, it prints an error
        message and returns. Otherwise, it checks if the location has been 
        previously guessed and updates the status accordingly. 
        If the location contains a ship, it marks it as hit and checks if the 
        ship has been sunk. If all ships have been sunk, it prints a game over
        message and ends the game.
        Parameters:
            x: the x-coord
            y: the y-coord
        Returns:
            None
        """
        x, y = int(x), int(y)
        if x not in range(0,10) or y not in range(0,10):
            print("illegal guess")
            return
        location = self._grid[x][y]
        again = ''
        if location._prev_guessed:
            again = ' (again)'
        if location._ship == None:            
            print(f'miss{again}')
        else:
            location._ship.get_points_range()[(x, y)] = 'Hit'
            if location._ship.is_sunk():
                print(f"{location._ship} sunk")    
            else:
                print(f'hit{again}')
        location._prev_guessed = True

        for ship in self._ships:
            if not ship.is_sunk():
                return
            
        print("all ships sunk: game over")
        sys.exit(0)

    def get_ships(self):
        return self._ships
        
class Ship:
    """
    This class represents a ship of the battleship board game.
    It has raw_line, ship, points_range, and size attributes.
    """
    def __init__(self, line):
        """
        This function initializes a ship object with a given line of 
        information, including the ship's abbreviation, coordinates, and size. 
        It also performs error checking to ensure that the ship is placed 
        correctly, has the correct size and is within the bounds of the game 
        board.
        Parameters:
            line
        Returns:
            None
        """
        self._raw_line = line
        abbreviation = line.split()[0]
        x1, y1 = (int(line.split()[1]), int(line.split()[2]))
        x2, y2 = (int(line.split()[3]), int(line.split()[4]))
        self._ship = abbreviation
        abbrev_to_size = { "A": 5, "B": 4, "S": 3, "D": 3, "P": 2 }
        self._points_range = {}
        # this loop iterates over the points of the ship (inclusive)
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                # Each point is given a default value of "not hit"
                self._points_range[(x,y)] = 'Not Hit'
        self._size = max(max(y2,y1)-min(y2,y1)+1, max(x2,x1)-min(x2,x1)+1)
        # ERROR CHECKING (#2, #3, #5)
        # at least one of abs(x2-x1) and abs(y2-y1) must be 0
        if min(abs(x2-x1), abs(y2-y1)) != 0:
            print("ERROR: ship not horizontal or vertical: " + line)
            sys.exit(0)

        values = [x1,x2,y1,y2]
        if not in_range(values):
            print("ERROR: ship out-of-bounds: " + line)
            sys.exit(0)

        if self._size != abbrev_to_size[abbreviation]:
            print("ERROR: incorrect ship size: " + line)
            sys.exit(0)
    
    def get_points_range(self):
        return self._points_range
    
    def get_type(self):
        return self._ship
    
    def is_sunk(self):
        """
        This method checks if the ship has been sunk by comparing the values of
        the points range to a set of len 1 -- every element in the list should
        be the same and that the elements are all 'Hit'
        Parameters:
            None
        Returns:
            a boolean
        """
        pts_range = self.get_points_range().values()
        return len(set(pts_range)) == 1 and list(pts_range)[0] == 'Hit'
    
    def __str__(self):
        return self._ship
    
def handle_placement(input_filename):
    """
    This function takes in an input file containing ship placement information,
    creates a board, and adds the ships to the board according to the given
    coordinates. It then checks if the fleet composition is correct
    returns the board.
    Args:
        input_filename
    Returns:
        the board
    """
    board = Board()
    file = open(input_filename, 'r')
    for line in file:
        ship = Ship(line.strip())
        for point in ship.get_points_range():
            x_pt, y_pt = point[0], point[1]
            board.add_ship(ship, x_pt, y_pt)    
    ship_types = []
    for ship in board.get_ships():
        ship_types.append(ship.get_type())
    # set of ship_types should be as below and len of ships should be 17
    if set(ship_types) != {'A', 'P', 'D', 'B', 'S'} or len(ship_types) != 17:
        print("ERROR: fleet composition incorrect")
        sys.exit(0)
    return board

def handle_guesses(input_filename, board):
    """
    This function takes in an input file and a board object, reads each line in
    the file, and uses the coordinates from each line to call the process_guess
    method on the board object.
    Args:
        input_filename
        board
    Returns:
        None
    """
    file = open(input_filename, 'r')
    for line in file:
        x1, y1 = line.strip().split()
        board.process_guess(x1, y1)

def main():
    placement_file = input()
    guess_file = input()
    board = handle_placement(placement_file)
    handle_guesses(guess_file, board)

if __name__ == '__main__':
    main()

