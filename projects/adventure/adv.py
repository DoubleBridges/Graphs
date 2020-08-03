from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Keep track of rooms that have been visited
visited = set()

# Keep track of directions back to a room with available exits
anchorline = Stack()

# Dictionary for reversing the direction you've travelled in order to add them to the anchorline
inverted_dir = {"n": "s", "s": "n", "e": "w", "w": "e"}

no_of_rooms = len(room_graph)

while len(visited) < no_of_rooms:
    # Create a move variable
    next_room = None

    for direction in player.current_room.get_exits():
        # For every way out not in visited, make that the value of next_room
        if player.current_room.get_room_in_direction(direction) not in visited:
            next_room = direction

    if next_room is not None:

        # Add the move to the path
        traversal_path.append(next_room)
        # Add the inverse to the anchorline
        anchorline.push(inverted_dir[next_room])
        # Move to next room and add it to visited
        player.travel(next_room)
        visited.add(player.current_room)

    # If there are no exits, travel back up the
    # anchorline until exits are available
    else:
        # Get the direction back off the top of the stck
        next_room = anchorline.pop()
        # Add it to you traversal path
        traversal_path.append(next_room)
        # Go there
        player.travel(next_room)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited"
    )
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
