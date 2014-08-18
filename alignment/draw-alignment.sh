if [ $# = 0 ];then
	echo "usage: draw-alignment.sh ch-file en-file align-file line-num"
	exit 0
fi
set -x
python /home/xqli/tools/draw/alignment/draw-alignment-matrix-tikz.py $1 $2 $3 $4
pdflatex a.tex >/dev/null
rm a.aux a.log a.tex
