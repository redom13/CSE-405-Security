"""Audit question completeness, portable links, offline HTML and compiled PDF labels."""
from pathlib import Path
import json,re,collections,subprocess,sys
from urllib.parse import urlsplit,unquote
from bs4 import BeautifulSoup
from math_markup import render_markdown
ROOT=Path(__file__).resolve().parents[2]
errors=[]
for sec in ['Sec A','Sec B']:
 section=ROOT/sec;sol=section/'solutions'
 qs=json.loads((section/'analysis/question_index.json').read_text())
 index=json.loads((sol/'solutions_index.json').read_text())
 labels=json.loads((sol/'pdf_page_map.json').read_text())['solutions']
 expected={(q['session'],q['question']) for q in qs}
 found={(q['session'],q['question']) for q in index}
 if found!=expected:errors.append((sec,'index mismatch'))
 if len(expected)!=len(qs):errors.append((sec,'duplicate questions'))
 if set(labels)!={q['solution_id'].lower() for q in index}:errors.append((sec,'PDF label mismatch'))
 full=BeautifulSoup((sol/'SOLUTIONS.html').read_text(),'html.parser')
 ids=[n['id'] for n in full.select('[id]')]
 duplicates=[k for k,n in collections.Counter(ids).items() if n>1]
 if duplicates:errors.append((sec,'duplicate HTML IDs',duplicates[:10]))
 if full.select('script[src]') or full.select('img[src^="http"]'):errors.append((sec,'external HTML runtime'))
 if len(full.select('section.question'))!=len(qs):errors.append((sec,'HTML answer count'))
 for p in list(section.rglob('*.md'))+[sol/'SOLUTIONS.html']:
  if '_build' in p.parts:continue
  soup=full if p.suffix=='.html' else BeautifulSoup(render_markdown(p.read_text()),'html.parser')
  for n in soup.select('a[href],img[src]'):
   u=n.get('href',n.get('src',''));parts=urlsplit(u)
   if parts.scheme or parts.netloc:continue
   path=(p.parent/unquote(parts.path)).resolve() if parts.path else p
   if not path.exists():errors.append((str(p.relative_to(ROOT)),'missing target',u))
   if parts.fragment and (not parts.path or path.suffix=='.html'):
    target=full if path==sol/'SOLUTIONS.html' else soup if path==p else BeautifulSoup(path.read_text(),'html.parser')
    if not target.find(id=unquote(parts.fragment)):errors.append((str(p.relative_to(ROOT)),'missing anchor',u))
  if '/home/nhr13/' in p.read_text() or 'file://' in p.read_text():errors.append((str(p),'machine-specific path'))
 log=(section/'_build/latex/SOLUTIONS.log').read_text()
 warnings=[l for l in log.splitlines() if re.search(r'Overfull|Missing character|^!|undefined references|multiply defined',l)]
 if warnings:errors.append((sec,'TeX warnings',warnings[:6]))
 out=section/'_build/pdf-audit.txt';subprocess.run(['pdftotext',str(sol/'SOLUTIONS.pdf'),str(out)],check=True)
 text=out.read_text()
 absent=[q['solution_id'] for q in index if q['solution_id'] not in text]
 if absent:errors.append((sec,'missing PDF answer identifiers',absent))
 print(sec,':',len(qs),'answers;',len(full.find_all('math')),'MathML formulas;',len(labels),'PDF destinations')
if errors:
 print(json.dumps(errors,indent=2,ensure_ascii=False));raise SystemExit(1)
print('All document checks passed.')
