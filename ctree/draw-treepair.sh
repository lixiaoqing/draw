if [ $# = 0 ];then
	echo "usage: draw-treepair.sh ch-parse en-parse align-file line-num"
	exit 0
fi
set -x
python draw-treepair.py $1 $2 $3 $4
pdflatex tree-pair.tex > /dev/null
rm tree-pair.tex tree-pair.aux tree-pair.log
