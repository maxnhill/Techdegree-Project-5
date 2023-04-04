from datetime import datetime

def format_date(date_str):
    date_obj = datetime.strptime(date_str, '%B, %Y')
    date = date_obj.date()
    return date





