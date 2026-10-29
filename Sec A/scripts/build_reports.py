"""Build Sec A reports using topic scope across both printed exam sections."""
from pathlib import Path
import json,csv,subprocess,re
from urllib.parse import quote
from catalog import ROOT,SECTION,DECKS,TOPICS,EXAMS,EXCLUDED_INPUTS,EXCLUDED_INTRO_PAGES
from questions import questions,GAPS
OUT=SECTION/'analysis';OUT.mkdir(exist_ok=True)
CACHE=SECTION/'_build/extracted';CACHE.mkdir(parents=True,exist_ok=True)
def link(path,label,page=None):
 from os.path import relpath
 url=quote(relpath(path,OUT))+(f'#page={page}' if page else '')
 return f'[{label}](<{url}>)'
inv=[]
for file in sorted((SECTION/'slides').glob('*.pdf'))+sorted((SECTION/'notes').glob('*.pdf')):
 text=CACHE/(file.stem+'.txt')
 subprocess.run(['pdftotext','-layout',str(file),str(text)],check=True)
 info=subprocess.check_output(['pdfinfo',str(file)],text=True)
 n=int(re.search(r'^Pages:\s+(\d+)',info,re.M)[1]);raw=text.read_text()
 inv.append(dict(file=file.relative_to(ROOT).as_posix(),pages=n,in_scope=file.name not in EXCLUDED_INPUTS,text_characters=len(raw),text_file=text.relative_to(ROOT).as_posix(),short_pages=[i+1 for i,p in enumerate(raw.split('\f')[:-1]) if len(p.strip())<80]))
(OUT/'inventory.json').write_text(json.dumps(inv,indent=2)+'\n')
(OUT/'question_index.json').write_text(json.dumps(questions,indent=2,ensure_ascii=False)+'\n')
fields=list(dict.fromkeys(k for q in questions for k in q))
with (OUT/'question_index.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for q in questions:w.writerow({**q,'topics':'; '.join(q['topics'])})
notes=[('1–9','Adversarial reasoning, threat models, human factors, malware/ransomware case discussions'),('10–16','CIA/AAA, threats, ten principles and access-control models'),('19–23','Locks, cards/QR/SIM/GSM/RFID, biometrics and physical emanations'),('24–30','Memory layout, unsafe C, stack overflow, assessment tools, privileges and canary sketch'),('31–36','OS concepts, real/effective identity, boot/live media, hibernation, logging and OS password-file/salt handling'),('37–40','ACLs, file/directory permissions, setuid/setgid/sticky, chmod and identity commands'),('41–49','Insiders/backdoors/logic bombs, viruses, encryption/mutation, anti-debugging and detection'),('50–57','Worms/SI model, botnets/honeypots, rootkits/hooking, Trojans, malware economics and countermeasures'),('58–65','ARP, switch tables, MAC flooding, DHCP starvation/spoofing and defenses'),('66–71','TCP hijacking, coordinated spoofing, DoS/Smurf/SYN cookies, traceback and brief tunnel/VPN notes'),('72–80','DNS hierarchy/messages/cache poisoning, source-port entropy, DNSSEC and squatting')]
lines=['# Sec A syllabus','',
f'**{len(DECKS)} in-scope decks ({sum(d[2] for d in DECKS.values())} physical PDF pages), with selected topics from the 80-page handwritten notebook.**','',
'Sec A covers foundations, physical authentication, operating systems, filesystem access, memory attacks, malware and network/DNS/IDS defenses. The source files also contain older material assigned to Sec B; file placement does not add that material to Sec A.','',
'Cryptographic algorithms, number-theory exercises, password-guessing/recovery question sets and browser/application attack chapters are excluded from this syllabus and its frequency/solution guides. OS account/salt handling, DNSSEC, IPsec and network identity checks remain where they are part of Sec A system/network security.','',
'Page numbers below are physical PDF pages, beginning at 1; several PDFs contain two printed slides per page. The handwritten notebook was reviewed visually; its text extraction is empty. The Buffer Overflow PDF has corrupt glyph extraction and was checked as rendered pages.','',
'## In-scope slide decks','']
for key,(file,title,n,parts) in DECKS.items():
 lines += [f'## {title}','',link(SECTION/'slides'/file,file)+f' · {n} PDF pages.','', '| PDF pages | Sec A topics |','|---|---|']
 for a,b,desc in parts:lines.append(f'| {a}–{b} | {desc} |')
 if key=='intro':lines+=['','**Excluded range:** '+EXCLUDED_INTRO_PAGES]
 lines.append('')
lines+=['## Handwritten notes: Sec A reading map','',link(SECTION/'notes/CSE-405-Till-Mid.pdf','CSE-405-Till-Mid.pdf'),'', '| PDF pages | Sec A material |','|---|---|']
for p,desc in notes:lines.append(f'| {p} | {desc} |')
lines+=['','The crypto recap and standalone guessing calculations on notebook pp. 17–18 are excluded. Any such examples on otherwise included pages are background, not additional Sec A exam topics. The notebook ends at DNS; use the firewall/IDS deck for its later material.','',
'## Preserved files outside this study scope','',
'The following PDFs remain untouched as supplied references. They do not appear as Sec A teaching chapters, ranked topics or standalone worked solutions.','']
for name,reason in EXCLUDED_INPUTS.items():lines.append('- '+link(SECTION/'slides'/name,name)+' — '+reason)
lines+=['','## Source cautions and extensions','',
'- OS salts are normally public and unique. They prevent shared precomputation and cross-account reuse; they do not add secret entropy to a known-salt account.',
'- DNSSEC needs a validated chain to an already trusted key. Protecting one DNS transport hop does not automatically authenticate every recursive lookup.',
'- Promiscuous packet capture does not force a switch to deliver all VLAN traffic; MAC-table exhaustion and unknown-unicast behavior are conditional.',
'- Memory offsets depend on ABI/compiler/layout. The old stack exercise stipulates an artificial instruction-size model. Random canaries are explicit on overflow PDF p. 8; format strings and return-to-libc need additional explanation.',
'- Master-wafer lock design, Bayesian IDS base rates and forensic acquisition/custody extend the source overviews; their answers identify the assumptions.',
'', '## Exam preparation','',
'Use [the Sec A frequency report](FINAL_EXAM_TOPIC_ANALYSIS.md) for questions grouped under deck and precise topic. It checks both printed exam sections each year. Foundational details with no standalone mapped question remain part of this reading map—for example GSM/RFID, ACL masks/inheritance, NTFS ACE evaluation, scheduling/VM/boot details, malware quarantine and routine DNS hierarchy exercises.','']
(OUT/'SYLLABUS.md').write_text('\n'.join(lines))
bytopic={t:[q for q in questions if t in q['topics']] for t in TOPICS}
rank=sorted(TOPICS,key=lambda t:(-len(bytopic[t]),-len({q['session'] for q in bytopic[t]}),TOPICS[t][0]))
bydeck={d:[q for q in questions if any(TOPICS[t][1]==d for t in q['topics'])] for d in DECKS}
component_count=sum(q['scope']=='sec_a_components' for q in questions)
lines=['# Sec A final-exam topic analysis','',f'**{len(questions)} mapped printed questions: {len(questions)-component_count} whole-question entries and {component_count} entries limited to Sec A components.** [CSV](question_index.csv) · [JSON](question_index.json) · [Worked solutions](../solutions/SOLUTIONS.pdf).','',
'## Scope and counting','',
'**Assignment is by current topic, not by the printed Section A/B heading. Both printed sections of all six yearly papers are checked.** A Sec A topic printed under Section B in an older year still counts here; a Sec B topic printed under Section A does not.','',
'This report covers foundations, physical/OS/filesystem security, memory attacks, malware and network/DNS/IDS defenses. It excludes the standalone crypto, number-theory, password-guessing/recovery and web-attack sets previously imported from Sec B. The presence of an older recap PDF in the source folder does not change that boundary.','',
'One occurrence is a printed lettered subquestion; unlettered 2018–19 Q10 is one whole question. A mixed question counts once per relevant Sec A topic and once per deck. For a question spanning both current sections, only its Sec A tasks are ranked and solved, and its scope note states what was left out. Optional choices are explicitly labeled. Marks printed beside a parent question must not be attributed wholly to a retained component.','',
'Question summaries are paraphrases. Open the original PDF for exact wording, code and diagrams. “Related/extension” means the Sec A source supplies a foundation but the requested mechanism needs more explanation. This is distinct from a question component assigned to Sec B.','',
'## Coverage of both printed sections, year by year','',
'| Academic session | Sitting date | Root PDF pages | Sec A topics in printed A | Sec A topics in printed B | Total |','|---|---|---|---:|---:|---:|']
audit=[]
for y,(date,a,b) in EXAMS.items():
 arr=[q for q in questions if q['session']==y];na=sum(q['printed_section']=='A' for q in arr);nb=len(arr)-na
 lines.append(f'| {y} | {date} | {a}–{b} | {na} | {nb} | {len(arr)} |')
 audit.append(dict(session=y,printed_A=na,printed_B=nb,total=len(arr)))
with (OUT/'EXAM_SECTION_AUDIT.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['session','printed_A','printed_B','total']);w.writeheader();w.writerows(audit)
lines+=['','The audit counts mapped parent-question occurrences, including the explicitly scoped mixed entries. Source-code queries for permission delegation and DNS authentication remain system/network questions; they do not create SQL-injection or signature-algorithm chapters.','',
'## Topics ranked by printed-question frequency','','| Rank | Exact topic group | All mapped | Direct | Related / extension | Papers / 6 | Main deck |','|---:|---|---:|---:|---:|---:|---|']
for i,t in enumerate(rank,1):
 arr=bytopic[t];direct=sum(q['coverage']=='direct' for q in arr)
 lines.append(f'| {i} | [{TOPICS[t][0]}](#{t}) | {len(arr)} | {direct} | {len(arr)-direct} | {len({q["session"] for q in arr})}/6 | {DECKS[TOPICS[t][1]][1]} |')
lines+=['','## Slide decks ranked by unique mapped questions','','| Deck | Distinct Sec A questions | Papers / 6 |','|---|---:|---:|']
for d in sorted(DECKS,key=lambda d:-len(bydeck[d])):lines.append(f'| {DECKS[d][1]} | {len(bydeck[d])} | {len({q["session"] for q in bydeck[d]})}/6 |')
lines+=['','## Questions under slide deck → exact topic','']
for d,(file,title,n,_) in DECKS.items():
 lines += [f'## {title}','',link(SECTION/'slides'/file,file),'']
 for t in (t for t in rank if TOPICS[t][1]==d):
  title,_,pages,np=TOPICS[t];arr=bytopic[t]
  lines += [f'<a id="{t}"></a>',f'### {title} — {len(arr)} questions',f'\n**Study:** deck PDF pp. {pages}; handwritten-note PDF pp. {np}.','']
  if not arr:lines+=['No standalone mapped question in these six papers.','']
  for q in arr:
   marks_label='printed marks' if q['scope']=='sec_a_components' else 'marks'
   lines += [f'**{q["session"]} · Q{q["question"]} · {q["marks"]} {marks_label} · {q["coverage"]}** · '+link(ROOT/'CSE405-Security_Merged.pdf',f'paper p. {q["pdf_page"]}',q['pdf_page'])+f' · printed Section {q["printed_section"]} · [Solution {q["solution_id"]}](../solutions/SOLUTIONS.html#{q["solution_id"].lower()})','',f'**Exact Sec A task:** {q["exact_skill"]}.','',q['question_paraphrase'],'']
   if q['scope_note']:lines+=['**Section boundary:** '+q['scope_note'],'']
   if q['coverage_note']:lines+=['**Coverage / reading note:** '+q['coverage_note'],'']
lines+=['## Extensions needed for Sec A practice','']
for topic,note in GAPS:lines+=['- **'+topic+':** '+note]
lines+=['','## Study sequence','','Use the rankings together with marks and task type. Practice TCP/DNS and LAN message diagrams, then malware distinctions and IDS probability. Rehearse stack, lock and permission calculations separately. An optional three-mark short note is not the same study workload as a twenty-mark protocol analysis.','']
(OUT/'FINAL_EXAM_TOPIC_ANALYSIS.md').write_text('\n'.join(lines))
(OUT/'topic_frequencies.json').write_text(json.dumps([dict(topic=t,title=TOPICS[t][0],deck=TOPICS[t][1],questions=len(bytopic[t]),papers=len({q['session'] for q in bytopic[t]}),direct=sum(q['coverage']=='direct' for q in bytopic[t])) for t in rank],indent=2)+'\n')
print('Sec A reports:',len(questions),'questions;',len(DECKS),'in-scope decks; both printed sections checked.')
for row in audit:print(row)
