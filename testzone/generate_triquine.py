"""
We have the python source, which checks for the command line argument. If it finds arb then
it prints out the perl source code. The python quine source needs to be converted to a perl
string representation containing hex characters. Thus, we construct the python code to be
a string representation "$p=4372712..." (which is exactly the python list c) followed by "$c=234234..." 
(which is exactly the python list p). Following this, we 
print the perl code which is represented by our list c. This list is exactly the representation
of "perl_src".

When the perl code is run, it in turn prints its own source code, which is its own variable $c. If
the arb keyword is found, it converts the $p and $c strings to an equivalent python list as a string representation,
followed by printing the exact python code in $p after packing
"""
python_src = """import sys
def a(): print "p="+str(p);print "c="+str(c);print "f="+str(f);print ''.join([chr(x) for x in p])
def b(): print "$p=\\\""+''.join(map(lambda x: hex(x)[2:] if x > 15 else hex(x)[2:].zfill(2), p))+"\\\";";print "$c=\\\""+''.join(map(lambda x: hex(x)[2:] if x > 15 else hex(x)[2:].zfill(2), c))+"\\\";";print "$f=\\\""+''.join(map(lambda x: hex(x)[2:] if x > 15 else hex(x)[2:].zfill(2), f))+"\\\";";print ''.join([chr(x) for x in c])
def d(): print "let pl = "+(lambda x: "%s%s%s%s%s" % (x[0], "|", x[1:len(x)-1], "; |", x[-1]))(str(c).replace(',',';'));print "let py = "+(lambda x: "%s%s%s%s%s" % (x[0], "|", x[1:len(x)-1], "; |", x[-1]))(str(p).replace(',',';'));print "let fs = "+(lambda x: "%s%s%s%s%s" % (x[0], "|", x[1:len(x)-1], "; |", x[-1]))(str(f).replace(',',';'));print ''.join([chr(x) for x in f])
q = b if len(sys.argv) > 1 and sys.argv[1] == 'pl' else d if len(sys.argv) > 1 and sys.argv[1] == 'fs' else a
q()"""

perl_src = """sub a{
  @x=unpack("C*",pack("H*",$p));
  print "p=[".join(', ',@x)."]\\n";
  @y=unpack("C*",pack("H*",$c));
  print "c=[".join(', ',@y)."]\\n";
  @z=unpack("C*",pack("H*",$f));
  print "f=[".join(', ',@z)."]\\n";
  print pack('H*',$p)."\\n";
}
sub b{
  print "\$p=\\\"$p\\\";\\n";
  print "\$c=\\\"$c\\\";\\n";
  print "\$f=\\\"$f\\\";\\n";
  print pack('H*',$c)."\\n";
}
sub c{
  @x=unpack("C*",pack("H*",$c));
  print "let pl = [|".join('; ',@x)."; |]\\n";
  @y=unpack("C*",pack("H*",$p));
  print "let py = [|".join('; ',@y)."; |]\\n";
  @z=unpack("C*",pack("H*",$f));
  print "let fs = [|".join('; ',@z)."; |]\\n";
  print pack('H*',$f)."\\n";
}
if (defined($ARGV[0]) && $ARGV[0] eq "py"){
  a;
} elsif (defined($ARGV[0]) && $ARGV[0] eq "fs"){
  c;
} else {
  b;
}"""

fsharp_src = """let z s i (l:array<int>) e = printf s; Array.iter (printf i) l.[0..l.Length-2]; printf "%d" l.[l.Length-1]; printf e
let p s i l e = printf s; [for i in l -> if i < 16 then printf "0%x" i else printf "%x" i] |> ignore; printf e
let s = function
| "py" -> z "p=[" "%d, " py "]\\n"; z "c=[" "%d, " pl "]\\n"; z "f=[" "%d, " fs "]\\n"; printfn "%s" <| new string(Array.map char py)
| "pl" -> p "$p=\\\"" "%x" py "\\\";\\n"; p "$c=\\\"" "%x" pl "\\\";\\n"; p "$f=\\\"" "%x" fs "\\\";\\n"; printfn "%s" <| new string(Array.map char pl)
| _ -> printf "let pl = [|"; Array.iter (printf "%d; ") pl; printf "|]\\n";
        printf "let py = [|"; Array.iter (printf "%d; ") py; printf "|]\\n";
        printf "let fs = [|"; Array.iter (printf "%d; ") fs; printf "|]\\n";
        printfn "%s" <| new string(Array.map char fs);
if fsi.CommandLineArgs.Length > 1 then s fsi.CommandLineArgs.[1] else s "" """


print "p=" + str([ord(x) for x in python_src])
print "c=" + str([ord(x) for x in perl_src])
print "f=" + str([ord(x) for x in fsharp_src])
print python_src
