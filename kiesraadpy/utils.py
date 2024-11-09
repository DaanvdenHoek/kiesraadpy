from datetime import date

DUTCH_MONTHS = [
    'januari', 
    'februari', 
    'maart', 
    'april', 
    'mei', 
    'juni', 
    'juli', 
    'augustus', 
    'september', 
    'oktober', 
    'november', 
    'december'
]

def parse_dutch_date_string(v: str) -> date:
    day, month, year = v.split(' ')
    month = DUTCH_MONTHS.index(month) + 1
    return date(int(year), month, int(day))
