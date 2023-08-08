## puzzle.py
class Puzzle:
    def __init__(self, question: str, answer: str) -> None:
        """
        Initializes the Puzzle object.

        Args:
            question (str): The question of the puzzle.
            answer (str): The answer to the puzzle.
        """
        self.question = question
        self.answer = answer

    def solve(self, answer: str) -> bool:
        """
        Solves the puzzle by checking if the provided answer is correct.

        Args:
            answer (str): The answer to the puzzle.

        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        return answer.lower() == self.answer.lower()
