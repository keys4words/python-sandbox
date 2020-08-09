import datetime
import statistics as st


filename = 'inout/data/data3.txt'
message_fmt = '''
# Статистика на дату:  {date}
# Количество цифер:    {count}
# Сумма:               {sum}
# Среднее:             {mean}
# Медиана:             {median}
'''

with open(filename, 'r+', encoding='utf-8') as f:
    numbers = [float(line) for line in f
                if line != '\n' and not line.startswith('#')]
    message = message_fmt.format(date=datetime.datetime.now(),
            count=len(numbers),
            sum=sum(numbers),
            mean=st.mean(numbers),
            median=st.median(numbers))
    print(message, file=f)
