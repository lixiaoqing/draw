#!/usr/bin/python
import sys
from nltk.tree import Tree

parse_file = sys.argv[1]
line_num = int(sys.argv[2])
fout = open('tree.tex','w')
print >>fout,r'''\documentclass[tikz]{standalone}
\usepackage{CJKutf8}
\usepackage{color}
\usepackage{tikz}
\usepackage{tikz-qtree}
\thispagestyle{empty}
\begin{document}
\begin{CJK}{UTF8}{gbsn}

\begin{tikzpicture}'''
f = open(parse_file)
for i,s in enumerate(f):
    if i == line_num:
        s = s.replace('$','\$')
        tree = Tree.parse(s)
        h = tree.height()
        print >>fout,'''\\begin{{scope}}[frontier/.style={{distance from root={}}}]\n'''.format(h*28)
        for pos in tree.treepositions('leaves'):
	    tree[pos] = r'\edge[dashed]; {' + tree[pos] + '}'
        print >>fout,tree.pprint_latex_qtree()
        break
print >>fout,r'''
\end{scope}
\end{tikzpicture}
\end{CJK}
\end{document}
'''
f.close()
