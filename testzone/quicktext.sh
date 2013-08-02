python dev.py > oracle.py
python oracle.py cc > a.cc
gcc -o a a.cc
./a > q.cc
diff a.cc q.cc
