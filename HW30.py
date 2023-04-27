from datetime import datetime
import datetime as td

l_count = 32
first_l = '27/03/2023 19:15'

diff_1 = td.timedelta(days=3)
diff_2 = td.timedelta(days=4)
date = datetime.strptime(first_l, '%d/%m/%Y %H:%M')
counter = 1

while counter <= l_count:
    print("Lecture {:>2}: {:>17}".format(str(counter), date.strftime('%d %b %Y %H:%M')))
    counter += 1
    date += diff_1
    print("Lecture {:>2}: {:>17}".format(str(counter), date.strftime('%d %b %Y %H:%M')))
    counter += 1
    date += diff_2
