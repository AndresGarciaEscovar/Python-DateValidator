""" File that contains the date validator custom execptions. """

# ##############################################################################
# Imports
# ##############################################################################

# User defined.
import date_validator.utilities.utilities_strings as us

# ##############################################################################
# Classes
# ##############################################################################


class EmptyFormatError(Exception):
    """
        Class that contains the constructor for the exception when the date
        format is empty.

        Parameters:
        __________

        - self.dformat: The request date format.

        - self.fields: The format of the fields that can be included.

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

            :return: The base message for when the field format constains no
             valid fields.
        """
        return (
            f"The date format doesn't contain any fields to be checked. Make "
            f"sure to include at least one valid field."
        )

    # ##########################################################################
    # Constructor
    # ##########################################################################

    def __init__(self, dformat: str, fields: tuple):
        """
            The method that builds the exception.

            :param dformat: The current date format.

            :param fields: The tuple that contains the valid fields to be given
             in the date format.
        """

        # Store the valid fields and the current date format.
        self.fields = fields
        self.dformat = dformat

        # Customize the message.
        message = "\n" + us.to_length(self._customize())

        super(EmptyFormatError, self).__init__(message)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Private Interface
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # ##########################################################################
    # Methods
    # ##########################################################################

    # --------------------------------------------------------------------------
    # Customize Methods
    # --------------------------------------------------------------------------

    def _customize(self):
        """
            The method that further customizes the message.

            :return: The customized message.
        """

        fmts = list(map(lambda x: f"'{x}'", self.fields))
        fmts = ", ".join(fmts[:-1]) + " and " + fmts[-1]

        message = (
            f" The requested date format, '{self.dformat}', is not valid, since"
            f" it doesn't contain any valid fields.\nValid fields are: {fmts}."
        )

        return self.base_message + message


class FieldFormatError(Exception):
    """
        Class that contains the constructor for the exception when the given
        date field format is wrong.

        Parameters:
        __________

        - self.field: The name of the field with the error.

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

    def __init__(self, field: str, field_format: str, formats: tuple):
        """
            The method that builds the exception.

            :param field: The name of the field with the error.

            :param field_format: The requested field format string.

            :param formats: The tuple that contains the valid formats for the
             year.
        """

        # Store the field name here.
        self.field = field

        # Customize the message.
        message = "\n" + us.to_length(self._customize(field_format, formats))

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

    def _customize(self, field_format: str, formats: tuple) -> str:
        """
            The method that further customizes the message.

            :param field_format: The requested field format string.

            :param formats: The tuple that contains the valid formats for the
             field.

            :return: The message with more information.
        """

        fmts = list(map(lambda x: f"'{x}'", formats))
        fmts = ", ".join(fmts[:-1]) + " and " + fmts[-1]

        message = (
            f" The requested {self.field} format, '{field_format}', is not "
            f"valid. The only available "
            f"{'formats' if len(fmts) > 1 else 'format'} for the "
            f"{self.field} field {'are' if len(fmts) > 1 else 'is'} {fmts}."
        )

        return self.base_message + message
