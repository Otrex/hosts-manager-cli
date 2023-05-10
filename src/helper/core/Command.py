class Command:
  __model = [
    'add-record', 
    { 'help': 'Add a host to the hosts file' }, 
    [
      [ 'ip', { 'help': 'The IP address of the host' } ],
      [ 'hostname', { 'help': 'The hostname to associate with the IP address' } ],
    ],
  ]

  @property
  def model (self):
    self.__model.append(self.handler)
    return self.__model

  def handler(self, **kwargs):
    pass
    
class C1(Command):
  __model = [
    'add-records', 
    { 'help': 'Add a host to the hosts file' }, 
    [
      [ 'ip', { 'help': 'The IP address of the host' } ],
      [ 'hostname', { 'help': 'The hostname to associate with the IP address' } ],
    ],
  ]

  def handler(self, **kwargs):
    print("Hello, world!")

if __name__ == '__main__':
  c1 = C1()
  print(c1.model)