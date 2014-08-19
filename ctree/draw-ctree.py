#!/usr/bin/python
import sys
from nltk.tree import Tree

flag = sys.argv[1]
parse_file = sys.argv[2]
line_num = int(sys.argv[3])
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
        if flag == '0':
            h = tree.height()
            print >>fout,'''\\begin{{scope}}[frontier/.style={{distance from root={}}}]\n'''.format(h*28)
            for pos in tree.treepositions('leaves'):
	        tree[pos] = r'\edge[dotted]; {' + tree[pos] + '}'
        else:
            print >>fout,r'\begin{scope}'
        print >>fout,tree.pprint_latex_qtree()
        break
print >>fout,r'''
\end{scope}
\end{tikzpicture}
\end{CJK}
\end{document}
'''
f.close()
