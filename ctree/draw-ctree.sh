if [ $# = 0 ];then
	echo "usage: draw-ctree.sh figure-type(0/1) parse-file line-num"
	exit 0
fi
set -x
python /home/xqli/tools/draw/ctree/draw-ctree.py $1 $2 $3
pdflatex tree.tex > /dev/null
rm tree.tex tree.aux tree.log
