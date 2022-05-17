from datetime import datetime


def get_duration_in_sec(time_b, time_a, datetime_fmt):
    time_b_dt = datetime.strptime(time_b, datetime_fmt)
    time_a_dt = datetime.strptime(time_a, datetime_fmt)
    time_diff = time_b_dt - time_a_dt
    return time_diff.total_seconds()
