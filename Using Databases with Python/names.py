fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
names = dict()
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    org_pieces = email.split('@')
    org = org_pieces[1]
    names[org] = names.get(org,0) + 1
	
print(names)