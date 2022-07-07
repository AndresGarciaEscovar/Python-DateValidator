""" File that contains the validator functions."""

# ##############################################################################
# Imports
# ##############################################################################


# General.
import copy
import re

# User defined.
from errors.errors_date import DateFormatError

# ##############################################################################
# Classes
# ##############################################################################


class DateValidator:
    """
        Class that contains the methods and variables to validate the dates,
        given the date format.

        Date formats must be given by specifying the year with the 'Y'
        character, the month with the 'M' character, the day with the 'D'
        character, the hour with the 'h' character, the minute with the 'm'
        character, the seconds with the 's' character and the tenth of seconds
        with the 't' character; that are protected characters. If the date
        is a 12-hr date, it must include the 'ii' or 'i' string somewhere in the
        format string; if the date is given in 24-hr format, the 'i' character
        will be treated as a separator character. For the date format to be a
        valid date, all fields must appear only once, i.e., there must be, at
        most, a single year, a single month, etc.

        The conditions for the date can be relaxed and can be specified.

        Parameters:
        __________

        - self.dformat: str
            The date format to be used.

        - self.ampm: bool
            Flag that indicates of the date is given in 12-hr or 24-hr format.
            True, if the date is given in 12-hr format; False, otherwise.
    """

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Public Interface
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # --------------------------------------------------------------------------
    # Properties
    # --------------------------------------------------------------------------

    @property
    def ampm(self) -> bool:
        """
            Returns the ampm flag.

            :return: True, if the hour is given in 12-hr format. False,
             otherwise.
        """
        return self.__ampm

    @ampm.setter
    def ampm(self, ampm: bool) -> None:
        """
            Sets the ampm flag.

            :param ampm: A boolean flag that indicates if the date is given in
             12-hr format. True, if the hour is given in 12-hr format. False,
             otherwise.
        """
        self.__ampm = bool(ampm)

    # ------------------------------------------------------------------------ #

    @property
    def date(self) -> str:
        """
            Returns the string with the date to be validated.

            :return: The string that represents the date.
        """
        return self.__date

    @date.setter
    def date(self, date: str) -> None:
        """
            Sets the string of the date to be validated.

            :param date: The date string to be validated.
        """
        self.__date = str(date).strip()

    # ------------------------------------------------------------------------ #

    @property
    def dformat(self) -> str:
        """
            Returns the string with the date format.

            :return: The string that represents the date format.
        """
        return self.__dformat

    @dformat.setter
    def dformat(self, dformat: str) -> None:
        """
            Sets the string of the date format.

            :param dformat: The format that the date must take.
        """
        self.__dformat = str(dformat).strip()
        self._validate_format()

    # --------------------------------------------------------------------------
    # Constructor
    # --------------------------------------------------------------------------

    def __init__(self, dformat: str, date: str = "", ampm: bool = False):
        """
            Constructs a date validator.

            :param dformat: The format in which the date to validate should be
             given.

            :param date: The date string to be validate agains the date format.

            :param ampm: The boolean flag that indicates if the date is given in
             12-hr format. True, if the date is given in 12-hr format. False,
             otherwise.
        """

        # Set the variables.
        self.ampm = ampm
        self.dformat = dformat
        self.date = date

        # Initialize the validation dictionary.
        self.quantites = dict((var, None) for var in DateValidator._FORMATS)
        print(self.quantites)


    # ##########################################################################
    # Methods
    # ##########################################################################

    # --------------------------------------------------------------------------
    # Validate Methods
    # --------------------------------------------------------------------------

    def validate_date(self) -> bool:
        """
            Validates that the stored date is given in the requested format. If
            the date is in 12-hr format, it checks that the time, if it's noon,
            has a 'pm' or 'm' symbol.

            :return: True, if the date is valid and in the given format. False,
             otherwise.
        """

        # //////////////////////////////////////////////////////////////////////
        # Auxiliary Functions
        # //////////////////////////////////////////////////////////////////////

        def find_ampm_index_0(tokens_0: tuple) -> int:
            """
                Finds the location of the token that contains the am/pm string
                in the tuples.

                :param tokens_0: The tuple with the date format tokens.

                :return: The index of the tuple that contains the am/pm string.
            """

            # A string must, at least contain the ii token.
            for i_0, strings_0 in enumerate(tokens_0):
                if 'ii' in strings_0:
                    return i_0

            return -1

        def remove_ampm_date_0(token_0: str, index_0: int) -> str:
            """
                Removes the am/pm/m string.

                :param token_0: The string from which the date will be removed.

                :param index_0: The index where the am/pm/m string is located.

                :return: The string with the am/pm/m string removed.
            """

            # -------------- String at the Beginning ------------------------- #

            # Trivial cases.
            if index_0 == 0 and token_0[index_0] == 'm':
                return token_0[1:]

            elif index_0 == 0:
                return token_0[2:]

            # ------------------- String at any Other Point ------------------ #

            # Trivial cases.
            if token_0[index_0] == 'm':
                return token_0[:index_0] + token_0[index_0 + 1:]

            return token_0[:index_0] + token_0[index_0 + 2:]

        def remove_ampm_dformat_0(token_0: str) -> str:
            """
                Removes the am/pm/m string.

                :param token_0: The string from which the date will be removed.

                :param index_0: The index where the am/pm/m string is located.

                :return: The string with the am/pm/m string removed.
            """

            # Auxiliary variables.
            string_0 = ""

            # For all characters.
            for character_0 in token_0:

                # Skip the am/pm indicator.
                if character_0 == "i":
                    continue

                # Appends the valid characters.
                string_0 += character_0

            return string_0

        def validate_ampm_0(index_0: int, string_0: str) -> bool:
            """
                Validates that the am/pm/m string is in the given string.

                :param index_0: The index where the am/pm/m string should be
                 located.

                :param string_0: The string where the am/pm/m string should be
                 found.

                :return: True, if the m, am or pn string is found. False,
                 otherwise.
            """

            # Check the string is long enough.
            if not 0 <= index_0 < len(string_0):
                return False

            # Check the location of the string.
            valid_0 = string_0[index_0] == "m"
            valid_0 = valid_0 or string_0[index_0: index_0 + 2] == "am"
            valid_0 = valid_0 or string_0[index_0: index_0 + 2] == "pm"

            return valid_0

        # //////////////////////////////////////////////////////////////////////
        # Implementation
        # //////////////////////////////////////////////////////////////////////

        # TODO: Add a function that checks that given date is not blank.

        # Auxiliary variables.
        is_noon = False

        # Get the tokens of the data.
        dformat = self._get_separators_dformat()
        date = self._get_separators_date(dformat)

        # If the separator list is not identical.
        if not dformat == date:
            return False

        # Get the different parts of the string.
        dformat = self._split_string(self.dformat, dformat)
        date = self._split_string(self.date, date)

        # Length of tokenizing must be the same.
        if not len(dformat) == len(date):
            return False

        print("Hree")
        #
        # # Look for the string that contains the am/pm string, if needed.
        # index = find_ampm_index_0(dformat) if self.ampm else -1
        #
        # # Look for the ampm string, validate it and remove it.
        # if index >= 0:
        #     # Get the index of appearance of the am/pm sign.
        #     index0 = dformat[index].index('i')
        #
        #     # If the string is not valid.
        #     if not validate_ampm_0(index0, date[index]):
        #         return False
        #
        #     # Flag to validate that the time is noon.
        #     is_noon = date[index][index0] == 'm'
        #
        #     # Remove the am/pm/m string.
        #     date = list(date)
        #     date[index] = remove_ampm_date_0(date[index], index0)
        #     date = tuple(date)
        #
        #     # Remove the am/pm/m indicator.
        #     dformat = list(dformat)
        #     dformat[index] = remove_ampm_dformat_0(dformat[index])
        #     dformat = tuple(dformat)
        #
        # # Check that the fields match in length.
        # if not all(map(lambda x, y: len(x) == len(y), date, dformat)):
        #     return False
        #
        # # Extract the different fields.
        # extract_fields = extract_fields_0(date, dformat)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Private Interface
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # ##########################################################################
    # Variables
    # ##########################################################################

    # Protected characters.
    _PROTECTED = 'Y', 'M', 'D', 'h', 'm', 's', 't'

    # Valid date field formats.
    _FORMATS = 'YYYY', 'YY', 'MM', 'MMM', 'DDD', 'DD', 'hh', 'mm', 'ss', 't'

    # ##########################################################################
    # Methods
    # ##########################################################################

    # --------------------------------------------------------------------------
    # Get Methods
    # --------------------------------------------------------------------------

    def _get_format_fields(self) -> list:
        """
            Splits the date format string into the reserved character fields.

            :return: The list of fields in the date format, self.dformat.
        """

        # Auxiliary variables.
        length = len(self.dformat) - 1
        parts = []
        string = ""

        # Remove all the separating characters.
        for i, character in enumerate(self.dformat):
            # When the character hits a non-reserved character.
            if character not in DateValidator._PROTECTED:
                # Add only non-empty blocks.
                if not string == "":
                    parts.append(string)

                # Reset the string.
                string = ""
                continue

            string += character

            # At the last character.
            if i == length and not string == "":
                parts.append(string)

        # Auxiliary variables.
        subparts = []

        # Tokenize further.
        for part in parts:

            # Reset the string.
            string = ""

            # Get every field in the substring.
            for i, character in enumerate(part):

                # The length of the string.
                length = len(part) - 1

                # Only to compare with the previous character.
                if i > 0 and not part[i] == part[i - 1]:
                    subparts.append(string)
                    string = ""

                # Append the string.
                string += character

                # Add the last string.
                if i == length:
                    subparts.append(string)

        return subparts

    def _get_separators_date(self, separators: tuple) -> tuple:
        """
            Gets the separators for the date at the same separators as that of
            the format.

            :return: The separators that match both the date and the date
             format.
        """

        # If there are no separators.
        if len(separators) == 0:
            return tuple()

        # Auxiliary variables.
        dseparators = []
        counter = 0

        # Look for each separator.
        for character in self.date:
            # Check the character exists and append it.
            if counter < len(separators) and separators[counter] == character:
                dseparators.append(character)
                counter += 1

        return tuple(dseparators)

    def _get_separators_dformat(self) -> tuple:
        """
            Gets the separators for the date format.

            :return: From the date format string, gets the non-protected
             characters.
        """

        # Auxiliary variables.
        separators = []

        # Check the characters.
        for character in self.dformat:
            # Check separating characters.
            if character not in DateValidator._PROTECTED:
                # Ignore the i character if it's in 12-hr format.
                if character == 'i' and self.ampm:
                    continue

                # Append the character.
                separators.append(character)

        return tuple(separators)

    # --------------------------------------------------------------------------
    # Split Methods
    # --------------------------------------------------------------------------

    @staticmethod
    def _split_string(string: str, separators: tuple):
        """
            Splits the string using the given characters are the splitting
            tokens. Empty strings will be ignored.

            :param string: The string to be split.

            :param separators: The characters at which the string must be split.

            :return: The split string using the separator characters as the
             characters where the string will be split. Only non-empty strings
             will be considered.
        """

        # No need to continue.
        if len(separators) == 0:
            return string,

        # Auxiliary variables.
        counter = 0
        length = len(string) - 1
        temporary = ""
        tokens = []

        # Look for the characters.
        for i, character in enumerate(string):
            # Add the string and update the counter.
            if counter < len(separators) and character == separators[counter]:
                # Add the token if needed.
                if not temporary == "":
                    tokens.append(copy.deepcopy(temporary))

                # Update the strings and continue.
                counter += 1
                temporary = ""
                continue

            # Append the character.
            temporary += character

            # Add the last string.
            if i == length and not temporary == "":
                tokens.append(temporary)

        return tokens

    # --------------------------------------------------------------------------
    # Validate Methods
    # --------------------------------------------------------------------------

    def _validate_format(self) -> None:
        """
            Validates that the date format is valid.

            :raise: DateFormatError: If the date format is not valid.
        """

        # TODO: Add a function that checks that given date format is not blank.

        # Check the am/pm field.
        if self.ampm:
            # Must contain a single occurrence of i or ii.
            indexes = list(x.span() for x in re.finditer("ii|i", self.dformat))

            # Since its a 12-hour format, the am/pm must appear once.
            valid = len(indexes) == 1

            # Format must give the position of the am/pm string.
            valid = valid and indexes[0][1] - indexes[0][0] == 2

            if not valid:
                raise DateFormatError(dformat=self.dformat, ampm=self.ampm)

        # Check the uniqueness of fields.
        raw_format = self._get_format_fields()
        valid = self._validate_format_fields(raw_format)

        # If there are repeated fields.
        if not valid:
            raise DateFormatError(dformat=self.dformat, ampm=self.ampm)

    def _validate_format_fields(self, fields: list) -> bool:
        """
            Validates that the requested fields are unique, i.e., there must be
            at most one year requested, one month requested, etc..

            :param fields: The list of the requested fields.

            :return: True, if the fields are NOT repeated. False, otherwise.
        """

        # Each field.
        for i, field0 in enumerate(fields):
            # Validate that the field is in the protected characters.
            valid = field0[0] in DateValidator._PROTECTED
            valid = valid or field0[0] == 'i' and self.ampm
            if not valid:
                return False

            # Must not be the same as the other fields.
            for field1 in fields[i + 1:]:
                if not valid or field0[0] == field1[0]:
                    return False

        # Check that the hour is given if the 12-hr format is given.
        if self.ampm:
            return any(char[0] == 'h' for char in fields)

        # Make sure that the fields are populated and in an available format.
        valid = len(fields) > 0 and all(
            map(lambda x: x in DateValidator._FORMATS, fields)
        )

        return valid


if __name__ == "__main__":

    dvalue = "4244,MM;77;77am-22,22-9"
    dforma = "YYYY,MM;DD;hhii-mm,ss-t"
    ampmp = True

    val = DateValidator(dforma, date=dvalue, ampm=ampmp)
    val.validate_date()
