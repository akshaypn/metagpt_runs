## object.py
class Object:
    def __init__(self, name: str, description: str) -> None:
        """
        Initializes the Object object.

        Args:
            name (str): The name of the object.
            description (str): The description of the object.
        """
        self.name = name
        self.description = description

    def interact(self) -> None:
        """
        Interacts with the object.
        """
        # Implement the interaction logic here
        pass
