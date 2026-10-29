# Sec A syllabus

**9 in-scope decks (315 physical PDF pages), with selected topics from the 80-page handwritten notebook.**

Sec A covers foundations, physical authentication, operating systems, filesystem access, memory attacks, malware and network/DNS/IDS defenses. The source files also contain older material assigned to Sec B; file placement does not add that material to Sec A.

Cryptographic algorithms, number-theory exercises, password-guessing/recovery question sets and browser/application attack chapters are excluded from this syllabus and its frequency/solution guides. OS account/salt handling, DNSSEC, IPsec and network identity checks remain where they are part of Sec A system/network security.

Page numbers below are physical PDF pages, beginning at 1; several PDFs contain two printed slides per page. The handwritten notebook was reviewed visually; its text extraction is empty. The Buffer Overflow PDF has corrupt glyph extraction and was checked as rendered pages.

## In-scope slide decks

## Introduction

[Ch01-Introduction.pdf](<../slides/Ch01-Introduction.pdf>) · 30 PDF pages.

| PDF pages | Sec A topics |
|---|---|
| 1–10 | Security relative to properties and attacker capabilities; CIA; authenticity, anonymity, assurance; attacks and countermeasures |
| 11–16 | Ten security principles: economy, defaults, mediation, open design, separation, least privilege/common mechanism, usability, work factor, compromise recording |
| 17–19 | Access matrices, ACLs, capabilities and RBAC |
| 30–30 | Human factors and social-engineering context for security-principle scenarios |

**Excluded range:** 20–29: cryptographic overview and password-guessing calculations are assigned to Sec B.

## Physical Security

[Ch02-Physical-Security.pdf](<../slides/Ch02-Physical-Security.pdf>) · 32 PDF pages.

| PDF pages | Sec A topics |
|---|---|
| 1–8 | Physical threat models; Yale pin-tumbler and tubular locks; shear line, correct/incorrect keys |
| 9–22 | Authentication factors; barcodes/QR; magnetic stripes and cloning; smart cards; SIM/IMSI; GSM challenge–response; RFID applications |
| 23–27 | Biometric requirements, enrollment/matching, candidates, permanence and privacy |
| 28–32 | Eavesdropping, electromagnetic/acoustic emanations, Faraday shielding and hardware keyloggers |

## Operating Systems Security

[Ch03-OS-Security.pdf](<../slides/Ch03-OS-Security.pdf>) · 37 PDF pages.

| PDF pages | Sec A topics |
|---|---|
| 1–18 | OS/kernel, scheduling, I/O, APIs/system calls, processes/PIDs, real/effective privileges, filesystem permissions |
| 19–26 | Text/data/BSS/heap/stack; virtual memory, paging, page faults and virtual machines |
| 27–33 | Boot trust, live-media attacks, BIOS passwords, hibernation and event logging |
| 34–37 | Password-file dictionary attacks and per-user salts |

## Buffer Overflow

[Ch03-BufferOverflow.pdf](<../slides/Ch03-BufferOverflow.pdf>) · 8 PDF pages.

| PDF pages | Sec A topics |
|---|---|
| 1–3 | Unsafe C memory access, array bounds, process memory and buffer overflow |
| 4–7 | Stack/heap attacks, unsafe strcpy/strncpy, return-address smashing, shell command substitution and native shellcode |
| 8–8 | Memory-safety/privilege mitigation and explicit random-canary detection; glyph extraction is corrupt, so consult the rendered PDF |

## Filesystem Security

[Ch03-FilesystemSecurity.pdf](<../slides/Ch03-FilesystemSecurity.pdf>) · 28 PDF pages.

| PDF pages | Sec A topics |
|---|---|
| 1–4 | DAC; open/closed policies; negative authorization and deny priority; Linux/Windows access decisions |
| 5–13 | Hard/symbolic links; Unix owner/group/other; file versus directory rwx; setuid/setgid/sticky; root/su/sudo; chmod/chown/chgrp and octal notation |
| 14–19 | Minimal/extended POSIX ACLs, mask, effective rights, getfacl/setfacl and default inheritance |
| 20–24 | NTFS permissions, ordered ACE evaluation, explicit/inherited rights, move/copy behavior |
| 25–28 | Permission-management tools and TrACE/treemap visualization |

## Malware

[Ch04-Malware.pdf](<../slides/Ch04-Malware.pdf>) · 67 PDF pages.

| PDF pages | Sec A topics |
|---|---|
| 1–10 | Taxonomy, insider attacks, debugging/malicious backdoors, logic bombs and defenses |
| 11–21 | Virus lifecycle, code injection, macro/stealth/P2P propagation, browser hijacking and drive-by downloads |
| 22–30 | Encrypted/polymorphic/metamorphic viruses, emulation, mutation, obfuscation and anti-debugging |
| 31–39 | Worm versus virus; Morris and other case studies; scanning/topological/flash strategies; epidemic SI model; signature limitations |
| 40–45 | Botnets, C&C, payloads, honeypot monitoring and P2P resilience |
| 46–54 | Rootkit cloaking; user/kernel API filtering, DKOM, cross-view detection and trusted recovery |
| 55–60 | Trojans, malware economics, adware/spyware revenue and data flow |
| 61–67 | Signatures, integrity baselines, allow/deny lists, heuristic/static/dynamic analysis and quarantine |

## Network Security

[Ch05-NetworkSecurity.pdf](<../slides/Ch05-NetworkSecurity.pdf>) · 36 PDF pages.

| PDF pages | Sec A topics |
|---|---|
| 1–4 | Security products and Wireshark packet analysis |
| 5–12 | MAC/IP/ARP, cache poisoning, two-way MITM and detection/DAI |
| 13–15 | Switch CAM learning, MAC flooding and port security |
| 16–19 | DHCP configuration, starvation, rogue offers and snooping/rate limits |
| 20–23 | TCP sequence/acknowledgment state, hijacking and coordinated source spoofing |
| 24–29 | DoS/DDoS, botnet floods, Smurf reflection and mitigation |
| 30–34 | SYN backlog attacks, SYN cookies, encoding and historical limitations |
| 35–36 | IP traceback, packet logging and privacy/storage challenges |

## DNS Security

[Ch06-1-NetworkDNS.pdf](<../slides/Ch06-1-NetworkDNS.pdf>) · 43 PDF pages.

| PDF pages | Sec A topics |
|---|---|
| 1–16 | Distributed hierarchy, roots/TLD/authoritative/local resolvers, zones, RR types and DNS messages |
| 17–26 | Recursive/iterative resolution, delegation, replication/dynamic resolution and TTL caching |
| 27–36 | Pharming, unauthenticated replies, transaction IDs, birthday/cache poisoning, subdomain races, source-port randomization and restricted recursion |
| 37–38 | Cybersquatting and typosquatting |
| 39–43 | DNSSEC signatures, RRSIG/DNSKEY, trust anchors and deployment considerations |

## Firewalls, Tunneling and IDS

[Ch06-2-FW-Tunneling-IDS-REDUCED.pdf](<../slides/Ch06-2-FW-Tunneling-IDS-REDUCED.pdf>) · 34 PDF pages.

| PDF pages | Sec A topics |
|---|---|
| 1–11 | Firewall policies and accept/drop/reject; allow/deny lists; stateless, stateful and application filters |
| 12–22 | VPN/tunneling, remote/site-to-site, IPsec AH/ESP, transport/tunnel encapsulation |
| 23–26 | IDS/IPS, sensors/manager and TP/FP/FN/TN |
| 27–32 | Port scanning, TCP/SYN, horizontal/vertical scans, Nmap/version/CVE workflow |
| 33–34 | Honeypot detection, evidence collection and diversion |

## Handwritten notes: Sec A reading map

[CSE-405-Till-Mid.pdf](<../notes/CSE-405-Till-Mid.pdf>)

| PDF pages | Sec A material |
|---|---|
| 1–9 | Adversarial reasoning, threat models, human factors, malware/ransomware case discussions |
| 10–16 | CIA/AAA, threats, ten principles and access-control models |
| 19–23 | Locks, cards/QR/SIM/GSM/RFID, biometrics and physical emanations |
| 24–30 | Memory layout, unsafe C, stack overflow, assessment tools, privileges and canary sketch |
| 31–36 | OS concepts, real/effective identity, boot/live media, hibernation, logging and OS password-file/salt handling |
| 37–40 | ACLs, file/directory permissions, setuid/setgid/sticky, chmod and identity commands |
| 41–49 | Insiders/backdoors/logic bombs, viruses, encryption/mutation, anti-debugging and detection |
| 50–57 | Worms/SI model, botnets/honeypots, rootkits/hooking, Trojans, malware economics and countermeasures |
| 58–65 | ARP, switch tables, MAC flooding, DHCP starvation/spoofing and defenses |
| 66–71 | TCP hijacking, coordinated spoofing, DoS/Smurf/SYN cookies, traceback and brief tunnel/VPN notes |
| 72–80 | DNS hierarchy/messages/cache poisoning, source-port entropy, DNSSEC and squatting |

The crypto recap and standalone guessing calculations on notebook pp. 17–18 are excluded. Any such examples on otherwise included pages are background, not additional Sec A exam topics. The notebook ends at DNS; use the firewall/IDS deck for its later material.

## Preserved files outside this study scope

The following PDFs remain untouched as supplied references. They do not appear as Sec A teaching chapters, ranked topics or standalone worked solutions.

- [Crypto-Hash-DigSign.pdf](<../slides/Crypto-Hash-DigSign.pdf>) — Sec B topic coverage; preserved source, excluded from the Sec A study scope.
- [WebDB-security.pdf](<../slides/WebDB-security.pdf>) — Sec B topic coverage; preserved source, excluded from the Sec A study scope.

## Source cautions and extensions

- OS salts are normally public and unique. They prevent shared precomputation and cross-account reuse; they do not add secret entropy to a known-salt account.
- DNSSEC needs a validated chain to an already trusted key. Protecting one DNS transport hop does not automatically authenticate every recursive lookup.
- Promiscuous packet capture does not force a switch to deliver all VLAN traffic; MAC-table exhaustion and unknown-unicast behavior are conditional.
- Memory offsets depend on ABI/compiler/layout. The old stack exercise stipulates an artificial instruction-size model. Random canaries are explicit on overflow PDF p. 8; format strings and return-to-libc need additional explanation.
- Master-wafer lock design, Bayesian IDS base rates and forensic acquisition/custody extend the source overviews; their answers identify the assumptions.

## Exam preparation

Use [the Sec A frequency report](FINAL_EXAM_TOPIC_ANALYSIS.md) for questions grouped under deck and precise topic. It checks both printed exam sections each year. Foundational details with no standalone mapped question remain part of this reading map—for example GSM/RFID, ACL masks/inheritance, NTFS ACE evaluation, scheduling/VM/boot details, malware quarantine and routine DNS hierarchy exercises.
