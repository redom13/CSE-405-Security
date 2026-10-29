"""Generate an editable XeLaTeX document from the canonical Markdown guide."""
from pathlib import Path
from bs4 import BeautifulSoup,Tag,NavigableString
import re,math
SECTION=Path(__file__).resolve().parents[1]
BASE=SECTION/'solutions'
PREAMBLE=r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=20mm,headheight=15pt]{geometry}
\usepackage{fontspec}
\setmainfont{DejaVu Serif}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}[Scale=0.82]
\usepackage{amsmath,amssymb,graphicx,longtable,array,booktabs}
\usepackage[dvipsnames]{xcolor}
\usepackage{fvextra,enumitem,needspace,fancyhdr}
\usepackage{xurl}
\urlstyle{same}
\usepackage[unicode,colorlinks=true,linkcolor=MidnightBlue,urlcolor=MidnightBlue]{hyperref}
\definecolor{Ink}{HTML}{1C3047}
\definecolor{Panel}{HTML}{F0F4F8}
\definecolor{PanelBorder}{HTML}{B7C9DB}
\color{Ink}
\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt}
\setlength{\emergencystretch}{3em}
\setlength{\tabcolsep}{4pt}
\renewcommand{\arraystretch}{1.2}
\setcounter{secnumdepth}{0}
\setcounter{tocdepth}{2}
\setlist{nosep,leftmargin=1.5em}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small CSE 405 · Sec B}
\fancyhead[R]{\small Worked final-exam solutions}
\fancyfoot[C]{\thepage}
\hypersetup{pdftitle={CSE 405 — Sec B Worked Final-Exam Solutions},pdfauthor={Sec B study guide},bookmarksopen=true}
\title{\sffamily\bfseries CSE 405\\[4pt]Worked Final-Exam Solutions}
\author{Sec B · 74 worked entries · six academic sessions}
\date{}
\begin{document}
\maketitle
\tableofcontents
\clearpage
'''
SPECIAL={'\\':r'\textbackslash{}','{':r'\{','}':r'\}','$':r'\$','&':r'\&','#':r'\#','%':r'\%','_':r'\_','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}
def plain(s):
    s=re.sub(r'(?<=[A-Za-z])\.(?=[A-Za-z])',lambda m:'.'+chr(0x200b),s)
    return ''.join((r'\allowbreak{}' if c==chr(0x200b) else SPECIAL.get(c,c) + (r'\allowbreak{}' if c in '/,=' else '')) for c in s)
def esc(s):
    chunks=re.split(r'(https?://[^\s<>]+)',s)
    out=[]
    for i,chunk in enumerate(chunks):
        if i%2:
            url=chunk.rstrip('.,;')
            tail=chunk[len(url):]
            out.append(r'\nolinkurl{'+url.replace('%',r'\%').replace('#',r'\#')+'}'+plain(tail))
        else:out.append(plain(chunk))
    return ''.join(out)
def href(h):return h.replace('%',r'\%').replace('#',r'\#').replace('&',r'\&')
first_question=True
pending_anchor=None

def render(node):
    global first_question,pending_anchor
    if isinstance(node,NavigableString):return esc(str(node))
    if not isinstance(node,Tag):return ''
    if 'math-inline' in node.get('class',[]):return r'\('+node['data-tex']+r'\)'
    if 'math-display' in node.get('class',[]):return '\n\\[\n'+node['data-tex']+'\n\\]\n'
    tag=node.name
    if tag=='a' and node.get('id'):
        pending_anchor=node['id'];return ''
    if tag=='pre':
        text=node.get_text().rstrip('\n')
        if '\\end{Verbatim}' in text:raise ValueError('Verbatim terminator in answer text')
        return '\n\\begin{Verbatim}[breaklines=true,breakanywhere=true,fontsize=\\small,frame=single,rulecolor=\\color{PanelBorder}]\n'+text+'\n\\end{Verbatim}\n'
    if tag=='img':
        path=Path(node['src'])
        if path.suffix=='.svg':path=path.with_suffix('.pdf')
        if not (BASE/path).exists():raise FileNotFoundError(BASE/path)
        return '\n\\begin{center}\n\\includegraphics[width=\\linewidth,height=.34\\textheight,keepaspectratio]{'+path.as_posix()+'}\n\\end{center}\n'
    if tag=='table':
        rows=node.find_all('tr')
        n=max(len(row.find_all(['th','td'],recursive=False)) for row in rows)
        weights=[]
        for i in range(n):
            lengths=[len(cells[i].get_text()) for row in rows if len(cells:=row.find_all(['th','td'],recursive=False))>i]
            weights.append(max(5,min(65,max(lengths))))
        if n>=8:weights=[1.6]+[1]*(n-1)
        else:weights=[math.sqrt(w) for w in weights]
        # Padding/rules consume width separately from paragraph columns.
        available=1-(6*n+2)/481.0
        widths=[available*w/sum(weights) for w in weights]
        cols=''.join(r'>{\raggedright\arraybackslash}p{'+f'{w:.5f}'+r'\linewidth}' for w in widths)
        out=['\n{\\small\\setlength{\\tabcolsep}{3pt}\n\\begin{longtable}{'+cols+'}',r'\toprule']
        for i,row in enumerate(rows):
            cells=row.find_all(['th','td'],recursive=False)
            values=[''.join(render(x) for x in c.children).strip() for c in cells]
            if i==0:values=[r'\textbf{'+v+'}' for v in values]
            out.append(' & '.join(values)+r' \\')
            if i==0:out.extend([r'\midrule',r'\endhead'])
        out.extend([r'\bottomrule',r'\end{longtable}',r'}',''])
        return '\n'.join(out)
    children=''.join(render(x) for x in node.children)
    if tag=='h1':return ''
    if tag=='h2':
        first_question=True
        return '\n\\clearpage\n\\section{'+children+'}\n'
    if tag=='h3':
        anchor=pending_anchor;pending_anchor=None
        lead='' if first_question else '\\clearpage\n'
        first_question=False
        return '\n'+lead+'\\subsection{'+children+'}'+('\\label{'+anchor+'}' if anchor else '')+'\n'
    if tag in ['h4','h5']:return '\n\\Needspace{4\\baselineskip}\\textbf{'+children+'}\n\n'
    if tag in ['strong','b']:return r'\textbf{'+children+'}'
    if tag in ['em','i']:return r'\emph{'+children+'}'
    if tag=='code':return r'\texttt{'+children+'}'
    if tag=='br':return r'\\'+'\n'
    if tag=='p':
        if not node.get_text().strip() and not node.find('img'):return children
        if node.get_text().startswith('Exam tip.'):
            return '\n\\Needspace{4\\baselineskip}\n{\\color{ForestGreen}'+children+'}\n\n'
        return children+'\n\n'
    if tag=='blockquote':return '\n\\begin{quote}\\small\n'+children+'\n\\end{quote}\n'
    if tag in ['ul','ol']:
        return '\n\\begin{'+('itemize' if tag=='ul' else 'enumerate')+'}\n'+children+'\\end{'+('itemize' if tag=='ul' else 'enumerate')+'}\n'
    if tag=='li':return '\\item '+children+'\n'
    if tag=='a':
        url=node.get('href','')
        if url.startswith('#'):return r'\hyperref['+url[1:]+']{'+children+'}'
        return r'\href{'+href(url)+'}{'+children+'}' if url else children
    return children

if __name__=='__main__':
    soup=BeautifulSoup((SECTION/'_build/render_body.html').read_text(),'html.parser')
    text=PREAMBLE+''.join(render(node) for node in soup.children)+'\n\\end{document}\n'
    (BASE/'SOLUTIONS.tex').write_text(text)
    print('Wrote LaTeX source:',len(text),'characters;',text.count('\\label{s'),'solution labels')
