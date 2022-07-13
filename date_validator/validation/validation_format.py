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

        def check_day_0() -> None:
            """
                Checks that, if the day is given in DD format, a month is
                present. If the day is given in DDD format, the month must NOT
                be present.

                :raise DayFormatError: If the given fields are not enough to
                 determine if the given day is valid.
            """

            # If the day is not given, no need to validate.
            if "DDD" not in fields and "DD" not in fields:
                return

            # Check that a month is given.
            if "DD" in fields:
                if not ("MMM" in fields or 'MM' in fields):
                    raise ef.DayFormatError()

        def check_hour_0() -> None:
            """
                Checks that, if the hour is given, no year, month or day is
                present or, at least, the day is present.

                :raise HourFormatError: If the given fields are not enough to
                 determine if the given hour is valid.
            """

            # If no hour is given, no need to validate.
            if 'hh' not in fields:
                return

            # If the year, month and day are not given, no need to validate.
            skip_0 = "YYYY" not in fields and "YY" not in fields
            skip_0 = skip_0 and "MMM" not in fields and "MM" not in fields
            skip_0 = skip_0 and "DDD" not in fields and "DD" not in fields

            # No need to validate.
            if skip_0:
                return

            # Must contain a day for the time to make sense.
            if "DDD" not in fields and "DD" not in fields:
                raise ef.HourFormatError()

        def check_minutes_0() -> None:
            """
                Checks that, if the minutes are given, no year, month, day or
                hour are present or, at least, an hour is present.

                :raise MinutesFormatError: If the given fields are not enough to
                 determine if the given minutes are valid.
            """

            # If no minutes are given, no need to validate.
            if 'mm' not in fields:
                return

            # If the year, month and day are not given, no need to validate.
            skip_0 = "YYYY" not in fields and "YY" not in fields
            skip_0 = skip_0 and "MMM" not in fields and "MM" not in fields
            skip_0 = skip_0 and "DDD" not in fields and "DD" not in fields
            skip_0 = skip_0 and "hh" not in fields

            # No need to validate.
            if skip_0:
                return

            # Must contain an hour for the time to make sense.
            if "hh" not in fields:
                raise ef.MinutesFormatError()

        def check_seconds_0() -> None:
            """
                Checks that, if the seconds are given, no year, month or day is
                present or, at least, the day is present.

                :raise SecondsFormatError: If the given fields are not enough to
                 determine if the given seconds are valid.
            """

            # If no minutes are given, no need to validate.
            if 'ss' not in fields:
                return

            # If the year, month and day are not given, no need to validate.
            skip_0 = "YYYY" not in fields and "YY" not in fields
            skip_0 = skip_0 and "MMM" not in fields and "MM" not in fields
            skip_0 = skip_0 and "DDD" not in fields and "DD" not in fields
            skip_0 = skip_0 and "hh" not in fields and "mm" not in fields

            # No need to validate.
            if skip_0:
                return

            # Must contain an hour for the time to make sense.
            if "mm" not in fields:
                raise ef.SecondsFormatError()

        def existing_fields_0() -> None:
            """
                Validates that the requested fields exist.

                :raise FieldFortmatError: If there is a field that that doesn't
                 exist.
            """

            field_names_0 = {
                'Y': 'years', 'M': 'months', 'D': 'days', 'h': 'hours',
                'm': 'minutes', 's': 'seconds', 't': 'tenths of seconds'
            }

            not_valid_0 = []

            # For each field.
            for field_0 in fields:
                # If the fields don't match.
                if field_0 not in self.formats:
                    # Get the field name.
                    field_name_0 = field_names_0[field_0[0]]
                    for key_0 in self.formats:
                        not_valid_0.append(key_0) if field_0[0] in key_0 else 0

                    raise ef.FieldFormatError(
                        field_name_0, field_0, tuple(not_valid_0)
                    )

        def unique_fields_0() -> None:
            """
                Validates that the requested fields are unique and valid.

                :raise UniqueFieldsError: If there is a repeated field.
            """

            # If the field is empty.
            if len(fields) == 0:
                raise ef.EmptyFormatError(self.dformat, self.get_fields())

            # For each field.
            for i_0, field_0_0 in enumerate(fields):
                # Compare against other fields.
                for j_0, field_0_1 in enumerate(fields[i_0 + 1:]):
                    # Repeated fields shouldn't exist.
                    if field_0_0[0] == field_0_1[0]:
                        raise ef.RepeatedFieldsError(fields)

        # //////////////////////////////////////////////////////////////////////
        # Implementation
        # //////////////////////////////////////////////////////////////////////

        # Auxiliary variables.
        fields = self.get_fields()

        # Validate the fields are unique.
        unique_fields_0()

        # Validate the fields exist.
        existing_fields_0()

        # Check the day.
        check_day_0()

        # Check the hour.
        check_hour_0()

        # Check the minutes.
        check_minutes_0()

        # Check the seconds.
        check_seconds_0()

        # TODO: Check the tenths of second.
        check_tenths_0()


# ##############################################################################
# TO DELETE AFTER VISUAL TESTS.
# ##############################################################################


if __name__ == "__main__":

    # TODO: THIS CAN BE MOVED TO THE TEST SECTION.
    dform = "MM:DD;hh;mmii;ss;t"
    ampms = True

    FormatValidator(dformat=dform, ampm=ampms)
