from datetime import datetime

def format_date(date_str):
    date_string = date_str.replace(",", " ")
    date_obj = datetime.strptime(date_str, '%B, %Y')
    formatted_date = date_obj.date().isoformat()
    return (formatted_date)


