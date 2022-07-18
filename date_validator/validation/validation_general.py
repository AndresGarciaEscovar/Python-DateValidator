"""
    File that contains the functions to validate different general quantities.
"""


# ##############################################################################
# Imports
# ##############################################################################


# ##############################################################################
# Functions
# ##############################################################################

# ------------------------------------------------------------------------------
# Validate Functions
# ------------------------------------------------------------------------------


def validate_day(dictionary: dict) -> bool:
    """
        Validates that the day is given as a day of the month or a day of the
        year.

        :param dictionary: The dictionary that contains the string, or object,
         that represents the day.


        :return: True, if the day is valid. False, otherwise.
    """

    # //////////////////////////////////////////////////////////////////////////
    # Auxiliary Functions.
    # //////////////////////////////////////////////////////////////////////////

    def get_month_days_0() -> int:
        """
            Gets the number of days in the given month. If no month is
            given, it can be safely assumed that the value to be returned is
            31.

            :return: The number of days in the given month.
        """

        # No month is given.
        if dictionary["MMM"] == "" and dictionary["MM"] == "":
            return 31

        # Get the year.
        year_0 = 0 if dictionary["YYYY"] == "" else int(dictionary["YYYY"])
        year_0 = year_0 if dictionary["YY"] == "" else int(dictionary["YY"])

        # Get the number month.
        if dictionary["MMM"] != "":
            month_0 = {
                "JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5,
                "JUN": 6, "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10,
                "NOV": 11, "DEC": 12
            }[dictionary["MMM"]]
        else:
            month_0 = int(dictionary["MM"])

        # Get the number of days in a month.
        return {
            1: 31, 2: 29 if year_0 % 4 == 0 else 28, 3: 31, 4: 30, 5: 31,
            6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }[month_0]

    def get_month_days_range_0() -> tuple:
        """
            Gets the number of days that have gone by in the given year, up
            to the given month and the month after.

            :return: The number of days gone up to given month, plus one.
        """

        # Get the year.
        year_0 = 0 if dictionary["YYYY"] == "" else int(dictionary["YYYY"])
        year_0 = year_0 if dictionary["YY"] == "" else int(dictionary["YY"])

        # No month is given.
        if dictionary["MMM"] == "" and dictionary["MM"] == "":
            return 1, 367 if year_0 % 4 == 0 else 366

        # Define the number of days in a month.
        days_in_month_0 = {
            0: 1, 1: 30, 2: 29 if year_0 % 4 == 0 else 28, 3: 31, 4: 30,
            5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }

        # Get the number month.
        if dictionary["MMM"] != "":
            month_0 = {
                "JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5,
                "JUN": 6, "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10,
                "NOV": 11, "DEC": 12
            }[dictionary["MMM"]]
        else:
            month_0 = int(dictionary["MM"])

        # Add the relevant months.
        counter_0_0 = 1 if month_0 > 1 else 0
        counter_0_1 = 1
        for i_0, value_0 in enumerate(days_in_month_0.values(), start=1):
            # Get the days gone.
            counter_0_0 += days_in_month_0[i_0 - 1]
            counter_0_1 += days_in_month_0[i_0]

            # Counter reaches the end.
            if i_0 == month_0:
                break

        return counter_0_0, counter_0_1 + 1

    # //////////////////////////////////////////////////////////////////////////
    # Implementation.
    # //////////////////////////////////////////////////////////////////////////

    # No day to validate.
    if dictionary["DD"] == "" and dictionary["DDD"] == "":
        return True

    # Validate the two-digit day.
    if dictionary["DD"] != "":
        try:
            days_0 = get_month_days_0() + 1
            return int(dictionary["DD"]) in range(1, days_0)
        except (TypeError, ValueError):
            return False

    # Get the number of days gone by in the year.
    range_0 = get_month_days_range_0()

    # Try to validate the day.
    try:
        return int(dictionary["DDD"]) in range(*range_0)
    except (TypeError, ValueError):
        return False


def validate_hour(dictionary: dict, ampm: bool) -> bool:
    """
        Validates that the hour is in the proper range, given the format.

        :param dictionary: The dictionary that contains the string, or object,
         that represents the hour.

        :param ampm: Boolean flag that indicates if the time is given in 12-hr
         format or 24-hr format. True, if the hour is given in 12-hr format;
         False, if the hour is given in 24-hr format.

        :return: True, if the hour is valid. False, otherwise.
    """

    # No need to check.
    if dictionary["hh"] == "":
        return False

    # Convert into numerical format.
    try:
        hour_0 = int(dictionary["hh"])
    except (TypeError, ValueError):
        return False

    # Check the 12-hr format.
    if ampm:
        # Check existence of the am/pm/m strings.
        if dictionary["ii"] not in ("am", "pm", "m"):
            return False

        # Must be noon.
        if dictionary["ii"] == "m":
            return hour_0 == 12

        return 1 <= hour_0 <= 12

    # Check that the 12-hr format string is empty.
    if dictionary["ii"] != "":
        raise ValueError(
            "\nTime is being validated in 24-hr format but the 'ii' "
            "field is present. This shouldn't happen."
        )

    return 0 <= hour_0 < 24


def validate_month(dictionary: dict) -> bool:
    """
        Validates that the month is given in numerical format or
        three-letter format.

        :param dictionary: The dictionary that contains the string, or object,
         that represents the month.


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


def validate_year(dictionary: dict) -> bool:
    """
        Validates that the year is given in numerical format and it's
        positive.

        :param dictionary: The dictionary that contains the string, or object,
         that represents the year.

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
