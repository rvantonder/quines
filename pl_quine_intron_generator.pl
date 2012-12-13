$s = "print \"\\\$src=\\\"\$src\\\";\\n\";\n\$intron;\nprint pack('H*',\$src).\"\\n\";";
print "\$src=\"".join('', unpack('H*', $s))."\";\n";
print $s."\n";
