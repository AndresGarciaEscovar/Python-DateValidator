""" File that contains the validator functions."""

# ##############################################################################
# Imports
# ##############################################################################


# General.
import copy


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


def check_not_repeated(pairs: list) -> bool:
    """
        Checks that the requested quantities are not repeated, i.e., that there
        is a single request for a year, a month, a day, an hour, a minute, a
        second and a decimal of a second, at most.

        :param pairs: The tuple of pairs that represent the dictionary entries
         to be checked.

        :return: True, if there are no repeated entries. False, otherwise.
    """

    # Auxiliary variables.
    valid = True
    length = len(pairs) - 1

    # Examine each pair.
    for i, pair0 in enumerate(pairs):
        # No need to compare the last element.
        if i == length:
            break

        # Loop over the shorter list.
        for j, pair1 in enumerate(pairs[i + 1:]):

            # Identical characters in different places -> repeated quantities.
            valid = valid and not pair0[0][0] == pair1[0][0]
            if not valid:
                return valid

    return valid


# ------------------------------------------------------------------------------
# Get Functions.
# ------------------------------------------------------------------------------


def get_protected() -> tuple:
    """
        Gets the protected characters.

        :return: The tuple with the protected characters.
    """
    return "Y", "M", "D", "h", "m", "s", "t"


def get_tokenized(string: str) -> tuple:
    """
        Tokenizes the given string at the special characters, i.e., the
        non-protected characters.

        :param string:

        :return: The list of generated, non-empty strings that are generated
         when breaking the string at the tokens.
    """

    # Auxiliary variables.
    indexes = []
    pchars = get_protected()
    string_ = ""
    tokens = []

    # Check character by character.
    for i, character in enumerate(string):

        # Add the string to the tokens.
        if character not in pchars:
            # Save the index where the characters are located.
            indexes.append(i)

            # Don't append empty strings.
            if string_ == "":
                continue

            # Append the token.
            tokens.append(copy.deepcopy(string_))
            string_ = ""
            continue

        # Kep adding characters.
        string_ += character

    # Append the final string.
    tokens.append(string_) if not string_ == "" else None

    return tuple(tokens), indexes


def get_tokenized_at(string: str, indexes: tuple) -> tuple:
    """
        Tokenizes the given string at the given locations, i.e., the
        indexes that are stored in the one-dimensional tuple 'indexes'.

        :param string: The string to be tokenized.

        :param indexes: The places where the string is to be split.

        :return: The list of generated, non-empty strings that are generated
         when breaking the string at the tokens.
    """

    # Some times the string is not tokenized.
    if len(indexes) == 0:
        return (string,)

    # Auxiliary variables.
    indexes_ = list(indexes)
    tokens = []

    # If zero is not in the indexes.
    if not indexes_[0] == 0:
        indexes_.insert(0, -1)
    length = len(indexes_) - 1

    # Get the tokens.
    for i, _ in enumerate(indexes_):
        # Get the tokens.
        if i == length:
            print(indexes_[i])
            token = string[indexes_[i] + 1:]

        else:
            token = string[indexes_[i] + 1: indexes_[i + 1]]

        # Append the final string.
        tokens.append(copy.deepcopy(token)) if not token == "" else None

    return tuple(tokens)


def get_tokenized_final(sdate: str, sdformat: str) -> list:
    """
        Tokenizes the final string to be placed into the dictionary. This gets
        the specific fields to be verified, i.e., only characters in the
        protected characters should be in the format string.

        :param sdate: The characters in the segment of date to be validated.

        :param sdformat: The characters in the format string to be validated.

        :return: The list of lists of the consecutive protected characters.
    """

    # Get the first character.
    cchar = sdformat[0]
    date_list = []
    dformat_list = []

    # Get the strings to place the further tokenized strings.
    string0 = ""
    string1 = ""

    # Separate the characters.
    for i, (datechar, dformatchar) in enumerate(zip(sdate, sdformat)):
        # Format doesn't match.
        if not cchar == dformatchar:
            # Strings match.
            date_list.append(copy.deepcopy(string0))
            dformat_list.append(copy.deepcopy(string1))

            # New string is started.
            string0 = ""
            string1 = ""

            # Update the character.
            cchar = dformatchar

        # Attach the strings.
        string0 += datechar
        string1 += dformatchar

        # Append the last bit.
        if i == len(sdate) - 1:
            # Last piece of string.
            date_list.append(string0)
            dformat_list.append(string1)

    return [(f, d) for d, f in zip(date_list, dformat_list)]


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

    # Check special character placement.
    valid = check_csspecial(date, dformat=dformat)
    if not valid:
        return valid

    # Get the specific format.
    dformat_tokens, indexes = get_tokenized(dformat)
    date_tokens = get_tokenized_at(date, indexes)

    # Get the pairs.
    pairs = []
    for datet, dformatt in zip(date_tokens, dformat_tokens):
        pairs.extend(get_tokenized_final(datet, dformatt))

    # Entries for the date must not repeated, i.e., entries are unique.
    valid = check_not_repeated(pairs)
    if not valid:
        return valid


# ##############################################################################
# Main Function
# ##############################################################################


def main() -> None:

    # Date and format.
    date = "22032122920305"
    dformat = "YYYYMMDDhhmmss"

    # Validate the date.
    validate_date(date, dformat=dformat, ampm=False)

    # TODO: Get the dictionaries of the date format and match.


# ##############################################################################
# Main Program
# ##############################################################################


if __name__ == "__main__":
    main()
