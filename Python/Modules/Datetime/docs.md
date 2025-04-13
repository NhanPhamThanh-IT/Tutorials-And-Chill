# Python `datetime` Module: A Beginner's Guide

The `datetime` module in Python provides classes for working with dates and times. It allows you to manipulate dates and times in various ways, making it a fundamental tool for many applications.

## Core Concepts

The `datetime` module supplies classes for manipulating dates and times. While date and time arithmetic is supported, the focus of the implementation is on efficient attribute extraction for output formatting and manipulation.

## Main Classes

The module defines the following main classes:

1.  **`datetime.date`**: Represents a date (year, month, day).
2.  **`datetime.time`**: Represents a time (hour, minute, second, microsecond, tzinfo).
3.  **`datetime.datetime`**: Represents a combination of date and time.
4.  **`datetime.timedelta`**: Represents a duration, the difference between two dates or times.
5.  **`datetime.tzinfo`**: An abstract base class for time zone information objects.
6.  **`datetime.timezone`**: A class that implements `tzinfo` as a fixed offset from UTC.

---

### 1. `datetime.date`

Represents an idealized naive date, assuming the current Gregorian calendar always was, and always will be, in effect.
Attributes: `year`, `month`, `day`.

**Creating a `date` object:**

```python
import datetime

# Create a specific date
d = datetime.date(2023, 10, 27)
print(f"Date: {d}")
print(f"Year: {d.year}")
print(f"Month: {d.month}")
print(f"Day: {d.day}")

# Get today's date
today = datetime.date.today()
print(f"Today's date: {today}")
```

**Output:**

```
Date: 2023-10-27
Year: 2023
Month: 10
Day: 27
Today's date: <current_date>
```

---

### 2. `datetime.time`

Represents an idealized time, independent of any particular day, assuming that every day has exactly 24*60*60 seconds.
Attributes: `hour`, `minute`, `second`, `microsecond`, `tzinfo`.

**Creating a `time` object:**

```python
import datetime

# Create a specific time
t = datetime.time(14, 30, 55, 123456)
print(f"Time: {t}")
print(f"Hour: {t.hour}")
print(f"Minute: {t.minute}")
print(f"Second: {t.second}")
print(f"Microsecond: {t.microsecond}")
print(f"Timezone info: {t.tzinfo}") # Will be None for naive time
```

**Output:**

```
Time: 14:30:55.123456
Hour: 14
Minute: 30
Second: 55
Microsecond: 123456
Timezone info: None
```

---

### 3. `datetime.datetime`

Represents a combination of a date and a time.
Attributes: `year`, `month`, `day`, `hour`, `minute`, `second`, `microsecond`, `tzinfo`.

**Creating a `datetime` object:**

```python
import datetime

# Create a specific datetime
dt = datetime.datetime(2023, 10, 27, 14, 30, 55, 123456)
print(f"DateTime: {dt}")
print(f"Year: {dt.year}")
print(f"Hour: {dt.hour}")

# Get the current date and time
now = datetime.datetime.now()
print(f"Current DateTime: {now}")

# Get the current UTC date and time
utcnow = datetime.datetime.utcnow() # Note: This creates a naive datetime representing UTC.
print(f"Current UTC DateTime (naive): {utcnow}")

# Combine date and time objects
d = datetime.date(2023, 1, 1)
t = datetime.time(12, 0)
dt_combined = datetime.datetime.combine(d, t)
print(f"Combined DateTime: {dt_combined}")
```

**Output:**

```
DateTime: 2023-10-27 14:30:55.123456
Year: 2023
Hour: 14
Current DateTime: <current_datetime>
Current UTC DateTime (naive): <current_utc_datetime>
Combined DateTime: 2023-01-01 12:00:00
```

---

### 4. `datetime.timedelta`

Represents a duration, the difference between two `date`, `time`, or `datetime` instances. Useful for date arithmetic.

**Creating and using `timedelta`:**

```python
import datetime

# Create timedelta objects
delta1 = datetime.timedelta(days=5, hours=3)
delta2 = datetime.timedelta(weeks=1)

print(f"Delta 1: {delta1}")
print(f"Delta 2: {delta2}")

# Perform date arithmetic
today = datetime.date.today()
five_days_later = today + delta1
print(f"Today: {today}")
print(f"Five days and 3 hours later (date part): {five_days_later}") # Note: timedelta hours don't affect date object

now = datetime.datetime.now()
one_week_ago = now - delta2
print(f"Now: {now}")
print(f"One week ago: {one_week_ago}")

# Calculate difference between two datetimes
dt1 = datetime.datetime(2023, 10, 20, 10, 0, 0)
dt2 = datetime.datetime(2023, 10, 27, 14, 30, 0)
difference = dt2 - dt1
print(f"Difference between dt2 and dt1: {difference}")
print(f"Difference in days: {difference.days}")
print(f"Difference in seconds: {difference.total_seconds()}")
```

**Output:**

```
Delta 1: 5 days, 3:00:00
Delta 2: 7 days, 0:00:00
Today: <current_date>
Five days and 3 hours later (date part): <date_5_days_later>
Now: <current_datetime>
One week ago: <datetime_1_week_ago>
Difference between dt2 and dt1: 7 days, 4:30:00
Difference in days: 7
Difference in seconds: 621000.0
```

---

### Formatting Dates and Times (`strftime`)

The `strftime()` method formats a `date`, `time`, or `datetime` object into a string based on format codes.

**Example:**

```python
import datetime

now = datetime.datetime.now()

# Format examples
print(now.strftime("%Y-%m-%d"))          # YYYY-MM-DD
print(now.strftime("%d/%m/%Y"))          # DD/MM/YYYY
print(now.strftime("%A, %B %d, %Y"))    # Weekday, Month Day, Year
print(now.strftime("%I:%M:%S %p"))       # HH:MM:SS AM/PM (12-hour clock)
print(now.strftime("%H:%M:%S"))          # HH:MM:SS (24-hour clock)
print(now.strftime("%Y-%m-%d %H:%M:%S")) # Common ISO-like format
```

**Common Format Codes:**

*   `%Y`: Year with century (e.g., 2023)
*   `%y`: Year without century (e.g., 23)
*   `%m`: Month as a zero-padded decimal number (01, 02, ..., 12)
*   `%B`: Month as locale’s full name (e.g., January)
*   `%b`: Month as locale’s abbreviated name (e.g., Jan)
*   `%d`: Day of the month as a zero-padded decimal number (01, 02, ..., 31)
*   `%A`: Weekday as locale’s full name (e.g., Sunday)
*   `%a`: Weekday as locale’s abbreviated name (e.g., Sun)
*   `%H`: Hour (24-hour clock) as a zero-padded decimal number (00, 01, ..., 23)
*   `%I`: Hour (12-hour clock) as a zero-padded decimal number (01, 02, ..., 12)
*   `%p`: Locale’s equivalent of either AM or PM.
*   `%M`: Minute as a zero-padded decimal number (00, 01, ..., 59)
*   `%S`: Second as a zero-padded decimal number (00, 01, ..., 59)
*   `%f`: Microsecond as a decimal number, zero-padded on the left (000000 - 999999)
*   `%Z`: Time zone name (if the object is timezone-aware).
*   `%z`: UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).
*   `%c`: Locale’s appropriate date and time representation.
*   `%x`: Locale’s appropriate date representation.
*   `%X`: Locale’s appropriate time representation.

---

### Parsing Strings into Datetime Objects (`strptime`)

The `strptime()` *class method* creates a `datetime` object from a string representing a date and time and a corresponding format string.

**Example:**

```python
import datetime

date_string = "2023-10-27 15:45:30"
format_string = "%Y-%m-%d %H:%M:%S"

dt_object = datetime.datetime.strptime(date_string, format_string)
print(f"Parsed DateTime object: {dt_object}")
print(f"Year: {dt_object.year}")

date_string_2 = "Friday, October 27, 2023"
format_string_2 = "%A, %B %d, %Y"
date_object = datetime.datetime.strptime(date_string_2, format_string_2).date() # Get only the date part
print(f"Parsed Date object: {date_object}")
```

**Output:**

```
Parsed DateTime object: 2023-10-27 15:45:30
Year: 2023
Parsed Date object: 2023-10-27
```

**Important:** The format string passed to `strptime` must exactly match the structure of the date string. If they don't match, a `ValueError` will be raised.

---

### Time Zones (`tzinfo`, `timezone`)

By default, `datetime` objects are "naive," meaning they don't have time zone information associated with them. To make them "aware," you need to attach `tzinfo` objects.

Python 3.2+ includes the `datetime.timezone` class, a concrete implementation of `tzinfo` representing a fixed offset from UTC.

**Example (Python 3.2+):**

```python
import datetime

# Define UTC timezone
utc_tz = datetime.timezone.utc
print(f"UTC Timezone: {utc_tz}")

# Define a timezone for EST (UTC-5) - Note: This doesn't account for DST
est_tz = datetime.timezone(datetime.timedelta(hours=-5), name="EST")
print(f"EST Timezone: {est_tz}")

# Create an aware datetime object for current time in UTC
now_utc_aware = datetime.datetime.now(utc_tz)
print(f"Aware UTC DateTime: {now_utc_aware}")
print(f"Timezone Name: {now_utc_aware.tzname()}")
print(f"UTC Offset: {now_utc_aware.utcoffset()}")

# Create an aware datetime object for current time in EST
now_est_aware = datetime.datetime.now(est_tz)
print(f"Aware EST DateTime: {now_est_aware}")
print(f"Timezone Name: {now_est_aware.tzname()}")
print(f"UTC Offset: {now_est_aware.utcoffset()}")

# Convert between timezones
now_in_est = now_utc_aware.astimezone(est_tz)
print(f"UTC time converted to EST: {now_in_est}")
```

**Output (will vary based on current time):**

```
UTC Timezone: UTC
EST Timezone: EST
Aware UTC DateTime: <current_utc_datetime_aware>+00:00
Timezone Name: UTC
UTC Offset: 0:00:00
Aware EST DateTime: <current_est_datetime_aware>-05:00
Timezone Name: EST
UTC Offset: -1 day, 19:00:00
UTC time converted to EST: <converted_est_datetime>-05:00
```

**Note:** For complex time zone handling, especially involving Daylight Saving Time (DST), it's highly recommended to use third-party libraries like `pytz` or the standard library's `zoneinfo` module (Python 3.9+), which use the IANA time zone database.

```python
# Example using zoneinfo (Python 3.9+)
try:
	import zoneinfo # Available from Python 3.9+
	import datetime

	# Get current time in New York timezone
	ny_tz = zoneinfo.ZoneInfo("America/New_York")
	now_ny = datetime.datetime.now(ny_tz)
	print(f"\nCurrent time in New York: {now_ny}")
	print(f"Timezone Name: {now_ny.tzname()}") # Will show EST or EDT depending on DST
	print(f"UTC Offset: {now_ny.utcoffset()}")

except ImportError:
	print("\nzoneinfo module not available (requires Python 3.9+).")
except zoneinfo.ZoneInfoNotFoundError:
	print("\nTimezone database not found. Ensure tzdata is installed (`pip install tzdata`).")

```

---

This guide covers the fundamental aspects of the `datetime` module. Experiment with these examples to get comfortable working with dates and times in Python.