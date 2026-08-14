import hashlib, re, sys
EXPECTED = {
'ci/text.b64.00': (14000,'8d510a3bb666481d6294e46c0281c619bf398a9ed6336c7a3ed70ff5f18045f6'),
'ci/text.b64.01': (14000,'cce8abee3e25b08ab66d7f67b9b0c89b3e17a21cf7fb78393e9572e8ddfab703'),
'ci/text.b64.02': (14000,'7e362a87f5fa0014f7fb584883fc941c4db1ea77d0b81caace5719283c6d5ecf'),
'ci/text.b64.03': (14000,'0e4059dc57f7edfaa42d47efba18f0835f43f6ea4130ddae3da603e17cdb51df'),
'ci/p04.00': (3500,'4adeb63db947e54243a45c4d61be8983048ea5397ec875ce1b032482f0b9dc0c'),
'ci/p04.01fix.00': (1000,'b03f6531a1976798519364956f380561dbd1b40ce32f821df57db7d6e2facb30'),
'ci/p04.01fix.01': (1000,'7495c6997b832e449e964534fce6c7aa3d5c4596b69804eca848bd6c3a1cc6da'),
'ci/p04.01fix.02': (1000,'bc06b643bddf1e3b81bee7b5518fe9620befaa5b5d739bf04a2eecbd40961a5f'),
'ci/p04.01fix.03': (500,'58bd7307658c3a3d24011cc04d5fdb6f1ebefdf3a7544f7a916556b5581d3325'),
'ci/p04.02': (3500,'e9cb5221b36f34aaaf61f4fff64240c0225e45f0120c2cf8853bbe2ff8cf4a97'),
'ci/p04.03': (3500,'1c9ba4db0a854a8dbeadcdc7881fcca487ad1457a1d2130df151eabaee39433d'),
'ci/p05.00': (3500,'3f33b9c6d3574a58a2145f51044602c2f7811a07e59224458d94154aefd9b13d'),
'ci/p05.01': (3500,'10fbe5ef6c5752ddce8c54fda23b49aa2fb8432eda20d60e885d5396e181975b'),
'ci/p05.02': (3500,'ed6d07131901b7dd259339c7cdfd1940807b7e2b18008e598e9d4e51bb546bbf'),
'ci/p05.03': (964,'99b3a8acdcc5d54a552e0787d8c6310b66278a15d476abab5f7a0cb718320964')}
bad=[]
for f,(n,h) in EXPECTED.items():
    s=re.sub(r'\s+','',open(f,encoding='utf-8').read())
    a=hashlib.sha256(s.encode()).hexdigest()
    print('%s len=%d sha=%s' % (f,len(s),a))
    if len(s)!=n or a!=h: bad.append(f)
if bad:
    print('MISMATCH: '+', '.join(bad), file=sys.stderr); sys.exit(1)
print('ALL FRAGMENTS MATCH')
