""" File that contains the validator functions."""

# ##############################################################################
# Imports
# ##############################################################################


# General.
import copy


# ##############################################################################
# Classes
# ##############################################################################
import re


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
        self.__dformat = str(dformat)
        self._validate_format()

    # --------------------------------------------------------------------------
    # Constructor
    # --------------------------------------------------------------------------

    def __init__(self, dformat: str, ampm: bool):
        """
            Constructs a date validator.

            :param dformat: The format in which the date to validate should be
             given.
        """

        # Set the variables.
        self.ampm = ampm
        self.dformat = dformat

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
    # Validate Methods
    # --------------------------------------------------------------------------

    def _validate_format(self):
        """
            Validates that the date format is valid.

            :raise: DateFormatError: If the date format is not valid.
        """

        # No need to check.
        if not ampmp:
            return

        # Must contain a single occurrence of i or ii.
        indexes = list(x.span() for x in re.finditer("ii|i", self.dformat))

        # Since its a 12-hour format, the am/pm must appear once.
        valid = len(indexes) == 1

        # Format must give the position of the am/pm string.
        valid = valid and indexes[0][1] - indexes[0][0] == 2

        if not valid:
            raise

        # Split the format into the different identifier


if __name__ == "__main__":

    dvalue = "4234-23-42:34::23:4*8"
    dforma = "YYYY-MM-DD:hh::mm:s*tii"
    ampmp = True

    val = DateValidator(dforma, ampmp)
