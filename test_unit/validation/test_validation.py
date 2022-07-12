"""
    File that contains the test unit for the date format validation.
"""

# ##############################################################################
# Imports
# ##############################################################################

# General.
import unittest

# User defined.
import date_validator.validation.validation_format as vf

# ##############################################################################
# Classes.
# ##############################################################################


class TestDateValidator(unittest.TestCase):
    """
        Class that contains the tests for the format validation.
    """

    def test_formats(self):
        """
            Tests that the date fields are valid, given the state of the ampm
            flag.
        """

        # Auxiliary variables.
        ampm = True
        dformat = "YYYY-MM-DDD;hh:mm:ss:t"

        # Create a date format object.
        dformat = vf.FormatValidator(dformat, ampm)

        # Formats WITH ampm.
        formats = (
            'YYYY', 'YY', 'MMM', 'MM', 'DDD', 'DD', 'hh', 'mm', 'ss', 't', 'ii'
        )
        self.assertEqual(formats, dformat.formats)

        # Formats WITHOUT ampm.
        dformat.ampm = False
        formats = (
            'YYYY', 'YY', 'MMM', 'MM', 'DDD', 'DD', 'hh', 'mm', 'ss', 't',
        )
        self.assertEqual(formats, dformat.formats)

    def test_protected(self):
        """
            Tests that the protected characters are valid, given the state of
            the ampm flag.
        """
        # Auxiliary variables.
        ampm = True
        dformat = "YYYY-MM-DDD;hh:mm:ss:t"

        # Create a date format object.
        dformat = vf.FormatValidator(dformat, ampm)

        # Protected characters WITH ampm.
        protected = 'Y', 'M', 'D', 'h', 'm', 's', 't', 'i'
        self.assertEqual(protected, dformat.protected)

        # Protected characters WITHOUT ampm.
        dformat.ampm = False
        protected = 'Y', 'M', 'D', 'h', 'm', 's', 't'
        self.assertEqual(protected, dformat.protected)


# ##############################################################################
# Main Program.
# ##############################################################################

if __name__ == "__main__":
    unittest.main()
