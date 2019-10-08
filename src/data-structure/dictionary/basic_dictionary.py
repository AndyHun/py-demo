# 1 how to init a dict
mailAddress = {
    'T1': 'T1@g.com',
    'T2': 'T2@g.com',
    'T3': 'T3@g.com'
}

print('Now, i have mail address:', mailAddress)

# 2 how to delete
del mailAddress['T1']
print('\nThere are {} contacts in the mail address\n'.format(len(mailAddress)))

# 3. how to travers dict
for name, mail in mailAddress.items():
    print('Name: {}, Mail: {}'.format(name, mail))

# 4 how to add item into dict
mailAddress['TT'] = 'TT@g.com'

if 'TT' in mailAddress:
    print('TT mail address is', mailAddress['TT'])
