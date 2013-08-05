python dev.py > oracle.py #bootstrap
#python quad_quine_generator.py > oracle.py

python oracle.py pl > oracle.pl
python oracle.py fs > oracle.fsx
python oracle.py ls > oracle.lsp
python oracle.py cc > oracle.cc
python oracle.py > a.py
diff oracle.py a.py

# for each one, test
perl oracle.pl > a.pl
diff oracle.pl a.pl
perl oracle.pl py > a.py
diff oracle.py a.py
perl oracle.pl fs > a.fsx
diff oracle.fsx a.fsx
perl oracle.pl ls > a.lsp
diff oracle.lsp a.lsp
perl oracle.pl cc > a.cc
diff oracle.cc a.cc

fsharpi oracle.fsx > a.fsx
diff oracle.fsx a.fsx
fsharpi oracle.fsx py > a.py
diff oracle.py a.py
fsharpi oracle.fsx pl > a.pl
diff oracle.pl a.pl
fsharpi oracle.fsx ls > a.lsp
diff oracle.lsp a.lsp
fsharpi oracle.fsx cc > a.cc
diff oracle.cc a.cc

newlisp oracle.lsp > a.lsp
diff oracle.lsp a.lsp
newlisp oracle.lsp py > a.py
diff oracle.py a.py
newlisp oracle.lsp pl > a.pl
diff oracle.pl a.pl
newlisp oracle.lsp fs > a.fsx
diff oracle.fsx a.fsx
newlisp oracle.lsp cc > a.cc
diff oracle.cc a.cc

gcc -o oracle oracle.cc
./oracle > a.cc
diff oracle.cc a.cc
./oracle py > a.py
diff oracle.py a.py
./oracle pl > a.pl
diff oracle.pl a.pl
./oracle fs > a.fsx
diff oracle.fsx a.fsx
./oracle ls > a.lsp
diff oracle.lsp a.lsp
