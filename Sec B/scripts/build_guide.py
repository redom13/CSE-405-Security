from pathlib import Path
import json, importlib.util, re, base64, html, os
from urllib.parse import quote
from math_markup import render_markdown, render_native_math
import markdown
from bs4 import BeautifulSoup
from collections import defaultdict
SECTION=Path(__file__).resolve().parents[1]
BASE=SECTION/'solutions'
ROOT=SECTION.parent
qs=json.loads((SECTION/'analysis/question_index.json').read_text())
answers={}
for p in sorted((BASE/'src').glob('answers_*.py')):
 spec=importlib.util.spec_from_file_location(p.stem,p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
 for k,v in m.answers.items():
  if k in answers:raise ValueError('Duplicate '+k)
  answers[k]=v.strip()
expected={q['session']+'|'+q['question'] for q in qs}
if set(answers)!=expected:raise ValueError({'missing':list(expected-set(answers)),'extra':list(set(answers)-expected)})
# The point table is the answer; a finite-field point plot adds a visual companion.
k='2021–22|2(b)'
if 'ecc-points.svg' not in answers[k]:answers[k]+='\n\n![Finite-field curve points](assets/ecc-points.svg)'
topicdeck={'principles':'L1','securitygoals':'L1','goals':'L2','classical':'L2','otp':'L3','block':'L3','modes':'L4','hash':'L5','mac':'L5','ae':'L5','prng':'L6','dh':'L6','ecc':'L6','rsa':'L7','elgamal':'L7','signature':'L7','keymodels':'L7','cert':'L8','password':'L8','cookies':'L10','session':'L10','csrf':'L10','xss':'L11','sql':'L12','ui':'L11','twofa':'L11'}
names={'L1':'Lecture 1 — Introduction and Security Principles','L2':'Lecture 2 — Cryptographic foundations and classical ciphers','L3':'Lecture 3 — One-time pads and block ciphers','L4':'Lecture 4 — Block-cipher modes','L5':'Lecture 5 — Hashes, MACs and authenticated encryption','L6':'Lecture 6 — PRNGs, Diffie–Hellman and ECC','L7':'Lecture 7 — Public-key encryption and signatures','L8':'Lecture 8 — Certificates and password security','L9':'Lecture 9 — Web foundations','L10':'Lecture 10 — Cookies, sessions and CSRF','L11':'Lecture 11 — XSS and UI Attacks','L12':'Lecture 12 — SQL Injection and CAPTCHAs'}
sourcefiles={d:next((x['file'] for x in json.loads((SECTION/'analysis/inventory.json').read_text()) if x.get('lecture')==int(d[1:])),None) for d in names if d.startswith('L')}

for i,q in enumerate(qs,1):q['solution_id']=f'S{i:02d}'
bydeck={d:[q for q in qs if topicdeck[q['topics'][0]]==d] for d in names}
front='''# CSE 405 · Worked Final-Exam Solutions

## How to use this guide

**73 complete worked solutions · six academic sessions · all gathered questions.** Each question appears once with its original index label S01–S73. The topic/deck index also points to mixed questions taught partly elsewhere. The HTML has search, question navigation, scalable diagrams and typeset equations; the PDF is compiled from LaTeX for printing. The Markdown is editable.

Question summaries are paraphrases. The root PDF remains the authority for wording, code and figures. The solution metadata links to its physical page. Each answer includes reasoning and an exam tip; assumptions and defects in printed questions are identified rather than silently repaired. These are independent worked solutions, not an official marking scheme.

**Conventions:** A=0,…,Z=25; Hill uses column vectors; XOR is bitwise addition modulo 2; || means unambiguous concatenation; exponents, matrices and modular arithmetic use LaTeX notation. Unless stated otherwise, tags/signatures cover the relevant identity, nonce and protocol context. Computational results use the numbers in the paper.

**Four corrections to keep in mind:** Cookie 2 in 2020–21 Q7(b) is non-secure; the 2018–19 Hill key is not invertible modulo 26; the full-group ElGamal question needs a valid nonzero-message argument; a visible cookie or freshly transmitted plaintext MAC key cannot authenticate against an eavesdropper. Relevant solutions explain each point.

Lecture 9 has no separate standalone question in the gathered index. Its URL/HTTP/origin foundations are used in the web solutions. The newly supplied Lecture 1 adds six principle/availability/TOCTOU questions (S68–S73) and gives an explicit source for the existing information-security CIA question. Other Sec A-only material remains in its own guide.

## Navigation by teaching source

'''
lines=[front]
for d in names:
 related=[q for q in qs if any(topicdeck[t]==d for t in q['topics'])]
 if not related:continue
 lines += [f'**{names[d]}**','']
 lines += ['; '.join(f'[{q["solution_id"]}: {q["session"]} Q{q["question"]}](#{q["solution_id"].lower()})' for q in related),'']
lines += ['## Numerical answers at a glance','',
'| Question | Result |','|---|---|',
'| 2023–24 Q6(b) | Affine keys K1=21, K2=9 |',
'| 2023–24 Q7(a) | ElGamal B=248, ciphertext (40,265), decrypted M=123 |',
'| 2021–22 Q1(c) | ACT → POH → ACT |',
'| 2021–22 Q2(b) | 12 finite points plus O; group order 13 |',
'| 2021–22 Q2(c) | DH public values 40,248; shared secret 160 |',
'| 2019–20 Q2(b) | $2^{70}$ passwords; mean $\\approx18.7$ million years at $10^6$ guesses/s |',
'| 2019–20 Q7(b) | x^8=9 mod 13: 2,3,10,11; x²=2: none; 3^128 mod 7=2 |',
'| 2019–20 Q7(c) | Totients A: 8200,3200; B: 160,64; ciphertext 130 |',
'| 2018–19 Q5(a) | DITECTIVE → VSBYUVGYZ (printed key is noninvertible) |',
'| 2018–19 Q6(a) | P-box labels 36720541; S-box sequence 21560374 |','']
for d in names:
 arr=bydeck[d]
 if not arr:continue
 lines += [f'## {names[d]}','',f'Primary source: [{Path(sourcefiles[d]).name}](<{quote(os.path.relpath(ROOT/sourcefiles[d],BASE))}>)','']
 for q in arr:
  sid=q['solution_id'];key=q['session']+'|'+q['question']
  lines += [f'<a id="{sid.lower()}"></a>',f'### {sid} · {q["session"]} · Q{q["question"]}','',f'**{q["exact_skill"]} · {q["marks"]} marks**','',
  f'Original: [root question PDF, page {q["pdf_page"]}](../../CSE405-Security_Merged.pdf#page={q["pdf_page"]}). Sitting date: {q["sitting_date"]}.','',
  '> **Question summary:** '+q['question_paraphrase'],'',answers[key],'']
lines += ['## Review checklist','',
'- For a numerical answer: declare conventions, show intermediate steps, reduce modulo the right modulus, then check by inversion/substitution.','- For a security claim: identify what the attacker knows/can change, what is trusted, the exact guarantee, and any freshness requirement.','- For SQL injection: expand the final statement; quote termination and comments must match the given query.','- For a browser attack: label the script origin, destination server, victim cookie and action; do not assume SOP blocks every cross-origin request.','- For a fix: explain the mechanism. “Use encryption” does not repair identity trust, and “use a MAC” does not automatically prevent replay.','',
'## Further primary references','',
'The local exam papers and supplied lectures/notes define the questions. These references clarify selected algorithm/interface details; the worked algebra and toy examples in this guide are derived for the specific papers.','',
'- [RFC 2104: HMAC definition, block-length key handling](https://www.rfc-editor.org/rfc/rfc2104)','- [NIST SP 800-90A Rev. 1: HMAC-DRBG algorithm](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf)','- [RFC 5246: historical TLS 1.2 handshake and record protection](https://www.rfc-editor.org/rfc/rfc5246)','- [RFC 5869: HKDF](https://www.rfc-editor.org/rfc/rfc5869)','- [Stanford: quadratic residues](https://crypto.stanford.edu/pbc/notes/numbertheory/qr.html)','- [PHP mysqli: prepared statements](https://www.php.net/manual/en/mysqli.quickstart.prepared-statements.php)','- [OWASP: SQL injection prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)','- [OWASP: clickjacking defenses](https://cheatsheetseries.owasp.org/cheatsheets/Clickjacking_Defense_Cheat_Sheet.html)','- [OWASP: CSRF prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)','']
md='\n'.join(lines)
(BASE/'SOLUTIONS.md').write_text(md)
body=render_markdown(md)
soup=BeautifulSoup(body,'html.parser')
native_math=render_native_math(soup)
# Scalable/embedded diagrams make the HTML a standalone offline artifact.
for img_no,img in enumerate(soup.find_all('img')):
 p=BASE/img['src']
 if not p.exists():raise FileNotFoundError(p)
 if p.suffix=='.svg':
  raw_svg=p.read_text()
  for old in re.findall(r'\bid="([^"]+)"',raw_svg):
   new=f'fig-{img_no}-'+old
   raw_svg=raw_svg.replace('id="'+old+'"','id="'+new+'"').replace('url(#'+old+')','url(#'+new+')').replace('href="#'+old+'"','href="#'+new+'"')
  svg=BeautifulSoup(raw_svg[raw_svg.index('<svg'):],'html.parser').find('svg')
  svg['role']='img';svg['aria-label']=img.get('alt','Diagram');svg['class']='diagram';img.replace_with(svg)
 else:img['src']='data:image/png;base64,'+base64.b64encode(p.read_bytes()).decode()
# Each heading+answer becomes a filterable section, preserving its original anchor.
for h in list(soup.find_all('h3')):
 sec=soup.new_tag('section');sec['class']='question'
 anchor=h.find_previous_sibling('p')
 # Explicit anchor is a direct <a>; section filtering need not move it.
 h.insert_before(sec);node=h
 while node:
  nxt=node.next_sibling
  if node!=h and getattr(node,'name',None) in ['h2','h3','a']:break
  sec.append(node);node=nxt
css='''
:root{--ink:#1c3047;--blue:#28557e;--muted:#5a6b7c;--line:#dce4eb}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#edf2f6;color:var(--ink);font:16px/1.65 system-ui,sans-serif}nav{position:fixed;inset:0 auto 0 0;width:280px;background:#172c44;color:#fff;padding:24px 18px;overflow:auto}nav h2{font-size:18px;color:white}nav a{color:#d8e8f5;text-decoration:none;display:block;font-size:12px;line-height:1.45;padding:5px 0}nav input{width:100%;padding:10px;border:0;border-radius:5px;margin:8px 0 16px}nav button{border:1px solid #9eb6c8;color:white;background:transparent;padding:7px 10px;border-radius:4px;cursor:pointer}main{max-width:1100px;margin:0 auto 0 300px;padding:42px 48px;background:white;min-height:100vh}h1{font-size:36px;line-height:1.2;letter-spacing:-.8px}h2{margin-top:55px;border-bottom:2px solid var(--line);padding-bottom:10px;color:var(--blue)}h3{margin-top:32px;font-size:23px;line-height:1.35}a{color:#225c8d}p,li{overflow-wrap:anywhere}blockquote{margin:20px 0;padding:14px 18px;border-left:4px solid #87a8c5;background:#f2f6f9;font-size:14px;color:#465b6b}pre{font:13px/1.55 'DejaVu Sans Mono',monospace;background:#f3f6f8;border:1px solid var(--line);padding:15px;border-radius:5px;overflow:auto;white-space:pre-wrap;overflow-wrap:anywhere}code{font: .88em 'DejaVu Sans Mono',monospace}table{border-collapse:collapse;width:100%;margin:20px 0;font-size:13px}th,td{text-align:left;vertical-align:top;padding:9px;border:1px solid var(--line)}th{background:#eaf1f7}tbody tr:nth-child(even){background:#f9fbfc}.math-display{overflow-x:auto;margin:1.2em 0;padding:.3em 0}.math-inline{white-space:nowrap}svg.diagram,img{display:block;max-width:100%;height:auto;margin:24px auto}section.question{padding-bottom:25px;border-bottom:1px solid var(--line)}.question p:has(>strong:first-child){scroll-margin-top:20px}.hidden{display:none!important}.hint{font-size:12px;color:#adc5d8}footer{margin-top:40px;font-size:12px;color:var(--muted)}@media(max-width:900px){nav{position:static;width:auto;max-height:350px}main{margin:0;padding:24px}h1{font-size:29px}}@media print{@page{size:A4;margin:18mm}nav{display:none}main{margin:0;max-width:none;padding:0}body{background:white;font-size:10.5pt}h2{break-before:page}h3{break-after:avoid}pre,table,svg{break-inside:avoid}a{color:inherit}section.question{border:0}.hidden{display:block!important}}
'''
navlinks=''.join(f'<a href="#{q["solution_id"].lower()}">{q["solution_id"]} · {q["session"]} Q{q["question"]}<br>{html.escape(q["exact_skill"])}</a>' for q in qs)
js='''document.querySelector('nav').addEventListener('click',e=>{if(e.target.closest('a')){document.getElementById('search').value='';document.querySelectorAll('section.question').forEach(x=>x.classList.remove('hidden'));}});document.getElementById('search').addEventListener('input',e=>{const term=e.target.value.toLowerCase();document.querySelectorAll('section.question').forEach(x=>x.classList.toggle('hidden',!x.textContent.toLowerCase().includes(term)));});'''
page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>CSE 405 — 73 Worked Solutions</title><style>'+css+'</style><script>window.MathJax={tex:{inlineMath:[["\\(","\\)"]],displayMath:[["\\[","\\]"]]},options:{skipHtmlTags:["script","noscript","style","textarea","pre","code"]}};</script><script defer src="https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-mml-chtml.js"></script></head><body><nav><h2>CSE 405 · Solutions</h2><p class="hint">73 answers · LaTeX math</p><input id="search" aria-label="Search solutions" placeholder="Search answers or topics…"><button onclick="window.print()">Print / save PDF</button>'+navlinks+'</nav><main>'+str(soup)+'<footer>Sources and assumptions are recorded in the individual answers. This is a study guide, not an official marking scheme.</footer></main><script>'+js+'</script></body></html>'
if native_math:
 page=re.sub(r'<script>window.MathJax=.*?</script><script defer src=.*?</script>','',page,flags=re.S)
 page=page.replace('MathJax equation rendering','native MathML equation rendering')
(BASE/'SOLUTIONS.html').write_text(page)
(BASE/'solutions_index.json').write_text(json.dumps([dict(solution_id=q['solution_id'],session=q['session'],question=q['question'],page_in_original=q['pdf_page'],topics=q['topics'],primary_deck=topicdeck[q['topics'][0]]) for q in qs],indent=2,ensure_ascii=False))
# Clean HTML for the ODT exporter; all content remains present and no scripts run.
(SECTION/'_build/render_body.html').write_text(body)
print('Wrote all',len(answers),'answers;',len(md.split()),'words;',len(md),'characters')
