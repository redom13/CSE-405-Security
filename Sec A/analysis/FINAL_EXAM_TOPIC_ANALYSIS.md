# Sec A final-exam topic analysis

**87 mapped printed questions: 84 whole-question entries and 3 entries limited to Sec A components.** [CSV](question_index.csv) · [JSON](question_index.json) · [Worked solutions](../solutions/SOLUTIONS.pdf).

## Scope and counting

**Assignment is by current topic, not by the printed Section A/B heading. Both printed sections of all six yearly papers are checked.** A Sec A topic printed under Section B in an older year still counts here; a Sec B topic printed under Section A does not.

This report covers foundations, physical/OS/filesystem security, memory attacks, malware and network/DNS/IDS defenses. It excludes the standalone crypto, number-theory, password-guessing/recovery and web-attack sets previously imported from Sec B. The presence of an older recap PDF in the source folder does not change that boundary.

One occurrence is a printed lettered subquestion; unlettered 2018–19 Q10 is one whole question. A mixed question counts once per relevant Sec A topic and once per deck. For a question spanning both current sections, only its Sec A tasks are ranked and solved, and its scope note states what was left out. Optional choices are explicitly labeled. Marks printed beside a parent question must not be attributed wholly to a retained component.

Question summaries are paraphrases. Open the original PDF for exact wording, code and diagrams. “Related/extension” means the Sec A source supplies a foundation but the requested mechanism needs more explanation. This is distinct from a question component assigned to Sec B.

## Coverage of both printed sections, year by year

| Academic session | Sitting date | Root PDF pages | Sec A topics in printed A | Sec A topics in printed B | Total |
|---|---|---|---:|---:|---:|
| 2023–24 | 06 September 2025 | 1–10 | 10 | 0 | 10 |
| 2022–23 | 18 April 2024 | 11–14 | 12 | 0 | 12 |
| 2021–22 | 30 October 2023 | 15–17 | 5 | 10 | 15 |
| 2020–21 | 25 September 2022 | 18–21 | 12 | 4 | 16 |
| 2019–20 | 07 September 2021 | 22–25 | 9 | 3 | 12 |
| 2018–19 | 24 October 2019 | 26–31 | 14 | 8 | 22 |

The audit counts mapped parent-question occurrences, including the explicitly scoped mixed entries. Source-code queries for permission delegation and DNS authentication remain system/network questions; they do not create SQL-injection or signature-algorithm chapters.

## Topics ranked by printed-question frequency

| Rank | Exact topic group | All mapped | Direct | Related / extension | Papers / 6 | Main deck |
|---:|---|---:|---:|---:|---:|---|
| 1 | [DNS poisoning, Kaminsky races, pharming and DNSSEC](#dns) | 7 | 6 | 1 | 5/6 | DNS Security |
| 2 | [OS trust, paging, boot and persistent memory images](#os) | 7 | 3 | 4 | 4/6 | Operating Systems Security |
| 3 | [TCP hijacking, spoofed segments and optimistic ACKs](#tcp) | 7 | 3 | 4 | 4/6 | Network Security |
| 4 | [Worm propagation, epidemic models and case studies](#worm) | 6 | 5 | 1 | 5/6 | Malware |
| 5 | [Stack/heap corruption and buffer-overflow payload reasoning](#buffer) | 6 | 1 | 5 | 4/6 | Buffer Overflow |
| 6 | [Firewall state, evasion and defense limits](#firewall) | 5 | 3 | 2 | 4/6 | Firewalls, Tunneling and IDS |
| 7 | [Honeypot topology, monitoring and overhead](#honey) | 5 | 5 | 0 | 4/6 | Firewalls, Tunneling and IDS |
| 8 | [DoS/DDoS, reflection and resource exhaustion](#dos) | 5 | 4 | 1 | 3/6 | Network Security |
| 9 | [Intrusion detection, base rates and audit data](#ids) | 5 | 1 | 4 | 3/6 | Firewalls, Tunneling and IDS |
| 10 | [Security principles and scenario analysis](#principles) | 5 | 3 | 2 | 3/6 | Introduction |
| 11 | [Adware, spyware and malware economics](#adware) | 4 | 3 | 1 | 4/6 | Malware |
| 12 | [Botnet creation, C&C and malicious agents](#botnet) | 4 | 4 | 0 | 4/6 | Malware |
| 13 | [ARP spoofing, MITM and detection](#arp) | 4 | 4 | 0 | 3/6 | Network Security |
| 14 | [Biometrics, authentication factors, SIM and RFID](#auth) | 4 | 2 | 2 | 3/6 | Physical Security |
| 15 | [StackGuard, ASLR and memory-corruption defenses](#canary) | 4 | 1 | 3 | 3/6 | Buffer Overflow |
| 16 | [Access matrices, ACLs, capabilities and RBAC](#access) | 3 | 2 | 1 | 3/6 | Introduction |
| 17 | [Encrypted, polymorphic and metamorphic viruses](#stealth) | 3 | 3 | 0 | 3/6 | Malware |
| 18 | [Reconnaissance, fingerprinting and vulnerability assessment](#recon) | 3 | 3 | 0 | 3/6 | Firewalls, Tunneling and IDS |
| 19 | [Rootkit cloaking, hooking and DLL injection](#rootkit) | 3 | 2 | 1 | 3/6 | Malware |
| 20 | [SYN flooding and stateless SYN cookies](#syn) | 3 | 3 | 0 | 3/6 | Network Security |
| 21 | [CIA, attacker models and security scope](#goals) | 3 | 2 | 1 | 2/6 | Introduction |
| 22 | [Pin-tumbler locks and master-key extensions](#physical) | 3 | 1 | 2 | 1/6 | Physical Security |
| 23 | [DHCP starvation, spoofing and defenses](#dhcp) | 2 | 2 | 0 | 2/6 | Network Security |
| 24 | [Switch MAC-table flooding and port security](#switch) | 2 | 2 | 0 | 2/6 | Network Security |
| 25 | [Unix permissions, setuid and filesystem access](#files) | 2 | 1 | 1 | 2/6 | Filesystem Security |
| 26 | [VPN and IPsec AH/ESP encapsulation](#vpn) | 2 | 2 | 0 | 2/6 | Firewalls, Tunneling and IDS |
| 27 | [Backdoors, logic bombs and insider abuse](#insider) | 2 | 2 | 0 | 1/6 | Malware |
| 28 | [Return-to-libc and calling conventions](#retlibc) | 2 | 0 | 2 | 1/6 | Buffer Overflow |
| 29 | [Faraday shielding and physical information leakage](#emanations) | 1 | 0 | 1 | 1/6 | Physical Security |
| 30 | [Format-string reads and writes](#format) | 1 | 0 | 1 | 1/6 | Buffer Overflow |

## Slide decks ranked by unique mapped questions

| Deck | Distinct Sec A questions | Papers / 6 |
|---|---:|---:|
| Malware | 20 | 6/6 |
| Firewalls, Tunneling and IDS | 20 | 6/6 |
| Network Security | 18 | 6/6 |
| Introduction | 11 | 4/6 |
| Buffer Overflow | 11 | 4/6 |
| Physical Security | 8 | 3/6 |
| Operating Systems Security | 7 | 4/6 |
| DNS Security | 7 | 5/6 |
| Filesystem Security | 2 | 2/6 |

## Questions under slide deck → exact topic

## Introduction

[Ch01-Introduction.pdf](<../slides/Ch01-Introduction.pdf>)

<a id="principles"></a>
### Security principles and scenario analysis — 5 questions

**Study:** deck PDF pp. 11–16; handwritten-note PDF pp. 2, 13–15.

**2023–24 · Q1(b) · 10 marks · direct** · [paper p. 2](<../../CSE405-Security_Merged.pdf#page=2>) · printed Section A · [Solution A002](../solutions/SOLUTIONS.html#a002)

**Exact Sec A task:** Match five scenarios to security principles.

Match principles to a valet key, bypassable laptop screen lock, irreversible water-damage sticker, bank recovery questions overridden by a representative, and encryption at rest and in transit.

**2022–23 · Q1(a) · 10 marks · direct** · [paper p. 11](<../../CSE405-Security_Merged.pdf#page=11>) · printed Section A · [Solution A021](../solutions/SOLUTIONS.html#a021)

**Exact Sec A task:** Least privilege versus separation; why record compromise?.

Differentiate least privilege and separation of privilege, and explain the importance of compromise recording with examples.

**2020–21 · Q1(c) · 11 marks · direct** · [paper p. 18](<../../CSE405-Security_Merged.pdf#page=18>) · printed Section A · [Solution A071](../solutions/SOLUTIONS.html#a071)

**Exact Sec A task:** Why compromise recording matters and which tools support it.

Explain the importance of compromise recording and name tools used for it.

**2020–21 · Q2(b) · 12 marks · partial** · [paper p. 18](<../../CSE405-Security_Merged.pdf#page=18>) · printed Section A · [Solution A073](../solutions/SOLUTIONS.html#a073)

**Exact Sec A task:** Mismatched boarding-pass and identity checks.

Explain how online-printable boarding passes permit a no-fly-list bypass in the described airport checks, and fix the weakness.

**Coverage / reading note:** An application of complete mediation/authentication; the exact airport workflow is in the paper.

**2020–21 · Q8(a) · 15 marks · partial** · [paper p. 20](<../../CSE405-Security_Merged.pdf#page=20>) · printed Section B · [Solution A087](../solutions/SOLUTIONS.html#a087)

**Exact Sec A task:** Audit scanf, privileged file opening and a name-based access race.

Analyze attacks on the printed C program (code on p. 21): scanf into buffer[60], fopen(fn,"a+"), access(fn,W_OK), fwrite; state environmental assumptions.

**Coverage / reading note:** Unsafe C, Unix privileges and complete-mediation principles support the answer; the exact race analysis is an application.

<a id="access"></a>
### Access matrices, ACLs, capabilities and RBAC — 3 questions

**Study:** deck PDF pp. 17–19; handwritten-note PDF pp. 16, 37.

**2022–23 · Q2(b) · 12 marks · direct** · [paper p. 11](<../../CSE405-Security_Merged.pdf#page=11>) · printed Section A · [Solution A025](../solutions/SOLUTIONS.html#a025)

**Exact Sec A task:** Why owner-only access cannot replace access-control systems.

Give at least two scenarios in which users other than a file owner need access, refuting a proposal to restrict all file permissions to owners only.

**2021–22 · Q8(a) · 12 marks · partial** · [paper p. 17](<../../CSE405-Security_Merged.pdf#page=17>) · printed Section B · [Solution A066](../solutions/SOLUTIONS.html#a066)

**Exact Sec A task:** Delegation through GRANT OPTION and revocation dependencies.

Analyze GRANT SELECT ON employees TO Alice WITH GRANT OPTION and revoke access safely when Alice leaves.

**Coverage / reading note:** Access-control delegation is an application of matrices/ACLs; DBMS-specific grant/revoke syntax is not taught in WebDB-security.

**2020–21 · Q2(a) · 12 marks · direct** · [paper p. 18](<../../CSE405-Security_Merged.pdf#page=18>) · printed Section A · [Solution A072](../solutions/SOLUTIONS.html#a072)

**Exact Sec A task:** RBAC diagram, benefits and limitations.

Define role-based access control with a figure, benefits and drawbacks.

<a id="goals"></a>
### CIA, attacker models and security scope — 3 questions

**Study:** deck PDF pp. 1–10; handwritten-note PDF pp. 1–12.

**2021–22 · Q1(a) · 5 marks · partial** · [paper p. 15](<../../CSE405-Security_Merged.pdf#page=15>) · printed Section A · [Solution A043](../solutions/SOLUTIONS.html#a043)

**Exact Sec A task:** Information, IT and cybersecurity scope diagram.

Illustrate the relationship between information security, cybersecurity and IT security with a Venn diagram.

**Coverage / reading note:** The introduction defines CIA and security, but does not specify this three-set taxonomy.

**2021–22 · Q2(a) · 5 marks · direct** · [paper p. 15](<../../CSE405-Security_Merged.pdf#page=15>) · printed Section A · [Solution A046](../solutions/SOLUTIONS.html#a046)

**Exact Sec A task:** Classify attacks by the information-security CIA triad.

Categorize security attacks with respect to confidentiality, integrity and availability.

**2020–21 · Q1(b) · 12 marks · direct** · [paper p. 18](<../../CSE405-Security_Merged.pdf#page=18>) · printed Section A · [Solution A070](../solutions/SOLUTIONS.html#a070)

**Exact Sec A task:** Selective packet dropping against a competitor.

An ISP deliberately drops 25% of a competing provider’s VoIP packets traversing its routers. Identify the attack.

## Physical Security

[Ch02-Physical-Security.pdf](<../slides/Ch02-Physical-Security.pdf>)

<a id="auth"></a>
### Biometrics, authentication factors, SIM and RFID — 4 questions

**Study:** deck PDF pp. 9–27; handwritten-note PDF pp. 20–22.

**2021–22 · Q1(b) · 10 marks · direct** · [paper p. 15](<../../CSE405-Security_Merged.pdf#page=15>) · printed Section A · [Solution A044](../solutions/SOLUTIONS.html#a044)

**Exact Sec A task:** Biometric requirements, recognition pipeline and privacy.

State biometric identification requirements, describe the process, and discuss privacy-preserving challenges.

**2020–21 · Q2(b) · 12 marks · partial** · [paper p. 18](<../../CSE405-Security_Merged.pdf#page=18>) · printed Section A · [Solution A073](../solutions/SOLUTIONS.html#a073)

**Exact Sec A task:** Mismatched boarding-pass and identity checks.

Explain how online-printable boarding passes permit a no-fly-list bypass in the described airport checks, and fix the weakness.

**Coverage / reading note:** An application of complete mediation/authentication; the exact airport workflow is in the paper.

**2018–19 · Q8(a) · 6 marks · direct** · [paper p. 28](<../../CSE405-Security_Merged.pdf#page=28>) · printed Section B · [Solution A131](../solutions/SOLUTIONS.html#a131)

**Exact Sec A task:** Good biometric criteria.

Name essential and desirable characteristics of biometric authentication.

**2018–19 · Q9(b) · 3 marks · partial** · [paper p. 28](<../../CSE405-Security_Merged.pdf#page=28>) · printed Section B · [Solution A134](../solutions/SOLUTIONS.html#a134)

**Exact Sec A task:** Expand ICCID, IMSI and ASLR.

Write the full forms of ICCID, IMSI and ASLR.

**Coverage / reading note:** SIM identifiers are in the physical deck/notes; ASLR is a memory-defense extension.

<a id="physical"></a>
### Pin-tumbler locks and master-key extensions — 3 questions

**Study:** deck PDF pp. 4–8; handwritten-note PDF pp. 19.

**2018–19 · Q6(b) · 7 marks · direct** · [paper p. 27](<../../CSE405-Security_Merged.pdf#page=27>) · printed Section B · [Solution A128](../solutions/SOLUTIONS.html#a128)

**Exact Sec A task:** Pin-tumbler cross section.

Draw a pin-tumbler lock cross section and label its parts.

**2018–19 · Q7(a) · 3 marks · partial** · [paper p. 27](<../../CSE405-Security_Merged.pdf#page=27>) · printed Section B · [Solution A129](../solutions/SOLUTIONS.html#a129)

**Exact Sec A task:** Count additional keys after three master wafers.

A five-pin lock has driver pins of height 5 and key pins 2,4,5,2,6. Add one master wafer in each of three selected chambers. How many additional keys theoretically open it?

**Coverage / reading note:** The deck teaches basic pin-tumbler operation; master-wafer combinatorics is an extension.

**2018–19 · Q7(b) · 12 marks · partial** · [paper p. 27](<../../CSE405-Security_Merged.pdf#page=27>) · printed Section B · [Solution A130](../solutions/SOLUTIONS.html#a130)

**Exact Sec A task:** Construct a lock accepting both stated keys.

Given L1 key-pin heights (2,4,5,2,6) and L2 (4,2,5,5,6), driver heights 5, design L3 with master wafers so both keys work, and show K1 opening it.

**Coverage / reading note:** Master-key construction extends the basic lock slides; the geometric interpretation is stated explicitly.

<a id="emanations"></a>
### Faraday shielding and physical information leakage — 1 questions

**Study:** deck PDF pp. 28–32; handwritten-note PDF pp. 23.

**2018–19 · Q8(b) · 9 printed marks · partial** · [paper p. 28](<../../CSE405-Security_Merged.pdf#page=28>) · printed Section B · [Solution A132](../solutions/SOLUTIONS.html#a132)

**Exact Sec A task:** Faraday cage and OS impersonation-token short notes.

From the printed “any three” short notes, cover the Sec A options: (i) Faraday cage and (iii) impersonation token.

**Section boundary:** Covers only options (i) Faraday cage and (iii) OS impersonation token, 3 marks each. Options (ii) blind SQL injection and (iv) homograph attack remain in Sec B. The printed 9 marks require any three choices.

**Coverage / reading note:** The printed subquestion is 9 marks for any three choices. This guide covers only two Sec A choices (3 marks each); it is not a full 9-mark answer. OS impersonation-token mechanics extend the supplied privilege material.

## Operating Systems Security

[Ch03-OS-Security.pdf](<../slides/Ch03-OS-Security.pdf>)

<a id="os"></a>
### OS trust, paging, boot and persistent memory images — 7 questions

**Study:** deck PDF pp. 19–33; handwritten-note PDF pp. 24, 31–36.

**2021–22 · Q4(a) · 5 marks · direct** · [paper p. 16](<../../CSE405-Security_Merged.pdf#page=16>) · printed Section A · [Solution A053](../solutions/SOLUTIONS.html#a053)

**Exact Sec A task:** Secrets persisted in swap/hibernation.

Explain how virtual memory or a swap partition can be an attacker target.

**2020–21 · Q1(c) · 11 marks · direct** · [paper p. 18](<../../CSE405-Security_Merged.pdf#page=18>) · printed Section A · [Solution A071](../solutions/SOLUTIONS.html#a071)

**Exact Sec A task:** Why compromise recording matters and which tools support it.

Explain the importance of compromise recording and name tools used for it.

**2020–21 · Q2(c) · 11 marks · partial** · [paper p. 18](<../../CSE405-Security_Merged.pdf#page=18>) · printed Section A · [Solution A074](../solutions/SOLUTIONS.html#a074)

**Exact Sec A task:** Forensic preservation: master and working images, custody.

Why make two copies of digital evidence? State precautions and how to maintain chain of custody.

**Coverage / reading note:** OS/hibernation notes mention forensic investigation; full acquisition and custody procedures are supplementary.

**2020–21 · Q3(a) · 12 marks · direct** · [paper p. 18](<../../CSE405-Security_Merged.pdf#page=18>) · printed Section A · [Solution A075](../solutions/SOLUTIONS.html#a075)

**Exact Sec A task:** Why preserve memory-region boundaries?.

Explain the risks of mixing heap and stack storage and give an example manipulation.

**2019–20 · Q2(c) · 11 marks · partial** · [paper p. 22](<../../CSE405-Security_Merged.pdf#page=22>) · printed Section A · [Solution A094](../solutions/SOLUTIONS.html#a094)

**Exact Sec A task:** Verify a reported DoS source and respond with evidence.

A hall administrator says your shared network segment is sending DoS traffic. You deny involvement but are unsure about your roommate. How do you verify and respond?

**Coverage / reading note:** Uses IDS/network logs and OS event logging; incident-handling workflow extends the slides.

**2019–20 · Q5(b) · 14 marks · partial** · [paper p. 24](<../../CSE405-Security_Merged.pdf#page=24>) · printed Section B · [Solution A102](../solutions/SOLUTIONS.html#a102)

**Exact Sec A task:** Audit-record fields and statistical intrusion detection.

List useful audit-record fields, explain statistical IDS and identify a weakness.

**Coverage / reading note:** Event logging and IDS sensors are taught; statistical-model design is an extension.

**2018–19 · Q8(b) · 9 printed marks · partial** · [paper p. 28](<../../CSE405-Security_Merged.pdf#page=28>) · printed Section B · [Solution A132](../solutions/SOLUTIONS.html#a132)

**Exact Sec A task:** Faraday cage and OS impersonation-token short notes.

From the printed “any three” short notes, cover the Sec A options: (i) Faraday cage and (iii) impersonation token.

**Section boundary:** Covers only options (i) Faraday cage and (iii) OS impersonation token, 3 marks each. Options (ii) blind SQL injection and (iv) homograph attack remain in Sec B. The printed 9 marks require any three choices.

**Coverage / reading note:** The printed subquestion is 9 marks for any three choices. This guide covers only two Sec A choices (3 marks each); it is not a full 9-mark answer. OS impersonation-token mechanics extend the supplied privilege material.

## Buffer Overflow

[Ch03-BufferOverflow.pdf](<../slides/Ch03-BufferOverflow.pdf>)

<a id="buffer"></a>
### Stack/heap corruption and buffer-overflow payload reasoning — 6 questions

**Study:** deck PDF pp. 1–8; handwritten-note PDF pp. 24–30.

**2023–24 · Q1(a) · 10 marks · partial** · [paper p. 1](<../../CSE405-Security_Merged.pdf#page=1>) · printed Section A · [Solution A001](../solutions/SOLUTIONS.html#a001)

**Exact Sec A task:** Trace the actual unsafe copies and construct a conditional control-flow payload.

For the printed 32-bit little-endian C program, decide whether hack() can be invoked and give symbolic-address payload pseudocode. All defenses are disabled; main reads 300 bytes into str[30]; overflow_in_action has buffer[300], two heap pointers, strcpy calls and an indirect callback.

**Coverage / reading note:** The source does not fix frame offsets or heap allocator layout. A conditional symbolic payload is justified; an unconditional offset is not.

**2023–24 · Q2(b) · 10 marks · partial** · [paper p. 3](<../../CSE405-Security_Merged.pdf#page=3>) · printed Section A · [Solution A005](../solutions/SOLUTIONS.html#a005)

**Exact Sec A task:** Leaked stack address and one-byte saved-frame-pointer overwrite.

32-bit x86 with ASLR: main prints simple[32] address and reads with fgets(simple,32). hack copies nine input bytes backward into buf[8]. Construct inputs for a 31-byte shellcode, identifying necessary stack-layout assumptions.

**Coverage / reading note:** Compiler local ordering, padding and the location of a surviving fake frame are not specified, so the intended off-by-one exploit is conditional.

**2020–21 · Q3(a) · 12 marks · direct** · [paper p. 18](<../../CSE405-Security_Merged.pdf#page=18>) · printed Section A · [Solution A075](../solutions/SOLUTIONS.html#a075)

**Exact Sec A task:** Why preserve memory-region boundaries?.

Explain the risks of mixing heap and stack storage and give an example manipulation.

**2020–21 · Q8(a) · 15 marks · partial** · [paper p. 20](<../../CSE405-Security_Merged.pdf#page=20>) · printed Section B · [Solution A087](../solutions/SOLUTIONS.html#a087)

**Exact Sec A task:** Audit scanf, privileged file opening and a name-based access race.

Analyze attacks on the printed C program (code on p. 21): scanf into buffer[60], fopen(fn,"a+"), access(fn,W_OK), fwrite; state environmental assumptions.

**Coverage / reading note:** Unsafe C, Unix privileges and complete-mediation principles support the answer; the exact race analysis is an application.

**2019–20 · Q1(b) · 12 marks · partial** · [paper p. 22](<../../CSE405-Security_Merged.pdf#page=22>) · printed Section A · [Solution A090](../solutions/SOLUTIONS.html#a090)

**Exact Sec A task:** Heartbleed as an out-of-bounds read.

Define Heartbleed and explain its major consequences.

**Coverage / reading note:** The buffer deck teaches memory-bound errors; the particular OpenSSL case is supplementary.

**2018–19 · Q10 · 15 marks · partial** · [paper p. 29](<../../CSE405-Security_Merged.pdf#page=29>) · printed Section B · [Solution A135](../solutions/SOLUTIONS.html#a135)

**Exact Sec A task:** Toy stack frames and an alphabet-only return target.

For the printed main/foo/bar C snippets, draw all frames using supplied addresses and create alphabet-only sample.txt so bar returns directly to main. Each source instruction is stipulated to occupy one byte; integer=4 bytes.

**Coverage / reading note:** Stack reasoning is taught, but this question imposes artificial instruction sizes/frame addresses and leaves the file-read body unspecified.

<a id="canary"></a>
### StackGuard, ASLR and memory-corruption defenses — 4 questions

**Study:** deck PDF pp. 8 (canary); ASLR/code-reuse defenses are extensions; handwritten-note PDF pp. 30.

**2023–24 · Q2(b) · 10 marks · partial** · [paper p. 3](<../../CSE405-Security_Merged.pdf#page=3>) · printed Section A · [Solution A005](../solutions/SOLUTIONS.html#a005)

**Exact Sec A task:** Leaked stack address and one-byte saved-frame-pointer overwrite.

32-bit x86 with ASLR: main prints simple[32] address and reads with fgets(simple,32). hack copies nine input bytes backward into buf[8]. Construct inputs for a 31-byte shellcode, identifying necessary stack-layout assumptions.

**Coverage / reading note:** Compiler local ordering, padding and the location of a surviving fake frame are not specified, so the intended off-by-one exploit is conditional.

**2020–21 · Q5(c) · 10 marks · partial** · [paper p. 19](<../../CSE405-Security_Merged.pdf#page=19>) · printed Section B · [Solution A083](../solutions/SOLUTIONS.html#a083)

**Exact Sec A task:** Four defenses against return-to-libc.

Briefly explain four countermeasures against return-to-libc attacks.

**Coverage / reading note:** Buffer-overflow basics are taught; code reuse and several defense mechanisms require supplementary material.

**2020–21 · Q7(c) · 10 marks · direct** · [paper p. 20](<../../CSE405-Security_Merged.pdf#page=20>) · printed Section B · [Solution A086](../solutions/SOLUTIONS.html#a086)

**Exact Sec A task:** StackGuard check and scope.

Define StackGuard and explain with a diagram how it counters buffer overflow.

**Coverage / reading note:** Overflow PDF p. 8 and handwritten notes p. 30 depict the canary mechanism; implementation limits are explained in the answer.

**2018–19 · Q9(b) · 3 marks · partial** · [paper p. 28](<../../CSE405-Security_Merged.pdf#page=28>) · printed Section B · [Solution A134](../solutions/SOLUTIONS.html#a134)

**Exact Sec A task:** Expand ICCID, IMSI and ASLR.

Write the full forms of ICCID, IMSI and ASLR.

**Coverage / reading note:** SIM identifiers are in the physical deck/notes; ASLR is a memory-defense extension.

<a id="retlibc"></a>
### Return-to-libc and calling conventions — 2 questions

**Study:** deck PDF pp. 4–8 (background; libc chaining is an extension); handwritten-note PDF pp. 24–30 (background).

**2020–21 · Q5(c) · 10 marks · partial** · [paper p. 19](<../../CSE405-Security_Merged.pdf#page=19>) · printed Section B · [Solution A083](../solutions/SOLUTIONS.html#a083)

**Exact Sec A task:** Four defenses against return-to-libc.

Briefly explain four countermeasures against return-to-libc attacks.

**Coverage / reading note:** Buffer-overflow basics are taught; code reuse and several defense mechanisms require supplementary material.

**2020–21 · Q6(c) · 10 marks · partial** · [paper p. 20](<../../CSE405-Security_Merged.pdf#page=20>) · printed Section B · [Solution A085](../solutions/SOLUTIONS.html#a085)

**Exact Sec A task:** Place system arguments using 32-bit cdecl.

Using diagrams, determine placement of the system() argument in a return-to-libc attack.

**Coverage / reading note:** The supplied C/stack material is background; the cdecl libc-chain layout is an extension.

<a id="format"></a>
### Format-string reads and writes — 1 questions

**Study:** deck PDF pp. 1–8 (background only; format strings are an extension); handwritten-note PDF pp. 24–30 (background).

**2018–19 · Q9(a) · 12 marks · partial** · [paper p. 28](<../../CSE405-Security_Merged.pdf#page=28>) · printed Section B · [Solution A133](../solutions/SOLUTIONS.html#a133)

**Exact Sec A task:** Four format-string tasks using the stated stack-word cursor.

For gets(user_input); printf(user_input), construct inputs to print secret1, change secret1, print secret2 and print secret3. Cursor starts 0xaabbcc20; secret1=0xaabbcc34, secret2=0xaabbcc38, secret3=0x11223344, input=0xaabbcc50; integers are 4 bytes.

**Coverage / reading note:** The slides teach unsafe C but do not develop format-string exploitation; the paper supplies a special cursor model.

## Filesystem Security

[Ch03-FilesystemSecurity.pdf](<../slides/Ch03-FilesystemSecurity.pdf>)

<a id="files"></a>
### Unix permissions, setuid and filesystem access — 2 questions

**Study:** deck PDF pp. 1–19; handwritten-note PDF pp. 28–29, 37–40.

**2020–21 · Q8(a) · 15 marks · partial** · [paper p. 20](<../../CSE405-Security_Merged.pdf#page=20>) · printed Section B · [Solution A087](../solutions/SOLUTIONS.html#a087)

**Exact Sec A task:** Audit scanf, privileged file opening and a name-based access race.

Analyze attacks on the printed C program (code on p. 21): scanf into buffer[60], fopen(fn,"a+"), access(fn,W_OK), fwrite; state environmental assumptions.

**Coverage / reading note:** Unsafe C, Unix privileges and complete-mediation principles support the answer; the exact race analysis is an application.

**2019–20 · Q3(c) · 11 marks · direct** · [paper p. 22](<../../CSE405-Security_Merged.pdf#page=22>) · printed Section A · [Solution A097](../solutions/SOLUTIONS.html#a097)

**Exact Sec A task:** Setuid/chmod under the paper’s no-revert assumption.

Alice wants Bob’s photo program without exposing her confidential files; Bob wants his code unreadable to Alice. Use Unix setuid/chmod, assume the process cannot revert to real UID after adopting its setuid identity, and consider exfiltration by malicious code.

## Malware

[Ch04-Malware.pdf](<../slides/Ch04-Malware.pdf>)

<a id="worm"></a>
### Worm propagation, epidemic models and case studies — 6 questions

**Study:** deck PDF pp. 31–39; handwritten-note PDF pp. 8–9, 49–51.

**2023–24 · Q3(b) · 5 marks · direct** · [paper p. 4](<../../CSE405-Security_Merged.pdf#page=4>) · printed Section A · [Solution A008](../solutions/SOLUTIONS.html#a008)

**Exact Sec A task:** Code Red patch status and propagation.

Did Code Red exploit a zero-day vulnerability? Explain its propagation.

**2022–23 · Q4(d) · 6 marks · direct** · [paper p. 12](<../../CSE405-Security_Merged.pdf#page=12>) · printed Section A · [Solution A033](../solutions/SOLUTIONS.html#a033)

**Exact Sec A task:** Zero-day meaning and detection limits.

Define a zero-day attack and explain why it is dangerous.

**2020–21 · Q1(a) · 12 marks · direct** · [paper p. 18](<../../CSE405-Security_Merged.pdf#page=18>) · printed Section A · [Solution A069](../solutions/SOLUTIONS.html#a069)

**Exact Sec A task:** WannaCry vulnerability, success and zero-day status.

Identify WannaCry’s main vulnerability, why it succeeded and whether it was a zero-day attack.

**2020–21 · Q3(c) · 11 marks · direct** · [paper p. 18](<../../CSE405-Security_Merged.pdf#page=18>) · printed Section A · [Solution A077](../solutions/SOLUTIONS.html#a077)

**Exact Sec A task:** Derive the SI epidemic worm model.

Explain an epidemic model of worm propagation with a figure.

**2019–20 · Q3(a) · 12 marks · partial** · [paper p. 22](<../../CSE405-Security_Merged.pdf#page=22>) · printed Section A · [Solution A095](../solutions/SOLUTIONS.html#a095)

**Exact Sec A task:** Three reasons ransomware grew during COVID-era disruption.

Give three major reasons ransomware attacks increased during the COVID-19 pandemic.

**Coverage / reading note:** Malware economics is taught, but COVID-specific comparative evidence is not supplied.

**2018–19 · Q2(d) · 8 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · printed Section A · [Solution A117](../solutions/SOLUTIONS.html#a117)

**Exact Sec A task:** Morris worm speed and consequences.

Why did the Morris worm spread rapidly and what were the consequences?

<a id="adware"></a>
### Adware, spyware and malware economics — 4 questions

**Study:** deck PDF pp. 55–60; handwritten-note PDF pp. 45, 54–55.

**2022–23 · Q3(c) · 11 marks · direct** · [paper p. 11](<../../CSE405-Security_Merged.pdf#page=11>) · printed Section A · [Solution A029](../solutions/SOLUTIONS.html#a029)

**Exact Sec A task:** Adware data flow and spyware revenue.

Explain adware operation with a figure and why its author benefits from adding spyware.

**2021–22 · Q5(a) · 12 marks · direct** · [paper p. 16](<../../CSE405-Security_Merged.pdf#page=16>) · printed Section B · [Solution A057](../solutions/SOLUTIONS.html#a057)

**Exact Sec A task:** Why sell many signature-distinct variants of one exploit?.

Explain the financial benefits of creating many malware variants exploiting the same popular-software vulnerability but having different signatures.

**2019–20 · Q3(a) · 12 marks · partial** · [paper p. 22](<../../CSE405-Security_Merged.pdf#page=22>) · printed Section A · [Solution A095](../solutions/SOLUTIONS.html#a095)

**Exact Sec A task:** Three reasons ransomware grew during COVID-era disruption.

Give three major reasons ransomware attacks increased during the COVID-19 pandemic.

**Coverage / reading note:** Malware economics is taught, but COVID-specific comparative evidence is not supplied.

**2018–19 · Q2(b) · 8 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · printed Section A · [Solution A115](../solutions/SOLUTIONS.html#a115)

**Exact Sec A task:** Why adware authors add spyware.

Explain why spyware benefits an adware author.

<a id="botnet"></a>
### Botnet creation, C&C and malicious agents — 4 questions

**Study:** deck PDF pp. 40–45; handwritten-note PDF pp. 5, 51–52.

**2021–22 · Q5(c) · 11 marks · direct** · [paper p. 16](<../../CSE405-Security_Merged.pdf#page=16>) · printed Section B · [Solution A059](../solutions/SOLUTIONS.html#a059)

**Exact Sec A task:** Disrupting C&C through coordinated investigation.

Formulate a process to take down a botnet command-and-control server.

**2020–21 · Q4(b) · 12 marks · direct** · [paper p. 19](<../../CSE405-Security_Merged.pdf#page=19>) · printed Section A · [Solution A079](../solutions/SOLUTIONS.html#a079)

**Exact Sec A task:** Value and defense of an internal malware agent.

Explain why an attacker installs an agent inside a corporate network, delivery methods and prevention; assess whether a firewall can help.

**2019–20 · Q2(a) · 12 marks · direct** · [paper p. 22](<../../CSE405-Security_Merged.pdf#page=22>) · printed Section A · [Solution A092](../solutions/SOLUTIONS.html#a092)

**Exact Sec A task:** Botnet architecture and distributed floods.

Explain botnet components and how they launch DDoS, with a figure.

**2018–19 · Q3(d) · 10 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · printed Section A · [Solution A121](../solutions/SOLUTIONS.html#a121)

**Exact Sec A task:** Bot creation, control and uses.

Explain botnet creation/control and possible activities.

<a id="stealth"></a>
### Encrypted, polymorphic and metamorphic viruses — 3 questions

**Study:** deck PDF pp. 22–30, 57–58; handwritten-note PDF pp. 46–49, 54–56.

**2021–22 · Q5(a) · 12 marks · direct** · [paper p. 16](<../../CSE405-Security_Merged.pdf#page=16>) · printed Section B · [Solution A057](../solutions/SOLUTIONS.html#a057)

**Exact Sec A task:** Why sell many signature-distinct variants of one exploit?.

Explain the financial benefits of creating many malware variants exploiting the same popular-software vulnerability but having different signatures.

**2019–20 · Q3(b) · 12 marks · direct** · [paper p. 22](<../../CSE405-Security_Merged.pdf#page=22>) · printed Section A · [Solution A096](../solutions/SOLUTIONS.html#a096)

**Exact Sec A task:** Encrypted-virus structure and detection.

Explain how an encrypted virus is formed and how to detect it.

**2018–19 · Q2(a) · 7 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · printed Section A · [Solution A114](../solutions/SOLUTIONS.html#a114)

**Exact Sec A task:** Polymorphic versus metamorphic viruses with examples.

Distinguish polymorphic and metamorphic viruses and give two examples of each.

<a id="rootkit"></a>
### Rootkit cloaking, hooking and DLL injection — 3 questions

**Study:** deck PDF pp. 46–54; handwritten-note PDF pp. 28, 53–54.

**2022–23 · Q3(b) · 12 marks · direct** · [paper p. 11](<../../CSE405-Security_Merged.pdf#page=11>) · printed Section A · [Solution A028](../solutions/SOLUTIONS.html#a028)

**Exact Sec A task:** Kernel API hooking and rootkit concealment.

List rootkit features and explain kernel-level hiding through function hooking.

**2021–22 · Q3(a) · 5 marks · partial** · [paper p. 15](<../../CSE405-Security_Merged.pdf#page=15>) · printed Section A · [Solution A049](../solutions/SOLUTIONS.html#a049)

**Exact Sec A task:** DLL injection and inherited process authority.

Explain why DLL injection poses high security risks.

**Coverage / reading note:** Rootkit/API filtering and process hijacking are taught; detailed DLL-injection mechanics are not.

**2018–19 · Q2(c) · 12 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · printed Section A · [Solution A116](../solutions/SOLUTIONS.html#a116)

**Exact Sec A task:** Function hooking and three concealment targets.

Define rootkit function hooking, its danger and three examples of avoiding detection.

<a id="insider"></a>
### Backdoors, logic bombs and insider abuse — 2 questions

**Study:** deck PDF pp. 3–10; handwritten-note PDF pp. 41–42.

**2018–19 · Q1(c) · 9 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · printed Section A · [Solution A112](../solutions/SOLUTIONS.html#a112)

**Exact Sec A task:** Threshold-triggered banking-data exfiltration.

A programmer secretly emails account details whenever a balance exceeds USD 5,000. Identify the attack and risks.

**2018–19 · Q3(a) · 6 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · printed Section A · [Solution A118](../solutions/SOLUTIONS.html#a118)

**Exact Sec A task:** Easter egg versus logic bomb.

Give examples of an Easter egg and a logic bomb.

## Network Security

[Ch05-NetworkSecurity.pdf](<../slides/Ch05-NetworkSecurity.pdf>)

<a id="tcp"></a>
### TCP hijacking, spoofed segments and optimistic ACKs — 7 questions

**Study:** deck PDF pp. 20–23 (optimistic ACK details are extensions); handwritten-note PDF pp. 65–67.

**2023–24 · Q2(c) · 15 marks · partial** · [paper p. 3](<../../CSE405-Security_Merged.pdf#page=3>) · printed Section A · [Solution A006](../solutions/SOLUTIONS.html#a006)

**Exact Sec A task:** Off-path TCP injection and establishing a replacement connection.

Using the printed TCP diagram (continued on p. 4), evaluate malicious actions by an off-path attacker and impersonating the client after it resets the connection.

**Coverage / reading note:** The network deck covers TCP state/hijacking; the modern blind-reset and ISN details extend it.

**2023–24 · Q3(a) · 10 printed marks · direct** · [paper p. 4](<../../CSE405-Security_Merged.pdf#page=4>) · printed Section A · [Solution A007](../solutions/SOLUTIONS.html#a007)

**Exact Sec A task:** Can NIDS/firewall plus HTTPS always stop the network attacks?.

An HTTPS-only server farm has a NIDS and firewall processing incoming requests. With an on-path attacker, assess the Sec A cases: RST injection, SYN flooding, DNS spoofing and DDoS.

**Section boundary:** Covers the four network-defense cases. The reflected-XSS case in the original five-part question belongs to Sec B and is excluded. The 10 printed marks cover all five cases; no per-case allocation is supplied.

**2023–24 · Q4(a) · 10 marks · direct** · [paper p. 5](<../../CSE405-Security_Merged.pdf#page=5>) · printed Section A · [Solution A010](../solutions/SOLUTIONS.html#a010)

**Exact Sec A task:** UDP chargen/echo feedback versus TCP handshake.

JULY on UDP port 36 returns 36–360 random characters; PROTIDHONI on port 5 echoes its input. Give one empty UDP packet creating a feedback loop between X and Y, then assess a single spoofed TCP SYN when both services require a handshake.

**2021–22 · Q6(a) · 12 marks · partial** · [paper p. 17](<../../CSE405-Security_Merged.pdf#page=17>) · printed Section B · [Solution A060](../solutions/SOLUTIONS.html#a060)

**Exact Sec A task:** Detect optimistic ACKs by withholding a segment.

Explain how randomly dropping data segments at the sender helps detect optimistic TCP ACK attacks.

**Coverage / reading note:** The network deck explains TCP ACK state; optimistic-ACK probing is beyond its explicit treatment.

**2019–20 · Q4(c) · 11 marks · partial** · [paper p. 23](<../../CSE405-Security_Merged.pdf#page=23>) · printed Section A · [Solution A100](../solutions/SOLUTIONS.html#a100)

**Exact Sec A task:** Withheld-segment detection of optimistic ACKs.

Explain with examples how sender-side random segment dropping detects optimistic ACKs.

**Coverage / reading note:** Optimistic-ACK details extend the TCP-state slides.

**2018–19 · Q3(b) · 9 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · printed Section A · [Solution A119](../solutions/SOLUTIONS.html#a119)

**Exact Sec A task:** Complete TCP hijacking.

Explain with a diagram how to perform TCP session hijacking.

**2018–19 · Q3(c) · 10 marks · partial** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · printed Section A · [Solution A120](../solutions/SOLUTIONS.html#a120)

**Exact Sec A task:** Optimistic TCP ACK mechanism and mitigation.

Define optimistic TCP ACK attack and give mitigations.

**Coverage / reading note:** The deck covers TCP state but not optimistic-ACK algorithms.

<a id="dos"></a>
### DoS/DDoS, reflection and resource exhaustion — 5 questions

**Study:** deck PDF pp. 24–29; handwritten-note PDF pp. 67–68.

**2023–24 · Q3(a) · 10 printed marks · direct** · [paper p. 4](<../../CSE405-Security_Merged.pdf#page=4>) · printed Section A · [Solution A007](../solutions/SOLUTIONS.html#a007)

**Exact Sec A task:** Can NIDS/firewall plus HTTPS always stop the network attacks?.

An HTTPS-only server farm has a NIDS and firewall processing incoming requests. With an on-path attacker, assess the Sec A cases: RST injection, SYN flooding, DNS spoofing and DDoS.

**Section boundary:** Covers the four network-defense cases. The reflected-XSS case in the original five-part question belongs to Sec B and is excluded. The 10 printed marks cover all five cases; no per-case allocation is supplied.

**2023–24 · Q4(a) · 10 marks · direct** · [paper p. 5](<../../CSE405-Security_Merged.pdf#page=5>) · printed Section A · [Solution A010](../solutions/SOLUTIONS.html#a010)

**Exact Sec A task:** UDP chargen/echo feedback versus TCP handshake.

JULY on UDP port 36 returns 36–360 random characters; PROTIDHONI on port 5 echoes its input. Give one empty UDP packet creating a feedback loop between X and Y, then assess a single spoofed TCP SYN when both services require a handshake.

**2020–21 · Q1(b) · 12 marks · direct** · [paper p. 18](<../../CSE405-Security_Merged.pdf#page=18>) · printed Section A · [Solution A070](../solutions/SOLUTIONS.html#a070)

**Exact Sec A task:** Selective packet dropping against a competitor.

An ISP deliberately drops 25% of a competing provider’s VoIP packets traversing its routers. Identify the attack.

**2019–20 · Q2(a) · 12 marks · direct** · [paper p. 22](<../../CSE405-Security_Merged.pdf#page=22>) · printed Section A · [Solution A092](../solutions/SOLUTIONS.html#a092)

**Exact Sec A task:** Botnet architecture and distributed floods.

Explain botnet components and how they launch DDoS, with a figure.

**2019–20 · Q2(c) · 11 marks · partial** · [paper p. 22](<../../CSE405-Security_Merged.pdf#page=22>) · printed Section A · [Solution A094](../solutions/SOLUTIONS.html#a094)

**Exact Sec A task:** Verify a reported DoS source and respond with evidence.

A hall administrator says your shared network segment is sending DoS traffic. You deny involvement but are unsure about your roommate. How do you verify and respond?

**Coverage / reading note:** Uses IDS/network logs and OS event logging; incident-handling workflow extends the slides.

<a id="arp"></a>
### ARP spoofing, MITM and detection — 4 questions

**Study:** deck PDF pp. 5–12; handwritten-note PDF pp. 58–61.

**2023–24 · Q2(a) · 10 marks · direct** · [paper p. 3](<../../CSE405-Security_Merged.pdf#page=3>) · printed Section A · [Solution A004](../solutions/SOLUTIONS.html#a004)

**Exact Sec A task:** Rogue DHCP gateway and MITM with the correct gateway.

Attacker IP is 10.10.10.32; router/DHCP server is 10.10.10.4. Give a forged client IP/default router for Alice. If the correct router is supplied, explain another way to become MITM.

**2020–21 · Q4(a) · 12 marks · direct** · [paper p. 19](<../../CSE405-Security_Merged.pdf#page=19>) · printed Section A · [Solution A078](../solutions/SOLUTIONS.html#a078)

**Exact Sec A task:** ARP prevention, monitoring and locating the attacking port.

Give ARP-spoofing defenses and ways to identify an attacking host on the internal network.

**2018–19 · Q3(b) · 9 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · printed Section A · [Solution A119](../solutions/SOLUTIONS.html#a119)

**Exact Sec A task:** Complete TCP hijacking.

Explain with a diagram how to perform TCP session hijacking.

**2018–19 · Q4(c) · 9 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · printed Section A · [Solution A124](../solutions/SOLUTIONS.html#a124)

**Exact Sec A task:** Rule-based ARP-spoofing detection.

Give rules a rule-based IDS can use to detect ARP spoofing.

<a id="syn"></a>
### SYN flooding and stateless SYN cookies — 3 questions

**Study:** deck PDF pp. 30–34; handwritten-note PDF pp. 69–70.

**2023–24 · Q3(a) · 10 printed marks · direct** · [paper p. 4](<../../CSE405-Security_Merged.pdf#page=4>) · printed Section A · [Solution A007](../solutions/SOLUTIONS.html#a007)

**Exact Sec A task:** Can NIDS/firewall plus HTTPS always stop the network attacks?.

An HTTPS-only server farm has a NIDS and firewall processing incoming requests. With an on-path attacker, assess the Sec A cases: RST injection, SYN flooding, DNS spoofing and DDoS.

**Section boundary:** Covers the four network-defense cases. The reflected-XSS case in the original five-part question belongs to Sec B and is excluded. The 10 printed marks cover all five cases; no per-case allocation is supplied.

**2022–23 · Q1(b) · 12 marks · direct** · [paper p. 11](<../../CSE405-Security_Merged.pdf#page=11>) · printed Section A · [Solution A022](../solutions/SOLUTIONS.html#a022)

**Exact Sec A task:** SYN backlog exhaustion and cookie validation.

Explain SYN flooding with a figure and evaluate SYN cookies.

**2021–22 · Q7(a) · 12 marks · direct** · [paper p. 17](<../../CSE405-Security_Merged.pdf#page=17>) · printed Section B · [Solution A063](../solutions/SOLUTIONS.html#a063)

**Exact Sec A task:** SYN-cookie defense.

Explain how SYN cookies defend against SYN flooding.

<a id="dhcp"></a>
### DHCP starvation, spoofing and defenses — 2 questions

**Study:** deck PDF pp. 16–19; handwritten-note PDF pp. 63–65.

**2023–24 · Q2(a) · 10 marks · direct** · [paper p. 3](<../../CSE405-Security_Merged.pdf#page=3>) · printed Section A · [Solution A004](../solutions/SOLUTIONS.html#a004)

**Exact Sec A task:** Rogue DHCP gateway and MITM with the correct gateway.

Attacker IP is 10.10.10.32; router/DHCP server is 10.10.10.4. Give a forged client IP/default router for Alice. If the correct router is supplied, explain another way to become MITM.

**2022–23 · Q1(c) · 13 marks · direct** · [paper p. 11](<../../CSE405-Security_Merged.pdf#page=11>) · printed Section A · [Solution A023](../solutions/SOLUTIONS.html#a023)

**Exact Sec A task:** DHCP starvation message flow and rogue-server relationship.

Explain DHCP starvation with a message diagram and analyze its relation to DHCP spoofing.

<a id="switch"></a>
### Switch MAC-table flooding and port security — 2 questions

**Study:** deck PDF pp. 13–15; handwritten-note PDF pp. 61–63.

**2022–23 · Q3(a) · 12 marks · direct** · [paper p. 11](<../../CSE405-Security_Merged.pdf#page=11>) · printed Section A · [Solution A027](../solutions/SOLUTIONS.html#a027)

**Exact Sec A task:** CAM exhaustion and switch behavior.

Explain MAC flooding with topology, effects on a switch and attacker benefits.

**2019–20 · Q4(b) · 12 marks · direct** · [paper p. 23](<../../CSE405-Security_Merged.pdf#page=23>) · printed Section A · [Solution A099](../solutions/SOLUTIONS.html#a099)

**Exact Sec A task:** Making a switch flood unknown destinations.

Why make a switch behave like a hub, what attack does this and how can it be prevented?

## DNS Security

[Ch06-1-NetworkDNS.pdf](<../slides/Ch06-1-NetworkDNS.pdf>)

<a id="dns"></a>
### DNS poisoning, Kaminsky races, pharming and DNSSEC — 7 questions

**Study:** deck PDF pp. 27–43; handwritten-note PDF pp. 72–80.

**2023–24 · Q3(a) · 10 printed marks · direct** · [paper p. 4](<../../CSE405-Security_Merged.pdf#page=4>) · printed Section A · [Solution A007](../solutions/SOLUTIONS.html#a007)

**Exact Sec A task:** Can NIDS/firewall plus HTTPS always stop the network attacks?.

An HTTPS-only server farm has a NIDS and firewall processing incoming requests. With an on-path attacker, assess the Sec A cases: RST injection, SYN flooding, DNS spoofing and DDoS.

**Section boundary:** Covers the four network-defense cases. The reflected-XSS case in the original five-part question belongs to Sec B and is excluded. The 10 printed marks cover all five cases; no per-case allocation is supplied.

**2023–24 · Q3(c) · 20 marks · direct** · [paper p. 4](<../../CSE405-Security_Merged.pdf#page=4>) · printed Section A · [Solution A009](../solutions/SOLUTIONS.html#a009)

**Exact Sec A task:** Kaminsky retries, bailiwick, DNS-over-TLS and DNSSEC.

An internal attacker loads many fakeN.buet.ac.bd image names to poison the shared resolver (no source-port randomization). Explain why many images help, whether the same page can poison www.google.com, and the effects of DNS-over-TLS and DNSSEC.

**2022–23 · Q4(a) · 12 marks · direct** · [paper p. 12](<../../CSE405-Security_Merged.pdf#page=12>) · printed Section A · [Solution A030](../solutions/SOLUTIONS.html#a030)

**Exact Sec A task:** DNS cache poisoning and three defenses.

Define DNS cache poisoning, explain exploitation and provide three defenses.

**2021–22 · Q6(b) · 12 marks · direct** · [paper p. 17](<../../CSE405-Security_Merged.pdf#page=17>) · printed Section B · [Solution A061](../solutions/SOLUTIONS.html#a061)

**Exact Sec A task:** Three DNS poisoning countermeasures.

Design three mechanisms to prevent or mitigate DNS cache poisoning.

**2019–20 · Q4(a) · 12 marks · direct** · [paper p. 23](<../../CSE405-Security_Merged.pdf#page=23>) · printed Section A · [Solution A098](../solutions/SOLUTIONS.html#a098)

**Exact Sec A task:** DNS redirection as a MITM precursor.

Explain with a diagram how DNS spoofing can launch MITM.

**2018–19 · Q4(a) · 10 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · printed Section A · [Solution A122](../solutions/SOLUTIONS.html#a122)

**Exact Sec A task:** Random-subdomain cache-poisoning advantage.

Why use subdomain DNS cache poisoning, and why can it succeed more readily than simple poisoning?

**2018–19 · Q4(b) · 8 printed marks · partial** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · printed Section A · [Solution A123](../solutions/SOLUTIONS.html#a123)

**Exact Sec A task:** DNS redirection in a pharming-versus-phishing comparison.

Explain the DNS-redirection (pharming) side of the printed comparison, with an example.

**Section boundary:** Covers the DNS/pharming component of the printed comparison. The phishing topic is assigned to Sec B. The printed 8 marks are for the complete comparison, not this component alone.

**Coverage / reading note:** Only the Sec A DNS/pharming component is developed here; the standalone phishing topic remains in Sec B.

## Firewalls, Tunneling and IDS

[Ch06-2-FW-Tunneling-IDS-REDUCED.pdf](<../slides/Ch06-2-FW-Tunneling-IDS-REDUCED.pdf>)

<a id="firewall"></a>
### Firewall state, evasion and defense limits — 5 questions

**Study:** deck PDF pp. 3–11; handwritten-note PDF pp. 71.

**2023–24 · Q3(a) · 10 printed marks · direct** · [paper p. 4](<../../CSE405-Security_Merged.pdf#page=4>) · printed Section A · [Solution A007](../solutions/SOLUTIONS.html#a007)

**Exact Sec A task:** Can NIDS/firewall plus HTTPS always stop the network attacks?.

An HTTPS-only server farm has a NIDS and firewall processing incoming requests. With an on-path attacker, assess the Sec A cases: RST injection, SYN flooding, DNS spoofing and DDoS.

**Section boundary:** Covers the four network-defense cases. The reflected-XSS case in the original five-part question belongs to Sec B and is excluded. The 10 printed marks cover all five cases; no per-case allocation is supplied.

**2023–24 · Q4(b) · 10 marks · partial** · [paper p. 5](<../../CSE405-Security_Merged.pdf#page=5>) · printed Section A · [Solution A011](../solutions/SOLUTIONS.html#a011)

**Exact Sec A task:** TCP segmentation, reassembly and limits of a guaranteed evasion.

A smart stateful firewall blocks bytes spelling admin and allows everything else. Mallory splits the word into five packets sent out of order. Will that evade the rule? If not, propose a guaranteed strategy.

**Coverage / reading note:** The deck distinguishes filter types; stream normalization and the impossibility of an unconditional guarantee are extensions.

**2022–23 · Q4(c) · 7 marks · direct** · [paper p. 12](<../../CSE405-Security_Merged.pdf#page=12>) · printed Section A · [Solution A032](../solutions/SOLUTIONS.html#a032)

**Exact Sec A task:** Stateful versus stateless filtering.

Compare stateful and stateless firewalls.

**2021–22 · Q8(c) · 11 marks · partial** · [paper p. 17](<../../CSE405-Security_Merged.pdf#page=17>) · printed Section B · [Solution A068](../solutions/SOLUTIONS.html#a068)

**Exact Sec A task:** Address-book allowlist as a spam policy.

Alice rejects all email except senders in her address book. Is this an effective spam defense?

**Coverage / reading note:** Applies allowlist policy and sender-identity validation; email-specific authentication is supplementary.

**2020–21 · Q4(b) · 12 marks · direct** · [paper p. 19](<../../CSE405-Security_Merged.pdf#page=19>) · printed Section A · [Solution A079](../solutions/SOLUTIONS.html#a079)

**Exact Sec A task:** Value and defense of an internal malware agent.

Explain why an attacker installs an agent inside a corporate network, delivery methods and prevention; assess whether a firewall can help.

<a id="honey"></a>
### Honeypot topology, monitoring and overhead — 5 questions

**Study:** deck PDF pp. 33–34; handwritten-note PDF pp. 28, 52.

**2022–23 · Q4(b) · 10 marks · direct** · [paper p. 12](<../../CSE405-Security_Merged.pdf#page=12>) · printed Section A · [Solution A031](../solutions/SOLUTIONS.html#a031)

**Exact Sec A task:** Honeypot placement, value and resource cost.

Explain with topology why an organization needs a honeypot and estimate its overhead.

**2021–22 · Q5(c) · 11 marks · direct** · [paper p. 16](<../../CSE405-Security_Merged.pdf#page=16>) · printed Section B · [Solution A059](../solutions/SOLUTIONS.html#a059)

**Exact Sec A task:** Disrupting C&C through coordinated investigation.

Formulate a process to take down a botnet command-and-control server.

**2021–22 · Q6(c) · 11 marks · direct** · [paper p. 17](<../../CSE405-Security_Merged.pdf#page=17>) · printed Section B · [Solution A062](../solutions/SOLUTIONS.html#a062)

**Exact Sec A task:** Honeypot topology and effect on normal operation.

Explain the need for a honeypot with topology and whether it hampers normal operation.

**2019–20 · Q5(c) · 7 marks · direct** · [paper p. 24](<../../CSE405-Security_Merged.pdf#page=24>) · printed Section B · [Solution A103](../solutions/SOLUTIONS.html#a103)

**Exact Sec A task:** Why a decoy helps intrusion detection.

Explain why a honeypot is an effective IDS tool.

**2018–19 · Q4(d) · 8 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · printed Section A · [Solution A125](../solutions/SOLUTIONS.html#a125)

**Exact Sec A task:** Honeypot detection, evidence and diversion.

Explain honeypot use cases with a diagram.

<a id="ids"></a>
### Intrusion detection, base rates and audit data — 5 questions

**Study:** deck PDF pp. 23–26; handwritten-note PDF pp. 23–24 (anomaly detection background).

**2020–21 · Q4(c) · 11 marks · partial** · [paper p. 19](<../../CSE405-Security_Merged.pdf#page=19>) · printed Section A · [Solution A080](../solutions/SOLUTIONS.html#a080)

**Exact Sec A task:** Base-rate fallacy with a numerical example.

Define the base-rate fallacy, give an example and explain its effect on daily incident handling.

**Coverage / reading note:** The deck teaches the four alarm outcomes; Bayes/base-rate calculation is an extension.

**2019–20 · Q2(c) · 11 marks · partial** · [paper p. 22](<../../CSE405-Security_Merged.pdf#page=22>) · printed Section A · [Solution A094](../solutions/SOLUTIONS.html#a094)

**Exact Sec A task:** Verify a reported DoS source and respond with evidence.

A hall administrator says your shared network segment is sending DoS traffic. You deny involvement but are unsure about your roommate. How do you verify and respond?

**Coverage / reading note:** Uses IDS/network logs and OS event logging; incident-handling workflow extends the slides.

**2019–20 · Q5(a) · 14 marks · partial** · [paper p. 24](<../../CSE405-Security_Merged.pdf#page=24>) · printed Section B · [Solution A101](../solutions/SOLUTIONS.html#a101)

**Exact Sec A task:** PIDS, alarm outcomes and base-rate interpretation.

Define protocol-based IDS, list alarm outcomes and explain base-rate fallacy.

**Coverage / reading note:** IDS and the confusion matrix are explicit; PIDS specialization and Bayesian analysis are supplementary.

**2019–20 · Q5(b) · 14 marks · partial** · [paper p. 24](<../../CSE405-Security_Merged.pdf#page=24>) · printed Section B · [Solution A102](../solutions/SOLUTIONS.html#a102)

**Exact Sec A task:** Audit-record fields and statistical intrusion detection.

List useful audit-record fields, explain statistical IDS and identify a weakness.

**Coverage / reading note:** Event logging and IDS sensors are taught; statistical-model design is an extension.

**2018–19 · Q4(c) · 9 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · printed Section A · [Solution A124](../solutions/SOLUTIONS.html#a124)

**Exact Sec A task:** Rule-based ARP-spoofing detection.

Give rules a rule-based IDS can use to detect ARP spoofing.

<a id="recon"></a>
### Reconnaissance, fingerprinting and vulnerability assessment — 3 questions

**Study:** deck PDF pp. 27–32; handwritten-note PDF pp. 27–28.

**2022–23 · Q2(c) · 11 marks · direct** · [paper p. 11](<../../CSE405-Security_Merged.pdf#page=11>) · printed Section A · [Solution A026](../solutions/SOLUTIONS.html#a026)

**Exact Sec A task:** Fingerprint/version/CVE assessment workflow.

Formulate the steps for finding and exploiting a target vulnerability by scanning OS/application versions.

**2021–22 · Q8(b) · 12 marks · direct** · [paper p. 17](<../../CSE405-Security_Merged.pdf#page=17>) · printed Section B · [Solution A067](../solutions/SOLUTIONS.html#a067)

**Exact Sec A task:** OS fingerprinting to validated vulnerability finding.

Formulate the steps for exploiting a target after scanning its OS version.

**2020–21 · Q3(b) · 12 marks · direct** · [paper p. 18](<../../CSE405-Security_Merged.pdf#page=18>) · printed Section A · [Solution A076](../solutions/SOLUTIONS.html#a076)

**Exact Sec A task:** Web-server assessment and validation workflow.

Give a stepwise approach and tools to find and exploit popular web-server vulnerabilities.

<a id="vpn"></a>
### VPN and IPsec AH/ESP encapsulation — 2 questions

**Study:** deck PDF pp. 12–22; handwritten-note PDF pp. 71 (brief).

**2021–22 · Q5(b) · 12 marks · direct** · [paper p. 16](<../../CSE405-Security_Merged.pdf#page=16>) · printed Section B · [Solution A058](../solutions/SOLUTIONS.html#a058)

**Exact Sec A task:** AH versus ESP and transport/tunnel layouts.

Compare IPsec AH and ESP with their encapsulations.

**2018–19 · Q1(b) · 9 marks · direct** · [paper p. 26](<../../CSE405-Security_Merged.pdf#page=26>) · printed Section A · [Solution A111](../solutions/SOLUTIONS.html#a111)

**Exact Sec A task:** Compare IPsec ESP and AH formats.

Contrast IPsec AH and ESP, including header encapsulations.

## Extensions needed for Sec A practice

- **System security:** Format-string reads/writes and return-to-libc need more detail than the eight-page overflow deck; the worked answers state the ABI/layout assumptions.
- **Physical security:** Master-wafer counting/design extends the basic pin-tumbler slides.
- **Detection and response:** Bayesian base rates, statistical IDS and forensic acquisition/custody extend the source overview and are explained in the corresponding Sec A answers.

## Study sequence

Use the rankings together with marks and task type. Practice TCP/DNS and LAN message diagrams, then malware distinctions and IDS probability. Rehearse stack, lock and permission calculations separately. An optional three-mark short note is not the same study workload as a twenty-mark protocol analysis.
