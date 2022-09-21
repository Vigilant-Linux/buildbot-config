machines = [
	      {
		              'name': 'user1',
		              'mach': 'i686',
		              'workdir': 'i686-workdir',  # created on the master
		              'hostdir': '/hostdir',      # must exist on the slave
		              'crosstarget': 'native',    # native or 'vpkg-src cross profile'
                  'subarch': '',              # subarch can be used for fake archs (i686-musl, x86_64-musl)
		              'slave_name': 'i686_vigilant',
		              'slave_pass': 'SLAVE_PASSWORD',
		              'admin': 'user1'
	      },
        {
                  'name': 'user2',
                  'mach': 'x86_64',
                  'workdir': 'x86_64-workdir',     # created on the master
                  'hostdir': '/hostdir',           # must exist on slave
                  'crosstarget': 'native',
                  'subarch': '',
                  'slave_name': 'x86_64_vigilant',
                  'slave_pass': 'SLAVE_PASSWORD',
                  'admin': 'user2'
        },
        {
                  'name': 'user3',
                  'mach': 'armv61',
                  'workdir': 'cross-rpi-workdir', # created on the master
                  'hostdir': '/hostdir',          # must exist on slave
                  'crosstarget': 'armv6hf',
                  'subarch': '',
                  'slave_name': 'crossrpi_vigilant',
                  'slave_pass': 'SLAVE_PASSWORD',
                  'admin': 'user3'
        }
]

web_users = [('user1', 'USER_PASSWORD'), ('user2', 'USER_PASSWORD')]
