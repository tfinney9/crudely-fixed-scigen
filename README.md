This is the source code for
[SCIgen](http://pdos.csail.mit.edu/scigen).  Detailed instructions on
dependencies and running the code still need to be written.

# 2020-02-04 -- My bad attempt at getting scigen to kinda work, notes for future self

0. Install perl 
1. export PERL5LIB=/home/$USERNAME/src/scigen to include it in the path or whatever
2. install gnuplot and inkscape if you want figures etc
3. Install latex - but I already had this installed so idk.
4. I fixed a few broken brackets in two files to get perl through less errors
```
./make-latex.pl --file $somefile --savedir /home/$USERNAME/src/scigen/out/
```
if you don't specify savedir it will then just write to /tmp dir...


then generate a nice file using latex and bibtex to get citations to work

can't figure out yet how to get a "talk" to work...


