# Sec A syllabus from the supplied slides and notes

**11 slide decks, 424 physical PDF pages; one 80-page scanned notebook.** This is a reconstruction of the supplied material, not an official instructor-issued exclusion list.

Page numbers below refer to physical PDF pages, beginning at 1. Several PDFs contain two printed slides per PDF page. The handwritten notebook was reviewed visually; its extracted text is empty. The Buffer Overflow PDF has corrupt text glyphs, so its rendered pages were checked as well.

## Complete slide-deck reading map

## Introduction

[Ch01-Introduction.pdf](<../slides/Ch01-Introduction.pdf>)
 · 30 PDF pages.

| PDF pages | Topics |
|---|---|
| 1–10 | Security relative to properties and attacker capabilities; CIA; authenticity, anonymity, assurance; attacks and countermeasures |
| 11–16 | Ten security principles: economy, defaults, mediation, open design, separation, least privilege/common mechanism, usability, work factor, compromise recording |
| 17–19 | Access matrices, ACLs, capabilities and RBAC |
| 20–26 | Cryptosystem components; Caesar; symmetric/public-key distribution; signatures, hashes, MACs and certificates |
| 27–30 | Password storage, alphabet/length search spaces, brute-force rates and social engineering |

## Physical Security

[Ch02-Physical-Security.pdf](<../slides/Ch02-Physical-Security.pdf>)
 · 32 PDF pages.

| PDF pages | Topics |
|---|---|
| 1–8 | Physical threat models; Yale pin-tumbler and tubular locks; shear line, correct/incorrect keys |
| 9–22 | Authentication factors; barcodes/QR; magnetic stripes and cloning; smart cards; SIM/IMSI; GSM challenge–response; RFID applications |
| 23–27 | Biometric requirements, enrollment/matching, candidates, permanence and privacy |
| 28–32 | Eavesdropping, electromagnetic/acoustic emanations, Faraday shielding and hardware keyloggers |

## Operating Systems Security

[Ch03-OS-Security.pdf](<../slides/Ch03-OS-Security.pdf>)
 · 37 PDF pages.

| PDF pages | Topics |
|---|---|
| 1–18 | OS/kernel, scheduling, I/O, APIs/system calls, processes/PIDs, real/effective privileges, filesystem permissions |
| 19–26 | Text/data/BSS/heap/stack; virtual memory, paging, page faults and virtual machines |
| 27–33 | Boot trust, live-media attacks, BIOS passwords, hibernation and event logging |
| 34–37 | Password-file dictionary attacks and per-user salts |

## Buffer Overflow

[Ch03-BufferOverflow.pdf](<../slides/Ch03-BufferOverflow.pdf>)
 · 8 PDF pages.

| PDF pages | Topics |
|---|---|
| 1–3 | Unsafe C memory access, array bounds, process memory and buffer overflow |
| 4–7 | Stack/heap attacks, unsafe strcpy/strncpy, return-address smashing, shell command substitution and native shellcode |
| 8–8 | Memory-safety/privilege mitigation and explicit random-canary detection; glyph extraction is corrupt, so consult the rendered PDF |

## Filesystem Security

[Ch03-FilesystemSecurity.pdf](<../slides/Ch03-FilesystemSecurity.pdf>)
 · 28 PDF pages.

| PDF pages | Topics |
|---|---|
| 1–4 | DAC; open/closed policies; negative authorization and deny priority; Linux/Windows access decisions |
| 5–13 | Hard/symbolic links; Unix owner/group/other; file versus directory rwx; setuid/setgid/sticky; root/su/sudo; chmod/chown/chgrp and octal notation |
| 14–19 | Minimal/extended POSIX ACLs, mask, effective rights, getfacl/setfacl and default inheritance |
| 20–24 | NTFS permissions, ordered ACE evaluation, explicit/inherited rights, move/copy behavior |
| 25–28 | Permission-management tools and TrACE/treemap visualization |

## Malware

[Ch04-Malware.pdf](<../slides/Ch04-Malware.pdf>)
 · 67 PDF pages.

| PDF pages | Topics |
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

[Ch05-NetworkSecurity.pdf](<../slides/Ch05-NetworkSecurity.pdf>)
 · 36 PDF pages.

| PDF pages | Topics |
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

[Ch06-1-NetworkDNS.pdf](<../slides/Ch06-1-NetworkDNS.pdf>)
 · 43 PDF pages.

| PDF pages | Topics |
|---|---|
| 1–16 | Distributed hierarchy, roots/TLD/authoritative/local resolvers, zones, RR types and DNS messages |
| 17–26 | Recursive/iterative resolution, delegation, replication/dynamic resolution and TTL caching |
| 27–36 | Pharming, unauthenticated replies, transaction IDs, birthday/cache poisoning, subdomain races, source-port randomization and restricted recursion |
| 37–38 | Cybersquatting and typosquatting |
| 39–43 | DNSSEC signatures, RRSIG/DNSKEY, trust anchors and deployment considerations |

## Firewalls, Tunneling and IDS

[Ch06-2-FW-Tunneling-IDS-REDUCED.pdf](<../slides/Ch06-2-FW-Tunneling-IDS-REDUCED.pdf>)
 · 34 PDF pages.

| PDF pages | Topics |
|---|---|
| 1–11 | Firewall policies and accept/drop/reject; allow/deny lists; stateless, stateful and application filters |
| 12–22 | VPN/tunneling, remote/site-to-site, IPsec AH/ESP, transport/tunnel encapsulation |
| 23–26 | IDS/IPS, sensors/manager and TP/FP/FN/TN |
| 27–32 | Port scanning, TCP/SYN, horizontal/vertical scans, Nmap/version/CVE workflow |
| 33–34 | Honeypot detection, evidence collection and diversion |

## Cryptography, Hashes and Digital Signatures

[Crypto-Hash-DigSign.pdf](<../slides/Crypto-Hash-DigSign.pdf>)
 · 69 PDF pages.

| PDF pages | Topics |
|---|---|
| 1–9 | Symmetric encryption, substitution, product ciphers and P/S boxes |
| 10–17 | DES Feistel rounds and 3DES EDE |
| 18–24 | AES state, key expansion and round operations; algorithm comparison |
| 25–28 | Long messages and CBC encryption/decryption, IV and error propagation |
| 29–40 | Division/congruences, cancellation/inverses, primes/factorization, gcd, Fermat and Euler |
| 41–47 | Public-key model, RSA generation, encryption/decryption and numerical example |
| 48–55 | Integrity, cryptographic hashes, MACs and MD5/SHA history |
| 56–60 | DH exchange and MITM |
| 61–69 | Signatures, hash-then-sign, public-key trust, CA and certificate contents |

## Web and Database Security

[WebDB-security.pdf](<../slides/WebDB-security.pdf>)
 · 40 PDF pages.

| PDF pages | Topics |
|---|---|
| 1–10 | Client/server/database architecture, URL/DNS/TCP/HTTP, plaintext risks, HTTPS and certificates |
| 11–13 | Browser attacks, phishing and input-versus-output injection distinction |
| 14–25 | Dynamic SQL, login bypass, destructive/stacked query examples and prevention |
| 26–32 | XSS origins/consequences, stored/reflected attacks and examples |
| 33–38 | CSRF, cookie-authenticated actions, GET/POST examples and mitigation |
| 39–40 | WAF strengths/limitations and web-vulnerability recap |

## Handwritten notes: page-by-page range map

[CSE-405-Till-Mid.pdf](<../notes/CSE-405-Till-Mid.pdf>)

| PDF pages | Material |
|---|---|
| 1–9 | Course introduction, adversarial reasoning, threat models, social engineering, malware/ransomware case discussions |
| 10–18 | CIA/AAA, attacks, ten principles, access-control models, cryptographic overview and password calculations |
| 19–23 | Locks, cards/QR/SIM/GSM/RFID, biometrics and physical emanations |
| 24–30 | Memory layout, unsafe C, stack overflow, assessment tools, privileges and canary sketch |
| 31–36 | OS concepts, real/effective identity, boot/live media, hibernation, logging, password attacks and salts |
| 37–40 | ACLs, file/directory permissions, setuid/setgid/sticky, chmod and identity commands |
| 41–49 | Insiders/backdoors/logic bombs, viruses, encryption/mutation, anti-debugging and detection |
| 50–57 | Worms/SI model, botnets/honeypots, rootkits/hooking, Trojans, malware economics and countermeasures |
| 58–65 | ARP, switch tables, MAC flooding, DHCP starvation/spoofing and defenses |
| 66–71 | TCP hijacking, coordinated spoofing, DoS/Smurf/SYN cookies, traceback and brief tunnel/VPN notes |
| 72–80 | DNS hierarchy/messages/cache poisoning, repeated queries, source-port entropy, DNSSEC and squatting |

The notebook stops at DNS and is titled “Till Mid.” It does not supply a complete handwritten counterpart for the crypto, web or firewall/IDS decks. Do not mistake a missing handwritten chapter for a syllabus exclusion.

## Teaching-source cautions and extensions

- **Salts:** the OS slides discuss hiding/encrypting a salt and multiplying a guessing space. Ordinary password salts are public and unique; they prevent shared precomputation/cross-account reuse. They do not add secret entropy to a single known-salt password. A separate secret pepper has a different threat model.
- **Hashes and MACs:** MD5/SHA-1 appear as historical examples. A bare digest is not a MAC, and the intro shorthand H(K||M) is not a universally safe MAC construction. Use the explicit HMAC reasoning in relevant answers.
- **Hash security properties:** collision resistance and preimage resistance are different properties; the equivalence shorthand on Crypto PDF p. 49 is incorrect. Three-key 3DES has 168 key bits, but a generic meet-in-the-middle upper bound is about 112 bits, so do not copy the nominal key length as effective strength.
- **Signatures:** “encrypt with the private key” describes a textbook RSA analogy, not every signature scheme or a safe raw-RSA implementation.
- **Web protocols:** the deck simplifies HTTPS as server-only authentication; TLS can also authenticate clients when configured. Input blacklists and user browsing habits are not substitutes for parameter binding, output encoding and deliberate CSRF defenses.
- **DNSSEC:** authentication requires a chain to an already trusted key, not simply accepting the DNSKEY that accompanies a reply. DNS-over-TLS protects its particular transport hop; it does not automatically protect all recursive lookups. Historical deployment statements are course history.
- **Packet capture and switching:** promiscuous mode does not force a switch to deliver all VLAN traffic; unknown-unicast flooding is conditional and remains scoped by switching/VLAN behavior.
- **Memory attacks:** exact offsets, local ordering, ABI and compiler protections matter. The 2018–19 stack question explicitly uses an artificial layout/instruction-size model. The deck explicitly includes a random canary on PDF p. 8. Format strings, return-to-libc and detailed ASLR/CFI mechanisms are related extensions.
- **Locks:** basic pin-tumbler operation is explicit; master-wafer combinatorics/geometric design in the old paper extends those slides.
- **IDS:** the four alarm outcomes are explicit. Base-rate calculations, PIDS specialization, statistical audit models and forensic custody need supplementary explanation supplied in the solutions.
- **Cryptographic overlap:** Sec A teaches DES/AES, CBC, modular arithmetic, RSA, DH, hashes/MACs/signatures and CA trust. Sec B has more extensive classical ciphers, PRNGs, ElGamal, modes, cookie policy and web-attack treatments. Questions are mapped by content in both sections, not by their printed Section A/B label.

## Study material versus exam frequency

Use [the question analysis](FINAL_EXAM_TOPIC_ANALYSIS.md) for the ranked evidence and all individual questions. A topic with no standalone question is still part of this file-derived syllabus. Core unqueried details include GSM challenge–response, QR/barcode comparison, RFID operation, extended ACL masks/default inheritance, NTFS ACE ordering/move-copy rules, most OS scheduling/VM/boot details, malware-analysis/quarantine mechanisms, routine DNS resource-record/hierarchy exercises and the VPN deployment variants.
