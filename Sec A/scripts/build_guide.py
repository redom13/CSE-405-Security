"""Build the complete Sec A Markdown and standalone HTML worked guide."""
from pathlib import Path
import json,re,html,base64,ast,shutil
from urllib.parse import quote
from bs4 import BeautifulSoup
from catalog import ROOT,SECTION,DECKS,TOPICS
from questions import questions,answers,new_questions
from math_markup import render_markdown,render_native_math
BASE=SECTION/'solutions';BUILD=SECTION/'_build';BUILD.mkdir(exist_ok=True)
count=len(questions)
lines=['# CSE 405 · Sec A Worked Final-Exam Solutions','',
'## How to use this guide','',
f'**{count} complete answers across six academic sessions.** {len(new_questions)} system/network/general-security answers are newly developed here; {count-len(new_questions)} questions overlap the previously checked Sec B collection. Each printed question appears once in this guide, under its primary teaching deck; the topic index points to every relevant mixed question. Exam tips appear before the reasoning to keep them with the question when printing.','',
'Question summaries are paraphrases, not official transcriptions or a marking scheme. Consult the linked physical paper page for original code/diagrams. Every indexed question has a worked answer, necessary assumptions, explanation and an exam tip. Related/extension flags identify tasks beyond the local slides rather than silently pretending they are fully taught.','',
'**Notation and limits:** toy memory examples use the paper’s stated 32-bit conventions; actual compiler/ABI layouts can differ. Probabilities identify their assumptions. Hashes, MACs and signatures provide different guarantees. A network address is not an authenticated identity. Several “guaranteed attack” requests are under-specified; the answers explain the intended mechanism and the conditions needed for it.','',
'The PDF uses XeLaTeX typesetting; this HTML embeds native MathML and diagrams for offline reading in a browser supporting MathML. The Markdown is editable and renders dollar math on GitHub. All sources, analysis and build tools stay within the section layout.','',
'## Navigation by slide deck and exact topic','']
for d,(file,title,_,_) in DECKS.items():
 lines += [f'**{title}** — [{file}](../slides/{quote(file)})','']
 for t,(name,deck,_,_) in TOPICS.items():
  if deck!=d:continue
  arr=[q for q in questions if t in q['topics']]
  if arr:lines += [f'**{name}:** '+ '; '.join(f'[{q["solution_id"]} · {q["session"]} Q{q["question"]}](#{q["solution_id"].lower()})' for q in arr),'']
lines += ['## Numerical and conceptual checkpoints','',
'| Exercise | Checkpoint |','|---|---|',
'| Three independently mastered pin chambers | $2^3=8$ total theoretical profiles, seven additional |',
'| Common master lock | Bottom pins (2,2,5,2,6); wafers (2,2,0,3,0) |',
'| SI worm model | $I(t)=N/[1+((N-I_0)/I_0)e^{-\\beta Nt}]$ |',
'| IDS example: prevalence 0.1%, sensitivity 99%, FPR 1% | About 9.02% of alarms are true positives |',
'| Toy printf cursor model | secret1 slot 6; controlled first input word slot 13 |',
'| Toy alphabet-only return | 0x41424349 encodes as little-endian ICBA; clean EBP restoration is a separate constraint |',
'| Known-salt password | Salt is public; it prevents shared precomputation, not guessing a single account |','']
for d,(file,title,_,_) in DECKS.items():
 arr=[q for q in questions if TOPICS[q['topics'][0]][1]==d]
 if not arr:continue
 lines += [f'## {title}','',f'Primary deck: [{file}](../slides/{quote(file)})','']
 for q in arr:
  key=q['session']+'|'+q['question'];sid=q['solution_id'];assert answers[key]
  lines += [f'<a id="{sid.lower()}"></a>',f'### {sid} · {q["session"]} · Q{q["question"]}','',f'**{q["exact_skill"]} · {q["marks"]} marks**','',f'Original: [past-paper PDF p. {q["pdf_page"]}](../../CSE405-Security_Merged.pdf#page={q["pdf_page"]}). Sitting date: {q["sitting_date"]}.','',
  '**Topics:** '+ '; '.join(TOPICS[t][0] for t in q['topics'])+'.','',
  '> **Question summary:** '+q['question_paraphrase'],'']
  if q['coverage']=='partial':lines+=['**Coverage:** related application/extension. '+q['coverage_note'],'']
  answer=answers[key]
  tips=re.findall(r'(?:^|\n\n)(\*\*Exam tip\.\*\*.*?)(?=\n\n|\Z)',answer,flags=re.S)
  for tip in tips:
   answer=answer.replace(tip,'').strip()
   lines += [tip,'']
  lines += [answer,'']
lines+=['## Review checklist','',
'- Protocol answers: label peers, message fields, authenticated identities, replay state and attacker position.','- Probability answers: define the population/conditioning, compute intermediate counts and check units.','- Memory answers: trace actual destination bounds, endianness, frame offsets and input restrictions; distinguish a control transfer from clean continuation.','- Permission answers: distinguish real/effective identity, pathname/object identity and revocation of delegated rights.','- Detection answers: discuss false positives, false negatives, attacker visibility and what the mechanism cannot observe.','',
'## Sources and overlap','',
'Local source page maps and exam-frequency evidence are in [the Sec A analysis](../analysis/FINAL_EXAM_TOPIC_ANALYSIS.md). The [Sec A syllabus](../analysis/SYLLABUS.md) records limitations and source errors. Matching crypto/web questions reuse checked Sec B answer text and vector diagrams; their complete bodies are included here. Six newly developed principle questions also appear in the updated Sec B guide, giving 60 shared questions overall. Sec A’s build reads those original answer sources from the same repository, so rebuild both sections together after editing shared answers.','',
'Primary technical references appear beside the answers that use them; these supplement the supplied course material rather than define a new course syllabus.','']
md='\n'.join(lines);(BASE/'SOLUTIONS.md').write_text(md)
# Refresh shared diagram copies when their Sec B sources change.
for asset in set(re.findall(r'!\[[^\]]*\]\(([^)]+)\)',md)):
 source=ROOT/'Sec B/solutions'/asset
 if source.exists():
  for suffix in [source.suffix,'.pdf','.png']:
   candidate=source.with_suffix(suffix)
   if candidate.exists():shutil.copy2(candidate,BASE/'assets'/candidate.name)
body=render_markdown(md);(BUILD/'render_body.html').write_text(body)
soup=BeautifulSoup(body,'html.parser')
if not render_native_math(soup):raise RuntimeError('Pandoc native MathML conversion failed; refusing unreadable HTML math')
for img_no,img in enumerate(list(soup.find_all('img'))):
 p=BASE/img['src']
 if not p.exists():raise FileNotFoundError(p)
 if p.suffix=='.svg':
  raw=p.read_text()
  for old in re.findall(r'\bid="([^"]+)"',raw):
   new=f'fig-{img_no}-'+old
   raw=raw.replace('id="'+old+'"','id="'+new+'"').replace('url(#'+old+')','url(#'+new+')').replace('href="#'+old+'"','href="#'+new+'"')
  svg=BeautifulSoup(raw[raw.index('<svg'):],'html.parser').find('svg');svg['class']='diagram';svg['role']='img';svg['aria-label']=img.get('alt','Diagram');img.replace_with(svg)
 else:img['src']='data:image/png;base64,'+base64.b64encode(p.read_bytes()).decode()
# Explicit Markdown anchors are inside paragraphs; put all question content in sections.
for h in list(soup.find_all('h3')):
 sid=h.get_text().split(' · ')[0].lower()
 prior=h.find_previous_sibling()
 if prior and prior.name=='p' and prior.find('a',id=sid):prior.decompose()
 sec=soup.new_tag('section',id=sid);sec['class']='question';h.insert_before(sec);node=h
 while node:
  nxt=node.next_sibling
  if node is not h and getattr(node,'name',None) in ['h2','h3']:break
  # Leave the next question's explicit anchor in place.
  if node is not h and getattr(node,'name',None)=='p' and node.find('a',id=re.compile(r'^a\d+$')):break
  sec.append(node);node=nxt
# Reuse the established readable visual stylesheet without executing Sec B generation.
module=ast.parse((ROOT/'Sec B/scripts/build_guide.py').read_text())
css=next(ast.literal_eval(n.value) for n in module.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='css' for t in n.targets))
css+=' section.question{scroll-margin-top:20px} math{font-size:1.08em} .math-display math{margin:auto}'
nav=''.join(f'<a href="#{q["solution_id"].lower()}">{q["solution_id"]} · {q["session"]} Q{q["question"]}<br>{html.escape(q["exact_skill"])}</a>' for q in questions)
js="""const search=document.getElementById('search');function filter(){const s=search.value.toLowerCase();document.querySelectorAll('.question').forEach(q=>q.classList.toggle('hidden',!q.textContent.toLowerCase().includes(s)));}search.addEventListener('input',filter);document.addEventListener('click',e=>{if(e.target.closest('a[href^="#a"]')){search.value='';filter();}});"""
page=f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sec A · {count} worked solutions</title><style>{css}</style></head><body><nav><h2>CSE 405 · Sec A</h2><p>{count} complete answers</p><input id="search" aria-label="Search solutions" placeholder="Search questions or answers"><button onclick="window.print()">Print / save PDF</button>{nav}</nav><main>{soup}</main><script>{js}</script></body></html>'
(BASE/'SOLUTIONS.html').write_text(page)
index=[dict(solution_id=q['solution_id'],session=q['session'],question=q['question'],page_in_original=q['pdf_page'],topics=q['topics'],primary_deck=TOPICS[q['topics'][0]][1]) for q in questions]
(BASE/'solutions_index.json').write_text(json.dumps(index,indent=2,ensure_ascii=False)+'\n')
print(f'Sec A guide: {count} answers; {len(md.split())} words')
