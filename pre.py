"""
Test program for pre-processing schedule
"""
import arrow

base = arrow.now()

def process(raw):
    """
    Line by line processing of syllabus file.  Each line that needs
    processing is preceded by 'head: ' for some string 'head'.  Lines
    may be continued if they don't contain ':'.  If # is the first
    non-blank character on a line, it is a comment ad skipped. 
    """
    field = None
    entry = { }
    cooked = [ ]
    beginDate = 0 #created new variable to hold the beginDate
    for line in raw:
        line = line.strip()
        if len(line) == 0 or line[0]=="#" :
            continue
        parts = line.split(':')
        if len(parts) == 1 and field:
            entry[field] = entry[field] + line + " "
            continue
        if len(parts) == 2: 
            field = parts[0]
            content = parts[1]
        else:
            raise ValueError("Trouble with line: '{}'\n".format(line) + 
                "Split into |{}|".format("|".join(parts)))

        if field == "begin":
            try:
                base = arrow.get(content, "MM/DD/YYYY")
                beginDate = base #save to the variable for later use.
                # print("Base date {}".format(base.isoformat()))
            except:
                raise ValueError("Unable to parse date {}".format(content))

        elif field == "week":
            if entry:
                cooked.append(entry)
                entry = { }
            entry['topic'] = ""
            entry['project'] = ""
            entry['week'] = content.strip() #strip to get rid of the space in the number
            entry['date'] = beginDate.replace(weeks=+(int(content)-1)).format('MMM D') #new entry field this will be the date column.
            
            #The only function added, determines if the entry is the current week. We create one 
            #final field to hold a 1 or 0 to check when our jinja template is processed.
            if isCurrentWeek(beginDate.replace(weeks=+(int(content)-1))): 
                entry['curWeek'] = 1
            else:
                entry['curWeek'] = 0

        elif field == 'topic' or field == 'project':
            entry[field] = content

        else:
            raise ValueError("Syntax error in line: {}".format(line))

    if entry:
        cooked.append(entry)

    return cooked

"""
This funciton will return a true/false on whether the date is in the current week.
Using the arrow library to make this easier. The arrow.isocalendar() returns
(year, week #, day), which is helpful because we can do a simple comparison then.
"""
def isCurrentWeek(date):
    startDate = date.isocalendar()
    curDate = arrow.now('local').isocalendar()
    if startDate[0] == curDate[0] and startDate[1] == curDate[1]: #if same year and week then this is the current week.
        return True
    return False


def main():
    f = open("data/schedule.txt")
    parsed = process(f)
    print(parsed)

if __name__ == "__main__":
    main()

    
    
            
    
