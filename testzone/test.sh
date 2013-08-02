python dev.py > oracle.py
#python quad_quine_generator.py > oracle.py

python oracle.py > a.py
echo "python from triquine against itself:"
diff oracle.py a.py

python oracle.py pl > oracle.pl
perl oracle.pl > a.pl
echo "perl from python against itself:"
diff oracle.pl a.pl

python oracle.py fs > oracle.fsx
fsharpi oracle.fsx > a.fsx
echo "fsharp from python against itself:"
diff oracle.fsx a.fsx

perl oracle.pl py > oracle.py
python oracle.py > a.py
echo "python from perl against itself:"
diff oracle.py a.py

perl oracle.pl fs > oracle.fsx
fsharpi oracle.fsx > a.fsx
echo "fsharp from perl against itself:"
diff oracle.fsx a.fsx

fsharpi oracle.fsx pl > oracle.pl
perl oracle.pl > a.pl
echo "perl from fsharp against itself:"
diff oracle.pl a.pl

fsharpi oracle.fsx py > oracle.py
python oracle.py > a.py
echo "python from fsharp against itself:"
diff oracle.py a.py

python oracle.py ls > oracle.lsp
newlisp oracle.lsp > a.lsp
echo "newlisp from python against itself:"
diff oracle.lsp a.lsp

perl oracle.pl ls > oracle.lsp
newlisp oracle.lsp > a.lsp
echo "newlisp from perl against itself"
diff oracle.lsp a.lsp

fsharpi oracle.fsx ls > oracle.lsp
newlisp oracle.lsp > a.lsp
echo "newlisp from fsharp against itself"
diff oracle.lsp a.lsp

newlisp oracle.lsp py > oracle.py
python oracle.py > a.py
echo "python from newlisp against itself"
diff oracle.py a.py

newlisp oracle.lsp pl > oracle.pl
perl oracle.pl > a.pl
echo "perl from newlisp against itself"
diff oracle.pl a.pl

newlisp oracle.lsp fs > oracle.fsx
fsharpi oracle.fsx > a.fsx
echo "fsharp from newlisp against itself"
diff oracle.fsx a.fsx

python oracle.py cc > oracle.cc
gcc -o oracle oracle.cc
./oracle > a.cc
echo "c from python against itself"
diff a.cc oracle.cc



