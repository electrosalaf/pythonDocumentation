# Explicit line joining
# Two or more lines are joined by \  and this only applicable to the string literals

if 1900 < year < 2100 and 1 <= month <= 12 \
    and 1 <= day <= 31 and 0 <= hour <= 24 \
        and 1 <= minute <= 60 and 1 <= second <= 60:    # looks like a valid date
             return 1
        
# Implicit line joining
# Two or more lines in parenthesis, brackets or curly braces can be joined without using backlashes
# Implicit line joining can take comments

month_names = ['January', 'February', 'March',      # These are the
               'April', 'May', 'June',              # English names
               'July', 'August', 'September',       # for the month
               'October', 'November', 'December']   # of the year


