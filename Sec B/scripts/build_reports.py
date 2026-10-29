from pathlib import Path
import json,csv,os
from urllib.parse import quote
from collections import defaultdict
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'Sec B'/'analysis'
inv=json.loads((OUT/'inventory.json').read_text())
files={}
for n in range(1,13): files[f'L{n}']=next(x['file'] for x in inv if x.get('lecture')==n)
files['Notes']='Sec B/notes/handwritten-notes.pdf'
files['Guide']='Sec B/notes/ct4-revision-guide.pdf'
names={'L1':'Lecture 1 — Introduction and Security Principles','L2':'Lecture 2 — Intro to Cryptography','L3':'Lecture 3 — One-Time Pads and Block Ciphers','L4':'Lecture 4 — Block Cipher Modes of Operation','L5':'Lecture 5 — Cryptographic Hashes and MACs','L6':'Lecture 6 — PRNGs and Diffie-Hellman Key Exchange','L7':'Lecture 7 — Public-Key Encryption and Digital Signatures','L8':'Lecture 8 — Certificates, Password Hashing, and Case Studies','L9':'Lecture 9 — Introduction to the Web','L10':'Lecture 10 — Cookies and CSRF','L11':'Lecture 11 — XSS and UI Attacks','L12':'Lecture 12 — SQL Injection and CAPTCHAs','Notes':'Handwritten Sec B notes','Guide':'CT4 Complete Revision Guide'}
def link(file,page=None,label=None):
 return f'[{label or file}](<{quote(os.path.relpath(ROOT/file,OUT))}'+(f'#page={page}' if page else '')+'>)'
def src(key,pages):return f"{link(files[key],int(str(pages).split('–')[0].split(',')[0]),names[key])}, PDF pp. {pages}"
# Every topic has its principal teaching source. Recap slides do not receive duplicate attribution.
topics={
 'principles':('Security principles: least privilege, mediation, human factors, economics and recording','L1','11–60','not developed; use Lecture 1'),
 'securitygoals':('Information-security CIA goals and availability attacks','L1','4–5, 12–17','not developed; use Lecture 1'),
 'classical':('Classical ciphers: Caesar, affine, Hill and transposition','L2','43–68','5–11'),
 'goals':('Cryptographic goals, confusion and diffusion','L2','7–21, 69–70','1–2, 12'),
 'otp':('One-time pads: XOR, correctness and security','L3','6–22','12–14'),
 'block':('Block-cipher internals: DES, AES, S-boxes and P-boxes','L3','25–41','14–15'),
 'modes':('Block-cipher modes: ECB, CBC, CTR and ciphertext modification','L4','5–55','16–20, 66'),
 'hash':('Hash properties, collision/birthday attacks and Merkle–Damgård','L5','13–26, 48','20–23'),
 'mac':('MACs, HMAC and file/message integrity','L5','27–39, 49','24–27'),
 'ae':('Authenticated encryption and encryption/MAC composition','L5','40–47, 50','28–29'),
 'prng':('PRNGs, HMAC-DRBG and rollback resistance','L6','8–28','30–32'),
 'dh':('Diffie–Hellman: calculation, MITM and authentication','L6','41–55, 58','32–36'),
 'ecc':('Elliptic-curve cryptography and ECDH','L6','56–57','36'),
 'rsa':('RSA encryption and its number-theory prerequisites','L7','18–25','35, 41–44'),
 'elgamal':('ElGamal encryption: calculation, correctness and malleability','L7','10–17','37–40'),
 'signature':('Digital signatures: RSA, hash-then-sign, non-repudiation and nonce reuse','L7','27–41','45'),
 'keymodels':('Symmetric versus public-key cryptography and hybrid encryption','L7','6–9, 26','1, 36–37, 45'),
 'cert':('Certificates, certificate authorities and trusted public keys','L8','5–20','46–49'),
 'password':('Password guessing, brute-force calculations and account recovery','L8','23–30','50–52'),
 'cookies':('Cookie policy, attributes and URL/cookie matching','L10','8–29, 71','55–56, 59'),
 'session':('Session authentication, cookie credentials and revocation','L10','37–43, 72','57–60'),
 'csrf':('CSRF attack construction and defenses','L10','44–69, 73–74','60–63'),
 'xss':('Cross-site scripting: stored/reflected XSS and malicious scripts','L11','11–29, 76–77','61–63'),
 'sql':('SQL injection, blind injection and prepared statements','L12','5–40, 57–66','64–65'),
 'ui':('Clickjacking, phishing, homographs and UI attacks','L11','30–68, 78–79','63'),
 'twofa':('SMS two-factor authentication and phishing relay attacks','L11','69–75','63–64'),
}
# Academic session, actual sitting date, inclusive PDF page interval.
exams={
 '2023–24':('06 September 2025',1,10),
 '2022–23':('18 April 2024',11,14),
 '2021–22':('30 October 2023',15,17),
 '2020–21':('25 September 2022',18,21),
 '2019–20':('07 September 2021',22,25),
 '2018–19':('24 October 2019',26,31),
}
qs=[]
def add(year,q,page,marks,tags,skill,question,coverage='direct',note=''):
 qs.append(dict(session=year,sitting_date=exams[year][0],question=q,pdf_page=page,marks=marks,topics=tags.split(),exact_skill=skill,question_paraphrase=question,coverage=coverage,coverage_note=note))
# Faithful question paraphrases from visual inspection of the root PDF. Keep lettered subquestions intact.
add('2023–24','5(a)',7,15,'goals mac ui','Short concepts; answer any three of five','Briefly explain any three, with diagrams where appropriate: (i) the CIA properties of cryptography, (ii) confusion and diffusion, (iii) message authentication code, (iv) homograph phishing attack, (v) clickjacking.',note='Each concept is optional. The 15 marks belong to the whole subquestion; each selected concept is worth 5. This is one question occurrence per relevant topic, not five compulsory questions.')
add('2023–24','5(b)',7,20,'modes','Unfamiliar chaining diagram; equations, parallelism and malleability','For the supplied block-cipher diagram with IV1 and IV2, derive encryption/decryption equations for the first three blocks; draw the decryption diagram; determine which operations parallelize. Given two known plaintext/ciphertext pairs and intercepted IV1, IV2, C1, C2, modify the transmitted values so Bob obtains chosen P1′ and P2′ without learning the key.',note='The diagram is a custom construction, not plain CBC. The original figure is essential. The handwritten notes p. 66 discuss this construction.')
add('2023–24','6(a)',8,15,'dh','Unauthenticated Diffie–Hellman MITM; defense without a trusted third party','Given the stated Diffie–Hellman protocol, act as Mallory when no trusted third parties can verify Alice or Bob. Explain and diagram a successful MITM attack, then briefly explain a defense.',note='The question explicitly rules out an available trusted third party. A defense must state another authenticated trust mechanism, such as a previously authenticated key or an out-of-band fingerprint check.')
add('2023–24','6(b)',8,20,'classical','Recover affine-cipher keys from two mappings','The diagram implements T = P×K1 mod 26 and C = T+K2 mod 26, with K1 coprime to 26. Given B→E and E→P, set up and solve simultaneous congruences to determine K1 and K2.')
add('2023–24','7(a)',9,15,'elgamal','Numerical ElGamal; IND-CPA and non-malleability','For ElGamal with p=353, g=3, Bob’s private key b=233, Alice’s message M=123 and random r=97, compute Bob’s public key and the ciphertext, and show decryption step by step. Is the scheme IND-CPA secure and non-malleable? Justify.',note='The exam writes Z*353. The lecture’s zero-message IND-CPA counterexample does not apply to that message space; see the coverage notes in the report.')
add('2023–24','7(b)',9,10,'rsa','RSA correctness proof','Prove mathematically that RSA decryption recovers the original message, using the necessary number-theory results.')
add('2023–24','7(c)',9,10,'signature','RSA signing/verifying; security of separately sending ciphertext and signature','Define RSA signature creation and verification using Sign(d,M) and Verify(e,N,M,sig). Alice encrypts M with Bob’s RSA public key and signs M with her own private key. Can she securely send both ciphertext and signature together? Justify cryptographically.')
add('2023–24','8(a)',9,5,'ae','Encrypt-then-MAC versus MAC-then-encrypt','What is authenticated encryption? Which of MAC-then-encrypt and encrypt-then-MAC is preferable, and why?')
add('2023–24','8(b)',9,10,'cookies','Cookie-send matrix','Three cookies are set by long.moodle.com: theme=dark, Domain=moodle.com, Path=/, Secure=true; auth=ok, Domain=long.moodle.com, Path=/test, Secure=false; file=secret, Domain=moodle.com, Path=/print, Secure=true. Fill the send/not-send matrix for (i) http://print.moodle.com/print, (ii) http://login.moodle.com/, (iii) http://moodle.com/test, (iv) https://moodle.com/print/test, (v) https://login.moodle.com/test/print.',note='The URL list continues on root PDF p. 10.')
add('2023–24','8(c)',10,10,'sql','Login bypass; prepared statements','The backend concatenates username and password into SELECT * FROM users WHERE username=... AND password=.... The table includes Alice with password password123. Determine whether SQL injection is possible; give concrete login inputs to log in as Alice without her password; explain how prepared statements prevent it.')
add('2023–24','8(d)',10,10,'xss','Stored versus reflected XSS','Define XSS and explain the difference between stored and reflected XSS using diagrams.')
add('2023–24','1(c)',2,15,'cert','Untrusted key bundled with its own signature; attacker positions','ARTBot broadcasts to learn CSBot’s phone number. CSBot replies with its number, public key, and a signature on the number. ARTBot verifies using that supplied key and caches the result. Explain how to poison the cached number as (i) an on-path attacker, (ii) a MITM attacker and (iii) an off-path attacker. Analyze a possible defense.',note='Cross-topic use of signatures, but the failure being examined is the absence of an authenticated public-key binding.')
add('2023–24','4(c)',6,15,'keymodels ae cert','TLS handshake authentication, directional keys and authenticated records','For the supplied TLS handshake: (i) why can a MITM not exploit unencrypted/unauthenticated ClientHello and ServerHello, in both the DH and RSA cases? (ii) Why is using one shared encryption key and one shared integrity key for both directions a bad idea? (iii) After ChangeCipherSpec, what vulnerability remains in the simplified protocol, and how would you fix it?','partial','The decks supply the cryptographic building blocks, not a full TLS handshake or record-protocol treatment. All 15 marks cover the combined subquestion.')
add('2022–23','5(a)',12,12,'modes','ECB/CBC/CTR comparison','Compare ECB, CBC and CTR, with diagrams, for (i) IND-CPA security, (ii) encryption/decryption parallelism and (iii) robustness to incorrect IV/nonce usage.')
add('2022–23','5(b)',12,12,'ae','Analyze encryption plus hash, plaintext MAC, or ciphertext MAC','Alice sends (1) Enc(K,m) with Hash(ciphertext), (2) Enc(K,m) with MAC(K,m), or (3) Enc(K,m) with MAC(K,ciphertext). Assume no harmful interactions from the shared key. For each, evaluate confidentiality against passive Eve and integrity against modifying MITM Mallory.')
add('2022–23','5(c)',12,11,'cookies csrf xss','Limits of cookie policy','Analyze how effective cookie policies are at (i) preventing CSRF, (ii) preventing session hijacking through XSS and (iii) preserving confidentiality of stored cookies.',note='A single lettered subquestion intentionally covers three issues. It is counted once in each relevant topic and once in the Lecture 10 total; its marks are not tripled.')
add('2022–23','6(a)',13,15,'dh signature','Authenticate Diffie–Hellman with RSA signatures','Explain Diffie–Hellman and its MITM security flaw with figures. Modify the algorithm using RSA digital signatures to remove that flaw.',note='The signing keys must themselves be authenticated; merely attaching an untrusted public key does not fix MITM.')
add('2022–23','6(b)',13,10,'sql','INSERT-query injection; bypass a cart quantity restriction','WorstBUY executes a formatted INSERT INTO cart(session,item) statement for each POST request. Alice cannot add more than three items through the website. Construct a POST request that inserts 100 pens, then give a preventive measure against SQL injection.')
add('2022–23','6(c)',13,10,'prng','HMAC-DRBG generation, security and rollback resistance','Describe how HMAC-DRBG generates pseudorandom numbers and why it is secure and rollback resistant, assuming secure HMAC.')
add('2022–23','7(a)',13,15,'csrf','CSRF synchronizer token; refreshing only on POST','The server puts a random CSRF token in each page’s DOM/hidden form field, and accepts a request only with a valid cookie and POST token. Tokens are refreshed on POST. Explain protection without special browser support; evaluate refreshing only on POST instead of on both GET and POST.')
add('2022–23','7(c)',13,7,'xss','Stored versus reflected XSS','Briefly explain how reflected XSS differs from stored XSS.')
add('2022–23','8(a)',14,15,'mac hash','Integrity tags in a file header; hash versus MAC; writable versus read-only storage','A file’s integrity tag is stored in its header and checked when opened. An attacker must not modify the file undetected. Compare (i) an unkeyed collision-resistant hash, (ii) a MAC under the owner’s secret key and (iii) the MAC scheme when the tag is in read-only memory. Decide whether each system is secure.',note='The final case puts the integrity tag in read-only memory; preserve the wording of the original when working the problem.')
add('2022–23','8(b)',14,8,'twofa','SMS 2FA against phishing','Is SMS-based two-factor authentication an effective defense against phishing? Justify.')
add('2022–23','8(c)',14,12,'ui','Clickjacking with iframes; repeated-click redirection','Describe clickjacking in two cases: (i) overlay a fake free-subscription button on an iframe advertisement so a visitor unknowingly clicks a paid buy button; (ii) an embedded public-exam result form whose first click goes to Twitter, second to Facebook, and third finally fetches the result.')
add('2022–23','2(a)',11,12,'password','Brute-force throughput under a password-expiration policy','A password policy requires uppercase, lowercase, numeric and special characters, minimum length 10, with monthly password changes. Estimate the minimum guesses per second needed to crack a credential, showing the calculations.','partial','The question does not specify the exact special-character alphabet or a precise success probability. State assumptions. Lecture 8 covers guessing attacks but not this exact counting problem.')
add('2021–22','1(c)',15,10,'classical','Hill encryption and decryption with a 3×3 key','Given Hill-cipher key GYBNQKURP and plaintext ACT, demonstrate encryption and decryption to judge correctness.')
add('2021–22','1(d)',15,10,'classical keymodels','Caesar as symmetric encryption; composition of affine ciphers','Why is Caesar a symmetric encryption algorithm? If you encrypt using one affine cipher and then a second affine cipher, both modulo 26, is there any advantage over one affine cipher? Derive the result.')
add('2021–22','2(a)',15,5,'goals','Attacks versus information-security CIA goals','Categorize security attacks with respect to C.I.A. goals.','partial','Here CIA is the information-security triad, including Availability. Lecture 2 calls its cryptographic goals Confidentiality, Integrity and Authenticity; those are different uses of A.')
add('2021–22','2(b)',15,10,'ecc','Compute an elliptic-curve point group','Explain elliptic-curve cryptographic applications. Find the group of points E11(1,6), with y²=x³+x+6 mod 11.','partial','Lecture 6 p. 57 gives ECDH intuition and explicitly does not require curve arithmetic; full point enumeration needs material beyond this deck.')
add('2021–22','2(c)',15,10,'dh','Numerical Diffie–Hellman exchange','Explain Diffie–Hellman. Given p=353, primitive root g=3, and private exponents 97 and 233, calculate both public keys and the shared secret.')
add('2021–22','2(d)',15,10,'modes','Identify ECB-style long-message weakness and replace the mode','A cryptanalyst says the system is secure for short messages but vulnerable for long messages because of its mode of operation. Identify and describe the mode and explain how to overcome the problem.')
add('2021–22','3(b)',15,10,'hash mac signature','Applications of hashing in authentication, confidentiality and signatures','Demonstrate uses of a hash function for authentication, confidentiality and digital signatures.','partial','The decks cover hashing, MACs and hash-then-sign; a bare hash does not provide confidentiality. Explain a suitable construction rather than attributing encryption properties to hashing.')
add('2021–22','3(c)',16,10,'hash','Evaluate XOR of fixed-size message blocks as a hash','Explain the desired properties of a cryptographic hash. A message consists of l blocks M1,…,Ml of 160 bits and h(x)=M1 XOR … XOR Ml. Evaluate this function against those properties.')
add('2021–22','3(d)',16,10,'keymodels signature','Symmetric/public-key comparison; key roles in signing versus encryption','Compare symmetric and public-key cryptography. Explain how the roles of public and private keys in signatures differ from their roles in public-key encryption.')
add('2021–22','4(b)',16,10,'mac','HMAC construction','Describe how a message authentication code is created by HMAC.')
add('2021–22','4(c)',16,10,'block','DES attack; meet-in-the-middle strength of fivefold DES','Explain an attack on DES. A proposed 5DES alternates five DES encryptions/decryptions using independent keys and claims 280-bit strength, exceeding AES-256. Compute the effective key strength and assess the claim.','partial','The deck introduces DES and its short key; multiple-DES meet-in-the-middle analysis is not developed.')
add('2021–22','4(d)',16,10,'block','Compare DES components with AES','For each DES component, identify its AES counterpart or explain why none is needed: (i) XOR of subkey with the f-function input, (ii) XOR of f output with the left half, (iii) f itself, (iv) permutation P, (v) swapping block halves.','partial','AES round operations appear in Lecture 3; detailed DES round structure is not supplied.')
add('2021–22','7(b)',17,12,'ui','Clickjacking versus phishing','Differentiate clickjacking and phishing with examples.')
add('2021–22','7(c)',17,11,'cert','Self-signed SSL certificate and server authentication','Why is buying from a shopping website that uses a self-signed SSL certificate a bad idea?',note='The issue is whether the server key is authenticated by a trust anchor, not whether a self-signed certificate can encrypt.')
add('2020–21','5(a)',19,15,'session mac','Authenticate UDP messages with a cookie/token; prevent replay','Bob uses UDP for a streaming service because confidentiality is unnecessary and he cannot use TLS/HTTPS. He needs integrity so attackers cannot impersonate the sender or alter or replay messages. Explain how to achieve this using cookies.','partial','Lecture 10 covers session cookies and Lecture 5 MACs. A complete application protocol also needs authenticated key/bootstrap delivery and freshness or replay tracking. Raw UDP does not carry HTTP cookies automatically.')
add('2020–21','5(b)',19,10,'sql','Single-statement SQL injection in a password-change form','A C++ web server allows only one SQL statement per database call. Show how SQL injection in the displayed old-password/new-password login form can still change everyone’s password.')
add('2020–21','6(a)',19,15,'csrf xss','CSRF plus stored XSS in a social-network friend request','Trudy builds trudymalicious.com. On a visitor A’s arrival, make A send Trudy a friend request and change A’s homepage so anyone visiting it sends Trudy a friend request. No CSRF/XSS defenses exist. The supplied GET is http://www.networksocial.com/action/friends/add?friend=20. Explain the malicious site.','partial','CSRF is taught directly in Lecture 10; the stored-XSS part is taught in Lecture 11 pp. 15–19 and handwritten notes pp. 62–63. The question continues on p. 20.')
add('2020–21','6(b)',20,10,'signature','ElGamal signature algorithm and reuse of secret k','Explain the ElGamal signature scheme. Why must the same random k not be used for two signatures?','partial','Lecture 7 pp. 38–41 gives the nonce-reuse principle for DSA/ECDSA, not the full ElGamal signature algorithm. The CT4 revision guide pp. 26–27 supplies the latter, with algebraic caveats noted in the report.')
add('2020–21','7(a)',20,15,'classical goals','Break a Caesar-then-Hill construction','Bob applies Caesar followed by Hill, calling it a CH network. He claims it meets Shannon confusion and diffusion because it is a substitution-permutation network. Alice says it is easy to break. Explain an attack.')
add('2020–21','7(b)',20,10,'cookies','Cookie-send matrix','Cookies set by docs.example.com: file=main, Domain=example.com, Path=/, Secure=true; file=test, Domain=docs.example.com, Path=/test, Secure=false; file=print, Domain=example.com, Path=/print, Secure=true. Determine which are sent to (i) http://print.example.com/print, (ii) https://docs.example.com/, (iii) http://example.com/test, (iv) https://example.com/print/test, (v) https://docs.example.com/test/print.')
add('2020–21','8(b)',21,10,'hash','Birthday bound for a b-bit hash','Prove that a b-bit hash function provides b/2-bit security.',note='This is the collision-search security bound, not a universal bound on preimage resistance.')
add('2020–21','8(c)',21,15,'session','Invalidate session cookies after password change','Bob’s authentication cookie expires after one year. Changing a password only updates the database. Explain Alice’s advice that resetting the password must also reset the authentication cookie.')
add('2019–20','1(a)',22,12,'signature','Digital signatures and non-repudiation','Explain, with a figure, how digital signatures ensure non-repudiation.')
add('2019–20','1(c)',22,11,'password','Public security questions and password-reset account takeover','Attackers reset Sarah Palin’s email password using publicly available personal information such as birthday, ZIP code and security-question answers. Identify the attack and evaluate the security of this password-reset feature.','partial','Account-recovery security is related to Lecture 8 password guessing; the specific recovery scenario is not taught in the deck. The CT4 guide pp. 52–53 discusses it.')
add('2019–20','2(b)',22,12,'password','Password-space size and average brute-force time','How many 10-character passwords can be made from all 128 ASCII characters? If an attacker tests one candidate per microsecond, how long does guessing take on average?','partial','Lecture 8 gives the guessing-attack background; the numerical model is specified by the paper.')
add('2019–20','6(a)',24,14,'otp classical','OTP encryption/decryption; transposition as a Hill cipher','Explain how the pad P is used directly for both encryption and decryption in a binary OTP. Define transposition cipher and explain why it is a special case of Hill cipher.','partial','OTP and Hill are taught; the permutation-matrix connection is an application rather than a separately developed slide topic.')
add('2019–20','6(b)',24,21,'hash','Weak/strong collision resistance; toy hash; Merkle–Damgård','State ideal hash properties and distinguish weak and strong collision resistance. Show H(x)=(5x+11) mod 19 is not weakly collision resistant for H(4). Draw Merkle–Damgård and explain why its compression function needs strong collision resistance.')
add('2019–20','7(a)',24,8,'rsa','Euler totient/theorem; modular inverse','Define Euler’s totient function and Euler’s theorem, and explain computing a modular inverse using Euler’s theorem.',note='Lecture 7 pp. 20–23 uses these prerequisites; handwritten notes p. 35 and CT4 guide pp. 19–20 expand them.')
add('2019–20','7(b)',24,12,'rsa','Modular equations and fast exponentiation','Solve (i) x^8 ≡ 9 (mod 13), (ii) x² ≡ 2 (mod 13), and compute 3^128 mod 7. A modular-exponentiation table modulo 13 is supplied.','partial','These number-theory exercises support RSA/DH. The current slides do not develop modular-root solving; the CT4 guide pp. 20–21 works this question.')
add('2019–20','7(c)',24,15,'rsa','RSA validity, repeated totients and encryption','System A: p=83, q=101, e=3, d=5467. System B: p=17, q=11, e=7, d=23. For both compute φ(n) and φ(φ(n)), and explain validity. For system B encrypt plaintext M=3.')
add('2019–20','8(a)',24,20,'elgamal signature hash','ElGamal encryption proof; birthday attack on signatures','Describe ElGamal encryption/decryption and prove decryption correctness. Give an illustrative example showing that digital signatures can be vulnerable to a birthday attack.',note='One lettered subquestion, shared by ElGamal and signature/hash topics. The printed 20 marks are not allocated between its tasks.')
add('2019–20','8(b)',24,15,'dh','Diffie–Hellman steps and active MITM','Write the Diffie–Hellman key-exchange steps and show the MITM attack when an adversary can intercept and modify messages.')
add('2018–19','1(a)',26,9,'cert','Digital-certificate contents and CA role','What key information is kept in a digital certificate? Explain the certification authority’s role with a figure.')
add('2018–19','1(d)',26,8,'signature','Risks of signing an apparently random string','Explain the risks if Bob agrees to sign a seemingly random string with his private key.')
add('2018–19','4(b)',26,8,'ui','Pharming versus phishing','Distinguish pharming and phishing, with examples.','partial','Handwritten notes p. 63 teaches phishing; pharming and DNS redirection are not developed there.')
add('2018–19','5(a)',27,12,'classical','Hill-cipher numerical encryption','Encrypt plaintext DITECTIVE using Hill cipher, block size m=3 and K=[[3,0,2],[2,0,2],[0,1,1]].',note='DITECTIVE is the spelling printed in the paper; do not silently replace it with DETECTIVE.')
add('2018–19','5(b)',27,3,'modes','Inserted ciphertext bit and CBC synchronization','A message is encrypted with DES-CBC. An extra 0 bit is inserted into the ciphertext stream after block C_i. How much plaintext is garbled?',note='This is insertion of a bit, not flipping a bit or replacing a whole block. Preserve that distinction.')
add('2018–19','6(a)',27,8,'block','Trace P-box and S-box diagrams','For the supplied P-box, find the output for input bits designated top-to-bottom 01234567. For the supplied S-box, find the output sequence for successive input octal numbers 76543210.','partial','The original diagrams are essential. Lecture 3 has AES SubBytes and ShiftRows, but not this specific P-box/S-box exercise.')
add('2018–19','8(b)',28,9,'sql session ui','Short notes; answer any three of four','Write short notes on any three: (i) Faraday cage, (ii) blind SQL injection, (iii) impersonation token, (iv) homograph attack.','partial','Each choice is 3 marks within the 9-mark subquestion. Blind SQL injection is in Lecture 12 pp. 36–37; homographs are in Lecture 11 pp. 62–64 (also handwritten notes pp. 63–64). The meaning of impersonation token is not established as web-session authentication in the supplied sources, so this choice is not counted under session frequency.')
# Remove the tentative session tag above; do not force an ambiguous OS impersonation term into web-session materials.
qs[-1]['topics'].remove('session')
add('2018–19','11(a)',29,5,'sql','UPDATE injection to change password and salary','Use the displayed employee-password-change form and PHP code to set employee EID100’s password to you_are_hacked and salary to 10$, without knowing the old password.',note='The PHP query/code appears on p. 30.')
add('2018–19','11(b)',30,10,'sql','Rewrite vulnerable PHP using prepared statements','Change changepasswd.php to use a prepared statement so the SQL injection in Q11(a) is prevented.')
add('2018–19','12(a)',30,15,'xss','Stored XSS in a guest book; malicious page actions','As Sammy (id=40), write a script in the guest-book Message field to demonstrate XSS damage. The first paragraph has id p1 and the friend-add action for user id 100 is http://vulnerable.com/action/friend/add?id=100.',note='The guest-book screenshot is on p. 31; consult it with the prompt on p. 30.')

# Lecture 1 adds explicit principle applications; retain every original S01–S67 entry.
for item in qs:
 if item['session']=='2021–22' and item['question']=='2(a)':
  item['topics']=['securitygoals'];item['coverage']='direct';item['coverage_note']='Information-security CIA uses Availability; Lecture 1 supplies the general desired-property/threat-model context.'
add('2023–24','1(b)',2,10,'principles','Match five scenarios to security principles','Match principles to a valet key, bypassable laptop screen lock, irreversible water-damage sticker, bank recovery questions overridden by a representative, and encryption at rest and in transit.','direct','')
add('2022–23','1(a)',11,10,'principles','Least privilege versus separation; why record compromise?','Differentiate least privilege and separation of privilege, and explain the importance of compromise recording with examples.','direct','')
add('2020–21','1(b)',18,12,'securitygoals','Selective packet dropping against a competitor','An ISP deliberately drops 25% of a competing provider’s VoIP packets traversing its routers. Identify the attack.','direct','')
add('2020–21','1(c)',18,11,'principles','Why compromise recording matters and which tools support it','Explain the importance of compromise recording and name tools used for it.','direct','')
add('2020–21','2(b)',18,12,'principles','Mismatched boarding-pass and identity checks','Explain how online-printable boarding passes permit a no-fly-list bypass in the described airport checks, and fix the weakness.','partial','An application of complete mediation/authentication; the exact airport workflow is in the paper.')
add('2020–21','8(a)',20,15,'principles','Audit scanf, privileged file opening and a name-based access race','Analyze attacks on the printed C program (code on p. 21): scanf into buffer[60], fopen(fn,"a+"), access(fn,W_OK), fwrite; state environmental assumptions.','partial','Lecture 1 pp. 47–49 supplies complete mediation/TOCTOU; buffer-overflow and Unix setuid details require Sec A. Full mixed answer retained.')

# Mixed question: only its explicit web-security case belongs to current Sec B.
add('2023–24','3(a)',4,10,'xss','Limits of HTTPS/firewall/NIDS protection against reflected XSS',
    'For the HTTPS-only server farm protected by a firewall and NIDS, assess whether reflected XSS can always be prevented when the attacker is on path.',
    'direct','Only case (2), reflected XSS, is in Sec B scope. The other four network-defense cases are covered in Sec A. The printed 10 marks cover all five cases; no per-case mark allocation is given.')
qs[-1]['scope']='sec_b_component'
qs[-1]['scope_note']=qs[-1]['coverage_note']

# Topics asked in older papers but not taught adequately by the supplied Sec B files.
gaps=[
 ('2023–24','1(a), 2(b)', '1, 3','Buffer-overflow payloads and defenses'),
 ('2023–24','2(a), 2(c), 3(a)–(c), 4(a)–(b)','3–5','DHCP spoofing, TCP attacks, network defenses, worms, DNS/Kaminsky, DoS and firewall evasion'),
 ('2022–23','1(b)–(c), 2(b)–(c), 3–4','11–12','System/network security, malware, access control, reconnaissance, honeypots and firewalls; principle Q1(a) and password Q2(a) are included above'),
 ('2022–23','7(b)','13','Tor anonymity and onion-routing cryptography'),
 ('2021–22','1(a)–(b), 3(a), 4(a), 5–6, 7(a), 8','15–17','Biometrics, memory/system security, DLL injection, malware, IPsec, botnets, intrusion detection, TCP/DNS defenses, access-control delegation and spam'),
 ('2020–21','1(a), 2(a), 2(c), 3–4','18–19','System/network security, access control, forensics, worms, ARP and incident response; Q1(b), Q1(c) and Q2(b) now map to Lecture 1'),
 ('2020–21','5(c), 6(c), 7(c)','19–21','Return-to-libc, stack-argument layout and StackGuard; Q8(a) is now included as a partial TOCTOU application with Sec A prerequisites'),
 ('2019–20','1(b), 2(a), 2(c), 3–5','22–24','Heartbleed, botnets, malware, Unix permissions, DNS/TCP/switch attacks, IDS/base-rate fallacy and honeypots'),
 ('2018–19','1(b)–(c), 2, 3, 4(a), 4(c)–(d)','26','IPsec, malware, rootkits, network attacks, botnets, DNS poisoning and intrusion detection'),
 ('2018–19','6(b), 7, 8(a), 8(b)(i), 9, 10, 13','27–31','Physical locks, biometrics, Faraday cage, format-string/stack exploits and quantum key distribution'),
]
# Printed location is recorded for audit, never used to select the current section.
for item in qs:
 item.setdefault('scope','sec_b')
 item.setdefault('scope_note','')
 item['printed_section']='A' if int(item['question'].split('(')[0])<=4 else 'B'
section_audit=[]
for year in exams:
 arr=[item for item in qs if item['session']==year]
 na=sum(item['printed_section']=='A' for item in arr)
 section_audit.append(dict(session=year,printed_A=na,printed_B=len(arr)-na,total=len(arr)))
with (OUT/'EXAM_SECTION_AUDIT.csv').open('w',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=['session','printed_A','printed_B','total']);writer.writeheader();writer.writerows(section_audit)
(OUT/'question_index.json').write_text(json.dumps(qs,indent=2,ensure_ascii=False)+'\n')
with (OUT/'question_index.csv').open('w',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=list(qs[0]));writer.writeheader()
 for q in qs:writer.writerow({**q,'topics':'; '.join(q['topics'])})

def refs(q):return f"**{q['session']} · Q{q['question']} · {q['marks']} marks** · printed Section {q['printed_section']} · "+link('CSE405-Security_Merged.pdf',q['pdf_page'],f"root PDF p. {q['pdf_page']}")
def questionblock(q):
 lines=[f"- {refs(q)}",f"  - **Task:** {q['exact_skill']}.",f"  - {q['question_paraphrase']}"]
 if q['coverage_note']:lines.append(f"  - **Coverage note:** {q['coverage_note']}")
 return '\n'.join(lines)
bytopic={t:[q for q in qs if t in q['topics']] for t in topics}
rank=sorted(topics,key=lambda t:(-len(bytopic[t]),-len(set(q['session'] for q in bytopic[t])),topics[t][0]))
bydeck={d:[q for q in qs if any(topics[t][1]==d for t in q['topics'])] for d in names if d not in ['Guide','Notes']}

def ranktable():
 lines=['| Rank | Topic | Questions | Papers out of 6 | Main material |','|---:|---|---:|---:|---|']
 for i,t in enumerate(rank,1):
  title,d,p,np=topics[t];n=len(bytopic[t]);papers=len(set(q['session'] for q in bytopic[t]))
  lines.append(f'| {i} | [{title}](#{t}) | {n} | {papers}/6 | {names[d]} |')
 return '\n'.join(lines)

report=['# Final exam topic analysis — all supplied Sec B material','',
'## Scope and how the counts work','',
'This report maps questions in the root past-paper PDF to the actual contents of Lectures 1–12 and the handwritten Sec B notes, including the former CT 4 material. The existing CT4 revision guide is supplementary; its frequency table is not treated as the source of truth.','',
'**Question text below is a faithful paraphrase, not a verbatim transcription.** Open the linked paper page for exact wording, code, figures and layout. Page numbers are physical PDF pages, starting at 1. Academic sessions label questions; sitting years are shown separately.','',
'**Counting unit:** one printed lettered subquestion, e.g. Q7(c). Internal tasks remain together unless explicitly split by the current section boundary. The reflected-XSS case in 2023–24 Q3(a) counts once here; its four network cases are in Sec A. A mixed question can count once under each topic it explicitly examines, but only once in a given deck total. Therefore topic totals and deck totals cannot be added to get a number of distinct questions. Optional short-note/concept choices are included and clearly identified. Marks shown belong to the whole subquestion; they are not marks attributable to every linked topic.','',
'**Attribution:** both printed sections are checked each year. Use the deck that teaches the topic, not decks that merely repeat it in a recap. Questions requiring applications beyond the slides are marked by coverage notes. Unrelated system/network-security questions are not ranked as if they were taught by these Sec B files.','',
'| Academic session | Sitting date printed on paper | Root PDF pages |','|---|---|---|']
for y,(date,a,b) in exams.items():report.append(f'| {y} | {date} | {a}–{b} |')
report += ['', '## Both printed sections checked in every year', '',
'Questions are assigned by current Sec B topics, regardless of whether an older paper printed them under Section A or Section B. These locations are recorded for traceability and do not filter the question set.', '',
'| Academic session | Sec B topics in printed A | Sec B topics in printed B | Total |','|---|---:|---:|---:|']
for row in section_audit:report.append(f"| {row['session']} | {row['printed_A']} | {row['printed_B']} | {row['total']} |")
report += ['',f'**Mapped question index:** {len(qs)} distinct lettered subquestions; machine-readable versions: [CSV](question_index.csv) and [JSON](question_index.json).','',
'## Topics ranked by question frequency','',ranktable(),'',
'Frequency measures what was asked in these six papers. It does not establish future exam probability. Paper coverage helps distinguish repeated yearly appearances from several questions concentrated in one paper.','',
'## Slide decks ranked by mapped questions','',
'| Material | Unique mapped subquestions | Papers out of 6 |','|---|---:|---:|']
for d in sorted(bydeck,key=lambda d:(-len(bydeck[d]),names[d])):
 report.append(f"| {names[d]} | {len(bydeck[d])} | {len(set(q['session'] for q in bydeck[d]))}/6 |")
report += ['', 'Lectures 11–12 now provide the primary sources for XSS, UI attacks, 2FA and SQL injection. The handwritten notes remain companion material; repeated coverage does not create additional question occurrences.', '',
'## Questions under slide deck → exact topic','',
'Within each teaching source, topics are ordered by frequency. The task line identifies the particular subtopic examined. Cross-topic questions may appear more than once so each topic has a complete list.','']
for d in ['L1','L2','L3','L4','L5','L6','L7','L8','L9','L10','L11','L12']:
 report += [f'## {names[d]}','',link(files[d],label='Open source material'), '']
 dt=[t for t in rank if topics[t][1]==d]
 if not dt:
  report += ['**0 standalone mapped questions.** URLs, HTTP, HTML/JavaScript, DOM, sandboxing, SOP and CORS are prerequisites for the cookie, CSRF and XSS questions. They are not counted again just because those questions use web concepts.','']
 for t in dt:
  title,_,p,np=topics[t];arr=bytopic[t]
  report += [f'<a id="{t}"></a>',f'### {title} — {len(arr)} questions across {len(set(q["session"] for q in arr))}/6 papers','',
   (f'**Study:** deck PDF pp. {p}. Lecture 1 is the primary source; Sec B handwritten notes do not develop this unit.' if d=='L1' else f'**Study:** deck PDF pp. {p}; handwritten notes PDF pp. {np}.'),'']
  for q in arr:report += [questionblock(q),'']
report += ['## Syllabus topics with no standalone mapped questions','',
'- Lecture 1: trusted-computing-base details, fail-safe examples and security-by-design as standalone questions. Its principle applications and CIA/availability questions are now mapped.\n- Lecture 2: Kerckhoff’s principle and key-management rules; a standalone IND-CPA game definition; Enigma history. IND-CPA is explicitly examined through mode and ElGamal questions.','- Lecture 3: OTP key reuse/two-time pads as a standalone question; AES round tracing as a standalone numerical exercise.','- Lecture 4: standalone CFB analysis.','- Lecture 5: standalone length-extension attack and NMAC construction; the underlying Merkle–Damgård construction is examined.','- Lecture 6: standalone entropy, seeding/reseeding, CTR-DRBG, UUID, stream-cipher seeking and the PRNG case studies. HMAC-DRBG is examined once.','- Lecture 8: a direct salted-password/PBKDF2 construction question; certificate revocation/CRLs as a standalone question; traffic analysis, side channels and transparent public parameters. Password-guessing questions are related but are not direct password-hashing questions.','- Lecture 9: all topics as standalone questions.','- Lecture 10: cookie ambiguity, Spectre/site isolation and detailed Referer-header tradeoffs as standalone questions.','- Lecture 12: command injection and CAPTCHA as standalone questions. Handwritten-note extensions: JWT format/verification and session fixation as standalone questions.','',
'## Material gaps that matter when practicing past papers','',
'These questions need material beyond Sec B; many are now covered by the [Sec A study guide](../../Sec%20A/README.md). This is a coverage checklist, not a second frequency ranking.','',
'| Session | Questions | Root PDF pages | Additional material needed |','|---|---|---|---|']
for y,q,p,desc in gaps: report.append(f'| {y} | {q} | {p} | {desc} |')
report += ['', '## Source-reading cautions','',
'1. **ElGamal message space matters.** Lecture 7 p. 15 says ElGamal is not IND-CPA secure by using message 0, and swaps the affected component in its explanation: zero makes C2 zero, not C1. The 2023–24 question explicitly uses Z*353, which excludes zero. Do not copy the slide’s zero-message counterexample into this answer unchanged: the paper requires reasoning about its stated message space and security assumptions. Multiplicative malleability is a separate issue addressed on the same slide.','2. **CIA has two meanings in these files.** Lecture 2’s cryptographic trio uses Authenticity. General information-security questions commonly use Availability. Follow the question’s context.','3. **The handwritten notes contain course annotations.** For example, p. 45 says DSA is “not in syllabus,” while the supplied Lecture 7 includes DSA attack slides. Include it in this file-derived syllabus and confirm any formal exclusion with your instructor.','4. **Supplementary-guide counts group topics differently.** Its “7 digital signature questions” leaves the ElGamal-signature question in a separate ElGamal category. This report includes that question under signatures. The guide’s RSA count also groups number-theory prerequisites with RSA; this report labels that grouping explicitly.','5. **The slide decks are not error-free reference specifications.** Examples include incorrect hexadecimal URL-encoding examples in Lecture 9 p. 19, simplified cookie matching/SameSite descriptions, and the HMAC key-normalization description in Lecture 5 pp. 36–37. This report maps study topics; it does not endorse every technical statement in the sources.','6. **ElGamal signature nonce-reuse algebra needs care.** The revision guide pp. 26–27 writes inverses modulo p−1 that may not exist; in that case solve linear congruences and check candidate keys. Do not assume the DSA derivation carries over unchanged.','',
'## Suggested study order from the evidence','',
'1. Digital signatures; hash properties/birthday attacks; MAC/HMAC; classical-cipher calculations.','2. Diffie–Hellman and MITM; RSA and number theory; ECB/CBC/CTR and ciphertext manipulation.','3. Cookie matrices and attributes; session authentication; CSRF; authenticated-encryption composition.','4. SQL injection and prepared statements; stored/reflected XSS; clickjacking/phishing from Lectures 11–12 and the handwritten notes.','5. Certificates; HMAC-DRBG; remaining syllabus topics.','',
'Use the ranking together with marks and breadth: a 3-mark optional short note is not equivalent preparation value to a 15–20-mark construction problem.']
(OUT/'FINAL_EXAM_TOPIC_ANALYSIS.md').write_text('\n'.join(report)+'\n')
print('Wrote',len(qs),'questions')
for t in rank:print(len(bytopic[t]),len(set(q['session'] for q in bytopic[t])),t)
