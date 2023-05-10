from src.constants import ADDED_REGISTER

__HOSTS_FILE = '/etc/hosts'

def read_hosts_file():
    with open(__HOSTS_FILE, 'r') as f:
        return f.read()

def write_hosts_file(content):
    with open(__HOSTS_FILE, 'w') as f:
        f.write(content)

def append_added(content):
  with open(ADDED_REGISTER, 'a') as f:
        return f.write(content)

def delete_added(content):
  content = ''
  with open(ADDED_REGISTER, 'r') as f:
      content = f.read()

  content.replace(content, '')
  with open(ADDED_REGISTER, 'w') as f:
        f.write(content)

def fetch_host_by(key, by='hostname'):
    results = []
    with open(__HOSTS_FILE, 'r') as f:
      line = f.readline()
      while line:
        line = f.readline()
        content = line.strip('\n').split(' ')
        if len(content) == 2 and ("docker" not in content[1] or "kubernetes" not in content[1]):
          keymap = dict(zip(['ip', 'hostname'], content))
          if (keymap[by] == key):
            results.append(keymap)
    return results


if __name__ == '__main__':
  print(fetch_host_by('192.168.1.100', 'ip'))
    

