""" File that contains the date validator custom execptions. """

# ##############################################################################
# Imports
# ##############################################################################

# ##############################################################################
# Classes
# ##############################################################################


class YearFormatError(Exception):
    """
        Class that contains the constructor for the exception when the date year
        format is wrong.

        Properties:
        __________

        - self.base_message: The standard message to be displayed. Will be
          customized further if parameters are passed to the constructor.
    """

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Public Interface
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # ##########################################################################
    # Properties
    # ##########################################################################

    @property
    def base_message(self) -> str:
        """
            Returns the base message.

            :return: The base message for when the year format is not valid.
        """
        return "The year format is not valid."

    # ##########################################################################
    # Constructor
    # ##########################################################################

    def __init__(self, year: str, formats: tuple):
        """
            The method that builds the exception.

            :param year: The requested year format string.

            :param formats: The tuple that contains the valid formats for the
             year.
        """

        # Customize the message.
        message = self._customize(year, formats)

        super(YearFormatError, self).__init__(message)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Private Interface
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # ##########################################################################
    # Methods
    # ##########################################################################

    # --------------------------------------------------------------------------
    # Customize Methods
    # --------------------------------------------------------------------------

    def _customize(self, year: str, formats: tuple):
        """
            The method that further customizes the message.

            :param year: The requested year format string.

            :param formats: The tuple that contains the valid formats for the
             year.
        """

        message = (
            f"The requested year format, '{year}', is not valid. The only "
            f"available formats are {formats}."
        )

        return self.base_message + message
