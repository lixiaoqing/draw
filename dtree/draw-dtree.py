import sys
from collections import defaultdict
from nltk.parse import DependencyGraph

flag = sys.argv[1]
parse_file = sys.argv[2]
line_num = int(sys.argv[3])
fout = open('tree.tex','w')
print >>fout,r'''\documentclass[tikz]{standalone}
\usepackage{CJKutf8}
\usepackage{color}
\usepackage{tikz}
\usepackage{tikz-dependency}
\usepackage{tikz-qtree}
\thispagestyle{empty}
\begin{document}
\begin{CJK}{UTF8}{gbsn}
'''

if flag == '0':
    print >>fout,r'''\begin{dependency}[theme = simple]
\begin{deptext}[column sep=1em] '''
    head2children = defaultdict(list)
    sen_src = []
    i = -1
    for s in open(parse_file):
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
else:
    print >>fout,r'''\begin{tikzpicture}'''
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
                    #print >>fout,'''\\begin{{scope}}[frontier/.style={{distance from root={}}}]\n'''.format(h*28)
                    print >>fout,'''\\begin{{scope}}\n'''.format(h*28)
                    for pos in tree.treepositions('leaves'):
    	                tree[pos] = r'\edge[dashed]; {' + tree[pos] + '}'
                else:
                    print >>fout,r'\begin{scope}'
                print >>fout,tree.pprint_latex_qtree()
                break
            dep_str = ''
        else:
            s = s.split()
            self,word,pos,head,rel = int(s[0]),s[1],s[3],int(s[6]),s[7]
            dep_str += ' '.join([word,pos,str(head),rel])+'\n'
            #dep_str += ' '.join([word,pos,str(max(2*head-1,0)),rel])+'\n'
            #dep_str += ' '.join([word,pos,str(2*self-1),'MOD'])+'\n'
    
    print >>fout,r'''
\end{scope}
\end{tikzpicture}
\end{CJK}
\end{document}
'''
