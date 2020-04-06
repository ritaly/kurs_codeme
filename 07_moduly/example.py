import sys

if sys.platform == 'darwin':
    print('Mac')
elif sys.platform == 'win32':
    print('Windows')
elif 'linux' in sys.platform: # linux , linux2
    print('Linux')
else:
    print('Inny system')