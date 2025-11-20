"""
RlDroneSim 
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """I dont know."""
    pass


def get_random_ingredients(kind=None):
    """
    Something
    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]
