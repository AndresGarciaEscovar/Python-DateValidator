""" File that contains the date validator custom execptions. """

# ##############################################################################
# Imports
# ##############################################################################

# User defined.
import date_validator.utilities.utilities_strings as us

# ##############################################################################
# Classes
# ##############################################################################


class FieldFormatError(Exception):
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

            :return: The base message for when the field format is not valid.
        """
        return f"The {self.field} format is not valid."

    # ##########################################################################
    # Constructor
    # ##########################################################################

    def __init__(self, field: str, year: str, formats: tuple):
        """
            The method that builds the exception.

            :param field: The name of the field with the error.

            :param year: The requested year format string.

            :param formats: The tuple that contains the valid formats for the
             year.
        """

        # Store the field name here.
        self.field = field

        # Customize the message.
        message = "\n" + us.to_length(self._customize(year, formats))

        super(FieldFormatError, self).__init__(message)

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

            :param field: The name of the field that contains the error.

            :param year: The requested field format string.

            :param formats: The tuple that contains the valid formats for the
             field.
        """

        fmts = list(map(lambda x: f"'{x}'", formats))
        fmts = ", ".join(fmts[:-1]) + " and " + fmts[-1]

        message = (
            f" The requested {self.field} format, '{year}', is not valid. The only "
            f"available {'formats' if len(fmts) > 1 else 'format'} for the "
            f"{self.field} {'are' if len(fmts) > 1 else 'is'} {fmts}."
        )

        return self.base_message + message
