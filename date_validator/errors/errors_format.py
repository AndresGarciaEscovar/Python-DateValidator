""" File that contains the date validator custom execptions. """

# ##############################################################################
# Imports
# ##############################################################################

# User defined.
import date_validator.utilities.utilities_strings as us

# ##############################################################################
# Classes
# ##############################################################################


class AmPmFormatError(Exception):
    """
        Class that contains the constructor for the exception when the date
        format contains the am/pm flag, but no hour is given.

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
            f"When the am/pm flag is given, an hour and the 'ii' string must be "
            f"provided for the time validation to be consistent."
        )

    # ##########################################################################
    # Constructor
    # ##########################################################################

    def __init__(self):
        """
            The method that builds the exception.
        """
        message = "\n" + us.to_length(self.base_message)
        super(AmPmFormatError, self).__init__(message)


class DayFormatError(Exception):
    """
        Class that contains the constructor for the exception when the date
        format contains a day in the 'DD' format and a month is NOT given.

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
            f"A day was provided in the format 'DD', but no month was provided."
            f" A month must be provided, either in 'MMM' or 'MM' format, for "
            f"the day to be validated."
        )

    # ##########################################################################
    # Constructor
    # ##########################################################################

    def __init__(self):
        """
            The method that builds the exception.
        """
        message = "\n" + us.to_length(self.base_message)
        super(DayFormatError, self).__init__(message)


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

        # Turn the formats into quoted strings.
        fmts = list(map(lambda x: f"'{x}'", self.fields))

        # Customize the message.
        if len(fmts) > 1:
            length = 2
            fmts = ", ".join(fmts[:-1]) + " and " + fmts[-1]
        else:
            length = 1
            fmts = f"'{fmts[0]}'"

        message = (
            f" The requested date format, '{self.dformat}', is not valid, since"
            f" it doesn't contain any valid fields.\nValid "
            f"{'fields are' if length > 1 else 'field is'}: {fmts}."
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

        # Customize the message.
        if len(fmts) > 1:
            length = 2
            fmts = ", ".join(fmts[:-1]) + " and " + fmts[-1]
        else:
            length = 1
            fmts = f"{fmts[0]}"

        message = (
            f" The requested {self.field} format, '{field_format}', is not "
            f"valid. The only available "
            f"{'formats' if length > 1 else 'format'} for the "
            f"{self.field} field {'are' if length > 1 else 'is'} {fmts}."
        )

        return self.base_message + message


class HourFormatError(Exception):
    """
        Class that contains the constructor for the exception when the date
        format contains an hour, a year and/or a month, but not a day 'DD'
        or 'DDD' format.

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
            f"An hour was provided with a year and/or a month, but no day was "
            f"provided, in 'DD' or 'DDD' format. In this case, if a day is not "
            f"provided, the hour cannot be consistently validated."
        )

    # ##########################################################################
    # Constructor
    # ##########################################################################

    def __init__(self):
        """
            The method that builds the exception.
        """
        message = "\n" + us.to_length(self.base_message)
        super(HourFormatError, self).__init__(message)


class MinutesFormatError(Exception):
    """
        Class that contains the constructor for the exception when the date
        format contains a minute field, a year, a month and/or a day, but
        not an hour in 'hh' format.

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
            f"A minute was provided with a year, a month and/or a day, but no "
            f"hour was provided, in 'hh' format. In this case, if an hour is "
            f"not provided, the minutes cannot be consistently validated."
        )

    # ##########################################################################
    # Constructor
    # ##########################################################################

    def __init__(self):
        """
            The method that builds the exception.
        """
        message = "\n" + us.to_length(self.base_message)
        super(MinutesFormatError, self).__init__(message)


class RepeatedFieldsError(Exception):
    """
        Class that contains the constructor for the exception when there is one,
        or more, repeated fields.

        Parameters:
        __________

        - self.fields: The fields that are being checked for repetition.

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
        return f"There are repeated fields, when there shouldn't."

    # ##########################################################################
    # Constructor
    # ##########################################################################

    def __init__(self, fields: tuple):
        """
            The method that builds the exception.

            :param fields: The requested fields.
        """

        # Store the field name here.
        self.fields = fields

        # Customize the message.
        message = "\n" + us.to_length(self._customize())

        super(RepeatedFieldsError, self).__init__(message)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Private Interface
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # ##########################################################################
    # Methods
    # ##########################################################################

    # --------------------------------------------------------------------------
    # Customize Methods
    # --------------------------------------------------------------------------

    def _customize(self) -> str:
        """
            The method that further customizes the message.

            :return: The message with more information.
        """

        # Get the field strings.
        fmts = list(map(lambda x: f"'{x}'", self.fields))

        # Customize the message.
        if len(fmts) > 1:
            fmts = ", ".join(fmts[:-1]) + " and " + fmts[-1]
        else:
            fmts = f"'{fmts[0]}'"

        # Get the repeated fields indexes.
        repeated = self._get_repeated()
        repeated = ", ".join(list(map(str, repeated)))

        # Customized message.
        message = (
            f" There are requested fields that are repeated: '{fmts}'. The "
            f"indexes of the repeated fields are: {repeated}."
        )

        return self.base_message + message

    # --------------------------------------------------------------------------
    # Get Methods
    # --------------------------------------------------------------------------

    def _get_repeated(self) -> list:
        """
            Gets the tuple with the tuple indexes of the repeated fields.

            :return: A list of tuples with the repeated indexes.
        """
        # Auxiliary variables.
        indexes = []

        # Search for repeated fields.
        for i, field0 in enumerate(self.fields):
            for j, field1 in enumerate(self.fields[i + 1:]):
                # Append the indexes of repeated fields.
                if field0[0] == field1[0]:
                    indexes.append((i, j + i + 1))

        return indexes


class SecondsFormatError(Exception):
    """
        Class that contains the constructor for the exception when the date
        format contains a minute field, a year, a month, a day and/or an hour,
        but not minutes in 'mm' format.

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
            f"A second was provided with a year, a month, a day and/or an hour,"
            f" but no minutes were provided, in 'mm' format. In this case, if "
            f"minutes are not provided, the seconds cannot be consistently "
            f"validated."
        )

    # ##########################################################################
    # Constructor
    # ##########################################################################

    def __init__(self):
        """
            The method that builds the exception.
        """
        message = "\n" + us.to_length(self.base_message)
        super(SecondsFormatError, self).__init__(message)


class TenthsFormatError(Exception):
    """
        Class that contains the constructor for the exception when the date
        format contains a minute field, a year, a month, a day, hours and/or
        minutes, but not seconds in 'ss' format.

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
            f"Tenths of second were provided with a year, a month, a day, "
            f"hours and/or minutes but no seconds were provided, in 'ss' "
            f"format. In this case, if seconds are not provided, the tenths of "
            f"seconds cannot be consistently validated."
        )

    # ##########################################################################
    # Constructor
    # ##########################################################################

    def __init__(self):
        """
            The method that builds the exception.
        """
        message = "\n" + us.to_length(self.base_message)
        super(TenthsFormatError, self).__init__(message)
