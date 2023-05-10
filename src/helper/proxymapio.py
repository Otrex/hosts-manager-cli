import json
from os import getcwd, path
from src.constants import DOMAIN_MAP_REGISTER

__MAP_FILE=DOMAIN_MAP_REGISTER

def read_hosts_file():
  with open(__MAP_FILE, 'r') as f:
    hosts = json.load(f)
  return hosts

def write_hosts_file(hosts):
  with open(__MAP_FILE, 'w') as f:
    json.dump(hosts, f, indent=2)

def update_hosts_file(domain, uri):
  hosts = read_hosts_file()
  ip, port = uri.split(":")
  hosts[domain] = [ip, int(port)]
  write_hosts_file(hosts)

def delete_hosts_file(domain):
  hosts = read_hosts_file()
  del hosts[domain]
  write_hosts_file(hosts)

def get_host_entry(key, field = "domain"):
  hosts = read_hosts_file()
  if (field == "domain"):
    p = hosts.get(key, [])
    if len(p):
      return [key, ":".join([str(x) for x in p])]
    else: 
      None

  if (field == "uri"):
    for _key, value in hosts.items():
      separator = ":"
      _value = separator.join([str(x) for x in value])
      if _value == key:
        return [_key, _value]
    return None

