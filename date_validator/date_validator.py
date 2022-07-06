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

        def get_separators_date0() -> tuple:
            """
                Tokenize the date using the given tokens.

                :return: A tuple with the date fields, denoted by the separators
                 in the date format.
            """

            # Auxiliary variables.
            counter0 = 0
            token_sep0 = get_separators_format0()
            tokens0 = []

            # If there are no separation tokens.
            if len(token_sep0) == 0:
                return tuple()

            # Get each separator.
            for character0 in self.date:
                # Get the tokens.
                if character0 == token_sep0[counter0]:
                    counter0 += 1
                    tokens0.append(character0)

                # No need to look for more tokens.
                if counter0 >= len(token_sep0):
                    break

            return tuple(tokens0)

        def get_separators_format0() -> tuple:
            """
                Returns the tuple with the field separators for the date format
                string.

                :return: The tuple with the field separators for the date format
                string.
            """

            # Auxiliary variables.
            token_sep0 = []

            # Get the tokens of the format string.
            for i0, character0 in enumerate(self.dformat):
                # Non protected characters split the string.
                if character0 not in DateValidator._PROTECTED:
                    # 'i' characters are protected in the 12-hr date.
                    if not (self.ampm and self.dformat[i0] == "i"):
                        token_sep0.append(character0)

            return tuple(token_sep0)

        # //////////////////////////////////////////////////////////////////////
        # Implementation
        # //////////////////////////////////////////////////////////////////////

        # TODO: Add a function that checks that given date is not blank.

        # Get the tokens of the data.
        dformat = get_separators_format0()
        date = get_separators_date0()

        # If the separator list is not identical.
        if not dformat == date:
            return False

        print(dformat)
        print(date)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Private Interface
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # ##########################################################################
    # Variables
    # ##########################################################################

    # Protected characters.
    _PROTECTED = 'Y', 'M', 'D', 'h', 'm', 's', 't'

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
            # Must not be the same as the other fields.
            for field1 in fields[i + 1:]:
                if field0[0] == field1[0]:
                    return False

        # Check that the hour is given if the 12-hr format is given.
        if self.ampm:
            return any(char[0] == 'h' for char in fields)

        # TODO: Add a function that checks that given format is not blank.

        return True


if __name__ == "__main__":

    dvalue = "4234i;777;77;77;77;77-7;"
    dforma = "YYYYii;MMM;DD;hh;mm;ss-t"
    ampmp = True

    val = DateValidator(dforma, date=dvalue, ampm=True)
    val.validate_date()
