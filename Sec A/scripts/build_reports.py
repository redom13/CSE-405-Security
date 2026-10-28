"""Build reproducible Sec A syllabus, source inventory and exam-frequency reports."""
from pathlib import Path
import json,csv,subprocess,re
from urllib.parse import quote
from collections import Counter
from catalog import ROOT,SECTION,DECKS,TOPICS,EXAMS
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
 inv.append(dict(file=file.relative_to(ROOT).as_posix(),pages=n,text_characters=len(raw),text_file=text.relative_to(ROOT).as_posix(),short_pages=[i+1 for i,p in enumerate(raw.split('\f')[:-1]) if len(p.strip())<80]))
(OUT/'inventory.json').write_text(json.dumps(inv,indent=2)+'\n')
(OUT/'question_index.json').write_text(json.dumps(questions,indent=2,ensure_ascii=False)+'\n')
with (OUT/'question_index.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(questions[0]));w.writeheader()
 for q in questions:w.writerow({**q,'topics':'; '.join(q['topics'])})
notes=[('1–9','Course introduction, adversarial reasoning, threat models, social engineering, malware/ransomware case discussions'),('10–18','CIA/AAA, attacks, ten principles, access-control models, cryptographic overview and password calculations'),('19–23','Locks, cards/QR/SIM/GSM/RFID, biometrics and physical emanations'),('24–30','Memory layout, unsafe C, stack overflow, assessment tools, privileges and canary sketch'),('31–36','OS concepts, real/effective identity, boot/live media, hibernation, logging, password attacks and salts'),('37–40','ACLs, file/directory permissions, setuid/setgid/sticky, chmod and identity commands'),('41–49','Insiders/backdoors/logic bombs, viruses, encryption/mutation, anti-debugging and detection'),('50–57','Worms/SI model, botnets/honeypots, rootkits/hooking, Trojans, malware economics and countermeasures'),('58–65','ARP, switch tables, MAC flooding, DHCP starvation/spoofing and defenses'),('66–71','TCP hijacking, coordinated spoofing, DoS/Smurf/SYN cookies, traceback and brief tunnel/VPN notes'),('72–80','DNS hierarchy/messages/cache poisoning, repeated queries, source-port entropy, DNSSEC and squatting')]
lines=['# Sec A syllabus from the supplied slides and notes','',f'**11 slide decks, {sum(d[2] for d in DECKS.values())} physical PDF pages; one 80-page scanned notebook.** This is a reconstruction of the supplied material, not an official instructor-issued exclusion list.','',
'Page numbers below refer to physical PDF pages, beginning at 1. Several PDFs contain two printed slides per PDF page. The handwritten notebook was reviewed visually; its extracted text is empty. The Buffer Overflow PDF has corrupt text glyphs, so its rendered pages were checked as well.','',
'## Complete slide-deck reading map','']
for key,(file,title,n,parts) in DECKS.items():
 lines += [f'## {title}','',link(SECTION/'slides'/file,file),f' · {n} PDF pages.','', '| PDF pages | Topics |','|---|---|']
 for a,b,desc in parts:lines.append(f'| {a}–{b} | {desc} |')
 lines.append('')
lines+=['## Handwritten notes: page-by-page range map','',link(SECTION/'notes/CSE-405-Till-Mid.pdf','CSE-405-Till-Mid.pdf'),'', '| PDF pages | Material |','|---|---|']
for p,desc in notes:lines.append(f'| {p} | {desc} |')
lines+=['','The notebook stops at DNS and is titled “Till Mid.” It does not supply a complete handwritten counterpart for the crypto, web or firewall/IDS decks. Do not mistake a missing handwritten chapter for a syllabus exclusion.','',
'## Teaching-source cautions and extensions','',
'- **Salts:** the OS slides discuss hiding/encrypting a salt and multiplying a guessing space. Ordinary password salts are public and unique; they prevent shared precomputation/cross-account reuse. They do not add secret entropy to a single known-salt password. A separate secret pepper has a different threat model.','- **Hashes and MACs:** MD5/SHA-1 appear as historical examples. A bare digest is not a MAC, and the intro shorthand H(K||M) is not a universally safe MAC construction. Use the explicit HMAC reasoning in relevant answers.','- **Hash security properties:** collision resistance and preimage resistance are different properties; the equivalence shorthand on Crypto PDF p. 49 is incorrect. Three-key 3DES has 168 key bits, but a generic meet-in-the-middle upper bound is about 112 bits, so do not copy the nominal key length as effective strength.',
'- **Signatures:** “encrypt with the private key” describes a textbook RSA analogy, not every signature scheme or a safe raw-RSA implementation.','- **Web protocols:** the deck simplifies HTTPS as server-only authentication; TLS can also authenticate clients when configured. Input blacklists and user browsing habits are not substitutes for parameter binding, output encoding and deliberate CSRF defenses.',
'- **DNSSEC:** authentication requires a chain to an already trusted key, not simply accepting the DNSKEY that accompanies a reply. DNS-over-TLS protects its particular transport hop; it does not automatically protect all recursive lookups. Historical deployment statements are course history.','- **Packet capture and switching:** promiscuous mode does not force a switch to deliver all VLAN traffic; unknown-unicast flooding is conditional and remains scoped by switching/VLAN behavior.','- **Memory attacks:** exact offsets, local ordering, ABI and compiler protections matter. The 2018–19 stack question explicitly uses an artificial layout/instruction-size model. The deck explicitly includes a random canary on PDF p. 8. Format strings, return-to-libc and detailed ASLR/CFI mechanisms are related extensions.','- **Locks:** basic pin-tumbler operation is explicit; master-wafer combinatorics/geometric design in the old paper extends those slides.','- **IDS:** the four alarm outcomes are explicit. Base-rate calculations, PIDS specialization, statistical audit models and forensic custody need supplementary explanation supplied in the solutions.','- **Cryptographic overlap:** Sec A teaches DES/AES, CBC, modular arithmetic, RSA, DH, hashes/MACs/signatures and CA trust. Sec B has more extensive classical ciphers, PRNGs, ElGamal, modes, cookie policy and web-attack treatments. Questions are mapped by content in both sections, not by their printed Section A/B label.','',
'## Study material versus exam frequency','',
'Use [the question analysis](FINAL_EXAM_TOPIC_ANALYSIS.md) for the ranked evidence and all individual questions. A topic with no standalone question is still part of this file-derived syllabus. Core unqueried details include GSM challenge–response, QR/barcode comparison, RFID operation, extended ACL masks/default inheritance, NTFS ACE ordering/move-copy rules, most OS scheduling/VM/boot details, malware-analysis/quarantine mechanisms, routine DNS resource-record/hierarchy exercises and the VPN deployment variants.','']
(OUT/'SYLLABUS.md').write_text('\n'.join(lines))
bytopic={t:[q for q in questions if t in q['topics']] for t in TOPICS}
rank=sorted(TOPICS,key=lambda t:(-len(bytopic[t]),-len({q['session'] for q in bytopic[t]}),TOPICS[t][0]))
bydeck={d:[q for q in questions if any(TOPICS[t][1]==d for t in q['topics'])] for d in DECKS}
lines=['# Sec A final-exam topic analysis','',f'**{len(questions)} distinct mapped printed subquestions across six papers.** [CSV](question_index.csv) · [JSON](question_index.json) · [Worked solutions](../solutions/SOLUTIONS.pdf).','',
'## Scope and counting','',
'Both printed sections of every paper were checked because teaching assignments changed between years. One occurrence is a printed lettered subquestion; the unlettered 2018–19 Q10 is one whole question. Internal tasks remain together. A mixed question counts once per explicitly examined topic and once per related deck. Totals across topics/decks therefore cannot be added. Optional choices are included and identified; marks belong to the entire printed subquestion.','',
'Question summaries are paraphrases. Open the original PDF page for exact wording, code and diagrams. “Related/extension” means a relevant foundation is supplied but some requested mechanism or calculation requires more than the local slides; the table exposes these counts so they are not mistaken for direct coverage. A mixed answer is retained in full even if only part maps to Sec A. No frequency predicts a future exam.','',
'| Academic session | Sitting date | Root PDF pages |','|---|---|---|']
for y,(date,a,b) in EXAMS.items():lines.append(f'| {y} | {date} | {a}–{b} |')
lines+=['','## Topics ranked by printed-question frequency','','| Rank | Exact topic group | All mapped | Direct | Related / extension | Papers / 6 | Main deck |','|---:|---|---:|---:|---:|---:|---|']
for i,t in enumerate(rank,1):
 arr=bytopic[t];direct=sum(q['coverage']=='direct' for q in arr)
 lines.append(f'| {i} | [{TOPICS[t][0]}](#{t}) | {len(arr)} | {direct} | {len(arr)-direct} | {len({q["session"] for q in arr})}/6 | {DECKS[TOPICS[t][1]][1]} |')
lines+=['','A question-level extension flag applies to the whole mixed question. It does not claim that every linked topic is missing from the slides. Consult the per-question note for the particular missing task.','',
'## Slide decks ranked by unique mapped questions','','| Deck | Distinct questions | Papers / 6 |','|---|---:|---:|']
for d in sorted(DECKS,key=lambda d:-len(bydeck[d])):lines.append(f'| {DECKS[d][1]} | {len(bydeck[d])} | {len({q["session"] for q in bydeck[d]})}/6 |')
lines+=['','## Questions under slide deck → exact topic','']
for d,(file,title,n,_) in DECKS.items():
 lines += [f'## {title}','',link(SECTION/'slides'/file,file),'']
 for t in (t for t in rank if TOPICS[t][1]==d):
  title,_,pages,np=TOPICS[t];arr=bytopic[t]
  lines += [f'<a id="{t}"></a>',f'### {title} — {len(arr)} questions',f'\n**Study:** deck PDF pp. {pages}; handwritten-note PDF pp. {np}.','']
  if not arr:lines+=['No standalone mapped question in these six papers.','']
  for q in arr:
   lines += [f'**{q["session"]} · Q{q["question"]} · {q["marks"]} marks · {q["coverage"]}** · '+link(ROOT/'CSE405-Security_Merged.pdf',f'paper p. {q["pdf_page"]}',q['pdf_page'])+f' · [Solution {q["solution_id"]}](../solutions/SOLUTIONS.html#{q["solution_id"].lower()})','',f'**Exact task:** {q["exact_skill"]}.','',q['question_paraphrase'],'']
   if q['coverage_note']:lines+=['**Coverage / reading note:** '+q['coverage_note'],'']
lines+=['## Unmapped gaps and section boundaries','','These are not added to the rankings or silently included among the solved index. The source syllabus does not fully develop them.','', '| Session | Questions | Paper pages | Gap |','|---|---|---|---|']
for row in GAPS:lines.append('| '+' | '.join(row)+' |')
lines+=['','## Evidence-based study sequence','','Start with the high-frequency topics in the table, but also account for marks and task type. Practice diagram-driven network reasoning, then malware distinctions and IDS probability; rehearse stack/permission calculations separately. Work the shared crypto/web questions using Sec A’s page map, consulting Sec B for the explicitly labeled extensions. An optional three-mark concept is not the same study workload as a twenty-mark protocol analysis.','']
(OUT/'FINAL_EXAM_TOPIC_ANALYSIS.md').write_text('\n'.join(lines))
(OUT/'topic_frequencies.json').write_text(json.dumps([dict(topic=t,title=TOPICS[t][0],deck=TOPICS[t][1],questions=len(bytopic[t]),papers=len({q['session'] for q in bytopic[t]}),direct=sum(q['coverage']=='direct' for q in bytopic[t])) for t in rank],indent=2)+'\n')
print('Sec A reports:',len(questions),'questions;',len(inv),'source PDFs')
for t in rank[:10]:print(len(bytopic[t]),TOPICS[t][0])

# Cross-section labels prevent adding overlapping counts as distinct questions.
b_index=json.loads((ROOT/'Sec B/analysis/question_index.json').read_text())
a_map={(q['session'],q['question']):q for q in questions}
b_map={(q['session'],q['question']):dict(q,solution_id=f'S{i:02d}') for i,q in enumerate(b_index,1)}
keys=sorted(set(a_map)|set(b_map),key=lambda k:(list(EXAMS).index(k[0]),int(k[1].split('(')[0]),k[1]))
with (OUT/'CROSS_SECTION_COVERAGE.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['Academic session','Question','Original PDF page','Sec A solution','Sec B solution'])
 for k in keys:
  aq=a_map.get(k,{});bq=b_map.get(k,{})
  w.writerow([*k,(aq or bq)['pdf_page'],aq.get('solution_id',''),bq.get('solution_id','')])
print('Cross-section coverage:',len(keys),'distinct questions;',len(set(a_map)&set(b_map)),'shared.')
