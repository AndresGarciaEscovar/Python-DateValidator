"""
    File that contains several string utilities.
"""

# ##############################################################################
# Imports
# ##############################################################################


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# Get Functions
# ------------------------------------------------------------------------------


def get_indent(level: int = 1, spaces: bool = True, nspaces: int = 4) -> str:
    """
        Gets the given number of indentation character.

        :param level: The level of indentation, must be a positive integer; 1 by
         default.

        :param spaces: True, if the indentation must be given as spaces, rather
         than the indentation character.

        :param nspaces: The number of spaces that make an indentation.

        :return: The number of requested indentations.
    """
    # Get the appropriate level.
    level = int(level) if int(level) >= 1 else 1

    return (" " * int(nspaces)) * level if spaces else "\t" * level


# ------------------------------------------------------------------------------
# To Functions
# ------------------------------------------------------------------------------


def to_length(string: str, characters: int = 80, indentation: int = 0) -> str:
    """
        Sets the string to the given number of characters, per line. Deletes
        extra spaces between words and keeps spacing between lines.

        :param string: The string to re-size.

        :param characters: The maximum length of the line.

        :param indentation: The indentation level of the given string; no
         indentation by default, i.e., 0.

        :return: The properly indented and joined string so that its length
         doesn't exceed the given number of characters.
    """

    # //////////////////////////////////////////////////////////////////////////
    # Auxiliary Functions
    # //////////////////////////////////////////////////////////////////////////

    def set_length_0(line_0: str) -> str:
        """
            Given a line, it
        :param line_0:
        :return:
        """

    # //////////////////////////////////////////////////////////////////////////
    # Implementation
    # //////////////////////////////////////////////////////////////////////////

    # Split the string at the new line characters.
    lines = string.strip("\n")

    # For every line.
    for line in lines:
        # Split at the spaces.
        tokens = line.split(" ")
