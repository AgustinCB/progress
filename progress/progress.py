# Progress
# Christopher Su

from datetime import datetime
import os

# TODO: make filename format customizable
def get_week_string(date_=None, start_on_sunday=False):
  week_start = get_start_of_week(date_=date_,
      start_on_sunday=start_on_sunday)

  if start_on_sunday:
    return week_start.strftime("wk%U_%Y-%m-%d")
  return week_start.strftime("wk%W_%Y-%m-%d")

def get_start_of_week(date_=None, start_on_sunday=False):
  if not date_:
    date_ = datetime.now()

  if start_on_sunday:
    date_string = date_.strftime("%Y %U 0")
    return datetime.strptime(date_string, "%Y %U %w")

  # convert into week num and year
  date_string = date_.strftime("%Y %W 1")

  # convert back into a date and return
  return datetime.strptime(date_string, "%Y %W %w")

class Progress:
  # data_store_path should be either a file system path
  # or a SQLAlchemy compatible path (if use_db is enabled)
  # use_db functionality to be implemented
  def __init__(self, data_store_path, file_ext=None, use_db=False):
    self.data_store_path = data_store_path
    self.file_ext = file_ext

  def fpath(self, filename):
    return os.path.join(self.data_store_path, filename)

  def week_file_path(self, date_=None):
    filename = get_week_string(date_=date_)

    if self.file_ext:
      filename += "." + self.file_ext

    return self.fpath(filename)

  # week defaults to current week if not specified
  def get_week(self, date_=None):
    filepath = self.week_file_path(date_=date_)

    if os.path.isfile(filepath):
      with open(filepath, 'r') as f:
        data = f.read()
      return data

    return None

  def set_week(self, content, date_=None):
    filepath = self.week_file_path(date_=date_)
    with open(filepath, 'w') as f:
      f.write(content)