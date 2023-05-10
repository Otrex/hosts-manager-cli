import os

def get_file_path(filename):
  return os.path.join(os.getcwd(), "src", "__files__", filename)

PID_REGISTER = get_file_path(".pid")
DOMAIN_MAP_REGISTER = get_file_path("config.json")
ERROR_HTML_PATH = get_file_path("error.html")
OUTPUT_REGISTER = get_file_path(".output")
ADDED_REGISTER = get_file_path(".added")