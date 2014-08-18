import sys
def syn2tikz(s,lang):
    syn_id = 1
    lex_id = 0
    fout.write('\Tree ')
    for i in range(len(s)):
        if s[i] == '(':
            fout.write('[.')
        elif s[i] == ')':
            fout.write(' ] ')
        elif s[i+1] == ')':
            lex_id_str = str(lex_id)
            fout.write(' \\node('+lang+lex_id_str+'){'+s[i]+lex_id_str+'};')
            lex_id += 1
        else:
            syn_id_str = str(syn_id)
            fout.write(s[i]+syn_id_str+' ')
            syn_id += 1
    fout.write('\n')

def ali2tikz(s):
    for ali_pair in s:
        ali_pair = ali_pair.split('-')
        fout.write('\draw (c'+str(ali_pair[0])+')--(e'+ali_pair[1]+');\n')

fout = open('tree-pair.tex','w')
fout.write('''\documentclass[tikz]{standalone}
\usepackage{CJKutf8}
\usepackage{color}
\usepackage{tikz}
\usepackage{tikz-qtree}
\\thispagestyle{empty}
\\begin{document}
\\begin{CJK}{UTF8}{gbsn}

\\begin{tikzpicture}
\\begin{scope}[frontier/.style={distance from root=350}]\n''')
ch_file,en_file,al_file,line_num = sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4])
f1,f2,f3 = open(ch_file),open(en_file),open(al_file)
for i,(s1,s2,s3) in enumerate(zip(f1,f2,f3)):
    if i == line_num:
        s1,s2,s3 = s1.replace('$','\$').split(),s2.replace('$','\$').split(),s3.split()
        syn2tikz(s1,'c')
        fout.write('''\end{scope}
\\begin{scope}[xshift=-50pt,yshift=-11in,grow'=up,
frontier/.style={distance from root=400}]\n''')
        syn2tikz(s2,'e')
        fout.write('''\end{scope}
\\begin{scope}[dashed]\n''')
        ali2tikz(s3)
        fout.write('''
\end{scope}
\end{tikzpicture}
\end{CJK}
\end{document}''')
        break
f1.close()
f2.close()
f3.close()
