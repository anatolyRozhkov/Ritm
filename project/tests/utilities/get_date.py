from datetime import datetime
import pytz


def current_time_in_gmt_plus_0():
    """
    Get current time in GMT+0 (Greenwich Mean Time) in hh:mm*/dd/MM**/yyyy format.

        *m stands for minute
    **M stands for month
    """
    # Set the time zone to GMT+0 (Greenwich Mean Time, GMT)
    gmt_plus_0_timezone = pytz.timezone('GMT')

    # Get the current time in the GMT+0 time zone
    current_datetime = datetime.now(gmt_plus_0_timezone)

    # Format the time and date
    formatted_datetime = current_datetime.strftime('%H:%M/%d/%m/%Y')

    return formatted_datetime


def get_time_and_date(date: str) -> str:
    """
    Extract time and date from the input string and
    return in 'hh:mm*/dd/MM**/yyyy' format.

    *m stands for minute
    **M stands for month
    """
    date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")

    current_hour = date_obj.strftime('%H')
    current_minute = date_obj.strftime('%M')

    formatted_datetime = f"{current_hour}:{current_minute}/{date_obj.strftime('%d/%m/%Y')}"

    return formatted_datetime
