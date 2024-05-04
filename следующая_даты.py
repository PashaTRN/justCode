from datetime import datetime, timedelta
DatA = datetime.strptime(input(), '%d.%m.%Y')
print((DatA - timedelta(days=1)).strftime('%d.%m.%Y'),
      (DatA + timedelta(days=1)).strftime('%d.%m.%Y'), sep="\n")

## ВЫВОДИТ ДАТУ НА ДЕНЬ НАЗАД И ВПЕРЕД
