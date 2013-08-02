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
def t3(i): return ' '.join(map(str, i))
def t4(i,j): print "char %s[]={%s,};" % (i,','.join(map(lambda x: "0x%0.2x" % x, j)))
def py(): print "p="+str(p);print "c="+str(c);print "f="+str(f);print "l="+str(l);print ''.join([chr(x) for x in p])
def pl(): print "$p=\\\""+t1(p);print "$c=\\\""+t1(c);print "$f=\\\""+t1(f);print "$l=\\\""+t1(l);print ''.join([chr(x) for x in c])
def fs(): print "let pl = "+t2(c);print "let py = "+t2(p);print "let fs = "+t2(f); print "let ls = "+t2(l);print ''.join([chr(x) for x in f])
def ls(): print "(set 'p '(%s))" % t3(p);print "(set 'c '(%s))" % t3(c);print "(set 'f '(%s))" % t3(f);print "(set 'l '(%s))" % t3(l);print ''.join([chr(x) for x in l])
def cc(): t4("p", p); t4("c", c); t4("f", f); t4("l", l); t4("s", s);print ''.join([chr(x) for x in s])
q = pl if len(sys.argv) > 1 and sys.argv[1] == 'pl' else fs if len(sys.argv) > 1 and sys.argv[1] == 'fs' else ls if len(sys.argv) > 1 and sys.argv[1] == 'ls' else cc if len(sys.argv) > 1 and sys.argv[1] == 'cc' else py
q()"""

perl_src = """sub t1{unpack("C*",pack("H*",$_[0]));}
sub t2{;join(', ',@{$_[0]})."]\\n";}
sub t3{join('; ',@{$_[0]})."; |]\\n";}
sub t4{join(' ',@{$_[0]})."))\\n";}
sub py{
  @x=t1($p);print "p=[".t2(\@x);
  @x=t1($c);print "c=[".t2(\@x);
  @x=t1($f);print "f=[".t2(\@x);
  @x=t1($l);print "l=[".t2(\@x);
  print pack('H*',$p)."\\n";
}
sub pl{
  print "\$p=\\\"$p\\\";\\n";
  print "\$c=\\\"$c\\\";\\n";
  print "\$f=\\\"$f\\\";\\n";
  print "\$l=\\\"$l\\\";\\n";
  print pack('H*',$c)."\\n";
}
sub fs{
  @x=t1($c);print "let pl = [|".t3(\@x);
  @x=t1($p);print "let py = [|".t3(\@x);
  @x=t1($f);print "let fs = [|".t3(\@x);
  @x=t1($l);print "let ls = [|".t3(\@x);
  print pack('H*',$f)."\\n";
}
sub ls{
  @x=t1($p);print "(set 'p '(".t4(\@x);
  @x=t1($c);print "(set 'c '(".t4(\@x);
  @x=t1($f);print "(set 'f '(".t4(\@x);
  @x=t1($l);print "(set 'l '(".t4(\@x);
  print pack('H*',$l)."\\n";
}
if (defined($ARGV[0]) && $ARGV[0] eq "py"){py;} elsif (defined($ARGV[0]) && $ARGV[0] eq "fs"){fs;} elsif (defined($ARGV[0]) && $ARGV[0] eq "ls"){ls;} else {pl;}"""

fsharp_src = """let t1 s i (l:array<int>) e = printf s; Array.iter (printf i) l.[0..l.Length-2]; printf "%d" l.[l.Length-1]; printf e
let t2 s i l e = printf s; [for i in l -> if i < 16 then printf "0%x" i else printf "%x" i] |> ignore; printf e
let t3 s l = printf s; Array.iter (printf "%d; ") l; printf "|]\\n"
let t4 l = new string(Array.map char l)
let s = function
| "py" -> t1 "p=[" "%d, " py "]\\n"; t1 "c=[" "%d, " pl "]\\n"; t1 "f=[" "%d, " fs "]\\n"; t1 "l=[" "%d, " ls "]\\n"; printfn "%s" <| t4 py
| "pl" -> t2 "$p=\\\"" "%x" py "\\\";\\n"; t2 "$c=\\\"" "%x" pl "\\\";\\n"; t2 "$f=\\\"" "%x" fs "\\\";\\n"; t2 "$l=\\\"" "%x" ls "\\\";\\n"; printfn "%s" <| t4 pl
| "ls" -> t1 "(set 'p '(" "%d " py "))\\n"; t1 "(set 'c '(" "%d " pl "))\\n"; t1 "(set 'f '(" "%d " fs "))\\n";  t1 "(set 'l '(" "%d " ls "))\\n"; printfn "%s" <| t4 ls
| _ -> t3 "let pl = [|" pl; t3 "let py = [|" py; t3 "let fs = [|" fs; t3 "let ls = [|" ls; printfn "%s" <| t4 fs
if fsi.CommandLineArgs.Length > 1 then s fsi.CommandLineArgs.[1] else s "" """

newlisp_src = """(set 'x (main-args 2))
(define (t1 i j) (println (string i (join (map string j) ", ") "]")))
(define (t2 i j) (println (string i (join (map (lambda (x) (format "%02x" x)) j) "") "\\\";")))
(define (t3 i j) (println (string i (join (map string j) "; ") "; |]")))
(cond
  ((= x nil)  (println (string "(set 'p '" p ")"))
              (println (string "(set 'c '" c ")"))
              (println (string "(set 'f '" f ")"))
              (println (string "(set 'l '" l ")"))
              (println (join (map char l) "")))
  ((= x "py") (t1 "p=[" p)
              (t1 "c=[" c)
              (t1 "f=[" f)
              (t1 "l=[" l)
              (println (join (map char p) "")))
  ((= x "pl") (t2 "$p=\\\"" p)
              (t2 "$c=\\\"" c)
              (t2 "$f=\\\"" f)
              (t2 "$l=\\\"" l)
              (println (join (map char c) "")))
  ((= x "fs") (t3 "let pl = [|" c)
              (t3 "let py = [|" p)
              (t3 "let fs = [|" f)
              (t3 "let ls = [|" l)
              (println (join (map char f) ""))))
(exit)"""

#braces needed? spacing? macro for loop?
# change variable names of fsharp?
c_src = """#include <stdio.h>
#include <string.h>
#define M(z) printf("char " #z "[]={");for(i=0;i<sizeof(z);i++) {printf("%0#4x,", z[i]);}; printf("};\\n")
#define N(z) for(i=0;i<sizeof(z);i++) {putchar(z[i]);}; printf("\\n")
#define O(z) printf(#z "=[");for(i=0;i<sizeof(z)-1;i++) {printf("%d, ", z[i]);}; printf("%d]\\n", z[i])
#define P(z) printf("$" #z "=\\\"");for(i=0;i<sizeof(z);i++) {printf("%02x",z[i]);}; printf("\\\";\\n") 
#define Q(y, z) printf("let " y " = [|");for(i=0;i<sizeof(z);i++) {printf("%d; ", z[i]);}; printf("|]\\n")
#define R(z) printf("(set '" #z " '(");for(i=0;i<sizeof(z)-1;i++) {printf("%d ", z[i]);}; printf("%d))\\n", z[i])
void cc() {
  int i;
  M(p); M(c); M(f); M(l); M(s); N(s);
}
void py() {
  int i;
  O(p); O(c); O(f); O(l); O(s); N(p);
}
void pl() {
  int i;
  P(p); P(c); P(f); P(l); P(s); N(c);
}
void fs() {
  int i;
  Q("py",p); Q("pl",c); Q("fs",f); Q("ls",l); Q("cc",s); N(f);
}
void ls(){
 int i;
 R(p); R(c); R(f); R(l); R(s); N(l); 
}
int main (int argc, char *argv[]) {
if (argc >= 2 && strcmp(argv[1],"py") == 0) {
  py();
} else if (argc >= 2 && strcmp(argv[1],"pl") == 0) {
  pl();
} else if (argc >= 2 && strcmp(argv[1],"fs")==0) {
  fs();
} else if (argc >= 2 && strcmp(argv[1],"ls") == 0) {
  ls();
} else {
  cc();
}}"""


print "p=" + str([ord(x) for x in python_src])
print "c=" + str([ord(x) for x in perl_src])
print "f=" + str([ord(x) for x in fsharp_src])
print "l=" + str([ord(x) for x in newlisp_src])
print "s=" + str([ord(x) for x in c_src])
print python_src
