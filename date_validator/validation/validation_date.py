"""
    File that contains the functions to validate the date.
"""

# ##############################################################################
# Imports
# ##############################################################################

# General.
from typing import Any

# User defined.
import date_validator.validation.validation_format as vf
import date_validator.errors.errors_format as ef

# ##############################################################################
# Classes
# ##############################################################################


class DateValidator:
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
    def date(self) -> str:
        """
            Returns the date format.

            :return: The current stored date format.
        """
        return self.__date

    @date.setter
    def date(self, date: Any) -> None:
        """
            Sets the date to be validated.

            :param date: The string that represents the date to be formatted.
        """
        self.__date = str(date)

    # ------------------------------------------------------------------------ #

    @property
    def dformat(self) -> vf.FormatValidator:
        """
            Returns the date format.

            :return: The current stored date format.
        """
        return self.__dformat

    @dformat.setter
    def dformat(self, dformat: Any) -> None:
        """
            Sets the date format object.

            :param dformat: The string that represents the date format.
        """
        self.__dformat = vf.FormatValidator(str(dformat).strip(), self.ampm)

    # ##########################################################################
    # Constructor
    # ##########################################################################

    def __init__(self, date, dformat, ampm):
        """
            Initializes the variables of the date validator.

            :param date: The string that contains the date to be validated.

            :param dformat: The string that represents the format in which the
             date should be given.

            :param ampm: The boolean flag that indicates if the time is given
             in 12-hr or 24-hr format. True, if the time is given in 12-hr
             format; False, otherwise.
        """

        # Set the variables.
        self.ampm = ampm
        self.date = date
        self.dformat = dformat

    def __call__(self) -> bool:
        """
            The boolean value that indicates if the given date is valid, or not.

            :return: True, if the date given is in the given format. False,
             otherwise.
        """
        return self._validate_fields()

    # ##########################################################################
    # Methods
    # ##########################################################################

    # --------------------------------------------------------------------------
    # Get Methods
    # --------------------------------------------------------------------------

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Private Interface.
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # ##########################################################################
    # Methods
    # ##########################################################################

    # --------------------------------------------------------------------------
    # Get Methods
    # --------------------------------------------------------------------------

    def _get_fields_using_separators(self) -> tuple:
        """
            Gets the fields that are delimited by the separators.

            :return: The fields that are delimited by the separators.
        """

        # Auxiliary variables.
        cntr = 0
        fields = []
        length = len(self.date) - 1
        separators = self.dformat.get_separators()
        string = ""

        # Extract each field.
        for i, char in enumerate(self.date):

            # If the character is not protected.
            if cntr < len(separators) and char == separators[cntr]:

                # Append the string.
                if string != "":
                    fields.append(string)

                # Look for the next character.
                string = ""
                cntr += 1
                continue

            # Append the character.
            string += char

            # Append the last string.
            if i == length and string != "":
                fields.append(string)

        return tuple(fields)

    def _get_separators(self) -> tuple:
        """
            Gets the fields of the date, just considering the separators
            in the date format.

            :return: The fields in the date.
        """

        # Auxiliary variables.
        cntr = 0
        dfields = []

        # Get the separators from the date format.
        sfields = self.dformat.get_separators()

        # Search for each character.
        for i, char in enumerate(self.date):

            # If the character matches.
            if cntr < len(sfields) and char == sfields[cntr]:
                # Add the character.
                dfields.append(char)
                cntr += 1
                continue

        return tuple(dfields)

    # --------------------------------------------------------------------------
    # Validate Methods
    # --------------------------------------------------------------------------

    def _validate_fields(self) -> bool:
        """
            Validates that the fields are unique.

            :raise UniqueFieldsError: If there is a repeated field.
        """

        # //////////////////////////////////////////////////////////////////////
        # Auxiliary Functions
        # //////////////////////////////////////////////////////////////////////

        # --------------------------- Get Functions -------------------------- #

        def get_ampm_index_0() -> int:
            """
                Gets the location of where the am/pm index should be.
            """

            # No index to return.
            if not self.ampm:
                return -1

            # Get the fields only using the separators.
            fields_0 = self.dformat.get_fields_using_separators()

            # Get the location of the field.
            for i_0, field_0 in enumerate(fields_0):
                if "ii" in field_0:
                    return i_0

            raise ValueError(
                "The 'ii' field should appear somewhere in the format fields, "
                f"but this is not happening.\nDate Format Fields: {fields_0}."
            )

        def get_valid_fields_0() -> bool:
            """
                From the tokenized string by the separators, gets the different
                quantitities to validate.

                :return: False, if the fields cannot be extracted due to a
                 mismatch in size. True, otherwise.
            """

            # Get the fields using the separators.
            date_fields_0 = list(self._get_fields_using_separators())
            dformat_fields_0 = list(self.dformat.get_fields_using_separators())

            # Get the am/pm/m index and remove it.
            index_0 = get_ampm_index_0()

            # Find the am/pm/m field and remove it.
            if index_0 >= 0:
                # Get the am/pm field index.
                index_0_1 = dformat_fields_0[index_0].index("ii")

                # Remove the ii entry.
                str_ini_0 = dformat_fields_0[index_0][:index_0_1]
                str_end_0 = dformat_fields_0[index_0][index_0_1 + 2:]
                dformat_fields_0[index_0] = str_ini_0 + str_end_0

                # Get the ii entry.
                if index_0_1 < len(date_fields_0[index_0]):
                    # If it indicates noon.
                    if date_fields_0[index_0][index_0_1] == "m":
                        ent_0 = date_fields_0[index_0][index_0_1: index_0_1 + 1]
                        dictionary["ii"] = ent_0
                        str_ini_0 = date_fields_0[index_0][:index_0_1]
                        str_end_0 = date_fields_0[index_0][index_0_1 + 1:]
                        date_fields_0[index_0] = str_ini_0 + str_end_0
                    else:
                        ent_0 = date_fields_0[index_0][index_0_1: index_0_1 + 2]
                        dictionary["ii"] = ent_0
                        str_ini_0 = date_fields_0[index_0][:index_0_1]
                        str_end_0 = date_fields_0[index_0][index_0_1 + 2:]
                        date_fields_0[index_0] = str_ini_0 + str_end_0

            # Check ALL the fields have the same length.
            for entry_0_0, entry_0_1 in zip(date_fields_0, dformat_fields_0):

                # If fields are not the same length.
                if len(entry_0_0) != len(entry_0_1):
                    return False

                # Maximum allowed length.
                length_0 = len(entry_0_0) - 1

                # Define empty strings.
                string_0 = ""
                string_1 = ""

                # Go through each character.
                for i_0, (char0, char1) in enumerate(zip(entry_0_0, entry_0_1)):

                    # A field has been found.
                    if i_0 > 0 and char1 != entry_0_1[i_0 - 1]:
                        dictionary[string_1] = string_0
                        string_0 = ""
                        string_1 = ""

                    # Append the characters to the strings.
                    string_0 += char0
                    string_1 += char1

                    # Has reached the end.
                    if i_0 == length_0:
                        dictionary[string_1] = string_0

            return True

        # ------------------------ Validate Functions ------------------------ #

        def validate_day_0() -> bool:
            """"""
            return True

        def validate_hour_0() -> bool:
            """"""
            return True

        def validate_minutes_0() -> bool:
            """"""
            return True

        def validate_month_0() -> bool:
            """
                Validates that the month is given in numerical format or
                three-letter format.

                :return: True, if the month is valid. False, otherwise.
            """

            # No month provided, validation is fine.
            if dictionary['MMM'] == "" and dictionary['MM'] == "":
                return True

            # Verify three-letter month.
            if dictionary['MMM'] != "":
                return dictionary['MMM'].upper() in (
                    "JAN", "FEB", "MAR", "APR", "MAY", "JUN",
                    "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"
                )

            # Verify two-digit month.
            try:
                return int(dictionary['MM']) in range(1, 13)
            except (TypeError, ValueError):
                return False

        def validate_seconds_0() -> bool:
            """"""
            return True

        def validate_tenths_0() -> bool:
            """"""
            return True

        def validate_year_0() -> bool:
            """
                Validates that the year is given in numerical format and it's
                positive.

                :return: True, if the year is valid. False, otherwise.
            """

            # No year provided, validation is fine.
            if dictionary['YYYY'] == "" and dictionary['YY'] == "":
                return True

            # Verify four-digit year.
            if dictionary['YYYY'] != "":
                try:
                    return int(dictionary['YYYY']) > 0
                except (TypeError, ValueError):
                    return False

            # Verify two-digit year.
            try:
                return int(dictionary['YY']) > 0
            except (TypeError, ValueError):
                return False

        # //////////////////////////////////////////////////////////////////////
        # Implementation
        # //////////////////////////////////////////////////////////////////////

        # Auxiliary variables.
        dictionary = {
            "YYYY": "", "YY": "", "MMM": "", "MM": "", "DDD": "", "DD": "",
            "hh": "", "mm": "", "ss": "", "t": "", "ii": ""
        }

        # Separators are different.
        if self._get_separators() != self.dformat.get_separators():
            return False

        # Get the fields that are defined by the separators.
        fields = self._get_fields_using_separators()

        # Check the number of fields match.
        if len(fields) != len(self.dformat.get_fields_using_separators()):
            return False

        # Get the different fields in the dictionary.
        if not get_valid_fields_0():
            return False

        # Validate the date.
        valid = validate_year_0()
        valid = valid and validate_month_0()

        # TODO: Finish validating these entries.

        # valid = valid and validate_day_0()
        #
        # # Validate the time.
        # valid = valid and validate_hour_0()
        # valid = valid and validate_minutes_0()
        # valid = valid and validate_seconds_0()
        # valid = valid and validate_tenths_0()

        return valid

# ##############################################################################
# TO DELETE AFTER VISUAL TESTS.
# ##############################################################################


if __name__ == "__main__":

    vdate = "2025-DEC-29;12:32pm:10:9"
    dform = "YYYY-MMM-DD;hh:mmii:ss:t"
    ampms = True

    val = DateValidator(date=vdate, dformat=dform, ampm=ampms)
    print(val())

