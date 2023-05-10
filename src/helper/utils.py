import ipaddress
import os
import subprocess
import psutil
from src.constants import PID_REGISTER, OUTPUT_REGISTER

def is_ip(ip_str):
  try:
    ip_addr = ipaddress.ip_address(ip_str)
    return True
  except ValueError:
    return False

def delete_file(file):
  if os.path.exists(file):
      os.remove(file)

def is_process_running(pid):
    """
    Check if a process with the given PID is still running.
    """
    try:
        process = psutil.Process(pid)
        return process.is_running()
    except psutil.NoSuchProcess:
        return False

def kill_server():
  filename = PID_REGISTER
  if os.path.isfile(filename):
    with open(filename) as f:
      pid = f.read().strip("\n")

    if (is_process_running(int(pid))):
      subprocess.run(['kill', pid], check=True)
    
    delete_file(filename)
    print("\U00002705 Server terminated")

def handle_restart_server():
  kill_server()
  with open(OUTPUT_REGISTER, 'w') as outfile:
    sub = subprocess.Popen(['python', 'src/proxy_server.py'], stdout=outfile, stderr=outfile)
    print("\U00002705 Server has started, running @port 80")
    sub.poll()

def flusher():
  """
    sudo dscacheutil -flushcache
    ipconfig /flushdns
  """