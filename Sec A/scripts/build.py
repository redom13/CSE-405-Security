"""Build portable Markdown/HTML/LaTeX and compile the Sec A PDF with XeLaTeX."""
from pathlib import Path
import sys,subprocess,shutil,re,json,csv,argparse
SECTION=Path(__file__).resolve().parents[1]
SCRIPTS=SECTION/'scripts';SOLUTIONS=SECTION/'solutions';BUILD=SECTION/'_build/latex'
parser=argparse.ArgumentParser()
parser.add_argument('--source-only',action='store_true',help='Generate documents without compiling the PDF')
parser.add_argument('--diagrams',action='store_true',help='Regenerate diagram assets')
args=parser.parse_args()
def run(name):subprocess.run([sys.executable,str(SCRIPTS/name)],check=True)
if args.diagrams:run('make_diagrams.py')
run('build_guide.py');run('export_latex.py')
if args.source_only:raise SystemExit(0)
compiler=shutil.which('xelatex')
if not compiler:
    raise SystemExit('XeLaTeX is not available. Install texlive-xetex and texlive-latex-extra; source files are ready. Then run this build again.')
BUILD.mkdir(parents=True,exist_ok=True)
for pass_number in range(4):
    prior={ext:(BUILD/f'SOLUTIONS.{ext}').read_bytes() if (BUILD/f'SOLUTIONS.{ext}').exists() else b'' for ext in ['aux','toc']}
    result=subprocess.run([compiler,'-no-shell-escape','-interaction=nonstopmode','-halt-on-error',f'-output-directory={BUILD}','SOLUTIONS.tex'],cwd=SOLUTIONS,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (BUILD/'compiler-output.txt').write_text(result.stdout)
    if result.returncode:
        print(result.stdout[-5000:]);raise SystemExit('LaTeX compilation failed; see Sec A/_build/latex/compiler-output.txt')
    current={ext:(BUILD/f'SOLUTIONS.{ext}').read_bytes() if (BUILD/f'SOLUTIONS.{ext}').exists() else b'' for ext in ['aux','toc']}
    if pass_number>=1 and current==prior:break
shutil.copy2(BUILD/'SOLUTIONS.pdf',SOLUTIONS/'SOLUTIONS.pdf')
aux=(BUILD/'SOLUTIONS.aux').read_text()
pages=dict((k,int(v)) for k,v in re.findall(r'\\newlabel\{(a\d+)\}\{\{[^}]*\}\{(\d+)\}',aux))
index=json.loads((SOLUTIONS/'solutions_index.json').read_text())
with (SOLUTIONS/'QUESTION_LOOKUP.csv').open('w',newline='') as f:
    writer=csv.writer(f);writer.writerow(['Solution ID','Academic session','Question','Solution PDF page','Original PDF page','Topic keys'])
    for q in index:writer.writerow([q['solution_id'],q['session'],q['question'],pages.get(q['solution_id'].lower(),''),q['page_in_original'],'; '.join(q['topics'])])
(SOLUTIONS/'pdf_page_map.json').write_text(json.dumps({'compiler':'xelatex','solutions':pages},indent=2)+'\n')
print(f'Compiled LaTeX PDF with {len(pages)} question destinations: {SOLUTIONS/"SOLUTIONS.pdf"}')
