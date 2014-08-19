if [ $# = 0 ];then
	echo "usage: draw-dtree.sh figure-type dep-file line-num"
	exit 0
fi
set -x
python /home/xqli/tools/draw/dtree/draw-dtree.py $1 $2 $3
pdflatex tree.tex > /dev/null
rm tree.tex tree.aux tree.log
