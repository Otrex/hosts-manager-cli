from tabulate import tabulate

def get_printer(_data):
  data = [[i['ip'], i['hostname']] for i in _data]
  headers = ["IP", "Host Name"]

  if (len(data) == 0):
    print("\U00002705 No Hosts Found!")
  else:
    print("\U00002705 Saved Hosts Includes:")
    print(tabulate(data, headers=headers))

def add_printer(data):
  hostname, ip = data
  print(f'\U00002705 Added {hostname} with IP address {ip} to the hosts file.')
  print("""

  If it doesn't work immediately, run the following command:
    MAC OS: sudo dscacheutil -flushcache
    WINDOWS: ipconfig /flushdns

  Note: This command may restart your internet connection
  
  """)

def remove_printer(data):
  hostname = data
  print(f"\U00002705 Removed {hostname} from the hosts")

def add_proxy_printer(data):
  domain, uri = data
  print(f'\U00002705 Added "{domain}" with URI "{uri}" to map.')

def remove_proxy_printer(data):
  pass

def get_proxy_printer(data):
  if (data == None):
    print("\U00002705 No Proxy Found!")
  else:
    new_data = [data]
    headers = ["Domain", "URI"]
    print("\U00002705 Saved Proxies Includes:")
    print(tabulate(new_data, headers=headers))

def output(func):
  def wrapper(**kwargs):
    print("")
    print("\U0001F3C3 Executing...")
    data = func(**kwargs)

    if data[0] == 'get_host':
      get_printer(data[1])
    elif data[0] == 'add_host':
      add_printer(data[1])
    elif data[0] == 'remove_host':
      remove_printer(data[1])
    elif data[0] == 'add_proxy':
      add_proxy_printer(data[1])
    elif data[0] == 'remove_proxy':
      remove_proxy_printer(data[1])
    elif data[0] == 'get_proxy':
      get_proxy_printer(data[1])
    else:
      pass

    print("\U0001F91D Completed!")
    print("")

  return wrapper