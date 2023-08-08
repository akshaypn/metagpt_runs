## utils.py

import random

class Utils:
    @staticmethod
    def get_random_number(min_value: int, max_value: int) -> int:
        """
        Generates a random number between min_value and max_value (inclusive).

        Args:
            min_value (int): The minimum value of the random number.
            max_value (int): The maximum value of the random number.

        Returns:
            int: A random number between min_value and max_value.
        """
        return random.randint(min_value, max_value)
