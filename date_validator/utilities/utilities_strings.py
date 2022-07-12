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
            Given a line, it properly formats the line such that it has the
            given length.

            :param line_0: The line to be formatted.

            :return: The formatted line, at the given level of indentation.
        """

        # Get the indent level.
        indent_0 = "" if indentation == 0 else get_indent(indentation)

        # The base string.
        base_0 = [indent_0]

        # The words.
        tokens_0 = line_0.split(" ")

        # Where the lines will be stored.
        lines_0 = []

        # For every token.
        for i_0, word_0 in enumerate(tokens_0):

            # Build the line.
            base_0.append(word_0)

            # Check for character length.
            if len(" ".join(base_0)) > characters:
                lines_0.append(" ".join(base_0[:-1]))
                base_0 = [indent_0, base_0[-1]]

        # Append the last line, if needed.
        if len(base_0) > 1:
            lines_0.append(" ".join(base_0))

        return "\n".join(lines_0)

    # //////////////////////////////////////////////////////////////////////////
    # Implementation
    # //////////////////////////////////////////////////////////////////////////

    # Split the string at the new line characters.
    lines = string.split("\n")

    # For every line.
    for i, line in enumerate(lines):
        # Try to format the line.
        lines[i] = set_length_0(line)

    return "\n".join(lines)


# ##############################################################################
# TO DELETE
# ##############################################################################


if __name__ == "__main__":

    # TODO: MAKE TESTS FOR THESE FUNCTIONS, THIS IS POSSIBLE.
    # TODO: MUST BE REMOVED; FUNCTION MUST BE IMPROVED TO HANDLE LONGER WORDS.
    text = (
        "This is just an example of some text that I have written. For "
        "example:\nWe shall start by taking this sentence and just writing "
        "this, a story. This is really not meant to be anything sophisticated, "
        "but just an example of a paragraph that will be turned into a block "
        "of text with the proper length of each line. Of course, this is meant "
        "to be a test, not the reallity.\nOh, yes, just for the fun of it, this"
        " can contain words that are reaaaaaaaaaaaaaaaally long and could be, "
        "potentially formatted in a better way."
    )

    # Set the string to the proper length.
    text = to_length(text, characters=80, indentation=1)

    print(text)
