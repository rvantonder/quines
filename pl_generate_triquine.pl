$p = "import sys\ndef a(): print \"p=\"+str(p);print \"c=\"+str(c);print ''.join([chr(x) for x in p])\ndef b(): print ''.join([chr(x) for x in c])\nf = b if len(sys.argv) > 1 and sys.argv[1] == 'arb' else a\nf()";
$s = "sub a{\n\t\@x=unpack(\"C*\",pack(\"H*\",\$p));\n\tprint \"p=[\".join(', ',\@x).\"]\\n\";\n\t\@y=unpack(\"C*\",pack(\"H*\",\$c));\n\tprint \"c=[\".join(', ',\@y).\"]\\n\";\n\tprint pack('H*',\$p).\"\\n\";\n}\nsub b{\n\tprint \"\\\$p=\\\"\$p\\\";\\n\";\n\tprint \"\\\$c=\\\"\$c\\\";\\n\";\n\tprint pack('H*',\$c).\"\\n\";\n}\nif (defined(\$ARGV[0]) && \$ARGV[0] eq \"arb\"){\n\ta;\n} else {\n\tb;\n}";
$f = "let z s i (l:array<int>) e = printf s; Array.iter (printf i) l.[0..l.Length-2]; printf \"%d\" l.[l.Length-1]; printf e\nlet p s i l e = printf s; Array.iter (printf i) l; printf e\nlet s = function\n| \"py\" -> z \"p=[\" \"%d, \" py \"]\\n\"; z \"c=[\" \"%d, \" pl \"]\\n\"; printf \"%s\" <| new string(Array.map char py)\n| \"pl\" -> p \"$p=\\\"\" \"%x\" py \"\\\";\\n\"; p \"$c=\\\"\" \"%x\" pl \"\\\";\\n\"; printfn \"%s\" <| new string(Array.map char pl)\n| _ -> printf \"let pl = [|\"; Array.iter (printf \"%d; \") (Array.map int pl); printf \"|]\\n\";\n        printf \"let py = [|\"; Array.iter (printf \"%d; \") py; printf \"|]\\n\";\n        printf \"let fs = [|\"; Array.iter (printf \"%d; \") fs; printf \"|]\\n\";\n        printf \"%s\" <| new string(Array.map char fs);\ns fsi.CommandLineArgs.[1]";
print "\$p=\"".join('', unpack('H*', $p))."\";\n";
print "\$c=\"".join('', unpack('H*', $s))."\";\n";
print "\$f=\"".join('', unpack('H*', $f))."\";\n";
print $s."\n";

