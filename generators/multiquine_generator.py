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
def a(): print "p="+str(p);print "c="+str(c);print ''.join([chr(x) for x in p])
def b(): print "$p=\\\""+''.join(map(lambda x: hex(x)[2:] if x > 15 else hex(x)[2:].zfill(2), p))+"\\\";";print "$c=\\\""+''.join(map(lambda x: hex(x)[2:] if x > 15 else hex(x)[2:].zfill(2), c))+"\\\";";print ''.join([chr(x) for x in c])
f = b if len(sys.argv) > 1 and sys.argv[1] == 'arb' else a
f()"""
perl_src = """sub a{
\t@x=unpack("C*",pack("H*",$p));
\tprint "p=[".join(', ',@x)."]\\n";
\t@y=unpack("C*",pack("H*",$c));
\tprint "c=[".join(', ',@y)."]\\n";
\tprint pack('H*',$p)."\\n";\n}
sub b{
\tprint "\$p=\\\"$p\\\";\\n";
\t print "\$c=\\\"$c\\\";\\n";
\tprint pack('H*',$c)."\\n";
}
if (defined($ARGV[0]) && $ARGV[0] eq "arb"){
\ta;
} else {
\tb;
}"""
print "p=" + str([ord(x) for x in python_src])
print "c=" + str([ord(x) for x in perl_src])
print python_src
