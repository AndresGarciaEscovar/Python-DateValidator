""" File that contains the validator functions."""

# ##############################################################################
# Imports
# ##############################################################################

# ##############################################################################
# Functions
# ##############################################################################

# ------------------------------------------------------------------------------
# Check Functions.
# ------------------------------------------------------------------------------


def check_ampm(date: str, dformat: str, ampm: bool) -> bool:
    """
        Checks that the length of the date string matches with that of the
        format and the relative placement within the date and format strings is
        the same.

        :param date: The date to be checked.

        :param dformat: The date format.

        :param ampm: True, if the date is in the 12-hour (am/pm) format.

        :return: True, if the string is NOT given in 24-hour mode or if a single
        appearance of ai (for am) and pi (for pm) are present.
    """

    # Auxiliary variables.
    count0 = 0
    count1 = 0
    length = len(dformat) - 2

    # The date must at least have 2 characters.
    if length < 0:
        return not ampm

    # Set the index to zero.
    index = 0
    for i, _ in enumerate(dformat):
        # Add the count if the ai or pi string exists and get the indexes.
        if dformat[i:i+2] == "ai" or dformat[i:i+2] == "pi":
            count0 += 1
            index = i

        if date[i:i+2] == "ai" or date[i:i+2] == "pi":
            count1 += 1

        # Reached end of string.
        if i == length:
            break

    # Check the trivial cases.
    if not ampm:
        return count0 == 0 and count1 == 0

    if not (count0 == 1 and count1 == 1):
        return False

    return dformat[index:index+2] == date[index:index+2]


def check_csspecial(date: str, dformat: str) -> bool:
    """
        Checks the placement of the special characters.

        :param date: The date to be checked.

        :param dformat: The date format.

        :return: True, if placement of the special characters match in the
         strings. False, otherwise.
    """

    # Check that the strings have the same length.
    valid = len(date) == len(dformat)
    if not valid:
        return valid

    # Get the protected characters.
    protected = get_protected()

    # Check the special characters from the format match.
    for schar_date, schar_format in zip(date, dformat):
        # Validate the characters.
        if schar_format not in protected:
            # If special characters don't match.
            valid = valid and schar_date == schar_format
            if not valid:
                return valid

    return valid


def check_length(date: str, dformat: str) -> bool:
    """
        Checks that the length of the date string matches with that of the
        format.

        :param date: The date to be checked.

        :param dformat: The date format.

        :return: True, if the length of the date string is the same as that of
         date format. False, otherwise.
    """
    return len(date) == len(dformat)


# ------------------------------------------------------------------------------
# Get Functions.
# ------------------------------------------------------------------------------


def get_protected() -> tuple:
    """
        Gets the protected characters.

        :return: The tuple with the protected characters.
    """
    return "Y", "M", "D", "h", "m", "s", "t"


# ------------------------------------------------------------------------------
# Remove Functions.
# ------------------------------------------------------------------------------

def remove_ampm(string: str) -> str:
    """
        Removes the ai or pi string from the given string.

        :param string: The string from which 'ai' or 'pi' string must be
         removed.

        :return: The original string with the 'ai' or 'pi' string removed.
    """
    # Get the marker.
    marker = 0

    # Search for the ai/pi string.
    for i, _ in enumerate(string):
        # Abort if found.
        if string[i:i+2] == "ai" or string[i:i+2] == "pi":
            marker = i
            break

    # Remove the ai string.
    string = string[:marker] + string[marker+2:]

    return string

# ------------------------------------------------------------------------------
# Validate Functions.
# ------------------------------------------------------------------------------


def validate_date(date: str, dformat: str, ampm: bool = False) -> bool:
    """
        Validates that the given date is in the given format. The format string
        defines the possible values for the entry. Y indicates the year, M
        indicates the month, M indicates the month, h indicates an hour, m
        indicates minutes, s the seconds, t the tenths of the second. If the
        date is in 12-hour format, ai (for am) or pi (for pm) must be included
        in the format string.

        :param date: String with the date to be validated.

        :param dformat: The string that represents the format in which the date
         is given. If the date is in 12-hour format, ai (for am) or pi (for pm)
         must be included in the format string.

        :param ampm: True, if the time is given in the am-pm format, i.e., the
         maximum hour is 12. False, otherwise.

        :return: True, if the date is valid and in the proper format.
    """

    # Check the length of the date string and date format.
    valid = check_length(date, dformat)
    if not valid:
        return valid

    # Check that the ai and/or pi fields are included, if needed.
    valid = check_ampm(date, dformat, ampm)
    if not valid:
        return valid

    # If in 12-hour format.
    if ampm:
        # Remove the ai or pi strings.
        date = remove_ampm(date)
        dformat = remove_ampm(dformat)

    # Check special character placement.
    valid = check_csspecial(date, dformat)
    if not valid:
        return valid

    print(date)
    print(dformat)
    print("Here!")


# ##############################################################################
# Main Function
# ##############################################################################


def main() -> None:

    date =    "2pkai2;;11;30:20:32*18,9"
    dformat = "YYYaiY;;MM;DD:hh:mm*ss,t"

    validate_date(date, dformat=dformat, ampm=True)

# ##############################################################################
# Main Program
# ##############################################################################


if __name__ == "__main__":
    main()
