import sys
from collections import defaultdict
from nltk.parse import DependencyGraph

def traverse(t,h,fid): 
    try:
        t.node
    except AttributeError:
        x,w = t.split('-')
        print >>fout,'\\node(n{}) at({},{}) {{{}}};'.format(x,0.6*xpos[int(x)],1.5*h,w)
        print >>fout,'\\draw (n{}) -- (n{});'.format(fid,x)
    else:
        x,w = t.node.split('-')
        print >>fout,'\\node(n{}) at({},{}) {{{}}};'.format(x,0.6*xpos[int(x)],1.5*h,w)
        if fid != 0:
            print >>fout,'\\draw (n{}) -- (n{});'.format(fid,x)
        for child in t:
            traverse(child,h-1,x)

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

if flag == '1':
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
    wids = []
    wlens,xpos = [0],[0]
    for s in open(parse_file):
        if len(s.strip()) == 0:
            i += 1
            if i == line_num:
                dg = DependencyGraph(dep_str)
                tree = dg.tree()
                if flag == '0':
                    h = tree.height()
                    traverse(tree,h,0)
                    for k,w in wids:
                        print >>fout,'\\node(m{}) at({},{}) {{{}}};'.format(k,0.6*xpos[k],0,w)
                        print >>fout,'\\node at({},{}) {{{}}};'.format(0.6*xpos[k],-0.5,k-1)
                        print >>fout,'\\draw[dotted] (m{}) -- (n{});'.format(k,k)
                else:
                    print >>fout,tree.pprint_latex_qtree()
                break
            dep_str = ''
            wids = []
            wlens,xpos = [0],[0]
        else:
            s = s.split()
            idx,word,pos,head,rel = int(s[0]),s[1],s[3],int(s[6]),s[7]
            wids.append((idx,word))
            wlens.append(len(word.decode('utf8')))
            xpos.append(0.5*(wlens[-1]+wlens[-2])+xpos[-1])
            dep_str += ' '.join([str(idx)+'-'+word,pos,str(head),rel])+'\n'
    
    print >>fout,r'''
\end{tikzpicture}
\end{CJK}
\end{document}
'''
