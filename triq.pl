$p="696d706f7274207379730a646566206128293a207072696e742022703d222b7374722870293b7072696e742022633d222b7374722863293b7072696e742027272e6a6f696e285b63687228782920666f72207820696e20705d290a646566206228293a207072696e742027272e6a6f696e285b63687228782920666f72207820696e20635d290a66203d2062206966206c656e287379732e6172677629203e203120616e64207379732e617267765b315d203d3d20276172622720656c736520610a662829";
$c="73756220617b0a0940783d756e7061636b2822432a222c7061636b2822482a222c247029293b0a097072696e742022703d5b222e6a6f696e28272c20272c4078292e225d5c6e223b0a0940793d756e7061636b2822432a222c7061636b2822482a222c246329293b0a097072696e742022633d5b222e6a6f696e28272c20272c4079292e225d5c6e223b0a097072696e74207061636b2827482a272c2470292e225c6e223b0a7d0a73756220627b0a097072696e7420225c24703d5c2224705c223b5c6e223b0a097072696e7420225c24633d5c2224635c223b5c6e223b0a097072696e74207061636b2827482a272c2463292e225c6e223b0a7d0a69662028646566696e65642824415247565b305d292026262024415247565b305d206571202261726222297b0a09613b0a7d20656c7365207b0a09623b0a7d";
$f="6c6574207a2073206920286c3a61727261793c696e743e292065203d207072696e746620733b2041727261792e6974657220287072696e7466206929206c2e5b302e2e6c2e4c656e6774682d325d3b207072696e74662022256422206c2e5b6c2e4c656e6774682d315d3b207072696e746620650a6c6574207020732069206c2065203d207072696e746620733b2041727261792e6974657220287072696e7466206929206c3b207072696e746620650a6c65742073203d2066756e6374696f6e0a7c2022707922202d3e207a2022703d5b22202225642c202220707920225d5c6e223b207a2022633d5b22202225642c202220706c20225d5c6e223b207072696e74662022257322203c7c206e657720737472696e672841727261792e6d61702063686172207079290a7c2022706c22202d3e20702022696d706f7274207379730a646566206128293a207072696e742022703d222b7374722870293b7072696e742022633d222b7374722863293b7072696e742027272e6a6f696e285b63687228782920666f72207820696e20705d290a646566206228293a207072696e742027272e6a6f696e285b63687228782920666f72207820696e20635d290a66203d2062206966206c656e287379732e6172677629203e203120616e64207379732e617267765b315d203d3d20276172622720656c736520610a6628293d5c2222202225782220707920225c223b5c6e223b207020223d5c2222202225782220706c20225c223b5c6e223b207072696e74666e2022257322203c7c206e657720737472696e672841727261792e6d6170206368617220706c290a7c205f202d3e207072696e746620226c657420706c203d205b7c223b2041727261792e6974657220287072696e7466202225643b202229202841727261792e6d617020696e7420706c293b207072696e746620227c5d5c6e223b0a20202020202020207072696e746620226c6574207079203d205b7c223b2041727261792e6974657220287072696e7466202225643b2022292070793b207072696e746620227c5d5c6e223b0a20202020202020207072696e746620226c6574206673203d205b7c223b2041727261792e6974657220287072696e7466202225643b2022292066733b207072696e746620227c5d5c6e223b0a20202020202020207072696e74662022257322203c7c206e657720737472696e672841727261792e6d61702063686172206673293b0a73206673692e436f6d6d616e644c696e65417267732e5b315d";
sub a{
	@x=unpack("C*",pack("H*",$p));
	print "p=[".join(', ',@x)."]\n";
	@y=unpack("C*",pack("H*",$c));
	print "c=[".join(', ',@y)."]\n";
  @z=unpack("C*",pack("H*",$f));
  print "f=[".join(', ',@z)."]\n";
	print pack('H*',$p)."\n";
}
sub b{
	print "\$p=\"$p\";\n";
	print "\$c=\"$c\";\n";
  print "\$f=\"$f\";\n";
	print pack('H*',$c)."\n";
}
sub c{
  @x=unpack("C*",pack("H*",$c));
	print "let pl = [|".join('; ',@x)."|]\n";
	@y=unpack("C*",pack("H*",$p));
	print "let py = [|".join('; ',@y)."|]\n";
  @z=unpack("C*",pack("H*",$f));
  print "let fs = [|".join('; ',@z)."|]\n";
  print pack('H*',$f)."\n";
}
if (defined($ARGV[0]) && $ARGV[0] eq "py"){
	a;
} elsif (defined($ARGV[0]) && $ARGV[0] eq "fs"){
  c;
} else {
	b;
}
