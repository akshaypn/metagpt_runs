"""
import click
import pygame
import sqlite3
from typing import List, Optional
from room import Room
from object import Object
from puzzle import Puzzle
from database import Database
from utils import Utils
"""

import click
import pygame
import sqlite3
from typing import List, Optional
from room import Room
from object import Object
from puzzle import Puzzle
from database import Database
from utils import Utils

class Game:
    def __init__(self, db_file: str) -> None:
        self.db = Database(db_file)
        self.rooms = []
        self.current_room = None

    def start_game(self) -> None:
        click.echo("Welcome to the text adventure game!")

        game_state = self.db.load_game_state()
        if game_state:
            self.current_room = game_state["current_room"]
            click.echo("Game state loaded.")
        else:
            self.current_room = self.rooms[0].name
            click.echo("New game started.")

        self.play_game()

    def end_game(self) -> None:
        click.echo("Goodbye!")
        pygame.quit()

    def save_game(self) -> None:
        game_state = {"current_room": self.current_room}
        self.db.save_game_state(game_state)
        click.echo("Game state saved.")

    def load_game(self) -> None:
        game_state = self.db.load_game_state()
        if game_state:
            self.current_room = game_state["current_room"]
            click.echo("Game state loaded.")
        else:
            click.echo("No saved game state found.")

    def play_game(self) -> None:
        while True:
            room = self.get_room(self.current_room)
            click.echo(f"\n{room.name}")
            click.echo(room.description)

            objects = room.get_objects()
            if objects:
                click.echo("Objects in the room:")
                for obj in objects:
                    click.echo(f"- {obj.name}: {obj.description}")

            command = click.prompt("What do you want to do? (Type 'help' for a list of commands)")

            if command == "help":
                self.show_help()
            elif command == "quit":
                self.end_game()
                break
            elif command == "save":
                self.save_game()
            elif command == "load":
                self.load_game()
            elif command.startswith("go "):
                self.go_to_room(command[3:])
            elif command.startswith("interact "):
                self.interact_with_object(command[9:])
            else:
                click.echo("Invalid command. Type 'help' for a list of commands.")

    def show_help(self) -> None:
        click.echo("Available commands:")
        click.echo("- help: Display this help message")
        click.echo("- quit: Quit the game")
        click.echo("- save: Save the game state")
        click.echo("- load: Load the game state")
        click.echo("- go <room>: Go to the specified room")
        click.echo("- interact <object>: Interact with the specified object")

    def go_to_room(self, room_name: str) -> None:
        room = self.get_room(room_name)
        if room:
            self.current_room = room_name
            click.echo(f"You are now in the {room_name} room.")
        else:
            click.echo(f"The {room_name} room does not exist.")

    def interact_with_object(self, object_name: str) -> None:
        room = self.get_room(self.current_room)
        obj = room.get_object(object_name)
        if obj:
            obj.interact()
        else:
            click.echo(f"The {object_name} object does not exist in this room.")

    def get_room(self, room_name: str) -> Optional[Room]:
        for room in self.rooms:
            if room.name == room_name:
                return room
        return None

def main():
    db_file = "game_state.db"
    game = Game(db_file)

    room1 = Room("Room 1", "This is room 1.")
    room2 = Room("Room 2", "This is room 2.")

    object1 = Object("Object 1", "This is object 1.")
    object2 = Object("Object 2", "This is object 2.")

    puzzle = Puzzle("What is the answer to life, the universe, and everything?", "42")

    room1.add_object(object1)
    room2.add_object(object2)
    room2.add_object(puzzle)

    game.rooms.append(room1)
    game.rooms.append(room2)

    game.start_game()

if __name__ == "__main__":
    main()
