import src.handlers as handlers

Describers = [
  [
    'add-record', 
    { 'help': 'Add a host to the hosts file' }, 
    [
      [ 'ip', { 'help': 'The IP address of the host' } ],
      [ 'hostname', { 'help': 'The hostname to associate with the IP address' } ],
    ],
    handlers.add_host
  ],
  [
    'remove-record', 
    { 'help': 'Remove a host from the hosts file' }, 
    [
      [ 'hostname', { 'help': 'The hostname to remove' } ],
    ],
    handlers.remove_host
  ],
  [
    'get-record',
    { 'help': 'Get a host from the hosts file' },
    [
      [ 'needle', { 'help': 'This is what you are looking for' } ],
      [ 
        '-field', {
          'choices': ['hostname', 'ip'], 
          'default': 'hostname', 
          'help': 'This is the field to search by'
        }
      ]
    ],
    handlers.get_host
  ],
  [
    'add-proxy',
    { 'help': 'Add a Domain-URI map to the proxy list' }, 
    [
      [ 'domain', { 'help': 'The domain you want to map URI to' } ],
      [ 'uri', { 'help': 'The URI you want to map to the domain' } ],
    ],
    handlers.add_proxy
  ],
  [
    'remove-proxy',
    { 'help': 'Remove a Domain-URI map to the proxy list' }, 
    [
      [ 'domain', { 'help': 'The domain address of the host' } ],
      [ '--delete-record', { 'help': 'This would trigger the deletion of the record', 'action': 'store_true' }]
    ],
    handlers.remove_proxy
  ],
  [
    'get-proxy',
    { 'help': 'Get a proxy from the proxies file' },
    [
      [ 'needle', { 'help': 'This is what you are looking for' } ],
      [ 
        '-field', {
          'choices': ['domain', 'uri'], 
          'default': 'domain', 
          'help': 'This is the field to search by'
        }
      ]
    ],
    handlers.get_proxy
  ],
  [
    'start-server',
    { 'help': 'This kickstart the proxy server' }, 
    [],
    handlers.start_proxy_server
  ],
  [
    'stop-server',
    { 'help': 'This stops the proxy server' }, 
    [],
    handlers.stop_proxy_server
  ],
]