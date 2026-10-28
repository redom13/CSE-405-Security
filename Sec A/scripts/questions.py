"""Combine newly solved questions with overlapping, previously checked Sec B answers."""
import json,runpy,sys
from catalog import ROOT,SECTION,EXAMS,TOPICS
sys.path.insert(0,str(SECTION/'solutions/src'))
from new_questions import questions as new_questions,answers as new_answers
questions=[dict(q) for q in new_questions]
answers=dict(new_answers)
# Same printed questions, now attributed to Sec A's actual teaching sources.
# Preserve lettered subquestions and solve all tasks even when only part maps here.
reused={
'2023–24':{'5(a)':'goals mac phishing','5(b)':'modes','6(a)':'dh','7(b)':'rsa','7(c)':'signature rsa','8(a)':'mac','8(b)':'csrf','8(c)':'sql','8(d)':'xss','1(c)':'cert','4(c)':'web cert'},
'2022–23':{'5(a)':'modes','5(b)':'mac hash','5(c)':'csrf xss','6(a)':'dh signature','7(a)':'csrf','7(c)':'xss','8(a)':'mac hash','8(b)':'phishing','8(c)':'phishing','2(a)':'password'},
'2021–22':{'1(d)':'keymodels','2(a)':'goals','2(c)':'dh','2(d)':'modes','3(b)':'hash mac signature','3(c)':'hash','3(d)':'keymodels signature','4(b)':'mac','4(c)':'block','4(d)':'block','7(b)':'phishing','7(c)':'cert'},
'2020–21':{'5(a)':'mac','5(b)':'sql','6(a)':'csrf xss','8(b)':'hash','8(c)':'csrf'},
'2019–20':{'1(a)':'signature','1(c)':'password','2(b)':'password','6(b)':'hash','7(a)':'number','7(b)':'number','7(c)':'rsa','8(a)':'signature hash','8(b)':'dh'},
'2018–19':{'1(a)':'cert','1(d)':'signature','4(b)':'dns phishing','5(b)':'modes','6(a)':'block','8(b)':'emanations sql phishing','11(a)':'sql','11(b)':'sql','12(a)':'xss'}
}
# Cookie-domain/path matrices are not in Sec A's decks; keep as gaps, not forced into CSRF.
reused['2023–24'].pop('8(b)')
# The session-expiry question uses a web-session mechanism not developed here; track as gap.
reused['2020–21'].pop('8(c)')
base=json.loads((ROOT/'Sec B/analysis/question_index.json').read_text())
all_old={}
for p in sorted((ROOT/'Sec B/solutions/src').glob('answers_*.py')):
 for k,v in runpy.run_path(str(p))['answers'].items():
  if k in all_old:raise ValueError('duplicate Sec B answer '+k)
  all_old[k]=v
extra_notes={
 '2023–24|8(a)':'MAC/encryption foundations are taught; authenticated-encryption composition is a related extension.',
 '2023–24|5(a)':'Only the CIA and MAC choices are explicit in Sec A; confusion/diffusion, homographs and clickjacking extend the decks. The 15 marks belong to the whole optional subquestion.',
 '2023–24|5(b)':'Sec A teaches CBC, not this custom two-IV construction; a related mode-analysis extension, not a direct CBC question.',
 '2023–24|4(c)':'HTTPS/certificates and DH/RSA are taught; full historical TLS handshake/record details are supplementary.',
 '2022–23|5(a)':'CBC is explicit; ECB/CTR, IND-CPA and nonce-comparison details extend this deck.',
 '2022–23|5(b)':'MAC/hash/encryption are taught; formal composition security is supplementary.',
 '2022–23|5(c)':'XSS/CSRF are explicit; detailed cookie attributes/policy are supplementary.',
 '2022–23|8(b)':'Phishing and authentication factors are taught; live SMS relay is an application.',
 '2022–23|8(c)':'Phishing is taught, but the iframe clickjacking cases are a UI-attack extension.',
 '2021–22|1(d)':'Caesar/symmetric encryption are explicit; the affine-composition half is supplementary.',
 '2021–22|4(b)':'MAC is explicit; the detailed HMAC construction is supplementary.',
 '2021–22|4(c)':'DES/3DES are explicit; 5DES meet-in-the-middle analysis is supplementary.',
 '2021–22|7(b)':'Phishing is explicit; clickjacking is supplementary.',
 '2020–21|5(a)':'MACs and message integrity are explicit; a complete authenticated UDP protocol with replay tracking extends the decks.',
 '2019–20|6(b)':'Hash properties are explicit; detailed Merkle–Damgård is supplementary.',
 '2019–20|8(a)':'Hash/signature birthday attacks are related; ElGamal encryption is not developed by the supplied Sec A decks. Full answer retained for the mixed subquestion.',
 '2018–19|8(b)':'One optional 9-mark subquestion. Faraday cage is explicit; blind SQLi/homographs extend the web deck, and OS impersonation-token details are supplementary. Do not allocate all 9 marks to every choice.'}
for q in base:
 tags=reused.get(q['session'],{}).get(q['question'])
 if not tags:continue
 item=dict(q);item['topics']=tags.split();key=q['session']+'|'+q['question']
 if key in extra_notes:item['coverage']='partial';item['coverage_note']=extra_notes[key]
 questions.append(item);answers[key]=all_old[key].strip()
for q in questions:
 q['sitting_date']=EXAMS[q['session']][0]
 assert all(t in TOPICS for t in q['topics']),q
 # Every mixed task is explicitly described, rather than pretending every task is taught.
 if q['coverage']=='partial' and not q['coverage_note']:q['coverage_note']='Related application/prerequisites are in Sec A; the complete answer needs the extension stated in the solution.'
questions.sort(key=lambda q:(list(EXAMS).index(q['session']),int(q['question'].split('(')[0]),q['question']))
keys=[q['session']+'|'+q['question'] for q in questions]
assert len(keys)==len(set(keys))
assert set(keys)==set(answers)
for i,q in enumerate(questions,1):q['solution_id']=f'A{i:03d}'
GAPS=[
('2023–24','6(b), 7(a), 8(b)','7–9','Affine key recovery; ElGamal encryption; detailed cookie matching. Sec B covers these.'),
('2022–23','6(c), 7(b)','13','HMAC-DRBG (Sec B) and Tor/onion routing (not developed in either supplied section).'),
('2021–22','1(c), 2(b)','15','Hill matrices (Sec B) and elliptic-curve arithmetic (worked Sec B extension).'),
('2020–21','6(b), 7(a), 7(b), 8(c)','20–21','ElGamal signatures; Caesar/Hill attack; cookie matrix; session-token revocation (Sec B).'),
('2019–20','6(a)','24','OTP and the transposition/Hill connection (Sec B).'),
('2018–19','5(a), 13','27, 31','Hill numerical encryption (Sec B); quantum key distribution table (not developed in either section).')]
