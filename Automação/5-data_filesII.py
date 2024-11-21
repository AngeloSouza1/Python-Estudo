from pathlib import Path
from datetime import datetime

root_dir = Path('files')

for path in root_dir.glob('**/*'):
    if path.is_file():
        stats = path.stat()
        second_created = stats.st_ctime
        date_created = datetime.fromtimestamp(second_created)
        date_created_str = date_created.strftime('%Y-%m-%d_%H:%M:%S')
        new_filename = f'{date_created_str}-{path.name}'
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)
