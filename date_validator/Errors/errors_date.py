""" File that contains the date validator custom execptions. """

# ##############################################################################
# Imports
# ##############################################################################

# ##############################################################################
# Classes
# ##############################################################################


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

    def __init__(self, dformat: str = ""):
        """
            The method that builds the exception.

            :param dformat: The requested date format.
        """

        # Customize the message.
        message = self._customize(dformat)

        super(DateFormatError, self).__init__(message)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Private Interface
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # --------------------------------------------------------------------------
    # Customize Methods
    # --------------------------------------------------------------------------

    def _customize(self, dformat: str):
        """
            Finishes customizing the message to indicate the error with the
            date format.

            :param dformat: The invalid date format.

            :return: The customized message.
        """
        # TODO: Finish writing this method.
        return ""