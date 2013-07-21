$p = "import sys\ndef a(): print \"p=\"+str(p);print \"c=\"+str(c);print ''.join([chr(x) for x in p])\ndef b(): print ''.join([chr(x) for x in c])\nf = b if len(sys.argv) > 1 and sys.argv[1] == 'arb' else a\nf()";
$s = "sub a{\n\t\@x=unpack(\"C*\",pack(\"H*\",\$p));\n\tprint \"p=[\".join(', ',\@x).\"]\\n\";\n\t\@y=unpack(\"C*\",pack(\"H*\",\$c));\n\tprint \"c=[\".join(', ',\@y).\"]\\n\";\n\tprint pack('H*',\$p).\"\\n\";\n}\nsub b{\n\tprint \"\\\$p=\\\"\$p\\\";\\n\";\n\tprint \"\\\$c=\\\"\$c\\\";\\n\";\n\tprint pack('H*',\$c).\"\\n\";\n}\nif (defined(\$ARGV[0]) && \$ARGV[0] eq \"arb\"){\n\ta;\n} else {\n\tb;\n}";
print "\$p=\"".join('', unpack('H*', $p))."\";\n";
print "\$c=\"".join('', unpack('H*', $s))."\";\n";
print $s."\n";

