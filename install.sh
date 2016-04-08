BINDIR=/usr/bin/
DATADIR=/usr/share/

if [ "$#" -gt 0 -a "$1" = "-h" ]; then
	echo "Usage: $0 [-b] BINDIR [-d] DATADIR"
	echo "    -b BINDIR: Set the BINDIR. Default value is $BINDIR"
	echo "    -d DATADIR: Set the DATADIR. Default value is $DATADIR"
	exit 0
fi

if [ "$#" -gt 0 -a "$1" = "-b" ]; then
  BINDIR=$2 
fi

if [ "$#" -gt 0 -a "$1" = "-d" ]; then
  DATADIR=$2 
fi

if [ "$#" -gt 0 -a "$3" = "-d" ]; then
  DATADIR=$4 
fi


chmod -v +x unusedpkg
cp -v unusedpkg $BINDIR/
cp -v -r locale $DATADIR/
