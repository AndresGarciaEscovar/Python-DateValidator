""" File that contains the date validator custom execptions. """

# ##############################################################################
# Imports
# ##############################################################################

# ##############################################################################
# Classes
# ##############################################################################


class DateAmPmError(Exception):
    """
        Class that contains the constructor for the exception when the date
        is being validated in 12-hr format and there is a problem with this
        kind of formatting.

        Parameters:
        __________

        - _MESSAGE: The standard message to be displayed. Will be customized
          further if parameters are passed to the constructor.
    """

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Public Interface
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # ##########################################################################
    # Constructor
    # ##########################################################################

    def __init__(self, date: str, dformat: str):
        """
            The method that builds the exception.

            :param dformat: The requested date format.
        """

        # Customize the message.
        message = DateFormatError._customize(dformat, ampm)

        super(DateFormatError, self).__init__(message)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Private Interface
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # ##########################################################################
    # Global Variables
    # ##########################################################################

    _MESSAGE = "The date format is wrong. "

    # ##########################################################################
    # Methods
    # ##########################################################################

    # --------------------------------------------------------------------------
    # Customize Methods
    # --------------------------------------------------------------------------

    @staticmethod
    def _customize(dformat: str, ampm: bool):
        """
            Finishes customizing the message to indicate the error with the
            date format.

            :param dformat: The invalid date format.

            :param ampm: True, if the time being checked is in 12-hr format.
             False, otherwise.

            :return: The customized message.
        """

        # If its 12 or 24 hour format.
        fmt = "12" if ampm else '24'

        message = (
            f"\nThe date is currently being checked in {fmt}-hr format. Things "
            f"to check:\n"
            f"\t1. The date format must include the 'ii' literal, if the date "
            f"is given in 12-hr format; this is where the am/pm/m string in "
            f"the date must be placed.\n"
            f"\t2. If the date format is in 24-hr format, the 'i' character(s) "
            f"will be treated as separating characters.\n"
            f"\t3. There cannot be repeated fields, i.e., only a single year, "
            f"a single month, a single day, etc., field.\n"
            f"\t4. If the 12-hr format is requested, an hour must be provided."
            f"\n"
            f"Current requested format: {dformat}\n"
        )

        return DateFormatError._MESSAGE + message


class DateFormatError(Exception):
    """
        Class that contains the constructor for the exception when the date
        format is wrong.

        Parameters:
        __________

        - _MESSAGE: The standard message to be displayed. Will be customized
          further if parameters are passed to the constructor.
    """

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Public Interface
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # ##########################################################################
    # Constructor
    # ##########################################################################

    def __init__(self, dformat: str = "", ampm: bool = False):
        """
            The method that builds the exception.

            :param dformat: The requested date format.
        """

        # Customize the message.
        message = DateFormatError._customize(dformat, ampm)

        super(DateFormatError, self).__init__(message)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Private Interface
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # ##########################################################################
    # Global Variables
    # ##########################################################################

    _MESSAGE = "The date format is wrong. "

    # ##########################################################################
    # Methods
    # ##########################################################################

    # --------------------------------------------------------------------------
    # Customize Methods
    # --------------------------------------------------------------------------

    @staticmethod
    def _customize(dformat: str, ampm: bool):
        """
            Finishes customizing the message to indicate the error with the
            date format.

            :param dformat: The invalid date format.

            :param ampm: True, if the time being checked is in 12-hr format.
             False, otherwise.

            :return: The customized message.
        """

        # If its 12 or 24 hour format.
        fmt = "12" if ampm else '24'

        message = (
            f"\nThe date is currently being checked in {fmt}-hr format. Things "
            f"to check:\n"
            f"\t1. The date format must include the 'ii' literal, if the date "
            f"is given in 12-hr format; this is where the am/pm/m string in "
            f"the date must be placed.\n"
            f"\t2. If the date format is in 24-hr format, the 'i' character(s) "
            f"will be treated as separating characters.\n"
            f"\t3. There cannot be repeated fields, i.e., only a single year, "
            f"a single month, a single day, etc., field.\n"
            f"\t4. If the 12-hr format is requested, an hour must be provided."
            f"\n"
            f"Current requested format: {dformat}\n"
        )

        return DateFormatError._MESSAGE + message
