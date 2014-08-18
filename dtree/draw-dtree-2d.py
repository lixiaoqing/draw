import sys
from nltk.parse import DependencyGraph

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
i = -1
dep_str = ''
for s in open(parse_file):
    if len(s.strip()) == 0:
        i += 1
        if i == line_num:
            dg = DependencyGraph(dep_str)
            tree = dg.tree()
            if flag == '0':
                h = tree.height()
                print >>fout,'''\\begin{{scope}}[frontier/.style={{distance from root={}}}]\n'''.format(h*28)
                for pos in tree.treepositions('leaves'):
	            tree[pos] = r'\edge[dashed]; {' + tree[pos] + '}'
            else:
                print >>fout,r'\begin{scope}'
            print >>fout,tree.pprint_latex_qtree()
            break
        dep_str = ''
    else:
        s = s.split()
        #dep,word,pos,head,rel = int(s[0]),s[1],s[3],int(s[6]),s[7]
        dep_str += ' '.join([s[1],s[3],s[6],s[7]])+'\n'

print >>fout,r'''
\end{scope}
\end{tikzpicture}
\end{CJK}
\end{document}
'''
