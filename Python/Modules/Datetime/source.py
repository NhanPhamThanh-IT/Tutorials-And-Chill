import datetime
import zoneinfo

# Import the datetime module, which provides classes for working with dates and times.

# Import zoneinfo for timezone support (available in Python 3.9+)
# If zoneinfo is not available (older Python or missing tzdata), we'll handle it.
try:
except ImportError:
    zoneinfo = None # Set to None if import fails

print("--- Getting Current Date and Time ---")

# 1. Get the current date and time using datetime.datetime.now()
# This creates a 'datetime' object representing the current moment.
# By default, it's 'naive', meaning it doesn't have timezone information attached.
now_naive = datetime.datetime.now()
print(f"Current naive date and time: {now_naive}")
print(f"Type of now_naive: {type(now_naive)}")

# 2. Get the current date and time in Coordinated Universal Time (UTC)
# This creates an 'aware' datetime object, meaning it includes timezone information.
# datetime.timezone.utc represents the UTC timezone.
now_utc = datetime.datetime.now(datetime.timezone.utc)
print(f"Current UTC date and time: {now_utc}")
print(f"Type of now_utc: {type(now_utc)}")

# 3. Get the current local date using datetime.date.today()
# This creates a 'date' object, representing only the date (year, month, day).
today = datetime.date.today()
print(f"Current date: {today}")
print(f"Type of today: {type(today)}")

# You can also get the UTC date
today_utc = datetime.datetime.now(datetime.timezone.utc).date()
print(f"Current UTC date: {today_utc}")


print("\n--- Creating Specific Date and Time Objects ---")

# 1. Create a specific date object using datetime.date(year, month, day)
specific_date = datetime.date(2023, 10, 26) # October 26, 2023
print(f"Specific date: {specific_date}")

# 2. Create a specific time object using datetime.time(hour, minute, second, microsecond)
# Hour is in 24-hour format (0-23). Microsecond is optional.
specific_time = datetime.time(14, 30, 55, 123456) # 2:30:55.123456 PM
print(f"Specific time: {specific_time}")
print(f"Type of specific_time: {type(specific_time)}")

# 3. Create a specific naive datetime object using datetime.datetime(year, month, day, hour, minute, second, microsecond)
specific_datetime_naive = datetime.datetime(2024, 1, 15, 9, 0, 0) # January 15, 2024, 9:00:00 AM
print(f"Specific naive datetime: {specific_datetime_naive}")

# 4. Create a specific aware datetime object by providing timezone info (tzinfo)
# We can use datetime.timezone.utc for UTC.
specific_datetime_utc = datetime.datetime(2024, 3, 10, 18, 0, 0, tzinfo=datetime.timezone.utc)
print(f"Specific UTC datetime: {specific_datetime_utc}")

# 5. Create a specific aware datetime object with a specific timezone (e.g., 'America/New_York')
# This requires the 'zoneinfo' module (Python 3.9+) or a third-party library like 'pytz'.
# If using zoneinfo, you might need to install the timezone database separately
# (e.g., `pip install tzdata` on Windows, or system package manager on Linux/macOS).
if zoneinfo:
    try:
        # Create a ZoneInfo object for the desired timezone
        ny_tz = zoneinfo.ZoneInfo("America/New_York")

        # Create the datetime object with the timezone
        specific_datetime_ny = datetime.datetime(2024, 3, 10, 13, 0, 0, tzinfo=ny_tz) # March 10, 2024, 1:00 PM in New York
        print(f"Specific New York datetime: {specific_datetime_ny}")

        # You can convert between timezones using astimezone()
        utc_time_in_ny = now_utc.astimezone(ny_tz)
        print(f"Current New York time (converted from UTC): {utc_time_in_ny}")

    except zoneinfo.ZoneInfoNotFoundError:
        print("Timezone 'America/New_York' not found.")
        print("Ensure the timezone database is installed (e.g., 'pip install tzdata' or system package).")
else:
    print("\n'zoneinfo' module not available (requires Python 3.9+).")
    print("For timezone support in older Python versions, consider installing the 'pytz' library (`pip install pytz`).")


print("\n--- Accessing Date and Time Components ---")
# You can access individual parts of date, time, and datetime objects.
dt_obj = datetime.datetime(2023, 12, 31, 23, 59, 58, 123)

print(f"Original datetime object: {dt_obj}")
print(f"Year: {dt_obj.year}")       # e.g., 2023
print(f"Month: {dt_obj.month}")     # e.g., 12
print(f"Day: {dt_obj.day}")         # e.g., 31
print(f"Hour: {dt_obj.hour}")       # e.g., 23
print(f"Minute: {dt_obj.minute}")   # e.g., 59
print(f"Second: {dt_obj.second}")   # e.g., 58
print(f"Microsecond: {dt_obj.microsecond}") # e.g., 123

# Get the date part
print(f"Date part: {dt_obj.date()}")
# Get the time part
print(f"Time part: {dt_obj.time()}")

# Get the day of the week
# weekday(): Monday is 0 and Sunday is 6
print(f"Weekday (Mon=0, Sun=6): {dt_obj.weekday()}")
# isoweekday(): Monday is 1 and Sunday is 7
print(f"ISO Weekday (Mon=1, Sun=7): {dt_obj.isoweekday()}")

# Get the day of the year
print(f"Day of the year: {dt_obj.timetuple().tm_yday}")

# Get ISO calendar information (year, week number, weekday)
print(f"ISO Calendar (year, week, weekday): {dt_obj.isocalendar()}")

# Access timezone information (if the object is aware)
print(f"Timezone info (naive object): {dt_obj.tzinfo}") # Will be None for naive objects
print(f"Timezone info (UTC object): {now_utc.tzinfo}")
if zoneinfo and 'specific_datetime_ny' in locals(): # Check if NY object was created
    print(f"Timezone info (NY object): {specific_datetime_ny.tzinfo}")
    print(f"Timezone name (NY object): {specific_datetime_ny.tzname()}") # e.g., EST or EDT
    print(f"UTC offset (NY object): {specific_datetime_ny.utcoffset()}") # e.g., -05:00:00 or -04:00:00
    print(f"DST offset (NY object): {specific_datetime_ny.dst()}") # Daylight Saving Time offset, e.g., 0:00:00 or 1:00:00


print("\n--- Formatting Dates and Times (strftime) ---")
# strftime: Converts a datetime object into a formatted string.
# You provide a format code string to specify how you want it displayed.

# Common format codes:
# %Y: Year with century (e.g., 2023)
# %y: Year without century (e.g., 23)
# %m: Month as a zero-padded decimal number (e.g., 01, 12)
# %B: Month as locale's full name (e.g., January, February)
# %b: Month as locale's abbreviated name (e.g., Jan, Feb)
# %d: Day of the month as a zero-padded decimal number (e.g., 01, 31)
# %A: Weekday as locale's full name (e.g., Monday, Tuesday)
# %a: Weekday as locale's abbreviated name (e.g., Mon, Tue)
# %H: Hour (24-hour clock) as a zero-padded decimal number (e.g., 00, 23)
# %I: Hour (12-hour clock) as a zero-padded decimal number (e.g., 01, 12)
# %p: Locale's equivalent of either AM or PM.
# %M: Minute as a zero-padded decimal number (e.g., 00, 59)
# %S: Second as a zero-padded decimal number (e.g., 00, 59)
# %f: Microsecond as a decimal number, zero-padded on the left (e.g., 000000)
# %Z: Time zone name (if timezone aware). Empty string if naive.
# %z: UTC offset in the form +HHMM or -HHMM (if timezone aware). Empty string if naive.
# %j: Day of the year as a zero-padded decimal number (e.g., 001, 366).
# %U: Week number of the year (Sunday as the first day of the week) (e.g., 00, 53).
# %W: Week number of the year (Monday as the first day of the week) (e.g., 00, 53).
# %c: Locale's appropriate date and time representation.
# %x: Locale's appropriate date representation.
# %X: Locale's appropriate time representation.

current_dt = datetime.datetime.now()

# Example formats:
format1 = current_dt.strftime("%Y-%m-%d") # YYYY-MM-DD
print(f"Format 1 (YYYY-MM-DD): {format1}")

format2 = current_dt.strftime("%d/%m/%Y %H:%M:%S") # DD/MM/YYYY HH:MM:SS
print(f"Format 2 (DD/MM/YYYY HH:MM:SS): {format2}")

format3 = current_dt.strftime("%A, %B %d, %Y") # Weekday, Month Day, Year
print(f"Format 3 (Weekday, Month Day, Year): {format3}")

format4 = current_dt.strftime("%I:%M:%S %p") # HH:MM:SS AM/PM
print(f"Format 4 (HH:MM:SS AM/PM): {format4}")

# Formatting an aware object
format5_utc = now_utc.strftime("%Y-%m-%d %H:%M:%S %Z%z") # Include timezone info
print(f"Format 5 (UTC with TZ): {format5_utc}")

if zoneinfo and 'specific_datetime_ny' in locals():
    format6_ny = specific_datetime_ny.strftime("%Y-%m-%d %I:%M:%S %p %Z (%z)")
    print(f"Format 6 (NY with TZ): {format6_ny}")


print("\n--- Parsing Strings into Dates and Times (strptime) ---")
# strptime: Converts a string into a datetime object.
# You need to provide the string and the format code that matches the string's structure.

date_string1 = "2023-11-20"
format_code1 = "%Y-%m-%d"
# Use .date() at the end if you only want the date part
parsed_date1 = datetime.datetime.strptime(date_string1, format_code1).date()
print(f"Parsed '{date_string1}' into date object: {parsed_date1}, Type: {type(parsed_date1)}")

datetime_string1 = "25/Dec/2024 10:30:00 AM"
format_code2 = "%d/%b/%Y %I:%M:%S %p" # %b for abbreviated month, %I for 12-hour, %p for AM/PM
parsed_datetime1 = datetime.datetime.strptime(datetime_string1, format_code2)
print(f"Parsed '{datetime_string1}' into datetime object: {parsed_datetime1}, Type: {type(parsed_datetime1)}")

# Parsing a string with timezone offset information (%z)
# The offset must be in the format +HHMM or -HHMM (no colon)
datetime_string_offset = "2024-01-15 09:00:00+0100"
format_code_offset = "%Y-%m-%d %H:%M:%S%z"
try:
    parsed_datetime_offset = datetime.datetime.strptime(datetime_string_offset, format_code_offset)
    print(f"Parsed '{datetime_string_offset}' with offset: {parsed_datetime_offset}")
    print(f"Timezone info: {parsed_datetime_offset.tzinfo}")
except ValueError as e:
    print(f"Error parsing string with offset: {e}")

# Note: Parsing timezone names (%Z) is often unreliable and platform-dependent.
# It's generally better to parse the offset (%z) if available, or handle timezones after parsing a naive datetime.


print("\n--- Working with timedelta (Duration/Difference) ---")
# timedelta represents a duration or the difference between two dates or times.
# You can create timedelta objects specifying days, seconds, microseconds, milliseconds, minutes, hours, weeks.

# Create a timedelta representing 5 days, 3 hours, 30 minutes
delta1 = datetime.timedelta(days=5, hours=3, minutes=30)
print(f"Timedelta 1: {delta1}")

# Create a timedelta representing 2 weeks
delta2 = datetime.timedelta(weeks=2)
print(f"Timedelta 2 (2 weeks): {delta2}")

# Add a timedelta to a datetime object to get a future datetime
current_dt = datetime.datetime.now()
future_dt = current_dt + delta1
print(f"Current datetime: {current_dt}")
print(f"Future datetime (+ {delta1}): {future_dt}")

# Subtract a timedelta from a datetime object to get a past datetime
past_dt = current_dt - delta2
print(f"Past datetime (- {delta2}): {past_dt}")

# Calculate the difference between two datetime objects - the result is a timedelta
dt_start = datetime.datetime(2023, 1, 1, 10, 0, 0)
dt_end = datetime.datetime(2023, 1, 10, 14, 30, 0)
difference = dt_end - dt_start
print(f"Difference between {dt_end} and {dt_start}: {difference}")

# Get the total duration in seconds from a timedelta
total_seconds = difference.total_seconds()
print(f"Difference in total seconds: {total_seconds}")

# Access components of a timedelta (days, seconds, microseconds)
# Note: 'seconds' is only the seconds part (0-86399), not the total seconds.
print(f"Timedelta components: Days={difference.days}, Seconds={difference.seconds}, Microseconds={difference.microseconds}")

# You can also calculate differences between date objects
date1 = datetime.date(2023, 10, 26)
date2 = datetime.date(2023, 11, 5)
date_difference = date2 - date1
print(f"Difference between {date2} and {date1}: {date_difference}")


print("\n--- Comparing Dates and Times ---")
# You can compare date and datetime objects using standard comparison operators.

dt1 = datetime.datetime(2023, 1, 1)
dt2 = datetime.datetime(2024, 1, 1)
dt3 = datetime.datetime(2023, 1, 1)

print(f"Is {dt1} < {dt2}? {dt1 < dt2}")   # True
print(f"Is {dt1} > {dt2}? {dt1 > dt2}")   # False
print(f"Is {dt1} == {dt3}? {dt1 == dt3}") # True
print(f"Is {dt1} != {dt2}? {dt1 != dt2}") # True

# Comparing aware and naive datetimes will raise a TypeError
naive_dt = datetime.datetime(2023, 1, 1, 12, 0, 0)
aware_dt = datetime.datetime(2023, 1, 1, 12, 0, 0, tzinfo=datetime.timezone.utc)
try:
    print(naive_dt == aware_dt)
except TypeError as e:
    print(f"Cannot compare naive and aware datetimes directly: {e}")

# To compare, make them both naive or both aware (usually convert to UTC)
aware_dt_in_utc = aware_dt.astimezone(datetime.timezone.utc)
# If you know the naive time represents UTC, you can make it aware:
naive_dt_as_utc = naive_dt.replace(tzinfo=datetime.timezone.utc)
print(f"Comparing aware UTC and naive-made-aware UTC: {aware_dt_in_utc == naive_dt_as_utc}") # True


print("\n--- Date Arithmetic ---")
# You can add/subtract timedeltas from date objects as well.

today = datetime.date.today()
one_day = datetime.timedelta(days=1)
ten_days = datetime.timedelta(days=10)

tomorrow = today + one_day
yesterday = today - one_day
ten_days_ago = today - ten_days
ten_days_later = today + ten_days

print(f"Yesterday: {yesterday}")
print(f"Today: {today}")
print(f"Tomorrow: {tomorrow}")
print(f"10 days ago: {ten_days_ago}")
print(f"10 days later: {ten_days_later}")


print("\n--- Combining Date and Time ---")
# If you have separate date and time objects, you can combine them into a datetime object.
my_date = datetime.date(2025, 5, 10)
my_time = datetime.time(16, 45, 0)

combined_dt = datetime.datetime.combine(my_date, my_time)
print(f"Combined date {my_date} and time {my_time}: {combined_dt}")
print(f"Type of combined object: {type(combined_dt)}")


print("\n--- ISO 8601 Format ---")
# ISO 8601 is a standard way to represent dates and times.
# Python's datetime objects have built-in methods for this.

# .isoformat(): Converts a date/datetime object to an ISO 8601 string.
iso_date_str = today.isoformat() # YYYY-MM-DD
print(f"ISO format date: {iso_date_str}")

iso_datetime_naive_str = now_naive.isoformat() # YYYY-MM-DDTHH:MM:SS.ffffff
print(f"ISO format naive datetime: {iso_datetime_naive_str}")

# For aware objects, the UTC offset is included
iso_datetime_utc_str = now_utc.isoformat() # YYYY-MM-DDTHH:MM:SS.ffffff+00:00
print(f"ISO format UTC datetime: {iso_datetime_utc_str}")

if zoneinfo and 'specific_datetime_ny' in locals():
    iso_datetime_ny_str = specific_datetime_ny.isoformat() # YYYY-MM-DDTHH:MM:SS.ffffff-HH:MM
    print(f"ISO format NY datetime: {iso_datetime_ny_str}")

# .fromisoformat(): Parses an ISO 8601 string back into a date/datetime object.
iso_str1 = "2023-10-26"
date_from_iso = datetime.date.fromisoformat(iso_str1)
print(f"Date from ISO string '{iso_str1}': {date_from_iso}")

iso_str2 = "2024-02-29T10:30:00"
dt_from_iso_naive = datetime.datetime.fromisoformat(iso_str2)
print(f"Naive datetime from ISO string '{iso_str2}': {dt_from_iso_naive}")

iso_str3 = "2024-03-15T15:00:00+02:00" # Includes timezone offset
dt_from_iso_aware = datetime.datetime.fromisoformat(iso_str3)
print(f"Aware datetime from ISO string '{iso_str3}': {dt_from_iso_aware}")
print(f"Timezone info: {dt_from_iso_aware.tzinfo}")

print("\n--- End of Datetime Examples ---")