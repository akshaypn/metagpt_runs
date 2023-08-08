## database.py

import sqlite3

class Database:
    def __init__(self, db_file: str) -> None:
        """
        Initializes the Database object.

        Args:
            db_file (str): The path to the SQLite database file.
        """
        self.db_file = db_file

    def save_game_state(self, game_state: dict) -> None:
        """
        Saves the game state to the database.

        Args:
            game_state (dict): The game state to be saved.
        """
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()

        # Create the game_state table if it doesn't exist
        c.execute('''CREATE TABLE IF NOT EXISTS game_state
                     (key TEXT PRIMARY KEY, value TEXT)''')

        # Insert or update the game state in the database
        for key, value in game_state.items():
            c.execute("INSERT OR REPLACE INTO game_state VALUES (?, ?)", (key, str(value)))

        conn.commit()
        conn.close()

    def load_game_state(self) -> dict:
        """
        Loads the game state from the database.

        Returns:
            dict: The loaded game state.
        """
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()

        # Retrieve the game state from the database
        c.execute("SELECT * FROM game_state")
        rows = c.fetchall()

        game_state = {}
        for row in rows:
            key, value = row
            game_state[key] = value

        conn.close()

        return game_state
