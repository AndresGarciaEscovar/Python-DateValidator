"""
    File that contains the functions to validate the date format.
"""

# ##############################################################################
# Imports
# ##############################################################################

# General.
from typing import Any

# User defined.
import date_validator.errors.errors_format as ef
# ##############################################################################
# Classes
# ##############################################################################


class FormatValidator:
    """
        Class that contains the functions to validate the date format string.
    """

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Public Interface.
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # ##########################################################################
    # Properties
    # ##########################################################################

    @property
    def ampm(self) -> bool:
        """
            Returns the boolean flag that indicates if the date is in am or pm
             format.

            :return: The boolean flag that indicates if the date is in am or pm
             format.
        """
        return self.__ampm

    @ampm.setter
    def ampm(self, ampm: Any) -> None:
        """
            Sets the boolean flag that indicates whether the time is in 12-hr
            format.

            :param ampm: the boolean flag that indicates whether the time is in
             12-hr format.
        """
        self.__ampm = bool(ampm)

    # ------------------------------------------------------------------------ #

    @property
    def dformat(self) -> str:
        """
            Returns the date format.

            :return: The current stored date format.
        """
        return self.__dformat

    @dformat.setter
    def dformat(self, dformat: Any) -> None:
        """
            Sets the date format.

            :param dformat: The string that represents the date format.
        """
        self.__dformat = str(dformat).strip()
        self._validate_fields()

    # ------------------------------------------------------------------------ #

    @property
    def formats(self) -> tuple:
        """
            Returns the dictionary of valid formats that the different date
            fields can take.

            :return: Returns the valid formats that the date can take.
        """

        formats = (
            'YYYY', 'YY', 'MMM', 'MM', 'DDD', 'DD', 'hh', 'mm', 'ss', 't',
            'ii',
        )

        return formats if self.ampm else formats[:-1]

    # ------------------------------------------------------------------------ #

    @property
    def protected(self) -> tuple:
        """
            Returns the protected characters

            :return: Returns the protected characters.
        """

        characters = (
            'Y', 'M', 'D', 'h', 'm', 's', 't', 'i'
        )

        return characters if self.ampm else characters[:-1]

    # ##########################################################################
    # Constructor
    # ##########################################################################

    def __init__(self, dformat, ampm):
        """
            Initializes the variables of the date formatter.
        """

        # Set the variables.
        self.ampm = ampm
        self.dformat = dformat

    # ##########################################################################
    # Methods
    # ##########################################################################

    # --------------------------------------------------------------------------
    # Get Methods
    # --------------------------------------------------------------------------

    def get_fields(self) -> tuple:
        """
            Gets the fields that are in the date format.

            :return: The fields that are in the date format.
        """

        # Auxiliary variables.
        dformat = self.dformat
        fields = []
        length = len(dformat) - 1
        string = ""

        # Extract each field.
        for i, char in enumerate(dformat):

            # If the character is not protected.
            if char not in self.protected:
                fields.append(string) if string != "" else None
                string = ""
                continue

            # Get the field.
            if i > 0 and char != dformat[i - 1]:
                fields.append(string) if string != "" else None
                string = ""

            # Append the character.
            string += char

            # Append the last string.
            if i == length and string != "":
                fields.append(string) if string != "" else None

        return tuple(fields)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Private Interface.
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # ##########################################################################
    # Methods
    # ##########################################################################

    # --------------------------------------------------------------------------
    # Validate Methods
    # --------------------------------------------------------------------------

    def _validate_fields(self) -> None:
        """
            Validates that the fields are unique.

            :raise UniqueFieldsError: If there is a repeated field.
        """

        # //////////////////////////////////////////////////////////////////////
        # Auxiliary Functions
        # //////////////////////////////////////////////////////////////////////

        def unique_fields_0() -> None:
            """
                Validates that the requested fields are unique and valid.

                :raise UniqueFieldsError: If there is a repeated field.
            """

            if len(fields) == 0:
                raise EmptyFormatError()

        # //////////////////////////////////////////////////////////////////////
        # Implementation
        # //////////////////////////////////////////////////////////////////////

        # Auxiliary variables.
        fields = self.get_fields()

        print(fields)

# ##############################################################################
# TO DELETE AFTER VISUAL TESTS.
# ##############################################################################

if __name__ == "__main__":

    # TODO: THIS CAN BE MOVED TO THE TEST SECTION.
    dform = "YYYYMM;DDhh;mmii;ss;t"
    ampms = True

    FormatValidator(dformat=dform, ampm=ampms)
