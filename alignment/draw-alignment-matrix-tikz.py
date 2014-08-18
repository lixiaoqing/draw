import sys

ch_file,en_file,align_file,line = sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4])

s1 = '''\documentclass[border=1mm]{standalone}
\usepackage{tikz}
\usepackage{CJKutf8}

\\begin{document}
\\begin{CJK}{UTF8}{gbsn}

\\begin{tikzpicture}[scale=0.7]
  \\tikzstyle{vertex}=[rectangle,rounded corners, fill=blue!80, minimum size=0.6cm]
'''
s2 = '''
\end{tikzpicture}
\end{CJK}
\end{document}
'''

n = -1
for sch,sen,sal in zip(open(ch_file),open(en_file),open(align_file)):
    n += 1
    if n == line:
        f = open('a.tex','w')
        f.write(s1)
        #sch,sen,sal = sch.split(),sen.split(),sal.split()
        sch,sen,sal = sch.replace(',','{,}').split(),sen.replace(',','{,}').split(),sal.split()
        f.write('\draw[step=1cm,draw=gray] (0,0) grid ({},{});\n'.format(len(sen),len(sch)))
        lc,le=[],[]
        for i,c in enumerate(sch):
            lc.append(str(i)+'/'+c)
        f.write('''\\foreach \y/\\f in {'''+','.join(lc)+'''} {'''+'\n')
        f.write('''\\node[left] at (-.2,'''+str(len(sch)-0.5)+'''-\y) { \\f };'''+'\n}\n')
        for i,e in enumerate(sen):
            le.append(str(i)+'/'+e)
        f.write('''\\foreach \\x/\e in {'''+','.join(le)+'''} {'''+'\n')
        f.write('''\\node[rotate=60,right] at (\\x+.4,'''+str(len(sch)+0.2)+''') { \e };'''+'\n}\n')
    
        la = []
        for a in sal:
            a = a.split('-')
            la.append(a[1]+'/'+a[0])
        f.write('\\foreach \\x/\y in {'+','.join(la).strip()+'} {\n')
        f.write('\\node[vertex] at (\\x+.5, '+str(len(sch)-0.5)+'-\y) {};\n}\n')
        f.write(s2)
        f.close()
        break
