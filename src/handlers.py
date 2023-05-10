from src.helper import hostio, decorators, proxymapio, utils

import ipaddress

@decorators.output
def add_host(**kwargs):
  ip = kwargs["ip"]
  hostname = kwargs["hostname"]
  new_content = f'{ip} {hostname}\n'

  content = hostio.read_hosts_file()
  content += new_content
  hostio.write_hosts_file(content)
  hostio.append_added(new_content)

  return 'add_host', [hostname, ip]


@decorators.output
def remove_host(**kwargs):
  hostname = kwargs["hostname"]

  content = hostio.read_hosts_file()
  lines = content.split('\n')

  new_lines = []
  for line in lines:
      if not line.startswith('#') and hostname in line:
        hostio.delete_added(line)
      
      if not line.startswith('#') and hostname not in line:
          new_lines.append(line)
  new_content = '\n'.join(new_lines)
  hostio.write_hosts_file(new_content)

  return 'remove_host', hostname


@decorators.output
def get_host(**kwargs):
  try:
    field = kwargs['field']
    key = kwargs['needle']
    return 'get_host', hostio.fetch_host_by(key, field)
  except KeyError:
    return 'get_host', hostio.fetch_host_by(kwargs['needle'])

@decorators.output
def add_proxy(**kwargs):
  domain = kwargs['domain']
  uri = kwargs['uri']

  domain_exists = bool(len(hostio.fetch_host_by(domain)))
  if (not domain_exists):
    should_create = input("\U00002754 Should the domain be added to the host file? (y/n): ")
    if should_create == "y" or should_create == "Y" or should_create == "Yes" or should_create == "yes":
      ip_str, port = uri.split(":")
      if (ip_str == "localhost"):
        ip_str = "127.0.0.1"
      if (not utils.is_ip(ip_str)):
        print("\U0000274C Invalid IP: %s" % ip_str)
        return 'error',

      new_content = f'{ip_str} {domain}\n'
      content = hostio.read_hosts_file()
      content += new_content
      hostio.write_hosts_file(content)
      hostio.append_added(new_content)
    else:
      print("\U0000274C We can not proceed further")
      return 'error',

  proxymapio.update_hosts_file(domain, uri)

  utils.handle_restart_server()

  return 'add_proxy', [domain, uri]

@decorators.output
def remove_proxy(**kwargs):
  domain = kwargs['domain']
  delete_record = kwargs['delete_record']

  try:
    proxymapio.delete_hosts_file(domain)
    if (delete_record):
      remove_host(**{ 'hostname' : domain })
  except Exception as e:
    return 'error'

  return 'remove_proxy', domain

@decorators.output
def get_proxy(**kwargs):
  field = kwargs['field']
  key = kwargs['needle']

  result = proxymapio.get_host_entry(key, field)
  return 'get_proxy', result

@decorators.output
def start_proxy_server(**kwargs):
  utils.handle_restart_server()
  return 'server'

@decorators.output
def stop_proxy_server(**kwargs):
  utils.kill_server()
  return 'server'

  
if __name__ == '__main__':
  get_host(**{ 'key': 'myhost.local' })
