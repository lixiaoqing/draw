if [ $# = 0 ];then
	echo "usage: draw-tree.sh parse-file line-num"
	exit 0
fi
set -x
python /home/xqli/tools/draw/ctree/draw-ctree.py $1 $2
pdflatex tree.tex > /dev/null
rm tree.tex tree.aux tree.log