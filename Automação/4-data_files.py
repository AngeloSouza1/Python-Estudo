from pathlib import Path
from datetime import datetime

path = Path('files/dados/a.txt')
stats = path.stat()
second_created = stats.st_ctime
date_created = datetime.fromtimestamp(second_created)
date_created_str = date_created.strftime('%Y-%m-%d_%H:%M:%S')
print(stats)
print(second_created)
print(date_created)
print(date_created_str)
