python dev.py > oracle.py

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
