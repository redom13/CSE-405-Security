# Sec A final-exam topic analysis

**138 distinct mapped printed subquestions across six papers.** [CSV](question_index.csv) · [JSON](question_index.json) · [Worked solutions](../solutions/SOLUTIONS.pdf).

## Scope and counting

Both printed sections of every paper were checked because teaching assignments changed between years. One occurrence is a printed lettered subquestion; the unlettered 2018–19 Q10 is one whole question. Internal tasks remain together. A mixed question counts once per explicitly examined topic and once per related deck. Totals across topics/decks therefore cannot be added. Optional choices are included and identified; marks belong to the entire printed subquestion.

Question summaries are paraphrases. Open the original PDF page for exact wording, code and diagrams. “Related/extension” means a relevant foundation is supplied but some requested mechanism or calculation requires more than the local slides; the table exposes these counts so they are not mistaken for direct coverage. A mixed answer is retained in full even if only part maps to Sec A. No frequency predicts a future exam.

| Academic session | Sitting date | Root PDF pages |
|---|---|---|
| 2023–24 | 06 September 2025 | 1–10 |
| 2022–23 | 18 April 2024 | 11–14 |
| 2021–22 | 30 October 2023 | 15–17 |
| 2020–21 | 25 September 2022 | 18–21 |
| 2019–20 | 07 September 2021 | 22–25 |
| 2018–19 | 24 October 2019 | 26–31 |

## Topics ranked by printed-question frequency

| Rank | Exact topic group | All mapped | Direct | Related / extension | Papers / 6 | Main deck |
|---:|---|---:|---:|---:|---:|---|
| 1 | [DNS poisoning, Kaminsky races, pharming and DNSSEC](#dns) | 7 | 6 | 1 | 5/6 | DNS Security |
| 2 | [Digital signatures and signing-key security](#signature) | 7 | 5 | 2 | 5/6 | Cryptography, Hashes and Digital Signatures |
| 3 | [Hash properties, collisions and birthday security](#hash) | 7 | 3 | 4 | 4/6 | Cryptography, Hashes and Digital Signatures |
| 4 | [MAC/HMAC and authenticated data](#mac) | 7 | 1 | 6 | 4/6 | Cryptography, Hashes and Digital Signatures |
| 5 | [Phishing, homographs and UI deception](#phishing) | 7 | 0 | 7 | 4/6 | Web and Database Security |
| 6 | [TCP hijacking, spoofed segments and optimistic ACKs](#tcp) | 7 | 3 | 4 | 4/6 | Network Security |
| 7 | [Worm propagation, epidemic models and case studies](#worm) | 6 | 5 | 1 | 5/6 | Malware |
| 8 | [Stack/heap corruption and buffer-overflow payload reasoning](#buffer) | 6 | 1 | 5 | 4/6 | Buffer Overflow |
| 9 | [Stored/reflected XSS and injected scripts](#xss) | 6 | 4 | 2 | 4/6 | Web and Database Security |
| 10 | [OS trust, paging, boot and persistent memory images](#os) | 6 | 3 | 3 | 3/6 | Operating Systems Security |
| 11 | [Firewall state, evasion and defense limits](#firewall) | 5 | 3 | 2 | 4/6 | Firewalls, Tunneling and IDS |
| 12 | [Honeypot topology, monitoring and overhead](#honey) | 5 | 5 | 0 | 4/6 | Firewalls, Tunneling and IDS |
| 13 | [DoS/DDoS, reflection and resource exhaustion](#dos) | 5 | 4 | 1 | 3/6 | Network Security |
| 14 | [Intrusion detection, base rates and audit data](#ids) | 5 | 1 | 4 | 3/6 | Firewalls, Tunneling and IDS |
| 15 | [SQL injection and prepared statements](#sql) | 5 | 4 | 1 | 3/6 | Web and Database Security |
| 16 | [Security principles and scenario analysis](#principles) | 5 | 3 | 2 | 3/6 | Introduction |
| 17 | [Adware, spyware and malware economics](#adware) | 4 | 3 | 1 | 4/6 | Malware |
| 18 | [Block-cipher modes, CBC and ciphertext manipulation](#modes) | 4 | 2 | 2 | 4/6 | Cryptography, Hashes and Digital Signatures |
| 19 | [Botnet creation, C&C and malicious agents](#botnet) | 4 | 4 | 0 | 4/6 | Malware |
| 20 | [Diffie–Hellman calculations and authentication](#dh) | 4 | 4 | 0 | 4/6 | Cryptography, Hashes and Digital Signatures |
| 21 | [ARP spoofing, MITM and detection](#arp) | 4 | 4 | 0 | 3/6 | Network Security |
| 22 | [Biometrics, authentication factors, SIM and RFID](#auth) | 4 | 2 | 2 | 3/6 | Physical Security |
| 23 | [CIA, attacker models and security scope](#goals) | 4 | 2 | 2 | 3/6 | Introduction |
| 24 | [Certificates, CA trust and key binding](#cert) | 4 | 3 | 1 | 3/6 | Cryptography, Hashes and Digital Signatures |
| 25 | [StackGuard, ASLR and memory-corruption defenses](#canary) | 4 | 1 | 3 | 3/6 | Buffer Overflow |
| 26 | [Access matrices, ACLs, capabilities and RBAC](#access) | 3 | 2 | 1 | 3/6 | Introduction |
| 27 | [Encrypted, polymorphic and metamorphic viruses](#stealth) | 3 | 3 | 0 | 3/6 | Malware |
| 28 | [Reconnaissance, fingerprinting and vulnerability assessment](#recon) | 3 | 3 | 0 | 3/6 | Firewalls, Tunneling and IDS |
| 29 | [Rootkit cloaking, hooking and DLL injection](#rootkit) | 3 | 2 | 1 | 3/6 | Malware |
| 30 | [SYN flooding and stateless SYN cookies](#syn) | 3 | 3 | 0 | 3/6 | Network Security |
| 31 | [CSRF and cookie-authenticated requests](#csrf) | 3 | 1 | 2 | 2/6 | Web and Database Security |
| 32 | [DES/AES internals, P/S boxes and multiple-DES strength](#block) | 3 | 0 | 3 | 2/6 | Cryptography, Hashes and Digital Signatures |
| 33 | [Password guessing, recovery and search-space calculations](#password) | 3 | 0 | 3 | 2/6 | Introduction |
| 34 | [RSA encryption and correctness](#rsa) | 3 | 3 | 0 | 2/6 | Cryptography, Hashes and Digital Signatures |
| 35 | [Pin-tumbler locks and master-key extensions](#physical) | 3 | 1 | 2 | 1/6 | Physical Security |
| 36 | [DHCP starvation, spoofing and defenses](#dhcp) | 2 | 2 | 0 | 2/6 | Network Security |
| 37 | [HTTP/HTTPS and browser trust](#web) | 2 | 0 | 2 | 2/6 | Web and Database Security |
| 38 | [Switch MAC-table flooding and port security](#switch) | 2 | 2 | 0 | 2/6 | Network Security |
| 39 | [Unix permissions, setuid and filesystem access](#files) | 2 | 1 | 1 | 2/6 | Filesystem Security |
| 40 | [VPN and IPsec AH/ESP encapsulation](#vpn) | 2 | 2 | 0 | 2/6 | Firewalls, Tunneling and IDS |
| 41 | [Backdoors, logic bombs and insider abuse](#insider) | 2 | 2 | 0 | 1/6 | Malware |
| 42 | [Modular arithmetic, Fermat, Euler and inverses](#number) | 2 | 1 | 1 | 1/6 | Cryptography, Hashes and Digital Signatures |
| 43 | [Return-to-libc and calling conventions](#retlibc) | 2 | 0 | 2 | 1/6 | Buffer Overflow |
| 44 | [Symmetric/public-key models and Caesar as symmetric encryption](#keymodels) | 2 | 1 | 1 | 1/6 | Cryptography, Hashes and Digital Signatures |
| 45 | [Faraday shielding and physical information leakage](#emanations) | 1 | 0 | 1 | 1/6 | Physical Security |
| 46 | [Format-string reads and writes](#format) | 1 | 0 | 1 | 1/6 | Buffer Overflow |

A question-level extension flag applies to the whole mixed question. It does not claim that every linked topic is missing from the slides. Consult the per-question note for the particular missing task.

## Slide decks ranked by unique mapped questions

| Deck | Distinct questions | Papers / 6 |
|---|---:|---:|
| Cryptography, Hashes and Digital Signatures | 35 | 6/6 |
| Malware | 20 | 6/6 |
| Firewalls, Tunneling and IDS | 20 | 6/6 |
| Web and Database Security | 20 | 6/6 |
| Network Security | 18 | 6/6 |
| Introduction | 15 | 5/6 |
| Buffer Overflow | 11 | 4/6 |
| Physical Security | 8 | 3/6 |
| DNS Security | 7 | 5/6 |
| Operating Systems Security | 6 | 3/6 |
| Filesystem Security | 2 | 2/6 |

## Questions under slide deck → exact topic

## Introduction

[Ch01-Introduction.pdf](<../slides/Ch01-Introduction.pdf>)

<a id="principles"></a>
### Security principles and scenario analysis — 5 questions

**Study:** deck PDF pp. 11–16; handwritten-note PDF pp. 2, 13–15.

**2023–24 · Q1(b) · 10 marks · direct** · [paper p. 2](<../../CSE405-Security_Merged.pdf#page=2>) · [Solution A002](../solutions/SOLUTIONS.html#a002)

**Exact task:** Match five scenarios to security principles.

Match principles to a valet key, bypassable laptop screen lock, irreversible water-damage sticker, bank recovery questions overridden by a representative, and encryption at rest and in transit.

**2022–23 · Q1(a) · 10 marks · direct** · [paper p. 11](<../../CSE405-Security_Merged.pdf#page=11>) · [Solution A021](../solutions/SOLUTIONS.html#a021)

**Exact task:** Least privilege versus separation; why record compromise?.

Differentiate least privilege and separation of privilege, and explain the importance of compromise recording with examples.

**2020–21 · Q1(c) · 11 marks · direct** · [paper p. 18](<../../CSE405-Security_Merged.pdf#page=18>) · [Solution A071](../solutions/SOLUTIONS.html#a071)

**Exact task:** Why compromise recording matters and which tools support it.

Explain the importance of compromise recording and name tools used for it.

**2020–21 · Q2(b) · 12 marks · partial** · [paper p. 18](<../../CSE405-Security_Merged.pdf#page=18>) · [Solution A073](../solutions/SOLUTIONS.html#a073)

**Exact task:** Mismatched boarding-pass and identity checks.

Explain how online-printable boarding passes permit a no-fly-list bypass in the described airport checks, and fix the weakness.

**Coverage / reading note:** An application of complete mediation/authentication; the exact airport workflow is in the paper.

**2020–21 · Q8(a) · 15 marks · partial** · [paper p. 20](<../../CSE405-Security_Merged.pdf#page=20>) · [Solution A087](../solutions/SOLUTIONS.html#a087)

**Exact task:** Audit scanf, privileged file opening and a name-based access race.

Analyze attacks on the printed C program (code on p. 21): scanf into buffer[60], fopen(fn,"a+"), access(fn,W_OK), fwrite; state environmental assumptions.

**Coverage / reading note:** Unsafe C, Unix privileges and complete-mediation principles support the answer; the exact race analysis is an application.

<a id="goals"></a>
### CIA, attacker models and security scope — 4 questions

**Study:** deck PDF pp. 1–10; handwritten-note PDF pp. 1–12.

**2023–24 · Q5(a) · 15 marks · partial** · [paper p. 7](<../../CSE405-Security_Merged.pdf#page=7>) · [Solution A013](../solutions/SOLUTIONS.html#a013)

**Exact task:** Short concepts; answer any three of five.

Briefly explain any three, with diagrams where appropriate: (i) the CIA properties of cryptography, (ii) confusion and diffusion, (iii) message authentication code, (iv) homograph phishing attack, (v) clickjacking.

**Coverage / reading note:** Only the CIA and MAC choices are explicit in Sec A; confusion/diffusion, homographs and clickjacking extend the decks. The 15 marks belong to the whole optional subquestion.

**2021–22 · Q1(a) · 5 marks · partial** · [paper p. 15](<../../CSE405-Security_Merged.pdf#page=15>) · [Solution A043](../solutions/SOLUTIONS.html#a043)

**Exact task:** Information, IT and cybersecurity scope diagram.

Illustrate the relationship between information security, cybersecurity and IT security with a Venn diagram.

**Coverage / reading note:** The introduction defines CIA and security, but does not specify this three-set taxonomy.

**2021–22 · Q2(a) · 5 marks · direct** · [paper p. 15](<../../CSE405-Security_Merged.pdf#page=15>) · [Solution A046](../solutions/SOLUTIONS.html#a046)

**Exact task:** Attacks versus information-security CIA goals.

Categorize security attacks with respect to C.I.A. goals.

**Coverage / reading note:** Information-security CIA uses Availability; Lecture 1 supplies the general desired-property/threat-model context.

**2020–21 · Q1(b) · 12 marks · direct** · [paper p. 18](<../../CSE405-Security_Merged.pdf#page=18>) · [Solution A070](../solutions/SOLUTIONS.html#a070)

**Exact task:** Selective packet dropping against a competitor.

An ISP deliberately drops 25% of a competing provider’s VoIP packets traversing its routers. Identify the attack.

<a id="access"></a>
### Access matrices, ACLs, capabilities and RBAC — 3 questions

**Study:** deck PDF pp. 17–19; handwritten-note PDF pp. 16, 37.

**2022–23 · Q2(b) · 12 marks · direct** · [paper p. 11](<../../CSE405-Security_Merged.pdf#page=11>) · [Solution A025](../solutions/SOLUTIONS.html#a025)

**Exact task:** Why owner-only access cannot replace access-control systems.

Give at least two scenarios in which users other than a file owner need access, refuting a proposal to restrict all file permissions to owners only.

**2021–22 · Q8(a) · 12 marks · partial** · [paper p. 17](<../../CSE405-Security_Merged.pdf#page=17>) · [Solution A066](../solutions/SOLUTIONS.html#a066)

**Exact task:** Delegation through GRANT OPTION and revocation dependencies.

Analyze GRANT SELECT ON employees TO Alice WITH GRANT OPTION and revoke access safely when Alice leaves.

**Coverage / reading note:** Access-control delegation is an application of matrices/ACLs; DBMS-specific grant/revoke syntax is not taught in WebDB-security.

**2020–21 · Q2(a) · 12 marks · direct** · [paper p. 18](<../../CSE405-Security_Merged.pdf#page=18>) · [Solution A072](../solutions/SOLUTIONS.html#a072)

**Exact task:** RBAC diagram, benefits and limitations.

Define role-based access control with a figure, benefits and drawbacks.

<a id="password"></a>
### Password guessing, recovery and search-space calculations — 3 questions

**Study:** deck PDF pp. 26–29; handwritten-note PDF pp. 17–18, 35–36.

**2022–23 · Q2(a) · 12 marks · partial** · [paper p. 11](<../../CSE405-Security_Merged.pdf#page=11>) · [Solution A024](../solutions/SOLUTIONS.html#a024)

**Exact task:** Brute-force throughput under a password-expiration policy.

A password policy requires uppercase, lowercase, numeric and special characters, minimum length 10, with monthly password changes. Estimate the minimum guesses per second needed to crack a credential, showing the calculations.

**Coverage / reading note:** The question does not specify the exact special-character alphabet or a precise success probability. State assumptions. Lecture 8 covers guessing attacks but not this exact counting problem.

**2019–20 · Q1(c) · 11 marks · partial** · [paper p. 22](<../../CSE405-Security_Merged.pdf#page=22>) · [Solution A091](../solutions/SOLUTIONS.html#a091)

**Exact task:** Public security questions and password-reset account takeover.

Attackers reset Sarah Palin’s email password using publicly available personal information such as birthday, ZIP code and security-question answers. Identify the attack and evaluate the security of this password-reset feature.

**Coverage / reading note:** Account-recovery security is related to Lecture 8 password guessing; the specific recovery scenario is not taught in the deck. The CT4 guide pp. 52–53 discusses it.

**2019–20 · Q2(b) · 12 marks · partial** · [paper p. 22](<../../CSE405-Security_Merged.pdf#page=22>) · [Solution A093](../solutions/SOLUTIONS.html#a093)

**Exact task:** Password-space size and average brute-force time.

How many 10-character passwords can be made from all 128 ASCII characters? If an attacker tests one candidate per microsecond, how long does guessing take on average?

**Coverage / reading note:** Lecture 8 gives the guessing-attack background; the numerical model is specified by the paper.

## Physical Security

[Ch02-Physical-Security.pdf](<../slides/Ch02-Physical-Security.pdf>)

<a id="auth"></a>
### Biometrics, authentication factors, SIM and RFID — 4 questions

**Study:** deck PDF pp. 9–27; handwritten-note PDF pp. 20–22.

**2021–22 · Q1(b) · 10 marks · direct** · [paper p. 15](<../../CSE405-Security_Merged.pdf#page=15>) · [Solution A044](../solutions/SOLUTIONS.html#a044)

**Exact task:** Biometric requirements, recognition pipeline and privacy.

State biometric identification requirements, describe the process, and discuss privacy-preserving challenges.

**2020–21 · Q2(b) · 12 marks · partial** · [paper p. 18](<../../CSE405-Security_Merged.pdf#page=18>) · [Solution A073](../solutions/SOLUTIONS.html#a073)

**Exact task:** Mismatched boarding-pass and identity checks.

Explain how online-printable boarding passes permit a no-fly-list bypass in the described airport checks, and fix the weakness.

**Coverage / reading note:** An application of complete mediation/authentication; the exact airport workflow is in the paper.

**2018–19 · Q8(a) · 6 marks · direct** · [paper p. 28](<../../CSE405-Security_Merged.pdf#page=28>) · [Solution A131](../solutions/SOLUTIONS.html#a131)

**Exact task:** Good biometric criteria.

Name essential and desirable characteristics of biometric authentication.

**2018–19 · Q9(b) · 3 marks · partial** · [paper p. 28](<../../CSE405-Security_Merged.pdf#page=28>) · [Solution A134](../solutions/SOLUTIONS.html#a134)

**Exact task:** Expand ICCID, IMSI and ASLR.

Write the full forms of ICCID, IMSI and ASLR.

**Coverage / reading note:** SIM identifiers are in the physical deck/notes; ASLR is a memory-defense extension.

<a id="physical"></a>
### Pin-tumbler locks and master-key extensions — 3 questions

**Study:** deck PDF pp. 4–8; handwritten-note PDF pp. 19.

**2018–19 · Q6(b) · 7 marks · direct** · [paper p. 27](<../../CSE405-Security_Merged.pdf#page=27>) · [Solution A128](../solutions/SOLUTIONS.html#a128)

**Exact task:** Pin-tumbler cross section.

Draw a pin-tumbler lock cross section and label its parts.

**2018–19 · Q7(a) · 3 marks · partial** · [paper p. 27](<../../CSE405-Security_Merged.pdf#page=27>) · [Solution A129](../solutions/SOLUTIONS.html#a129)

**Exact task:** Count additional keys after three master wafers.

A five-pin lock has driver pins of height 5 and key pins 2,4,5,2,6. Add one master wafer in each of three selected chambers. How many additional keys theoretically open it?

**Coverage / reading note:** The deck teaches basic pin-tumbler operation; master-wafer combinatorics is an extension.

**2018–19 · Q7(b) · 12 marks · partial** · [paper p. 27](<../../CSE405-Security_Merged.pdf#page=27>) · [Solution A130](../solutions/SOLUTIONS.html#a130)

**Exact task:** Construct a lock accepting both stated keys.

Given L1 key-pin heights (2,4,5,2,6) and L2 (4,2,5,5,6), driver heights 5, design L3 with master wafers so both keys work, and show K1 opening it.

**Coverage / reading note:** Master-key construction extends the basic lock slides; the geometric interpretation is stated explicitly.

<a id="emanations"></a>
### Faraday shielding and physical information leakage — 1 questions

**Study:** deck PDF pp. 28–32; handwritten-note PDF pp. 23.

**2018–19 · Q8(b) · 9 marks · partial** · [paper p. 28](<../../CSE405-Security_Merged.pdf#page=28>) · [Solution A132](../solutions/SOLUTIONS.html#a132)

**Exact task:** Short notes; answer any three of four.

Write short notes on any three: (i) Faraday cage, (ii) blind SQL injection, (iii) impersonation token, (iv) homograph attack.

**Coverage / reading note:** One optional 9-mark subquestion. Faraday cage is explicit; blind SQLi/homographs extend the web deck, and OS impersonation-token details are supplementary. Do not allocate all 9 marks to every choice.

## Operating Systems Security

[Ch03-OS-Security.pdf](<../slides/Ch03-OS-Security.pdf>)

<a id="os"></a>
### OS trust, paging, boot and persistent memory images — 6 questions

**Study:** deck PDF pp. 19–33; handwritten-note PDF pp. 24, 31–36.

**2021–22 · Q4(a) · 5 marks · direct** · [paper p. 16](<../../CSE405-Security_Merged.pdf#page=16>) · [Solution A053](../solutions/SOLUTIONS.html#a053)

**Exact task:** Secrets persisted in swap/hibernation.

Explain how virtual memory or a swap partition can be an attacker target.

**2020–21 · Q1(c) · 11 marks · direct** · [paper p. 18](<../../CSE405-Security_Merged.pdf#page=18>) · [Solution A071](../solutions/SOLUTIONS.html#a071)

**Exact task:** Why compromise recording matters and which tools support it.

Explain the importance of compromise recording and name tools used for it.

**2020–21 · Q2(c) · 11 marks · partial** · [paper p. 18](<../../CSE405-Security_Merged.pdf#page=18>) · [Solution A074](../solutions/SOLUTIONS.html#a074)

**Exact task:** Forensic preservation: master and working images, custody.

Why make two copies of digital evidence? State precautions and how to maintain chain of custody.

**Coverage / reading note:** OS/hibernation notes mention forensic investigation; full acquisition and custody procedures are supplementary.

**2020–21 · Q3(a) · 12 marks · direct** · [paper p. 18](<../../CSE405-Security_Merged.pdf#page=18>) · [Solution A075](../solutions/SOLUTIONS.html#a075)

**Exact task:** Why preserve memory-region boundaries?.

Explain the risks of mixing heap and stack storage and give an example manipulation.

**2019–20 · Q2(c) · 11 marks · partial** · [paper p. 22](<../../CSE405-Security_Merged.pdf#page=22>) · [Solution A094](../solutions/SOLUTIONS.html#a094)

**Exact task:** Verify a reported DoS source and respond with evidence.

A hall administrator says your shared network segment is sending DoS traffic. You deny involvement but are unsure about your roommate. How do you verify and respond?

**Coverage / reading note:** Uses IDS/network logs and OS event logging; incident-handling workflow extends the slides.

**2019–20 · Q5(b) · 14 marks · partial** · [paper p. 24](<../../CSE405-Security_Merged.pdf#page=24>) · [Solution A102](../solutions/SOLUTIONS.html#a102)

**Exact task:** Audit-record fields and statistical intrusion detection.

List useful audit-record fields, explain statistical IDS and identify a weakness.

**Coverage / reading note:** Event logging and IDS sensors are taught; statistical-model design is an extension.

## Buffer Overflow

[Ch03-BufferOverflow.pdf](<../slides/Ch03-BufferOverflow.pdf>)

<a id="buffer"></a>
### Stack/heap corruption and buffer-overflow payload reasoning — 6 questions

**Study:** deck PDF pp. 1–8; handwritten-note PDF pp. 24–30.

**2023–24 · Q1(a) · 10 marks · partial** · [paper p. 1](<../../CSE405-Security_Merged.pdf#page=1>) · [Solution A001](../solutions/SOLUTIONS.html#a001)

**Exact task:** Trace the actual unsafe copies and construct a conditional control-flow payload.

For the printed 32-bit little-endian C program, decide whether hack() can be invoked and give symbolic-address payload pseudocode. All defenses are disabled; main reads 300 bytes into str[30]; overflow_in_action has buffer[300], two heap pointers, strcpy calls and an indirect callback.

**Coverage / reading note:** The source does not fix frame offsets or heap allocator layout. A conditional symbolic payload is justified; an unconditional offset is not.

**2023–24 · Q2(b) · 10 marks · partial** · [paper p. 3](<../../CSE405-Security_Merged.pdf#page=3>) · [Solution A005](../solutions/SOLUTIONS.html#a005)

**Exact task:** Leaked stack address and one-byte saved-frame-pointer overwrite.

32-bit x86 with ASLR: main prints simple[32] address and reads with fgets(simple,32). hack copies nine input bytes backward into buf[8]. Construct inputs for a 31-byte shellcode, identifying necessary stack-layout assumptions.

**Coverage / reading note:** Compiler local ordering, padding and the location of a surviving fake frame are not specified, so the intended off-by-one exploit is conditional.

**2020–21 · Q3(a) · 12 marks · direct** · [paper p. 18](<../../CSE405-Security_Merged.pdf#page=18>) · [Solution A075](../solutions/SOLUTIONS.html#a075)

**Exact task:** Why preserve memory-region boundaries?.

Explain the risks of mixing heap and stack storage and give an example manipulation.

**2020–21 · Q8(a) · 15 marks · partial** · [paper p. 20](<../../CSE405-Security_Merged.pdf#page=20>) · [Solution A087](../solutions/SOLUTIONS.html#a087)

**Exact task:** Audit scanf, privileged file opening and a name-based access race.

Analyze attacks on the printed C program (code on p. 21): scanf into buffer[60], fopen(fn,"a+"), access(fn,W_OK), fwrite; state environmental assumptions.

**Coverage / reading note:** Unsafe C, Unix privileges and complete-mediation principles support the answer; the exact race analysis is an application.

**2019–20 · Q1(b) · 12 marks · partial** · [paper p. 22](<../../CSE405-Security_Merged.pdf#page=22>) · [Solution A090](../solutions/SOLUTIONS.html#a090)

**Exact task:** Heartbleed as an out-of-bounds read.

Define Heartbleed and explain its major consequences.

**Coverage / reading note:** The buffer deck teaches memory-bound errors; the particular OpenSSL case is supplementary.

**2018–19 · Q10 · 15 marks · partial** · [paper p. 29](<../../CSE405-Security_Merged.pdf#page=29>) · [Solution A135](../solutions/SOLUTIONS.html#a135)

**Exact task:** Toy stack frames and an alphabet-only return target.

For the printed main/foo/bar C snippets, draw all frames using supplied addresses and create alphabet-only sample.txt so bar returns directly to main. Each source instruction is stipulated to occupy one byte; integer=4 bytes.

**Coverage / reading note:** Stack reasoning is taught, but this question imposes artificial instruction sizes/frame addresses and leaves the file-read body unspecified.

<a id="canary"></a>
### StackGuard, ASLR and memory-corruption defenses — 4 questions

**Study:** deck PDF pp. 8 (canary); ASLR/code-reuse defenses are extensions; handwritten-note PDF pp. 30.

**2023–24 · Q2(b) · 10 marks · partial** · [paper p. 3](<../../CSE405-Security_Merged.pdf#page=3>) · [Solution A005](../solutions/SOLUTIONS.html#a005)

**Exact task:** Leaked stack address and one-byte saved-frame-pointer overwrite.

32-bit x86 with ASLR: main prints simple[32] address and reads with fgets(simple,32). hack copies nine input bytes backward into buf[8]. Construct inputs for a 31-byte shellcode, identifying necessary stack-layout assumptions.

**Coverage / reading note:** Compiler local ordering, padding and the location of a surviving fake frame are not specified, so the intended off-by-one exploit is conditional.

**2020–21 · Q5(c) · 10 marks · partial** · [paper p. 19](<../../CSE405-Security_Merged.pdf#page=19>) · [Solution A083](../solutions/SOLUTIONS.html#a083)

**Exact task:** Four defenses against return-to-libc.

Briefly explain four countermeasures against return-to-libc attacks.

**Coverage / reading note:** Buffer-overflow basics are taught; code reuse and several defense mechanisms require supplementary material.

**2020–21 · Q7(c) · 10 marks · direct** · [paper p. 20](<../../CSE405-Security_Merged.pdf#page=20>) · [Solution A086](../solutions/SOLUTIONS.html#a086)

**Exact task:** StackGuard check and scope.

Define StackGuard and explain with a diagram how it counters buffer overflow.

**Coverage / reading note:** Overflow PDF p. 8 and handwritten notes p. 30 depict the canary mechanism; implementation limits are explained in the answer.

**2018–19 · Q9(b) · 3 marks · partial** · [paper p. 28](<../../CSE405-Security_Merged.pdf#page=28>) · [Solution A134](../solutions/SOLUTIONS.html#a134)

**Exact task:** Expand ICCID, IMSI and ASLR.

Write the full forms of ICCID, IMSI and ASLR.

**Coverage / reading note:** SIM identifiers are in the physical deck/notes; ASLR is a memory-defense extension.

<a id="retlibc"></a>
### Return-to-libc and calling conventions — 2 questions

**Study:** deck PDF pp. 4–8 (background; libc chaining is an extension); handwritten-note PDF pp. 24–30 (background).

**2020–21 · Q5(c) · 10 marks · partial** · [paper p. 19](<../../CSE405-Security_Merged.pdf#page=19>) · [Solution A083](../solutions/SOLUTIONS.html#a083)

**Exact task:** Four defenses against return-to-libc.

Briefly explain four countermeasures against return-to-libc attacks.

**Coverage / reading note:** Buffer-overflow basics are taught; code reuse and several defense mechanisms require supplementary material.

**2020–21 · Q6(c) · 10 marks · partial** · [paper p. 20](<../../CSE405-Security_Merged.pdf#page=20>) · [Solution A085](../solutions/SOLUTIONS.html#a085)

**Exact task:** Place system arguments using 32-bit cdecl.

Using diagrams, determine placement of the system() argument in a return-to-libc attack.

**Coverage / reading note:** The supplied C/stack material is background; the cdecl libc-chain layout is an extension.

<a id="format"></a>
### Format-string reads and writes — 1 questions

**Study:** deck PDF pp. 1–8 (background only; format strings are an extension); handwritten-note PDF pp. 24–30 (background).

**2018–19 · Q9(a) · 12 marks · partial** · [paper p. 28](<../../CSE405-Security_Merged.pdf#page=28>) · [Solution A133](../solutions/SOLUTIONS.html#a133)

**Exact task:** Four format-string tasks using the stated stack-word cursor.

For gets(user_input); printf(user_input), construct inputs to print secret1, change secret1, print secret2 and print secret3. Cursor starts 0xaabbcc20; secret1=0xaabbcc34, secret2=0xaabbcc38, secret3=0x11223344, input=0xaabbcc50; integers are 4 bytes.

**Coverage / reading note:** The slides teach unsafe C but do not develop format-string exploitation; the paper supplies a special cursor model.

## Filesystem Security

[Ch03-FilesystemSecurity.pdf](<../slides/Ch03-FilesystemSecurity.pdf>)

<a id="files"></a>
### Unix permissions, setuid and filesystem access — 2 questions

**Study:** deck PDF pp. 1–19; handwritten-note PDF pp. 28–29, 37–40.

**2020–21 · Q8(a) · 15 marks · partial** · [paper p. 20](<../../CSE405-Security_Merged.pdf#page=20>) · [Solution A087](../solutions/SOLUTIONS.html#a087)

**Exact task:** Audit scanf, privileged file opening and a name-based access race.

Analyze attacks on the printed C program (code on p. 21): scanf into buffer[60], fopen(fn,"a+"), access(fn,W_OK), fwrite; state environmental assumptions.

**Coverage / reading note:** Unsafe C, Unix privileges and complete-mediation principles support the answer; the exact race analysis is an application.

**2019–20 · Q3(c) · 11 marks · direct** · [paper p. 22](<../../CSE405-Security_Merged.pdf#page=22>) · [Solution A097](../solutions/SOLUTIONS.html#a097)

**Exact task:** Setuid/chmod under the paper’s no-revert assumption.

Alice wants Bob’s photo program without exposing her confidential files; Bob wants his code unreadable to Alice. Use Unix setuid/chmod, assume the process cannot revert to real UID after adopting its setuid identity, and consider exfiltration by malicious code.

## Malware

[Ch04-Malware.pdf](<../slides/Ch04-Malware.pdf>)

<a id="worm"></a>
### Worm propagation, epidemic models and case studies — 6 questions

**Study:** deck PDF pp. 31–39; handwritten-note PDF pp. 8–9, 49–51.

**2023–24 · Q3(b) · 5 marks · direct** · [paper p. 4](<../../CSE405-Security_Merged.pdf#page=4>) · [Solution A008](../solutions/SOLUTIONS.html#a008)

**Exact task:** Code Red patch status and propagation.

Did Code Red exploit a zero-day vulnerability? Explain its propagation.

**2022–23 · Q4(d) · 6 marks · direct** · [paper p. 12](<../../CSE405-Security_Merged.pdf#page=12>) · [Solution A033](../solutions/SOLUTIONS.html#a033)

**Exact task:** Zero-day meaning and detection limits.

Define a zero-day attack and explain why it is dangerous.

**2020–21 · Q1(a) · 12 marks · direct** · [paper p. 18](<../../CSE405-Security_Merged.pdf#page=18>) · [Solution A069](../solutions/SOLUTIONS.html#a069)

**Exact task:** WannaCry vulnerability, success and zero-day status.

Identify WannaCry’s main vulnerability, why it succeeded and whether it was a zero-day attack.

**2020–21 · Q3(c) · 11 marks · direct** · [paper p. 18](<../../CSE405-Security_Merged.pdf#page=18>) · [Solution A077](../solutions/SOLUTIONS.html#a077)

**Exact task:** Derive the SI epidemic worm model.

Explain an epidemic model of worm propagation with a figure.

**2019–20 · Q3(a) · 12 marks · partial** · [paper p. 22](<../../CSE405-Security_Merged.pdf#page=22>) · [Solution A095](../solutions/SOLUTIONS.html#a095)

**Exact task:** Three reasons ransomware grew during COVID-era disruption.

Give three major reasons ransomware attacks increased during the COVID-19 pandemic.

**Coverage / reading note:** Malware economics is taught, but COVID-specific comparative evidence is not supplied.

**2018–19 · Q2(d) · 8 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · [Solution A117](../solutions/SOLUTIONS.html#a117)

**Exact task:** Morris worm speed and consequences.

Why did the Morris worm spread rapidly and what were the consequences?

<a id="adware"></a>
### Adware, spyware and malware economics — 4 questions

**Study:** deck PDF pp. 55–60; handwritten-note PDF pp. 45, 54–55.

**2022–23 · Q3(c) · 11 marks · direct** · [paper p. 11](<../../CSE405-Security_Merged.pdf#page=11>) · [Solution A029](../solutions/SOLUTIONS.html#a029)

**Exact task:** Adware data flow and spyware revenue.

Explain adware operation with a figure and why its author benefits from adding spyware.

**2021–22 · Q5(a) · 12 marks · direct** · [paper p. 16](<../../CSE405-Security_Merged.pdf#page=16>) · [Solution A057](../solutions/SOLUTIONS.html#a057)

**Exact task:** Why sell many signature-distinct variants of one exploit?.

Explain the financial benefits of creating many malware variants exploiting the same popular-software vulnerability but having different signatures.

**2019–20 · Q3(a) · 12 marks · partial** · [paper p. 22](<../../CSE405-Security_Merged.pdf#page=22>) · [Solution A095](../solutions/SOLUTIONS.html#a095)

**Exact task:** Three reasons ransomware grew during COVID-era disruption.

Give three major reasons ransomware attacks increased during the COVID-19 pandemic.

**Coverage / reading note:** Malware economics is taught, but COVID-specific comparative evidence is not supplied.

**2018–19 · Q2(b) · 8 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · [Solution A115](../solutions/SOLUTIONS.html#a115)

**Exact task:** Why adware authors add spyware.

Explain why spyware benefits an adware author.

<a id="botnet"></a>
### Botnet creation, C&C and malicious agents — 4 questions

**Study:** deck PDF pp. 40–45; handwritten-note PDF pp. 5, 51–52.

**2021–22 · Q5(c) · 11 marks · direct** · [paper p. 16](<../../CSE405-Security_Merged.pdf#page=16>) · [Solution A059](../solutions/SOLUTIONS.html#a059)

**Exact task:** Disrupting C&C through coordinated investigation.

Formulate a process to take down a botnet command-and-control server.

**2020–21 · Q4(b) · 12 marks · direct** · [paper p. 19](<../../CSE405-Security_Merged.pdf#page=19>) · [Solution A079](../solutions/SOLUTIONS.html#a079)

**Exact task:** Value and defense of an internal malware agent.

Explain why an attacker installs an agent inside a corporate network, delivery methods and prevention; assess whether a firewall can help.

**2019–20 · Q2(a) · 12 marks · direct** · [paper p. 22](<../../CSE405-Security_Merged.pdf#page=22>) · [Solution A092](../solutions/SOLUTIONS.html#a092)

**Exact task:** Botnet architecture and distributed floods.

Explain botnet components and how they launch DDoS, with a figure.

**2018–19 · Q3(d) · 10 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · [Solution A121](../solutions/SOLUTIONS.html#a121)

**Exact task:** Bot creation, control and uses.

Explain botnet creation/control and possible activities.

<a id="stealth"></a>
### Encrypted, polymorphic and metamorphic viruses — 3 questions

**Study:** deck PDF pp. 22–30, 57–58; handwritten-note PDF pp. 46–49, 54–56.

**2021–22 · Q5(a) · 12 marks · direct** · [paper p. 16](<../../CSE405-Security_Merged.pdf#page=16>) · [Solution A057](../solutions/SOLUTIONS.html#a057)

**Exact task:** Why sell many signature-distinct variants of one exploit?.

Explain the financial benefits of creating many malware variants exploiting the same popular-software vulnerability but having different signatures.

**2019–20 · Q3(b) · 12 marks · direct** · [paper p. 22](<../../CSE405-Security_Merged.pdf#page=22>) · [Solution A096](../solutions/SOLUTIONS.html#a096)

**Exact task:** Encrypted-virus structure and detection.

Explain how an encrypted virus is formed and how to detect it.

**2018–19 · Q2(a) · 7 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · [Solution A114](../solutions/SOLUTIONS.html#a114)

**Exact task:** Polymorphic versus metamorphic viruses with examples.

Distinguish polymorphic and metamorphic viruses and give two examples of each.

<a id="rootkit"></a>
### Rootkit cloaking, hooking and DLL injection — 3 questions

**Study:** deck PDF pp. 46–54; handwritten-note PDF pp. 28, 53–54.

**2022–23 · Q3(b) · 12 marks · direct** · [paper p. 11](<../../CSE405-Security_Merged.pdf#page=11>) · [Solution A028](../solutions/SOLUTIONS.html#a028)

**Exact task:** Kernel API hooking and rootkit concealment.

List rootkit features and explain kernel-level hiding through function hooking.

**2021–22 · Q3(a) · 5 marks · partial** · [paper p. 15](<../../CSE405-Security_Merged.pdf#page=15>) · [Solution A049](../solutions/SOLUTIONS.html#a049)

**Exact task:** DLL injection and inherited process authority.

Explain why DLL injection poses high security risks.

**Coverage / reading note:** Rootkit/API filtering and process hijacking are taught; detailed DLL-injection mechanics are not.

**2018–19 · Q2(c) · 12 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · [Solution A116](../solutions/SOLUTIONS.html#a116)

**Exact task:** Function hooking and three concealment targets.

Define rootkit function hooking, its danger and three examples of avoiding detection.

<a id="insider"></a>
### Backdoors, logic bombs and insider abuse — 2 questions

**Study:** deck PDF pp. 3–10; handwritten-note PDF pp. 41–42.

**2018–19 · Q1(c) · 9 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · [Solution A112](../solutions/SOLUTIONS.html#a112)

**Exact task:** Threshold-triggered banking-data exfiltration.

A programmer secretly emails account details whenever a balance exceeds USD 5,000. Identify the attack and risks.

**2018–19 · Q3(a) · 6 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · [Solution A118](../solutions/SOLUTIONS.html#a118)

**Exact task:** Easter egg versus logic bomb.

Give examples of an Easter egg and a logic bomb.

## Network Security

[Ch05-NetworkSecurity.pdf](<../slides/Ch05-NetworkSecurity.pdf>)

<a id="tcp"></a>
### TCP hijacking, spoofed segments and optimistic ACKs — 7 questions

**Study:** deck PDF pp. 20–23 (optimistic ACK details are extensions); handwritten-note PDF pp. 65–67.

**2023–24 · Q2(c) · 15 marks · partial** · [paper p. 3](<../../CSE405-Security_Merged.pdf#page=3>) · [Solution A006](../solutions/SOLUTIONS.html#a006)

**Exact task:** Off-path TCP injection and establishing a replacement connection.

Using the printed TCP diagram (continued on p. 4), evaluate malicious actions by an off-path attacker and impersonating the client after it resets the connection.

**Coverage / reading note:** The network deck covers TCP state/hijacking; the modern blind-reset and ISN details extend it.

**2023–24 · Q3(a) · 10 marks · direct** · [paper p. 4](<../../CSE405-Security_Merged.pdf#page=4>) · [Solution A007](../solutions/SOLUTIONS.html#a007)

**Exact task:** Can NIDS/firewall plus HTTPS always stop five attacks?.

An HTTPS-only server farm has a NIDS and firewall processing incoming requests. With an on-path attacker, assess RST injection, reflected XSS, SYN flooding, DNS spoofing and DDoS.

**2023–24 · Q4(a) · 10 marks · direct** · [paper p. 5](<../../CSE405-Security_Merged.pdf#page=5>) · [Solution A010](../solutions/SOLUTIONS.html#a010)

**Exact task:** UDP chargen/echo feedback versus TCP handshake.

JULY on UDP port 36 returns 36–360 random characters; PROTIDHONI on port 5 echoes its input. Give one empty UDP packet creating a feedback loop between X and Y, then assess a single spoofed TCP SYN when both services require a handshake.

**2021–22 · Q6(a) · 12 marks · partial** · [paper p. 17](<../../CSE405-Security_Merged.pdf#page=17>) · [Solution A060](../solutions/SOLUTIONS.html#a060)

**Exact task:** Detect optimistic ACKs by withholding a segment.

Explain how randomly dropping data segments at the sender helps detect optimistic TCP ACK attacks.

**Coverage / reading note:** The network deck explains TCP ACK state; optimistic-ACK probing is beyond its explicit treatment.

**2019–20 · Q4(c) · 11 marks · partial** · [paper p. 23](<../../CSE405-Security_Merged.pdf#page=23>) · [Solution A100](../solutions/SOLUTIONS.html#a100)

**Exact task:** Withheld-segment detection of optimistic ACKs.

Explain with examples how sender-side random segment dropping detects optimistic ACKs.

**Coverage / reading note:** Optimistic-ACK details extend the TCP-state slides.

**2018–19 · Q3(b) · 9 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · [Solution A119](../solutions/SOLUTIONS.html#a119)

**Exact task:** Complete TCP hijacking.

Explain with a diagram how to perform TCP session hijacking.

**2018–19 · Q3(c) · 10 marks · partial** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · [Solution A120](../solutions/SOLUTIONS.html#a120)

**Exact task:** Optimistic TCP ACK mechanism and mitigation.

Define optimistic TCP ACK attack and give mitigations.

**Coverage / reading note:** The deck covers TCP state but not optimistic-ACK algorithms.

<a id="dos"></a>
### DoS/DDoS, reflection and resource exhaustion — 5 questions

**Study:** deck PDF pp. 24–29; handwritten-note PDF pp. 67–68.

**2023–24 · Q3(a) · 10 marks · direct** · [paper p. 4](<../../CSE405-Security_Merged.pdf#page=4>) · [Solution A007](../solutions/SOLUTIONS.html#a007)

**Exact task:** Can NIDS/firewall plus HTTPS always stop five attacks?.

An HTTPS-only server farm has a NIDS and firewall processing incoming requests. With an on-path attacker, assess RST injection, reflected XSS, SYN flooding, DNS spoofing and DDoS.

**2023–24 · Q4(a) · 10 marks · direct** · [paper p. 5](<../../CSE405-Security_Merged.pdf#page=5>) · [Solution A010](../solutions/SOLUTIONS.html#a010)

**Exact task:** UDP chargen/echo feedback versus TCP handshake.

JULY on UDP port 36 returns 36–360 random characters; PROTIDHONI on port 5 echoes its input. Give one empty UDP packet creating a feedback loop between X and Y, then assess a single spoofed TCP SYN when both services require a handshake.

**2020–21 · Q1(b) · 12 marks · direct** · [paper p. 18](<../../CSE405-Security_Merged.pdf#page=18>) · [Solution A070](../solutions/SOLUTIONS.html#a070)

**Exact task:** Selective packet dropping against a competitor.

An ISP deliberately drops 25% of a competing provider’s VoIP packets traversing its routers. Identify the attack.

**2019–20 · Q2(a) · 12 marks · direct** · [paper p. 22](<../../CSE405-Security_Merged.pdf#page=22>) · [Solution A092](../solutions/SOLUTIONS.html#a092)

**Exact task:** Botnet architecture and distributed floods.

Explain botnet components and how they launch DDoS, with a figure.

**2019–20 · Q2(c) · 11 marks · partial** · [paper p. 22](<../../CSE405-Security_Merged.pdf#page=22>) · [Solution A094](../solutions/SOLUTIONS.html#a094)

**Exact task:** Verify a reported DoS source and respond with evidence.

A hall administrator says your shared network segment is sending DoS traffic. You deny involvement but are unsure about your roommate. How do you verify and respond?

**Coverage / reading note:** Uses IDS/network logs and OS event logging; incident-handling workflow extends the slides.

<a id="arp"></a>
### ARP spoofing, MITM and detection — 4 questions

**Study:** deck PDF pp. 5–12; handwritten-note PDF pp. 58–61.

**2023–24 · Q2(a) · 10 marks · direct** · [paper p. 3](<../../CSE405-Security_Merged.pdf#page=3>) · [Solution A004](../solutions/SOLUTIONS.html#a004)

**Exact task:** Rogue DHCP gateway and MITM with the correct gateway.

Attacker IP is 10.10.10.32; router/DHCP server is 10.10.10.4. Give a forged client IP/default router for Alice. If the correct router is supplied, explain another way to become MITM.

**2020–21 · Q4(a) · 12 marks · direct** · [paper p. 19](<../../CSE405-Security_Merged.pdf#page=19>) · [Solution A078](../solutions/SOLUTIONS.html#a078)

**Exact task:** ARP prevention, monitoring and locating the attacking port.

Give ARP-spoofing defenses and ways to identify an attacking host on the internal network.

**2018–19 · Q3(b) · 9 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · [Solution A119](../solutions/SOLUTIONS.html#a119)

**Exact task:** Complete TCP hijacking.

Explain with a diagram how to perform TCP session hijacking.

**2018–19 · Q4(c) · 9 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · [Solution A124](../solutions/SOLUTIONS.html#a124)

**Exact task:** Rule-based ARP-spoofing detection.

Give rules a rule-based IDS can use to detect ARP spoofing.

<a id="syn"></a>
### SYN flooding and stateless SYN cookies — 3 questions

**Study:** deck PDF pp. 30–34; handwritten-note PDF pp. 69–70.

**2023–24 · Q3(a) · 10 marks · direct** · [paper p. 4](<../../CSE405-Security_Merged.pdf#page=4>) · [Solution A007](../solutions/SOLUTIONS.html#a007)

**Exact task:** Can NIDS/firewall plus HTTPS always stop five attacks?.

An HTTPS-only server farm has a NIDS and firewall processing incoming requests. With an on-path attacker, assess RST injection, reflected XSS, SYN flooding, DNS spoofing and DDoS.

**2022–23 · Q1(b) · 12 marks · direct** · [paper p. 11](<../../CSE405-Security_Merged.pdf#page=11>) · [Solution A022](../solutions/SOLUTIONS.html#a022)

**Exact task:** SYN backlog exhaustion and cookie validation.

Explain SYN flooding with a figure and evaluate SYN cookies.

**2021–22 · Q7(a) · 12 marks · direct** · [paper p. 17](<../../CSE405-Security_Merged.pdf#page=17>) · [Solution A063](../solutions/SOLUTIONS.html#a063)

**Exact task:** SYN-cookie defense.

Explain how SYN cookies defend against SYN flooding.

<a id="dhcp"></a>
### DHCP starvation, spoofing and defenses — 2 questions

**Study:** deck PDF pp. 16–19; handwritten-note PDF pp. 63–65.

**2023–24 · Q2(a) · 10 marks · direct** · [paper p. 3](<../../CSE405-Security_Merged.pdf#page=3>) · [Solution A004](../solutions/SOLUTIONS.html#a004)

**Exact task:** Rogue DHCP gateway and MITM with the correct gateway.

Attacker IP is 10.10.10.32; router/DHCP server is 10.10.10.4. Give a forged client IP/default router for Alice. If the correct router is supplied, explain another way to become MITM.

**2022–23 · Q1(c) · 13 marks · direct** · [paper p. 11](<../../CSE405-Security_Merged.pdf#page=11>) · [Solution A023](../solutions/SOLUTIONS.html#a023)

**Exact task:** DHCP starvation message flow and rogue-server relationship.

Explain DHCP starvation with a message diagram and analyze its relation to DHCP spoofing.

<a id="switch"></a>
### Switch MAC-table flooding and port security — 2 questions

**Study:** deck PDF pp. 13–15; handwritten-note PDF pp. 61–63.

**2022–23 · Q3(a) · 12 marks · direct** · [paper p. 11](<../../CSE405-Security_Merged.pdf#page=11>) · [Solution A027](../solutions/SOLUTIONS.html#a027)

**Exact task:** CAM exhaustion and switch behavior.

Explain MAC flooding with topology, effects on a switch and attacker benefits.

**2019–20 · Q4(b) · 12 marks · direct** · [paper p. 23](<../../CSE405-Security_Merged.pdf#page=23>) · [Solution A099](../solutions/SOLUTIONS.html#a099)

**Exact task:** Making a switch flood unknown destinations.

Why make a switch behave like a hub, what attack does this and how can it be prevented?

## DNS Security

[Ch06-1-NetworkDNS.pdf](<../slides/Ch06-1-NetworkDNS.pdf>)

<a id="dns"></a>
### DNS poisoning, Kaminsky races, pharming and DNSSEC — 7 questions

**Study:** deck PDF pp. 27–43; handwritten-note PDF pp. 72–80.

**2023–24 · Q3(a) · 10 marks · direct** · [paper p. 4](<../../CSE405-Security_Merged.pdf#page=4>) · [Solution A007](../solutions/SOLUTIONS.html#a007)

**Exact task:** Can NIDS/firewall plus HTTPS always stop five attacks?.

An HTTPS-only server farm has a NIDS and firewall processing incoming requests. With an on-path attacker, assess RST injection, reflected XSS, SYN flooding, DNS spoofing and DDoS.

**2023–24 · Q3(c) · 20 marks · direct** · [paper p. 4](<../../CSE405-Security_Merged.pdf#page=4>) · [Solution A009](../solutions/SOLUTIONS.html#a009)

**Exact task:** Kaminsky retries, bailiwick, DNS-over-TLS and DNSSEC.

An internal attacker loads many fakeN.buet.ac.bd image names to poison the shared resolver (no source-port randomization). Explain why many images help, whether the same page can poison www.google.com, and the effects of DNS-over-TLS and DNSSEC.

**2022–23 · Q4(a) · 12 marks · direct** · [paper p. 12](<../../CSE405-Security_Merged.pdf#page=12>) · [Solution A030](../solutions/SOLUTIONS.html#a030)

**Exact task:** DNS cache poisoning and three defenses.

Define DNS cache poisoning, explain exploitation and provide three defenses.

**2021–22 · Q6(b) · 12 marks · direct** · [paper p. 17](<../../CSE405-Security_Merged.pdf#page=17>) · [Solution A061](../solutions/SOLUTIONS.html#a061)

**Exact task:** Three DNS poisoning countermeasures.

Design three mechanisms to prevent or mitigate DNS cache poisoning.

**2019–20 · Q4(a) · 12 marks · direct** · [paper p. 23](<../../CSE405-Security_Merged.pdf#page=23>) · [Solution A098](../solutions/SOLUTIONS.html#a098)

**Exact task:** DNS redirection as a MITM precursor.

Explain with a diagram how DNS spoofing can launch MITM.

**2018–19 · Q4(a) · 10 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · [Solution A122](../solutions/SOLUTIONS.html#a122)

**Exact task:** Random-subdomain cache-poisoning advantage.

Why use subdomain DNS cache poisoning, and why can it succeed more readily than simple poisoning?

**2018–19 · Q4(b) · 8 marks · partial** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · [Solution A123](../solutions/SOLUTIONS.html#a123)

**Exact task:** Pharming versus phishing.

Distinguish pharming and phishing, with examples.

**Coverage / reading note:** Handwritten notes p. 63 teaches phishing; pharming and DNS redirection are not developed there.

## Firewalls, Tunneling and IDS

[Ch06-2-FW-Tunneling-IDS-REDUCED.pdf](<../slides/Ch06-2-FW-Tunneling-IDS-REDUCED.pdf>)

<a id="firewall"></a>
### Firewall state, evasion and defense limits — 5 questions

**Study:** deck PDF pp. 3–11; handwritten-note PDF pp. 71.

**2023–24 · Q3(a) · 10 marks · direct** · [paper p. 4](<../../CSE405-Security_Merged.pdf#page=4>) · [Solution A007](../solutions/SOLUTIONS.html#a007)

**Exact task:** Can NIDS/firewall plus HTTPS always stop five attacks?.

An HTTPS-only server farm has a NIDS and firewall processing incoming requests. With an on-path attacker, assess RST injection, reflected XSS, SYN flooding, DNS spoofing and DDoS.

**2023–24 · Q4(b) · 10 marks · partial** · [paper p. 5](<../../CSE405-Security_Merged.pdf#page=5>) · [Solution A011](../solutions/SOLUTIONS.html#a011)

**Exact task:** TCP segmentation, reassembly and limits of a guaranteed evasion.

A smart stateful firewall blocks bytes spelling admin and allows everything else. Mallory splits the word into five packets sent out of order. Will that evade the rule? If not, propose a guaranteed strategy.

**Coverage / reading note:** The deck distinguishes filter types; stream normalization and the impossibility of an unconditional guarantee are extensions.

**2022–23 · Q4(c) · 7 marks · direct** · [paper p. 12](<../../CSE405-Security_Merged.pdf#page=12>) · [Solution A032](../solutions/SOLUTIONS.html#a032)

**Exact task:** Stateful versus stateless filtering.

Compare stateful and stateless firewalls.

**2021–22 · Q8(c) · 11 marks · partial** · [paper p. 17](<../../CSE405-Security_Merged.pdf#page=17>) · [Solution A068](../solutions/SOLUTIONS.html#a068)

**Exact task:** Address-book allowlist as a spam policy.

Alice rejects all email except senders in her address book. Is this an effective spam defense?

**Coverage / reading note:** Applies allowlist policy and phishing concepts; email-specific authentication is supplementary.

**2020–21 · Q4(b) · 12 marks · direct** · [paper p. 19](<../../CSE405-Security_Merged.pdf#page=19>) · [Solution A079](../solutions/SOLUTIONS.html#a079)

**Exact task:** Value and defense of an internal malware agent.

Explain why an attacker installs an agent inside a corporate network, delivery methods and prevention; assess whether a firewall can help.

<a id="honey"></a>
### Honeypot topology, monitoring and overhead — 5 questions

**Study:** deck PDF pp. 33–34; handwritten-note PDF pp. 28, 52.

**2022–23 · Q4(b) · 10 marks · direct** · [paper p. 12](<../../CSE405-Security_Merged.pdf#page=12>) · [Solution A031](../solutions/SOLUTIONS.html#a031)

**Exact task:** Honeypot placement, value and resource cost.

Explain with topology why an organization needs a honeypot and estimate its overhead.

**2021–22 · Q5(c) · 11 marks · direct** · [paper p. 16](<../../CSE405-Security_Merged.pdf#page=16>) · [Solution A059](../solutions/SOLUTIONS.html#a059)

**Exact task:** Disrupting C&C through coordinated investigation.

Formulate a process to take down a botnet command-and-control server.

**2021–22 · Q6(c) · 11 marks · direct** · [paper p. 17](<../../CSE405-Security_Merged.pdf#page=17>) · [Solution A062](../solutions/SOLUTIONS.html#a062)

**Exact task:** Honeypot topology and effect on normal operation.

Explain the need for a honeypot with topology and whether it hampers normal operation.

**2019–20 · Q5(c) · 7 marks · direct** · [paper p. 24](<../../CSE405-Security_Merged.pdf#page=24>) · [Solution A103](../solutions/SOLUTIONS.html#a103)

**Exact task:** Why a decoy helps intrusion detection.

Explain why a honeypot is an effective IDS tool.

**2018–19 · Q4(d) · 8 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · [Solution A125](../solutions/SOLUTIONS.html#a125)

**Exact task:** Honeypot detection, evidence and diversion.

Explain honeypot use cases with a diagram.

<a id="ids"></a>
### Intrusion detection, base rates and audit data — 5 questions

**Study:** deck PDF pp. 23–26; handwritten-note PDF pp. 23–24 (anomaly detection background).

**2020–21 · Q4(c) · 11 marks · partial** · [paper p. 19](<../../CSE405-Security_Merged.pdf#page=19>) · [Solution A080](../solutions/SOLUTIONS.html#a080)

**Exact task:** Base-rate fallacy with a numerical example.

Define the base-rate fallacy, give an example and explain its effect on daily incident handling.

**Coverage / reading note:** The deck teaches the four alarm outcomes; Bayes/base-rate calculation is an extension.

**2019–20 · Q2(c) · 11 marks · partial** · [paper p. 22](<../../CSE405-Security_Merged.pdf#page=22>) · [Solution A094](../solutions/SOLUTIONS.html#a094)

**Exact task:** Verify a reported DoS source and respond with evidence.

A hall administrator says your shared network segment is sending DoS traffic. You deny involvement but are unsure about your roommate. How do you verify and respond?

**Coverage / reading note:** Uses IDS/network logs and OS event logging; incident-handling workflow extends the slides.

**2019–20 · Q5(a) · 14 marks · partial** · [paper p. 24](<../../CSE405-Security_Merged.pdf#page=24>) · [Solution A101](../solutions/SOLUTIONS.html#a101)

**Exact task:** PIDS, alarm outcomes and base-rate interpretation.

Define protocol-based IDS, list alarm outcomes and explain base-rate fallacy.

**Coverage / reading note:** IDS and the confusion matrix are explicit; PIDS specialization and Bayesian analysis are supplementary.

**2019–20 · Q5(b) · 14 marks · partial** · [paper p. 24](<../../CSE405-Security_Merged.pdf#page=24>) · [Solution A102](../solutions/SOLUTIONS.html#a102)

**Exact task:** Audit-record fields and statistical intrusion detection.

List useful audit-record fields, explain statistical IDS and identify a weakness.

**Coverage / reading note:** Event logging and IDS sensors are taught; statistical-model design is an extension.

**2018–19 · Q4(c) · 9 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · [Solution A124](../solutions/SOLUTIONS.html#a124)

**Exact task:** Rule-based ARP-spoofing detection.

Give rules a rule-based IDS can use to detect ARP spoofing.

<a id="recon"></a>
### Reconnaissance, fingerprinting and vulnerability assessment — 3 questions

**Study:** deck PDF pp. 27–32; handwritten-note PDF pp. 27–28.

**2022–23 · Q2(c) · 11 marks · direct** · [paper p. 11](<../../CSE405-Security_Merged.pdf#page=11>) · [Solution A026](../solutions/SOLUTIONS.html#a026)

**Exact task:** Fingerprint/version/CVE assessment workflow.

Formulate the steps for finding and exploiting a target vulnerability by scanning OS/application versions.

**2021–22 · Q8(b) · 12 marks · direct** · [paper p. 17](<../../CSE405-Security_Merged.pdf#page=17>) · [Solution A067](../solutions/SOLUTIONS.html#a067)

**Exact task:** OS fingerprinting to validated vulnerability finding.

Formulate the steps for exploiting a target after scanning its OS version.

**2020–21 · Q3(b) · 12 marks · direct** · [paper p. 18](<../../CSE405-Security_Merged.pdf#page=18>) · [Solution A076](../solutions/SOLUTIONS.html#a076)

**Exact task:** Web-server assessment and validation workflow.

Give a stepwise approach and tools to find and exploit popular web-server vulnerabilities.

<a id="vpn"></a>
### VPN and IPsec AH/ESP encapsulation — 2 questions

**Study:** deck PDF pp. 12–22; handwritten-note PDF pp. 71 (brief).

**2021–22 · Q5(b) · 12 marks · direct** · [paper p. 16](<../../CSE405-Security_Merged.pdf#page=16>) · [Solution A058](../solutions/SOLUTIONS.html#a058)

**Exact task:** AH versus ESP and transport/tunnel layouts.

Compare IPsec AH and ESP with their encapsulations.

**2018–19 · Q1(b) · 9 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · [Solution A111](../solutions/SOLUTIONS.html#a111)

**Exact task:** Compare IPsec ESP and AH formats.

Contrast IPsec AH and ESP, including header encapsulations.

## Cryptography, Hashes and Digital Signatures

[Crypto-Hash-DigSign.pdf](<../slides/Crypto-Hash-DigSign.pdf>)

<a id="signature"></a>
### Digital signatures and signing-key security — 7 questions

**Study:** deck PDF pp. 61–65; handwritten-note PDF pp. 1, 11, 17 (brief).

**2023–24 · Q7(c) · 10 marks · direct** · [paper p. 9](<../../CSE405-Security_Merged.pdf#page=9>) · [Solution A017](../solutions/SOLUTIONS.html#a017)

**Exact task:** RSA signing/verifying; security of separately sending ciphertext and signature.

Define RSA signature creation and verification using Sign(d,M) and Verify(e,N,M,sig). Alice encrypts M with Bob’s RSA public key and signs M with her own private key. Can she securely send both ciphertext and signature together? Justify cryptographically.

**2022–23 · Q6(a) · 15 marks · direct** · [paper p. 13](<../../CSE405-Security_Merged.pdf#page=13>) · [Solution A037](../solutions/SOLUTIONS.html#a037)

**Exact task:** Authenticate Diffie–Hellman with RSA signatures.

Explain Diffie–Hellman and its MITM security flaw with figures. Modify the algorithm using RSA digital signatures to remove that flaw.

**Coverage / reading note:** The signing keys must themselves be authenticated; merely attaching an untrusted public key does not fix MITM.

**2021–22 · Q3(b) · 10 marks · partial** · [paper p. 15](<../../CSE405-Security_Merged.pdf#page=15>) · [Solution A050](../solutions/SOLUTIONS.html#a050)

**Exact task:** Applications of hashing in authentication, confidentiality and signatures.

Demonstrate uses of a hash function for authentication, confidentiality and digital signatures.

**Coverage / reading note:** The decks cover hashing, MACs and hash-then-sign; a bare hash does not provide confidentiality. Explain a suitable construction rather than attributing encryption properties to hashing.

**2021–22 · Q3(d) · 10 marks · direct** · [paper p. 16](<../../CSE405-Security_Merged.pdf#page=16>) · [Solution A052](../solutions/SOLUTIONS.html#a052)

**Exact task:** Symmetric/public-key comparison; key roles in signing versus encryption.

Compare symmetric and public-key cryptography. Explain how the roles of public and private keys in signatures differ from their roles in public-key encryption.

**2019–20 · Q1(a) · 12 marks · direct** · [paper p. 22](<../../CSE405-Security_Merged.pdf#page=22>) · [Solution A089](../solutions/SOLUTIONS.html#a089)

**Exact task:** Digital signatures and non-repudiation.

Explain, with a figure, how digital signatures ensure non-repudiation.

**2019–20 · Q8(a) · 20 marks · partial** · [paper p. 24](<../../CSE405-Security_Merged.pdf#page=24>) · [Solution A108](../solutions/SOLUTIONS.html#a108)

**Exact task:** ElGamal encryption proof; birthday attack on signatures.

Describe ElGamal encryption/decryption and prove decryption correctness. Give an illustrative example showing that digital signatures can be vulnerable to a birthday attack.

**Coverage / reading note:** Hash/signature birthday attacks are related; ElGamal encryption is not developed by the supplied Sec A decks. Full answer retained for the mixed subquestion.

**2018–19 · Q1(d) · 8 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · [Solution A113](../solutions/SOLUTIONS.html#a113)

**Exact task:** Risks of signing an apparently random string.

Explain the risks if Bob agrees to sign a seemingly random string with his private key.

<a id="hash"></a>
### Hash properties, collisions and birthday security — 7 questions

**Study:** deck PDF pp. 48–55; handwritten-note PDF pp. 11 (brief).

**2022–23 · Q5(b) · 12 marks · partial** · [paper p. 12](<../../CSE405-Security_Merged.pdf#page=12>) · [Solution A035](../solutions/SOLUTIONS.html#a035)

**Exact task:** Analyze encryption plus hash, plaintext MAC, or ciphertext MAC.

Alice sends (1) Enc(K,m) with Hash(ciphertext), (2) Enc(K,m) with MAC(K,m), or (3) Enc(K,m) with MAC(K,ciphertext). Assume no harmful interactions from the shared key. For each, evaluate confidentiality against passive Eve and integrity against modifying MITM Mallory.

**Coverage / reading note:** MAC/hash/encryption are taught; formal composition security is supplementary.

**2022–23 · Q8(a) · 15 marks · direct** · [paper p. 14](<../../CSE405-Security_Merged.pdf#page=14>) · [Solution A040](../solutions/SOLUTIONS.html#a040)

**Exact task:** Integrity tags in a file header; hash versus MAC; writable versus read-only storage.

A file’s integrity tag is stored in its header and checked when opened. An attacker must not modify the file undetected. Compare (i) an unkeyed collision-resistant hash, (ii) a MAC under the owner’s secret key and (iii) the MAC scheme when the tag is in read-only memory. Decide whether each system is secure.

**Coverage / reading note:** The final case puts the integrity tag in read-only memory; preserve the wording of the original when working the problem.

**2021–22 · Q3(b) · 10 marks · partial** · [paper p. 15](<../../CSE405-Security_Merged.pdf#page=15>) · [Solution A050](../solutions/SOLUTIONS.html#a050)

**Exact task:** Applications of hashing in authentication, confidentiality and signatures.

Demonstrate uses of a hash function for authentication, confidentiality and digital signatures.

**Coverage / reading note:** The decks cover hashing, MACs and hash-then-sign; a bare hash does not provide confidentiality. Explain a suitable construction rather than attributing encryption properties to hashing.

**2021–22 · Q3(c) · 10 marks · direct** · [paper p. 16](<../../CSE405-Security_Merged.pdf#page=16>) · [Solution A051](../solutions/SOLUTIONS.html#a051)

**Exact task:** Evaluate XOR of fixed-size message blocks as a hash.

Explain the desired properties of a cryptographic hash. A message consists of l blocks M1,…,Ml of 160 bits and h(x)=M1 XOR … XOR Ml. Evaluate this function against those properties.

**2020–21 · Q8(b) · 10 marks · direct** · [paper p. 21](<../../CSE405-Security_Merged.pdf#page=21>) · [Solution A088](../solutions/SOLUTIONS.html#a088)

**Exact task:** Birthday bound for a b-bit hash.

Prove that a b-bit hash function provides b/2-bit security.

**Coverage / reading note:** This is the collision-search security bound, not a universal bound on preimage resistance.

**2019–20 · Q6(b) · 21 marks · partial** · [paper p. 24](<../../CSE405-Security_Merged.pdf#page=24>) · [Solution A104](../solutions/SOLUTIONS.html#a104)

**Exact task:** Weak/strong collision resistance; toy hash; Merkle–Damgård.

State ideal hash properties and distinguish weak and strong collision resistance. Show H(x)=(5x+11) mod 19 is not weakly collision resistant for H(4). Draw Merkle–Damgård and explain why its compression function needs strong collision resistance.

**Coverage / reading note:** Hash properties are explicit; detailed Merkle–Damgård is supplementary.

**2019–20 · Q8(a) · 20 marks · partial** · [paper p. 24](<../../CSE405-Security_Merged.pdf#page=24>) · [Solution A108](../solutions/SOLUTIONS.html#a108)

**Exact task:** ElGamal encryption proof; birthday attack on signatures.

Describe ElGamal encryption/decryption and prove decryption correctness. Give an illustrative example showing that digital signatures can be vulnerable to a birthday attack.

**Coverage / reading note:** Hash/signature birthday attacks are related; ElGamal encryption is not developed by the supplied Sec A decks. Full answer retained for the mixed subquestion.

<a id="mac"></a>
### MAC/HMAC and authenticated data — 7 questions

**Study:** deck PDF pp. 48–52; handwritten-note PDF pp. 11 (brief).

**2023–24 · Q5(a) · 15 marks · partial** · [paper p. 7](<../../CSE405-Security_Merged.pdf#page=7>) · [Solution A013](../solutions/SOLUTIONS.html#a013)

**Exact task:** Short concepts; answer any three of five.

Briefly explain any three, with diagrams where appropriate: (i) the CIA properties of cryptography, (ii) confusion and diffusion, (iii) message authentication code, (iv) homograph phishing attack, (v) clickjacking.

**Coverage / reading note:** Only the CIA and MAC choices are explicit in Sec A; confusion/diffusion, homographs and clickjacking extend the decks. The 15 marks belong to the whole optional subquestion.

**2023–24 · Q8(a) · 5 marks · partial** · [paper p. 9](<../../CSE405-Security_Merged.pdf#page=9>) · [Solution A018](../solutions/SOLUTIONS.html#a018)

**Exact task:** Encrypt-then-MAC versus MAC-then-encrypt.

What is authenticated encryption? Which of MAC-then-encrypt and encrypt-then-MAC is preferable, and why?

**Coverage / reading note:** MAC/encryption foundations are taught; authenticated-encryption composition is a related extension.

**2022–23 · Q5(b) · 12 marks · partial** · [paper p. 12](<../../CSE405-Security_Merged.pdf#page=12>) · [Solution A035](../solutions/SOLUTIONS.html#a035)

**Exact task:** Analyze encryption plus hash, plaintext MAC, or ciphertext MAC.

Alice sends (1) Enc(K,m) with Hash(ciphertext), (2) Enc(K,m) with MAC(K,m), or (3) Enc(K,m) with MAC(K,ciphertext). Assume no harmful interactions from the shared key. For each, evaluate confidentiality against passive Eve and integrity against modifying MITM Mallory.

**Coverage / reading note:** MAC/hash/encryption are taught; formal composition security is supplementary.

**2022–23 · Q8(a) · 15 marks · direct** · [paper p. 14](<../../CSE405-Security_Merged.pdf#page=14>) · [Solution A040](../solutions/SOLUTIONS.html#a040)

**Exact task:** Integrity tags in a file header; hash versus MAC; writable versus read-only storage.

A file’s integrity tag is stored in its header and checked when opened. An attacker must not modify the file undetected. Compare (i) an unkeyed collision-resistant hash, (ii) a MAC under the owner’s secret key and (iii) the MAC scheme when the tag is in read-only memory. Decide whether each system is secure.

**Coverage / reading note:** The final case puts the integrity tag in read-only memory; preserve the wording of the original when working the problem.

**2021–22 · Q3(b) · 10 marks · partial** · [paper p. 15](<../../CSE405-Security_Merged.pdf#page=15>) · [Solution A050](../solutions/SOLUTIONS.html#a050)

**Exact task:** Applications of hashing in authentication, confidentiality and signatures.

Demonstrate uses of a hash function for authentication, confidentiality and digital signatures.

**Coverage / reading note:** The decks cover hashing, MACs and hash-then-sign; a bare hash does not provide confidentiality. Explain a suitable construction rather than attributing encryption properties to hashing.

**2021–22 · Q4(b) · 10 marks · partial** · [paper p. 16](<../../CSE405-Security_Merged.pdf#page=16>) · [Solution A054](../solutions/SOLUTIONS.html#a054)

**Exact task:** HMAC construction.

Describe how a message authentication code is created by HMAC.

**Coverage / reading note:** MAC is explicit; the detailed HMAC construction is supplementary.

**2020–21 · Q5(a) · 15 marks · partial** · [paper p. 19](<../../CSE405-Security_Merged.pdf#page=19>) · [Solution A081](../solutions/SOLUTIONS.html#a081)

**Exact task:** Authenticate UDP messages with a cookie/token; prevent replay.

Bob uses UDP for a streaming service because confidentiality is unnecessary and he cannot use TLS/HTTPS. He needs integrity so attackers cannot impersonate the sender or alter or replay messages. Explain how to achieve this using cookies.

**Coverage / reading note:** MACs and message integrity are explicit; a complete authenticated UDP protocol with replay tracking extends the decks.

<a id="modes"></a>
### Block-cipher modes, CBC and ciphertext manipulation — 4 questions

**Study:** deck PDF pp. 25–28; ECB/CTR details are extensions; handwritten-note PDF pp. Not developed.

**2023–24 · Q5(b) · 20 marks · partial** · [paper p. 7](<../../CSE405-Security_Merged.pdf#page=7>) · [Solution A014](../solutions/SOLUTIONS.html#a014)

**Exact task:** Unfamiliar chaining diagram; equations, parallelism and malleability.

For the supplied block-cipher diagram with IV1 and IV2, derive encryption/decryption equations for the first three blocks; draw the decryption diagram; determine which operations parallelize. Given two known plaintext/ciphertext pairs and intercepted IV1, IV2, C1, C2, modify the transmitted values so Bob obtains chosen P1′ and P2′ without learning the key.

**Coverage / reading note:** Sec A teaches CBC, not this custom two-IV construction; a related mode-analysis extension, not a direct CBC question.

**2022–23 · Q5(a) · 12 marks · partial** · [paper p. 12](<../../CSE405-Security_Merged.pdf#page=12>) · [Solution A034](../solutions/SOLUTIONS.html#a034)

**Exact task:** ECB/CBC/CTR comparison.

Compare ECB, CBC and CTR, with diagrams, for (i) IND-CPA security, (ii) encryption/decryption parallelism and (iii) robustness to incorrect IV/nonce usage.

**Coverage / reading note:** CBC is explicit; ECB/CTR, IND-CPA and nonce-comparison details extend this deck.

**2021–22 · Q2(d) · 10 marks · direct** · [paper p. 15](<../../CSE405-Security_Merged.pdf#page=15>) · [Solution A048](../solutions/SOLUTIONS.html#a048)

**Exact task:** Identify ECB-style long-message weakness and replace the mode.

A cryptanalyst says the system is secure for short messages but vulnerable for long messages because of its mode of operation. Identify and describe the mode and explain how to overcome the problem.

**2018–19 · Q5(b) · 3 marks · direct** · [paper p. 27](<../../CSE405-Security_Merged.pdf#page=27>) · [Solution A126](../solutions/SOLUTIONS.html#a126)

**Exact task:** Inserted ciphertext bit and CBC synchronization.

A message is encrypted with DES-CBC. An extra 0 bit is inserted into the ciphertext stream after block C_i. How much plaintext is garbled?

**Coverage / reading note:** This is insertion of a bit, not flipping a bit or replacing a whole block. Preserve that distinction.

<a id="dh"></a>
### Diffie–Hellman calculations and authentication — 4 questions

**Study:** deck PDF pp. 56–60; handwritten-note PDF pp. Not developed.

**2023–24 · Q6(a) · 15 marks · direct** · [paper p. 8](<../../CSE405-Security_Merged.pdf#page=8>) · [Solution A015](../solutions/SOLUTIONS.html#a015)

**Exact task:** Unauthenticated Diffie–Hellman MITM; defense without a trusted third party.

Given the stated Diffie–Hellman protocol, act as Mallory when no trusted third parties can verify Alice or Bob. Explain and diagram a successful MITM attack, then briefly explain a defense.

**Coverage / reading note:** The question explicitly rules out an available trusted third party. A defense must state another authenticated trust mechanism, such as a previously authenticated key or an out-of-band fingerprint check.

**2022–23 · Q6(a) · 15 marks · direct** · [paper p. 13](<../../CSE405-Security_Merged.pdf#page=13>) · [Solution A037](../solutions/SOLUTIONS.html#a037)

**Exact task:** Authenticate Diffie–Hellman with RSA signatures.

Explain Diffie–Hellman and its MITM security flaw with figures. Modify the algorithm using RSA digital signatures to remove that flaw.

**Coverage / reading note:** The signing keys must themselves be authenticated; merely attaching an untrusted public key does not fix MITM.

**2021–22 · Q2(c) · 10 marks · direct** · [paper p. 15](<../../CSE405-Security_Merged.pdf#page=15>) · [Solution A047](../solutions/SOLUTIONS.html#a047)

**Exact task:** Numerical Diffie–Hellman exchange.

Explain Diffie–Hellman. Given p=353, primitive root g=3, and private exponents 97 and 233, calculate both public keys and the shared secret.

**2019–20 · Q8(b) · 15 marks · direct** · [paper p. 24](<../../CSE405-Security_Merged.pdf#page=24>) · [Solution A109](../solutions/SOLUTIONS.html#a109)

**Exact task:** Diffie–Hellman steps and active MITM.

Write the Diffie–Hellman key-exchange steps and show the MITM attack when an adversary can intercept and modify messages.

<a id="cert"></a>
### Certificates, CA trust and key binding — 4 questions

**Study:** deck PDF pp. 66–69; handwritten-note PDF pp. Not developed.

**2023–24 · Q1(c) · 15 marks · direct** · [paper p. 2](<../../CSE405-Security_Merged.pdf#page=2>) · [Solution A003](../solutions/SOLUTIONS.html#a003)

**Exact task:** Untrusted key bundled with its own signature; attacker positions.

ARTBot broadcasts to learn CSBot’s phone number. CSBot replies with its number, public key, and a signature on the number. ARTBot verifies using that supplied key and caches the result. Explain how to poison the cached number as (i) an on-path attacker, (ii) a MITM attacker and (iii) an off-path attacker. Analyze a possible defense.

**Coverage / reading note:** Cross-topic use of signatures, but the failure being examined is the absence of an authenticated public-key binding.

**2023–24 · Q4(c) · 15 marks · partial** · [paper p. 6](<../../CSE405-Security_Merged.pdf#page=6>) · [Solution A012](../solutions/SOLUTIONS.html#a012)

**Exact task:** TLS handshake authentication, directional keys and authenticated records.

For the supplied TLS handshake: (i) why can a MITM not exploit unencrypted/unauthenticated ClientHello and ServerHello, in both the DH and RSA cases? (ii) Why is using one shared encryption key and one shared integrity key for both directions a bad idea? (iii) After ChangeCipherSpec, what vulnerability remains in the simplified protocol, and how would you fix it?

**Coverage / reading note:** HTTPS/certificates and DH/RSA are taught; full historical TLS handshake/record details are supplementary.

**2021–22 · Q7(c) · 11 marks · direct** · [paper p. 17](<../../CSE405-Security_Merged.pdf#page=17>) · [Solution A065](../solutions/SOLUTIONS.html#a065)

**Exact task:** Self-signed SSL certificate and server authentication.

Why is buying from a shopping website that uses a self-signed SSL certificate a bad idea?

**Coverage / reading note:** The issue is whether the server key is authenticated by a trust anchor, not whether a self-signed certificate can encrypt.

**2018–19 · Q1(a) · 9 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · [Solution A110](../solutions/SOLUTIONS.html#a110)

**Exact task:** Digital-certificate contents and CA role.

What key information is kept in a digital certificate? Explain the certification authority’s role with a figure.

<a id="block"></a>
### DES/AES internals, P/S boxes and multiple-DES strength — 3 questions

**Study:** deck PDF pp. 5–24; handwritten-note PDF pp. 17 (brief).

**2021–22 · Q4(c) · 10 marks · partial** · [paper p. 16](<../../CSE405-Security_Merged.pdf#page=16>) · [Solution A055](../solutions/SOLUTIONS.html#a055)

**Exact task:** DES attack; meet-in-the-middle strength of fivefold DES.

Explain an attack on DES. A proposed 5DES alternates five DES encryptions/decryptions using independent keys and claims 280-bit strength, exceeding AES-256. Compute the effective key strength and assess the claim.

**Coverage / reading note:** DES/3DES are explicit; 5DES meet-in-the-middle analysis is supplementary.

**2021–22 · Q4(d) · 10 marks · partial** · [paper p. 16](<../../CSE405-Security_Merged.pdf#page=16>) · [Solution A056](../solutions/SOLUTIONS.html#a056)

**Exact task:** Compare DES components with AES.

For each DES component, identify its AES counterpart or explain why none is needed: (i) XOR of subkey with the f-function input, (ii) XOR of f output with the left half, (iii) f itself, (iv) permutation P, (v) swapping block halves.

**Coverage / reading note:** AES round operations appear in Lecture 3; detailed DES round structure is not supplied.

**2018–19 · Q6(a) · 8 marks · partial** · [paper p. 27](<../../CSE405-Security_Merged.pdf#page=27>) · [Solution A127](../solutions/SOLUTIONS.html#a127)

**Exact task:** Trace P-box and S-box diagrams.

For the supplied P-box, find the output for input bits designated top-to-bottom 01234567. For the supplied S-box, find the output sequence for successive input octal numbers 76543210.

**Coverage / reading note:** The original diagrams are essential. Lecture 3 has AES SubBytes and ShiftRows, but not this specific P-box/S-box exercise.

<a id="rsa"></a>
### RSA encryption and correctness — 3 questions

**Study:** deck PDF pp. 41–47; handwritten-note PDF pp. 17 (brief).

**2023–24 · Q7(b) · 10 marks · direct** · [paper p. 9](<../../CSE405-Security_Merged.pdf#page=9>) · [Solution A016](../solutions/SOLUTIONS.html#a016)

**Exact task:** RSA correctness proof.

Prove mathematically that RSA decryption recovers the original message, using the necessary number-theory results.

**2023–24 · Q7(c) · 10 marks · direct** · [paper p. 9](<../../CSE405-Security_Merged.pdf#page=9>) · [Solution A017](../solutions/SOLUTIONS.html#a017)

**Exact task:** RSA signing/verifying; security of separately sending ciphertext and signature.

Define RSA signature creation and verification using Sign(d,M) and Verify(e,N,M,sig). Alice encrypts M with Bob’s RSA public key and signs M with her own private key. Can she securely send both ciphertext and signature together? Justify cryptographically.

**2019–20 · Q7(c) · 15 marks · direct** · [paper p. 24](<../../CSE405-Security_Merged.pdf#page=24>) · [Solution A107](../solutions/SOLUTIONS.html#a107)

**Exact task:** RSA validity, repeated totients and encryption.

System A: p=83, q=101, e=3, d=5467. System B: p=17, q=11, e=7, d=23. For both compute φ(n) and φ(φ(n)), and explain validity. For system B encrypt plaintext M=3.

<a id="number"></a>
### Modular arithmetic, Fermat, Euler and inverses — 2 questions

**Study:** deck PDF pp. 29–40; handwritten-note PDF pp. 17 (brief).

**2019–20 · Q7(a) · 8 marks · direct** · [paper p. 24](<../../CSE405-Security_Merged.pdf#page=24>) · [Solution A105](../solutions/SOLUTIONS.html#a105)

**Exact task:** Euler totient/theorem; modular inverse.

Define Euler’s totient function and Euler’s theorem, and explain computing a modular inverse using Euler’s theorem.

**Coverage / reading note:** Lecture 7 pp. 20–23 uses these prerequisites; handwritten notes p. 35 and CT4 guide pp. 19–20 expand them.

**2019–20 · Q7(b) · 12 marks · partial** · [paper p. 24](<../../CSE405-Security_Merged.pdf#page=24>) · [Solution A106](../solutions/SOLUTIONS.html#a106)

**Exact task:** Modular equations and fast exponentiation.

Solve (i) x^8 ≡ 9 (mod 13), (ii) x² ≡ 2 (mod 13), and compute 3^128 mod 7. A modular-exponentiation table modulo 13 is supplied.

**Coverage / reading note:** These number-theory exercises support RSA/DH. The current slides do not develop modular-root solving; the CT4 guide pp. 20–21 works this question.

<a id="keymodels"></a>
### Symmetric/public-key models and Caesar as symmetric encryption — 2 questions

**Study:** deck PDF pp. 2–8, 41–43; Introduction pp. 21–24; handwritten-note PDF pp. 17 (brief).

**2021–22 · Q1(d) · 10 marks · partial** · [paper p. 15](<../../CSE405-Security_Merged.pdf#page=15>) · [Solution A045](../solutions/SOLUTIONS.html#a045)

**Exact task:** Caesar as symmetric encryption; composition of affine ciphers.

Why is Caesar a symmetric encryption algorithm? If you encrypt using one affine cipher and then a second affine cipher, both modulo 26, is there any advantage over one affine cipher? Derive the result.

**Coverage / reading note:** Caesar/symmetric encryption are explicit; the affine-composition half is supplementary.

**2021–22 · Q3(d) · 10 marks · direct** · [paper p. 16](<../../CSE405-Security_Merged.pdf#page=16>) · [Solution A052](../solutions/SOLUTIONS.html#a052)

**Exact task:** Symmetric/public-key comparison; key roles in signing versus encryption.

Compare symmetric and public-key cryptography. Explain how the roles of public and private keys in signatures differ from their roles in public-key encryption.

## Web and Database Security

[WebDB-security.pdf](<../slides/WebDB-security.pdf>)

<a id="phishing"></a>
### Phishing, homographs and UI deception — 7 questions

**Study:** deck PDF pp. 11–13; handwritten-note PDF pp. 4–7, 23.

**2023–24 · Q5(a) · 15 marks · partial** · [paper p. 7](<../../CSE405-Security_Merged.pdf#page=7>) · [Solution A013](../solutions/SOLUTIONS.html#a013)

**Exact task:** Short concepts; answer any three of five.

Briefly explain any three, with diagrams where appropriate: (i) the CIA properties of cryptography, (ii) confusion and diffusion, (iii) message authentication code, (iv) homograph phishing attack, (v) clickjacking.

**Coverage / reading note:** Only the CIA and MAC choices are explicit in Sec A; confusion/diffusion, homographs and clickjacking extend the decks. The 15 marks belong to the whole optional subquestion.

**2022–23 · Q8(b) · 8 marks · partial** · [paper p. 14](<../../CSE405-Security_Merged.pdf#page=14>) · [Solution A041](../solutions/SOLUTIONS.html#a041)

**Exact task:** SMS 2FA against phishing.

Is SMS-based two-factor authentication an effective defense against phishing? Justify.

**Coverage / reading note:** Phishing and authentication factors are taught; live SMS relay is an application.

**2022–23 · Q8(c) · 12 marks · partial** · [paper p. 14](<../../CSE405-Security_Merged.pdf#page=14>) · [Solution A042](../solutions/SOLUTIONS.html#a042)

**Exact task:** Clickjacking with iframes; repeated-click redirection.

Describe clickjacking in two cases: (i) overlay a fake free-subscription button on an iframe advertisement so a visitor unknowingly clicks a paid buy button; (ii) an embedded public-exam result form whose first click goes to Twitter, second to Facebook, and third finally fetches the result.

**Coverage / reading note:** Phishing is taught, but the iframe clickjacking cases are a UI-attack extension.

**2021–22 · Q7(b) · 12 marks · partial** · [paper p. 17](<../../CSE405-Security_Merged.pdf#page=17>) · [Solution A064](../solutions/SOLUTIONS.html#a064)

**Exact task:** Clickjacking versus phishing.

Differentiate clickjacking and phishing with examples.

**Coverage / reading note:** Phishing is explicit; clickjacking is supplementary.

**2021–22 · Q8(c) · 11 marks · partial** · [paper p. 17](<../../CSE405-Security_Merged.pdf#page=17>) · [Solution A068](../solutions/SOLUTIONS.html#a068)

**Exact task:** Address-book allowlist as a spam policy.

Alice rejects all email except senders in her address book. Is this an effective spam defense?

**Coverage / reading note:** Applies allowlist policy and phishing concepts; email-specific authentication is supplementary.

**2018–19 · Q4(b) · 8 marks · partial** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · [Solution A123](../solutions/SOLUTIONS.html#a123)

**Exact task:** Pharming versus phishing.

Distinguish pharming and phishing, with examples.

**Coverage / reading note:** Handwritten notes p. 63 teaches phishing; pharming and DNS redirection are not developed there.

**2018–19 · Q8(b) · 9 marks · partial** · [paper p. 28](<../../CSE405-Security_Merged.pdf#page=28>) · [Solution A132](../solutions/SOLUTIONS.html#a132)

**Exact task:** Short notes; answer any three of four.

Write short notes on any three: (i) Faraday cage, (ii) blind SQL injection, (iii) impersonation token, (iv) homograph attack.

**Coverage / reading note:** One optional 9-mark subquestion. Faraday cage is explicit; blind SQLi/homographs extend the web deck, and OS impersonation-token details are supplementary. Do not allocate all 9 marks to every choice.

<a id="xss"></a>
### Stored/reflected XSS and injected scripts — 6 questions

**Study:** deck PDF pp. 26–32; handwritten-note PDF pp. Not developed.

**2023–24 · Q3(a) · 10 marks · direct** · [paper p. 4](<../../CSE405-Security_Merged.pdf#page=4>) · [Solution A007](../solutions/SOLUTIONS.html#a007)

**Exact task:** Can NIDS/firewall plus HTTPS always stop five attacks?.

An HTTPS-only server farm has a NIDS and firewall processing incoming requests. With an on-path attacker, assess RST injection, reflected XSS, SYN flooding, DNS spoofing and DDoS.

**2023–24 · Q8(d) · 10 marks · direct** · [paper p. 10](<../../CSE405-Security_Merged.pdf#page=10>) · [Solution A020](../solutions/SOLUTIONS.html#a020)

**Exact task:** Stored versus reflected XSS.

Define XSS and explain the difference between stored and reflected XSS using diagrams.

**2022–23 · Q5(c) · 11 marks · partial** · [paper p. 12](<../../CSE405-Security_Merged.pdf#page=12>) · [Solution A036](../solutions/SOLUTIONS.html#a036)

**Exact task:** Limits of cookie policy.

Analyze how effective cookie policies are at (i) preventing CSRF, (ii) preventing session hijacking through XSS and (iii) preserving confidentiality of stored cookies.

**Coverage / reading note:** XSS/CSRF are explicit; detailed cookie attributes/policy are supplementary.

**2022–23 · Q7(c) · 7 marks · direct** · [paper p. 13](<../../CSE405-Security_Merged.pdf#page=13>) · [Solution A039](../solutions/SOLUTIONS.html#a039)

**Exact task:** Stored versus reflected XSS.

Briefly explain how reflected XSS differs from stored XSS.

**2020–21 · Q6(a) · 15 marks · partial** · [paper p. 19](<../../CSE405-Security_Merged.pdf#page=19>) · [Solution A084](../solutions/SOLUTIONS.html#a084)

**Exact task:** CSRF plus stored XSS in a social-network friend request.

Trudy builds trudymalicious.com. On a visitor A’s arrival, make A send Trudy a friend request and change A’s homepage so anyone visiting it sends Trudy a friend request. No CSRF/XSS defenses exist. The supplied GET is http://www.networksocial.com/action/friends/add?friend=20. Explain the malicious site.

**Coverage / reading note:** CSRF is taught directly in Lecture 10; the stored-XSS part is taught in Lecture 11 pp. 15–19 and handwritten notes pp. 62–63. The question continues on p. 20.

**2018–19 · Q12(a) · 15 marks · direct** · [paper p. 30](<../../CSE405-Security_Merged.pdf#page=30>) · [Solution A138](../solutions/SOLUTIONS.html#a138)

**Exact task:** Stored XSS in a guest book; malicious page actions.

As Sammy (id=40), write a script in the guest-book Message field to demonstrate XSS damage. The first paragraph has id p1 and the friend-add action for user id 100 is http://vulnerable.com/action/friend/add?id=100.

**Coverage / reading note:** The guest-book screenshot is on p. 31; consult it with the prompt on p. 30.

<a id="sql"></a>
### SQL injection and prepared statements — 5 questions

**Study:** deck PDF pp. 14–25; handwritten-note PDF pp. 28 (brief).

**2023–24 · Q8(c) · 10 marks · direct** · [paper p. 10](<../../CSE405-Security_Merged.pdf#page=10>) · [Solution A019](../solutions/SOLUTIONS.html#a019)

**Exact task:** Login bypass; prepared statements.

The backend concatenates username and password into SELECT * FROM users WHERE username=... AND password=.... The table includes Alice with password password123. Determine whether SQL injection is possible; give concrete login inputs to log in as Alice without her password; explain how prepared statements prevent it.

**2020–21 · Q5(b) · 10 marks · direct** · [paper p. 19](<../../CSE405-Security_Merged.pdf#page=19>) · [Solution A082](../solutions/SOLUTIONS.html#a082)

**Exact task:** Single-statement SQL injection in a password-change form.

A C++ web server allows only one SQL statement per database call. Show how SQL injection in the displayed old-password/new-password login form can still change everyone’s password.

**2018–19 · Q8(b) · 9 marks · partial** · [paper p. 28](<../../CSE405-Security_Merged.pdf#page=28>) · [Solution A132](../solutions/SOLUTIONS.html#a132)

**Exact task:** Short notes; answer any three of four.

Write short notes on any three: (i) Faraday cage, (ii) blind SQL injection, (iii) impersonation token, (iv) homograph attack.

**Coverage / reading note:** One optional 9-mark subquestion. Faraday cage is explicit; blind SQLi/homographs extend the web deck, and OS impersonation-token details are supplementary. Do not allocate all 9 marks to every choice.

**2018–19 · Q11(a) · 5 marks · direct** · [paper p. 29](<../../CSE405-Security_Merged.pdf#page=29>) · [Solution A136](../solutions/SOLUTIONS.html#a136)

**Exact task:** UPDATE injection to change password and salary.

Use the displayed employee-password-change form and PHP code to set employee EID100’s password to you_are_hacked and salary to 10$, without knowing the old password.

**Coverage / reading note:** The PHP query/code appears on p. 30.

**2018–19 · Q11(b) · 10 marks · direct** · [paper p. 30](<../../CSE405-Security_Merged.pdf#page=30>) · [Solution A137](../solutions/SOLUTIONS.html#a137)

**Exact task:** Rewrite vulnerable PHP using prepared statements.

Change changepasswd.php to use a prepared statement so the SQL injection in Q11(a) is prevented.

<a id="csrf"></a>
### CSRF and cookie-authenticated requests — 3 questions

**Study:** deck PDF pp. 33–38; handwritten-note PDF pp. Not developed.

**2022–23 · Q5(c) · 11 marks · partial** · [paper p. 12](<../../CSE405-Security_Merged.pdf#page=12>) · [Solution A036](../solutions/SOLUTIONS.html#a036)

**Exact task:** Limits of cookie policy.

Analyze how effective cookie policies are at (i) preventing CSRF, (ii) preventing session hijacking through XSS and (iii) preserving confidentiality of stored cookies.

**Coverage / reading note:** XSS/CSRF are explicit; detailed cookie attributes/policy are supplementary.

**2022–23 · Q7(a) · 15 marks · direct** · [paper p. 13](<../../CSE405-Security_Merged.pdf#page=13>) · [Solution A038](../solutions/SOLUTIONS.html#a038)

**Exact task:** CSRF synchronizer token; refreshing only on POST.

The server puts a random CSRF token in each page’s DOM/hidden form field, and accepts a request only with a valid cookie and POST token. Tokens are refreshed on POST. Explain protection without special browser support; evaluate refreshing only on POST instead of on both GET and POST.

**2020–21 · Q6(a) · 15 marks · partial** · [paper p. 19](<../../CSE405-Security_Merged.pdf#page=19>) · [Solution A084](../solutions/SOLUTIONS.html#a084)

**Exact task:** CSRF plus stored XSS in a social-network friend request.

Trudy builds trudymalicious.com. On a visitor A’s arrival, make A send Trudy a friend request and change A’s homepage so anyone visiting it sends Trudy a friend request. No CSRF/XSS defenses exist. The supplied GET is http://www.networksocial.com/action/friends/add?friend=20. Explain the malicious site.

**Coverage / reading note:** CSRF is taught directly in Lecture 10; the stored-XSS part is taught in Lecture 11 pp. 15–19 and handwritten notes pp. 62–63. The question continues on p. 20.

<a id="web"></a>
### HTTP/HTTPS and browser trust — 2 questions

**Study:** deck PDF pp. 1–13; handwritten-note PDF pp. Not developed.

**2023–24 · Q4(c) · 15 marks · partial** · [paper p. 6](<../../CSE405-Security_Merged.pdf#page=6>) · [Solution A012](../solutions/SOLUTIONS.html#a012)

**Exact task:** TLS handshake authentication, directional keys and authenticated records.

For the supplied TLS handshake: (i) why can a MITM not exploit unencrypted/unauthenticated ClientHello and ServerHello, in both the DH and RSA cases? (ii) Why is using one shared encryption key and one shared integrity key for both directions a bad idea? (iii) After ChangeCipherSpec, what vulnerability remains in the simplified protocol, and how would you fix it?

**Coverage / reading note:** HTTPS/certificates and DH/RSA are taught; full historical TLS handshake/record details are supplementary.

**2019–20 · Q1(b) · 12 marks · partial** · [paper p. 22](<../../CSE405-Security_Merged.pdf#page=22>) · [Solution A090](../solutions/SOLUTIONS.html#a090)

**Exact task:** Heartbleed as an out-of-bounds read.

Define Heartbleed and explain its major consequences.

**Coverage / reading note:** The buffer deck teaches memory-bound errors; the particular OpenSSL case is supplementary.

## Unmapped gaps and section boundaries

These are not added to the rankings or silently included among the solved index. The source syllabus does not fully develop them.

| Session | Questions | Paper pages | Gap |
|---|---|---|---|
| 2023–24 | 6(b), 7(a), 8(b) | 7–9 | Affine key recovery; ElGamal encryption; detailed cookie matching. Sec B covers these. |
| 2022–23 | 6(c), 7(b) | 13 | HMAC-DRBG (Sec B) and Tor/onion routing (not developed in either supplied section). |
| 2021–22 | 1(c), 2(b) | 15 | Hill matrices (Sec B) and elliptic-curve arithmetic (worked Sec B extension). |
| 2020–21 | 6(b), 7(a), 7(b), 8(c) | 20–21 | ElGamal signatures; Caesar/Hill attack; cookie matrix; session-token revocation (Sec B). |
| 2019–20 | 6(a) | 24 | OTP and the transposition/Hill connection (Sec B). |
| 2018–19 | 5(a), 13 | 27, 31 | Hill numerical encryption (Sec B); quantum key distribution table (not developed in either section). |

## Evidence-based study sequence

Start with the high-frequency topics in the table, but also account for marks and task type. Practice diagram-driven network reasoning, then malware distinctions and IDS probability; rehearse stack/permission calculations separately. Work the shared crypto/web questions using Sec A’s page map, consulting Sec B for the explicitly labeled extensions. An optional three-mark concept is not the same study workload as a twenty-mark protocol analysis.
