"""
from typing import List, Optional
from object import Object

class Room:
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        self.objects = []

    def add_object(self, obj: Object) -> None:
        self.objects.append(obj)

    def remove_object(self, obj: Object) -> None:
        self.objects.remove(obj)

    def get_objects(self) -> List[Object]:
        return self.objects

    def get_object(self, name: str) -> Optional[Object]:
        for obj in self.objects:
            if obj.name == name:
                return obj
        return None
"""

from typing import List, Optional
from object import Object

class Room:
    def __init__(self, name: str, description: str) -> None:
        """
        Initializes the Room object.

        Args:
            name (str): The name of the room.
            description (str): The description of the room.
        """
        self.name = name
        self.description = description
        self.objects = []

    def add_object(self, obj: Object) -> None:
        """
        Adds an object to the room.

        Args:
            obj (Object): The object to be added.
        """
        self.objects.append(obj)

    def remove_object(self, obj: Object) -> None:
        """
        Removes an object from the room.

        Args:
            obj (Object): The object to be removed.
        """
        self.objects.remove(obj)

    def get_objects(self) -> List[Object]:
        """
        Returns a list of objects in the room.

        Returns:
            List[Object]: A list of objects in the room.
        """
        return self.objects

    def get_object(self, name: str) -> Optional[Object]:
        """
        Returns the object with the specified name, if it exists in the room.

        Args:
            name (str): The name of the object.

        Returns:
            Optional[Object]: The object with the specified name, or None if it doesn't exist.
        """
        for obj in self.objects:
            if obj.name == name:
                return obj
        return None
