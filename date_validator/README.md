# Date Validator Program

The intent of this program is to provide a lightweight and simple date and date 
format validator, i.e., given a string with a date and a date format, the
program determines if the date matches the date format and determines if the
format is consistent. The consistency of the date format is determined by
checking that the proper data is given so that checking the other quantities is
not ambiguous.

## Defining a Date Format

The available fields to be included in the date format are:

| Field             | Format | Details                             | Example |
|-------------------|--------|-------------------------------------|---------|
 | Year              | 'YYYY' | Four digit year.                    | '1943'  |
| Year              | 'YY'   | Two-digit year.                     | '43'    |
 | Month             | 'MMM'  | Three-letter month                  | 'FEB'   |
| Month             | 'MM'   | Two-digit month                     | '02'    |
| Day               | 'DDD'  | Three-digit day of year             | '029'   |
| Day               | 'DD'   | Two-digit day of month              | '29'    |
| Hour              | 'hh'   | Two-digit hour                      | '19'    |
| Minutes           | 'mm'   | Two-digit minutes of hour           | '39'    |
| Seconds           | 'ss'   | Two-digit seconds of minute         | '09'    |
| Tenths of Seconds | 't'    | One-digit tenths of second          | '4'     |
| am/pm/m marker*   | 'ii'   | One- or two-digit 12-hr format flag | 'm'     |
\* Only considered if the _**self.ampm**_ flag is set to True.

To define a format, the different fields can be placed into a format string, 
indicating the position of each digit within the date string, for example:
```python
dformat = 'YYYYDDDhh'  # Possibly valid format.
```
The above format contains a four-digit year, a three-digit day and a two-digit
hour. If repeated fields are requested, the format will be deemed invalid.
```python
dformat = 'YYYYMMMYY' # Invalid format, year is requested twice.
```
The characters that appear in the table above are **reserved characters** that
cannot be used as separators, except for the `'i'` character, that is reserved
only if the time is requested to be in 12-hr format.

Months requested in three-letter format are **NOT** case-sensitive, e.g., 
`FEB = fEb`.

### Hour in 12-hr Format

If the time is requested in 12-hr format, the format string must include the
`"ii"` string in the position where the `"am"`, `"pm"` or `"m"` strings are
placed.

#### Example
To request the date validation in 12-hr format:
```python
dformat = 'hhmmssii'
```
In this case, the validator will look for a date with the `'am'`, `"pm"` or 
`"m"` string at the final position. The validator is designed such that, in the
case that the 12-hr format is requested, the `"am"`, `"pm"` or `"m"` string will
be removed from the date, as well as the `"ii"` string from the date format, 
before moving forward with the validation.

### Separators

Separator characters are characters that are **NOT** in the reserved characters.
They are typically used to separate the fields in a logical way, although not
required.

#### Example
A typical format for dates is:
```python
dformat = 'YYYY-MM-DD'
```
That is the four-digit year (`YYYY`), a two-digit month (`MM`) and a two-digit 
day (`DD`) separated by a dash (`-`). In this case, the dash is the _separator_,
or a separating character.

## Getting Started

### Importing the module.

To start the validation, import the date validator:
```python
import date_validator.validation.validation_date
```
The only available function will be the "Validator" class. To create an instance
of the validator, a date and a date format must be probided:
```python
# Import the package.
import date_validator.validation.validation_date as dv

# Define the date and the date validator.
date = "202402292218453"
date_format = "YYYYMMDDhhmmsst"

# If the time is given in 12-hr format.
ampm = False

# Get an instance of the date creator.
validator = dv.DateValidator(date=date, dformat=date_format, ampm=ampm)
```
In this case, the year `YYYY` is given in a four-digit format, the month is
given in a two-digit format `MM`, the day is given in two-digit format `DD`, the
hours `hh` are given in a two-digit format, the minutes `mm` are given in a 
two-digit format, the seconds `ss` are given in a two-digit format and the 
tenths of second `t` are given in a three digit format.

To get the result of the date validation, use the class instance as a
**callable** object:
```python
# Import the package.
import date_validator.validation.validation_date as dv

# Define the date and the date validator.
date = "202402292218453"
date_format = "YYYYMMDDhhmmsst"

# If the time is given in 12-hr format.
ampm = False

# Get an instance of the date creator.
validator = dv.DateValidator(date=date, dformat=date_format, ampm=ampm)

# Extract the value.
valid = validator()

if valid:
    ...
```
There are currenty no other options available.

## Considerations

Certain quantities need other quantities to appear in order for them to be
consistently validated. Hours don't make sense if a month and/or
a year are provided, but no day is provided; minutes don't make sense if a
year, month and/or day are provided, but no hour is provided; etc.

#### Example

If, for example, a month and an hour are provided, it is ambiguous to validate 
the hour. Thus, to make the format consistent either a day has to be provided, 
or the month has to be removed.
```python
dformat = 'MM-hh' # Inconsistent, time of month is not a valid quantity.
```
```python
dformat = 'DDDhh' # If a day is provided, the hour of day makes sense.
```
```python
dformat = 'hh' # An hour by itself makes sense.
```

