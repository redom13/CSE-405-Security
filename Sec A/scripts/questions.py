"""Sec A question set with explicit section boundaries; no Sec B answer imports."""
import json,sys
from catalog import SECTION,EXAMS,TOPICS,EXCLUDED_TOPIC_KEYS
sys.path.insert(0,str(SECTION/'solutions/src'))
from new_questions import questions as authored_questions,answers as authored_answers

questions=[dict(q) for q in authored_questions]
answers=dict(authored_answers)
# Retain only Sec A components of mixed printed subquestions.
component_notes={
 '2023–24|3(a)': 'Covers the four network-defense cases. The reflected-XSS case in the original five-part question belongs to Sec B and is excluded. The 10 printed marks cover all five cases; no per-case allocation is supplied.',
 '2018–19|4(b)': 'Covers the DNS/pharming component of the printed comparison. The phishing topic is assigned to Sec B. The printed 8 marks are for the complete comparison, not this component alone.',
 '2018–19|8(b)': 'Covers only options (i) Faraday cage and (iii) OS impersonation token, 3 marks each. Options (ii) blind SQL injection and (iv) homograph attack remain in Sec B. The printed 9 marks require any three choices.'
}
# Stable identifiers preserve existing bookmarks despite removing unrelated answers.
id_file=SECTION/'scripts/solution_ids.json'
ids=json.loads(id_file.read_text())
for q in questions:
 key=q['session']+'|'+q['question']
 q['sitting_date']=EXAMS[q['session']][0]
 # In each supplied paper questions 1–4 are printed in A, later numbers in B.
 # Record that location for the audit; never use it to select the current section.
 q['printed_section']='A' if int(q['question'].split('(')[0])<=4 else 'B'
 assert q['topics'] and all(t in TOPICS for t in q['topics']),q
 assert not set(q['topics']) & set(EXCLUDED_TOPIC_KEYS),q
 q['scope']='sec_a_components' if key in component_notes else 'sec_a'
 q['scope_note']=component_notes.get(key,'')
 if key=='2018–19|8(b)':q['in_scope_marks']=6
 else:q['in_scope_marks']=q['marks'] if q['scope']=='sec_a' else None
 q['solution_id']=ids[key]
questions.sort(key=lambda q:(list(EXAMS).index(q['session']),int(q['question'].split('(')[0]),q['question']))
keys={q['session']+'|'+q['question'] for q in questions}
assert len(keys)==len(questions)
assert keys==set(answers)==set(ids)
assert len({q['solution_id'] for q in questions})==len(questions)
# Physical/system extensions belong to Sec A; crypto/web topics are not listed as gaps here.
GAPS=[
 ('System security','Format-string reads/writes and return-to-libc need more detail than the eight-page overflow deck; the worked answers state the ABI/layout assumptions.'),
 ('Physical security','Master-wafer counting/design extends the basic pin-tumbler slides.'),
 ('Detection and response','Bayesian base rates, statistical IDS and forensic acquisition/custody extend the source overview and are explained in the corresponding Sec A answers.')
]
