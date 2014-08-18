#!/usr/bin/python
#encoding=utf8
import sys
from collections import defaultdict

fn = sys.argv[1]
line_num = int(sys.argv[2])

fout = open('tree.tex','w')
print >>fout,r'''\documentclass[tikz]{standalone}
\usepackage{CJKutf8}
\usepackage{color}
\usepackage{tikz}
\usepackage{tikz-dependency}
\thispagestyle{empty}
\begin{document}
\begin{CJK}{UTF8}{gbsn}

\begin{dependency}[theme = simple]
\begin{deptext}[column sep=1em] '''
head2children = defaultdict(list)
sen_src = []
i = -1
for s in open(fn):
    if len(s.strip()) == 0:
        i += 1
        if i == line_num:
            print >>fout,' \& '.join(sen_src) + r' \\'
            print >>fout,r'\end{deptext}'
            print >>fout,r'\deproot{'+str(head2children[0][0])+'}{}'
            del head2children[0]
            for head,deps in head2children.items():
                for dep in deps:
                    print >>fout,r'\depedge{'+str(head)+'}{'+str(dep)+'}{}'
            break
        head2children = defaultdict(list)
        sen_src = []
    else:
        s = s.split()
        dep = int(s[0])
        head = int(s[6])
        word = s[1]
        head2children[head].append(dep)
        sen_src.append(word)

print >>fout,r'''
\end{dependency}
\end{CJK}
\end{document}
'''

