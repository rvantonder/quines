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
def t1(i): return ''.join(map(lambda x: hex(x)[2:] if x > 15 else hex(x)[2:].zfill(2), i))+"\\\";"
def t2(i): return (lambda x: "%s%s%s%s%s" % (x[0], "|", x[1:len(x)-1], "; |", x[-1]))(str(i).replace(',',';'))
def py(): print "p="+str(p);print "c="+str(c);print "f="+str(f);print ''.join([chr(x) for x in p])
def pl(): print "$p=\\\""+t1(p);print "$c=\\\""+t1(c);print "$f=\\\""+t1(f);print ''.join([chr(x) for x in c])
def fs(): print "let pl = "+t2(c);print "let py = "+t2(p);print "let fs = "+t2(f);print ''.join([chr(x) for x in f])
q = pl if len(sys.argv) > 1 and sys.argv[1] == 'pl' else fs if len(sys.argv) > 1 and sys.argv[1] == 'fs' else py
q()"""

perl_src = """sub py{
  @x=unpack("C*",pack("H*",$p));
  print "p=[".join(', ',@x)."]\\n";
  @y=unpack("C*",pack("H*",$c));
  print "c=[".join(', ',@y)."]\\n";
  @z=unpack("C*",pack("H*",$f));
  print "f=[".join(', ',@z)."]\\n";
  print pack('H*',$p)."\\n";
}
sub pl{
  print "\$p=\\\"$p\\\";\\n";
  print "\$c=\\\"$c\\\";\\n";
  print "\$f=\\\"$f\\\";\\n";
  print pack('H*',$c)."\\n";
}
sub fs{
  @x=unpack("C*",pack("H*",$c));
  print "let pl = [|".join('; ',@x)."; |]\\n";
  @y=unpack("C*",pack("H*",$p));
  print "let py = [|".join('; ',@y)."; |]\\n";
  @z=unpack("C*",pack("H*",$f));
  print "let fs = [|".join('; ',@z)."; |]\\n";
  print pack('H*',$f)."\\n";
}
if (defined($ARGV[0]) && $ARGV[0] eq "py"){py;} elsif (defined($ARGV[0]) && $ARGV[0] eq "fs"){fs;} else {pl;}"""

perl_src = """sub t1{unpack("C*",pack("H*",$_[0]));}
sub t2{;join(', ',@{$_[0]})."]\\n";}
sub t3{join('; ',@{$_[0]})."; |]\\n";}
sub py{
  @x=t1($p);print "p=[".t2(\@x);
  @x=t1($c);print "c=[".t2(\@x);
  @x=t1($f);print "f=[".t2(\@x);
  print pack('H*',$p)."\\n";
}
sub pl{
  print "\$p=\\\"$p\\\";\\n";
  print "\$c=\\\"$c\\\";\\n";
  print "\$f=\\\"$f\\\";\\n";
  print pack('H*',$c)."\\n";
}
sub fs{
  @x=t1($c);print "let pl = [|".t3(\@x);
  @x=t1($p);print "let py = [|".t3(\@x);
  @x=t1($f);print "let fs = [|".t3(\@x);
  print pack('H*',$f)."\n";
}
if (defined($ARGV[0]) && $ARGV[0] eq "py"){py;} elsif (defined($ARGV[0]) && $ARGV[0] eq "fs"){fs;} else {pl;}"""

fsharp_src = """let t1 s i (l:array<int>) e = printf s; Array.iter (printf i) l.[0..l.Length-2]; printf "%d" l.[l.Length-1]; printf e
let t2 s i l e = printf s; [for i in l -> if i < 16 then printf "0%x" i else printf "%x" i] |> ignore; printf e
let t3 s l = printf s; Array.iter (printf "%d; ") l; printf "|]\\n"
let t4 l = new string(Array.map char l)
let s = function
| "py" -> t1 "p=[" "%d, " py "]\\n"; t1 "c=[" "%d, " pl "]\\n"; t1 "f=[" "%d, " fs "]\\n"; printfn "%s" <| t4 py
| "pl" -> t2 "$p=\\\"" "%x" py "\\\";\\n"; t2 "$c=\\\"" "%x" pl "\\\";\\n"; t2 "$f=\\\"" "%x" fs "\\\";\\n"; printfn "%s" <| t4 pl
| _ -> t3 "let pl = [|" pl; t3 "let py = [|" py; t3 "let fs = [|" fs; printfn "%s" <| t4 fs
if fsi.CommandLineArgs.Length > 1 then s fsi.CommandLineArgs.[1] else s "" """


print "p=" + str([ord(x) for x in python_src])
print "c=" + str([ord(x) for x in perl_src])
print "f=" + str([ord(x) for x in fsharp_src])
print python_src
