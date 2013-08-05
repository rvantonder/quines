files = ['.py', '.pl', '.fsx', '.lsp', '.cc']
oracles = ["oracle%s" % i for i in files]
bins = ['python', 'perl', 'fsharpi', 'newlisp', './oracle']
flags = ['py', 'pl', 'fs', 'ls', 'cc']

print "python pentaquine.py > oracle.py"

for b in zip(bins, oracles, files):
  for f in zip(flags, oracles, files):
    if not b[2] == f[2]:
      print "%s %s %s > %s" % (b[0], b[1], f[0], f[1])

  print "%s %s > %s" % (b[0], b[1], "a%s" % b[2])
  print "diff %s %s" % (b[1], "a%s" % b[2])
  
  for ob in zip(bins, oracles, files): # for each other language
    for of in zip(flags, oracles, files): # for each flag/conversion
      if not b[0] == ob[0]: # we already checked this above
        if not of[2] == ob[2]:
          #if ob[0] == './oracle':
          #  print "gcc -o oracle oracle.cc" 
          print "%s %s %s > %s" % (ob[0], ob[1], of[0], "a%s" % of[2]) # iterate over flags
          print "diff %s %s" % ("oracle%s" % of[2], "a%s" % of[2])
        else:
          #if ob[0] == './oracle':
          #  print "gcc -o oracle oracle.cc"
          print "%s %s > %s" % (ob[0], ob[1], "a%s" % of[2]) # don't need a flag if same
          print "diff %s %s" % ("oracle%s" % of[2], "a%s" % of[2])
    print ""
        
  print ""
  
  

