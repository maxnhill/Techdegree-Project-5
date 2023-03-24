from datetime import datetime

def format_date(date_str):
    date_string = date_str.replace(",", " ")
    date_obj = datetime.strptime(date_string.strip(), '%B, %Y')
    formatted_date = date_obj.strftime('%Y-%m')
    return (formatted_date)


