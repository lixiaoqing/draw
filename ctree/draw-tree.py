#!/usr/bin/python
import sys
def syn2tikz(s):
	syn_id = 1
	lex_id = 0
	fout.write('\Tree ')
	for i in range(len(s)):
		if s[i] == '(':
			fout.write('[.')
		elif s[i] == ')':
			fout.write(' ] ')
		elif s[i+1] == ')':
			fout.write(s[i]+' ')
		else:
			fout.write(s[i]+' ')
	fout.write('\n')

parse_file = sys.argv[1]
line_num = int(sys.argv[2])
fout = open('tree.tex','w')
fout.write('''\documentclass[tikz]{standalone}
\usepackage{CJKutf8}
\usepackage{color}
\usepackage{tikz}
\usepackage{tikz-qtree}
\\thispagestyle{empty}
\\begin{document}
\\begin{CJK}{UTF8}{gbsn}

\\begin{tikzpicture}
\\begin{scope}\n''')
f = open(parse_file)
for i,s in enumerate(f):
    if i == line_num:
        s = s.replace('$','\$')
        syn2tikz(s.split())
        break
fout.write('''
\end{scope}
\end{tikzpicture}
\end{CJK}
\end{document}
''')
f.close()
