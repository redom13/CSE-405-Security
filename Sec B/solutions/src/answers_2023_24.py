"""Worked answers in Markdown with canonical LaTeX math."""
answers = {}
answers['2023–24|5(a)'] = r'''
**Answer all five for revision; the exam asks for any three.**

**(i) Cryptographic CIA.** Confidentiality means an unauthorized observer learns no protected message content. Integrity means unauthorized changes are detected. Authenticity establishes the claimed source. Encryption addresses confidentiality; MACs/signatures address integrity and authenticity. In this lecture, A means **authenticity**. In the general information-security triad it means **availability**, the ability of legitimate users to obtain service; mention the convention if necessary.

**(ii) Confusion and diffusion.** Confusion makes the relationship between key and ciphertext complex, typically through nonlinear substitution. Diffusion spreads each plaintext symbol’s influence across many ciphertext symbols, typically through permutations and linear mixing over repeated rounds. AES SubBytes contributes nonlinearity; ShiftRows/MixColumns spread influence. A cipher with only linear operations can remain easy to solve despite visibly mixing symbols.

**(iii) MAC.** Alice and Bob share a secret K. Alice sends M and T=MAC(K,M). Bob recomputes the tag and accepts only on a match. Without K, an attacker should not produce a valid tag for a new message, even after seeing tags on chosen messages. A MAC provides no encryption; both key holders can create tags, so it does not establish third-party non-repudiation. Include a sequence number in the authenticated data to address replay.

**(iv) Homograph phishing.** A deceptive domain uses visually similar characters, such as a Cyrillic letter resembling a Latin letter, to imitate a trusted domain. A victim sees a familiar-looking address and submits credentials to the attacker. Similar appearance does not imply the same DNS name or origin. Password managers tied to exact origins and phishing-resistant authenticators help; a padlock alone only authenticates the domain actually visited.

**(v) Clickjacking.** An attacker positions a transparent target-site iframe so a sensitive button lies beneath an enticing visible button. The user intends the visible action but clicks the hidden target. No reading of the cross-origin frame is required. The target can restrict framing with CSP `frame-ancestors` or X-Frame-Options.

![Clickjacking layers](assets/clickjacking.svg)

**Exam tip.** For each 5-mark concept give a definition, mechanism/example and limitation or defense. Do not use “MAC encrypts the message” or confuse cryptographic authenticity with service availability.
'''
answers['2023–24|5(b)'] = r'''
Let E and D be inverse block-cipher operations under K; all XOR operands are one block. **The second IV is XORed after the first encryption**, and the resulting C1 feeds the second block. Reading that wire correctly determines the answer.

**(i) Derive encryption and decryption.**

$$
\begin{aligned}
C_1&=E_K(P_1\oplus IV_1)\oplus IV_2, & P_1&=D_K(C_1\oplus IV_2)\oplus IV_1,\\
C_2&=E_K(P_2\oplus C_1), & P_2&=D_K(C_2)\oplus C_1,\\
C_3&=E_K(P_3\oplus C_2), & P_3&=D_K(C_3)\oplus C_2.
\end{aligned}
$$

For the first equation, XOR IV2 to both sides, apply D, then XOR IV1. For later blocks, apply D and XOR the preceding ciphertext.

![Custom-mode decryption](assets/custom-decryption.svg)

Encryption is sequential because C2 needs C1 and C3 needs C2. Decryption is parallelizable: every D input and every subsequent XOR operand comes from the already received ciphertext/IVs. There is no need to wait for the previous plaintext.

**(ii) Independently choose both recovered plaintext blocks.** Define:

$$
\begin{aligned}
\Delta_1&=P_1\oplus P_1^*, &\Delta_2&=P_2\oplus P_2^*,\\
IV_1'&=IV_1\oplus\Delta_1, & C_1'&=C_1\oplus\Delta_2,\\
IV_2'&=IV_2\oplus\Delta_2, & C_2'&=C_2.
\end{aligned}
$$

For block 1, $C_1'\oplus IV_2'=C_1\oplus IV_2$, so the unknown D output is unchanged. Thus:

$$
\begin{aligned}P_1'&=D_K(C_1\oplus IV_2)\oplus IV_1\oplus\Delta_1\\&=P_1\oplus\Delta_1=P_1^*.\end{aligned}
$$

For block 2:

$$
\begin{aligned}P_2'&=D_K(C_2)\oplus C_1'\\&=P_2\oplus\Delta_2=P_2^*.\end{aligned}
$$

The attacker needs the old plaintext blocks and desired targets, not K. Changing C1 alone would unpredictably corrupt block 1; changing IV2 by the same delta cancels that corruption. Authenticating the IVs and all ciphertext blocks before decryption prevents this modification attack.

**Exam tip.** First identify an expression you can keep constant through cancellation. Here it is `C1 XOR IV2`. State that the attack assumes the transmitted IVs/ciphertext are not authenticated.
'''
answers['2023–24|6(a)'] = r'''
**Attack.** Alice sends A=$g^{a}$ and Bob sends B=$g^{b}$ modulo p. Mallory chooses exponents x,y, replaces Alice’s contribution to Bob with X=$g^{x}$, and replaces Bob’s contribution to Alice with Y=$g^{y}$.

$$
\begin{aligned}K_A&=Y^a=g^{ay}=A^y,\\K_B&=X^b=g^{bx}=B^x.\end{aligned}
$$

Alice and Bob have keys with Mallory, not with each other. Mallory decrypts under KA, reads/changes the plaintext, encrypts under KB and forwards it. Passive interception alone does not permit this; contribution substitution does.

![DH MITM timing diagram](assets/dh-mitm.svg)

**Defense under the stated “no trusted third party” condition.** Alice and Bob can compare authenticated public-key fingerprints or a transcript hash over an independent authenticated channel, such as meeting in person. They can then sign fresh DH contributions using those verified keys. Alternatively, a pre-shared secret can authenticate the transcript. Both parties should bind identities, roles, nonces and both DH shares to authentication.

Simply signing with a public key attached to the same unauthenticated message does not help: Mallory attaches her own key and matching signature. TOFU helps detect later changes only if first contact was clean; it does not guarantee protection during an attacked first exchange. With no pre-existing trust or independent authentication at all, unauthenticated DH cannot establish the peer’s identity.

**Exam tip.** Draw two distinct shared keys. Do not “fix” this question merely by assuming an available CA, which the prompt excludes.
'''
answers['2023–24|6(b)'] = r'''
Using A=0,…,Z=25, B=1, E=4 and P=15. Encryption is C=K1·P+K2 modulo 26. The two observations give:

$$
\begin{aligned}K_1+K_2&\equiv4\pmod{26},\\4K_1+K_2&\equiv15\pmod{26},\\3K_1&\equiv11\pmod{26}.\end{aligned}
$$

Since 3·9=27≡1 mod 26, multiply by 9:

$$
\begin{aligned}K_1&\equiv99\equiv21\pmod{26},\\K_2&\equiv4-21\equiv9\pmod{26}.\end{aligned}
$$

**Answer: K1=21 and K2=9.** Check: 21·1+9=30≡4 (E), and 21·4+9=93≡15 (P). Also gcd(21,26)=1, satisfying key invertibility. Since $21^{-1}$≡5 mod 26, decryption is $P=5(C-9)\pmod{26}$.

**Exam tip.** Subtract the equations before looking for a modular inverse. Division by 3 means multiplication by its modular inverse, not ordinary fractional arithmetic.
'''
answers['2023–24|7(a)'] = r'''
**Public key and encryption.** With p=353, g=3, b=233, r=97:

$$
\begin{aligned}B&=3^{233}\bmod353=248,\\R&=3^{97}\bmod353=40,\\S&=B^{97}\bmod353=160,\\C&=123\cdot160\bmod353=265.\end{aligned}
$$

**Bob’s public key is 248; Alice sends (R,C)=(40,265).** Repeated-squaring residues for g at exponents 1,2,4,8,16,32,64,128 are `3,9,81,207,136,140,185,337`. Thus 97=64+32+1 gives R, and 233=128+64+32+8+1 gives B.

Bob computes $R^{233}\bmod353=160$. The inverse of 160 modulo 353 is 139, because $160\cdot139=22240=63\cdot353+1$. Therefore:

$$
M=265\cdot139\bmod353=123.
$$

**IND-CPA: state the group carefully.** The question uses the whole multiplicative group $\mathbb Z_{353}^{*}$; zero is not a valid message, so the slide’s M0=0 example is unavailable. There is nevertheless a distinguishing attack on the full group. Let $\chi(z)=z^{176}\bmod353$, represented as +1 or −1. Because g=3 is a primitive root, χ(g)=−1. The public R reveals r’s parity through χ(R). Hence the attacker computes $\chi(S)=\chi(B)^r$ using just that parity, then obtains:

$$
\chi(M)=\frac{\chi(C)}{\chi(S)}.
$$

Choose challenge messages M0=1 and M1=3, whose quadratic characters differ. The exposed character identifies the message. **Thus the full-group scheme as stated is not IND-CPA secure.** For the actual numbers χ(B)=−1, χ(R)=−1, χ(S)=−1 and χ(C)=+1, revealing χ(M)=−1. These values follow directly from modular exponentiation. Prime-order-group ElGamal under a suitable DDH assumption has a different security conclusion; do not generalize this failure to every ElGamal construction. Background on quadratic characters: [Stanford’s quadratic-residue notes](https://crypto.stanford.edu/pbc/notes/numbertheory/qr.html).

**Non-malleability: no.** Replace `(R,C)` by $(R,tC\bmod p)$ for known nonzero t. Decryption yields tM mod p. For t=2, `(40,177)` decrypts to 246. The adversary need not recover M to alter it predictably.

**Exam tip.** Separate confidentiality from malleability and distinguish Z*p from a suitable prime-order subgroup. A small example modulus is for arithmetic practice, not practical cryptographic security.
'''
answers['2023–24|7(b)'] = r'''
Choose distinct primes p,q; N=pq; φ(N)=(p−1)(q−1); gcd(e,φ(N))=1; and d=$e^{-1}$ mod φ(N). Therefore $ed=1+t(p-1)(q-1)$ for some integer t. We must prove $M^{ed}$≡M mod N for **every** residue M.

Work modulo p. If p divides M, both sides are 0 modulo p. Otherwise Fermat’s little theorem gives $M^{p-1}$≡1, so:

$$
M^{ed}=M\left(M^{p-1}\right)^{t(q-1)}\equiv M\pmod p.
$$

The identical argument modulo q gives $M^{ed}$≡M mod q, including the case q divides M. Since p and q are coprime, the Chinese remainder theorem implies:

$$
\begin{aligned}M^{ed}&\equiv M\pmod{pq},\\D_d(E_e(M))&=(M^e)^d\bmod N=M.\end{aligned}
$$

**Exam tip.** An Euler-theorem proof that assumes gcd(M,N)=1 is incomplete unless you address non-coprime messages. The two-case Fermat/CRT proof handles them. Correctness does not prove raw RSA is secure: deterministic RSA still fails IND-CPA.
'''
answers['2023–24|7(c)'] = r'''
**Signing and verification, using the lecture’s simplified notation.** Alice’s public key is (NA,eA), private key dA:

$$
\begin{aligned}\operatorname{Sign}(d_A,M)&=s=H(M)^{d_A}\bmod N_A,\\\operatorname{Verify}(e_A,N_A,M,s)&=1\quad\Longleftrightarrow\quad s^{e_A}\bmod N_A=H(M).\end{aligned}
$$

Actual RSA signature encodings are more elaborate; the question is about this mathematical model. Verification uses Alice’s authenticated public key. Encryption to Bob is $C=\operatorname{Enc}_{PK_B}(M)$.

**Can (C,s) be sent securely? Not with general message confidentiality.** Anyone can test a candidate message m by calling `Verify(PKA,m,s)`. For a low-entropy message such as BUY/SELL, an observer tries both and learns M without decrypting C. More formally, in a confidentiality challenge between distinct M0 and M1, an observer verifies the public signature against both candidates. This attack does not require reversing a hash or forging a signature.

With the simplified RSA signature, the observer can also compute $s^{e_A}=H(M)\pmod{N_A}$, supplying a public fingerprint for a dictionary attack. A signature authenticates content; it does not conceal it.

**Repair.** Encrypt the message and its signature together inside a secure, authenticated encryption construction, for example a hybrid envelope carrying `M || Sign(SKA, context || M)`. Bind sender, intended recipient and protocol context. Alternatively, a carefully specified scheme can sign the encrypted envelope; composition requirements must be stated rather than assuming any encryption/signature pair is automatically secure.

![Hash then sign](assets/signature.svg)

**Exam tip.** “Different keys” is not a sufficient justification for confidentiality. The decisive observation is that public verification tests candidate plaintexts.
'''
answers['2023–24|8(a)'] = r'''
Authenticated encryption protects message confidentiality and detects unauthorized ciphertext/message modification.

$$
\begin{aligned}\text{MAC-then-encrypt:}\quad C&=\operatorname{Enc}_{K_e}\!\left(M\parallel\operatorname{MAC}_{K_m}(M)\right),\\\text{Encrypt-then-MAC:}\quad C&=\operatorname{Enc}_{K_e}(M),\\T&=\operatorname{MAC}_{K_m}\!\left(\operatorname{encode}(IV,C,\text{context})\right).\end{aligned}
$$

**Prefer encrypt-then-MAC under the usual secure-primitive and independent-key assumptions.** The receiver checks T before decrypting C and rejects invalid packets uniformly. In MAC-then-encrypt, the receiver must decrypt and often parse padding before authenticating, creating opportunities for padding/error/timing oracles in incorrect implementations.

Authenticate the IV/nonce and relevant metadata as well as the ciphertext; otherwise an unauthenticated IV may permit plaintext changes. Dedicated AEAD schemes provide an integrated interface, with nonce requirements that still must be followed.

**Exam tip.** Show construction and receiver order. Do not claim that every possible MAC-then-encrypt system is automatically broken; the point is the stronger generic composition and easier implementation discipline of encrypt-then-MAC.
'''
answers['2023–24|8(b)'] = r'''
Check domain, path and the Secure flag separately. Cookie 1 covers moodle.com and its subdomains at every path, over HTTPS. Cookie 2 covers **long.moodle.com**, path /test, over either scheme. Cookie 3 covers moodle.com and subdomains under /print, over HTTPS. All three are validly set by long.moodle.com.

| Requested URL | C1 theme | C2 auth | C3 file |
|---|---:|---:|---:|
| (i) http://print.moodle.com/print | 0 | 0 | 0 |
| (ii) http://login.moodle.com/ | 0 | 0 | 0 |
| (iii) http://moodle.com/test | 0 | 0 | 0 |
| (iv) https://moodle.com/print/test | 1 | 0 | 1 |
| (v) https://login.moodle.com/test/print | 1 | 0 | 0 |

For (i)–(iii), Secure blocks C1/C3; none of the five hosts is long.moodle.com or its subdomain, so C2 never matches. In (iv), /print is a matching path prefix. In (v), /print occurs later but is not the path prefix; C3 is absent.

**Exam tip.** `login` and `long` are different labels. Do not treat a substring anywhere in the path as a match. These are the exam’s explicit Domain cookies, not host-only cookies.
'''
answers['2023–24|8(c)'] = r'''
**Yes: the SQL parser receives attacker-controlled syntax.** Enter:

```text
username: alice' -- 
password: anything
```

The trailing space after `--` is intentional for MySQL-style comments. The resulting query is:

```sql
SELECT * FROM users
WHERE username = 'alice' -- ' AND password = 'anything';
```

The commented password predicate is never evaluated, so Alice’s row is returned. This assumes the application treats that returned row as a successful login, as the question’s logic implies.

**Prevention:** parameter binding keeps data separate from SQL syntax:

```text
stmt = prepare("SELECT id, password_hash FROM users WHERE username = ?")
row = execute(stmt, [submitted_username]).one_or_none()
accept only if row exists and password_verify(submitted_password, row.password_hash)
```

The payload becomes a literal username string instead of changing the query. For a direct repair of the paper’s plaintext-password model, use `WHERE username=? AND password=?` with both parameters bound, but real password verification should use salted password hashes.

**Exam tip.** Write the expanded SQL, not just the input. One correctly formed statement is enough; stacked statements are unnecessary. Parameterization, not merely limiting statement count, fixes the syntax boundary. [OWASP’s parameterization guidance](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html).
'''
answers['2023–24|8(d)'] = r'''
XSS occurs when attacker-controlled content is interpreted as active script in a trusted website’s page. The script executes with that page’s origin and can modify its DOM, read accessible data and issue authenticated requests.

| Property | Stored XSS | Reflected XSS |
|---|---|---|
| Payload location | Persisted in comments/profile/database | Carried in a request, often a URL parameter |
| Trigger | A victim views the contaminated page | Victim follows a crafted link/request |
| Server behavior | Serves stored input as active HTML/script | Echoes request input as active HTML/script |
| Reach | Can affect many later visitors | Usually needs a victim-specific lure/request |

![Stored and reflected XSS](assets/xss.svg)

Example stored path: malicious guest-book entry → database → another visitor’s rendered page. Example reflected path: `/search?q=<script>...</script>` → server echoes q without context-appropriate escaping → browser executes it.

Defend with contextual output encoding; use safe DOM APIs such as textContent for text; sanitize intentionally permitted rich HTML; add CSP as defense in depth. HttpOnly prevents JavaScript from reading that cookie but does not prevent malicious script from sending authenticated requests from the victim page. CSRF tokens alone do not cure same-origin script execution.

**Exam tip.** The distinction is persistence/data flow, not “stored executes at the server.” Both execute in the victim’s browser.
'''
answers['2023–24|1(c)'] = r'''
**Core flaw:** a signature verified with a public key supplied by the same untrusted reply proves possession of that key, not that the sender is CSBot. Mallory generates (PKM,SKM), chooses fake number NM and sends `(NM,PKM,Sign(SKM,NM))`. Verification succeeds although the identity binding is false.

**(i) On-path observer/injector.** Mallory sees the broadcast and immediately injects the forged reply, spoofing any unauthenticated sender fields needed. If ARTBot accepts the first valid response for an outstanding lookup, winning the race poisons the cache. Being on-path does not necessarily give packet-dropping power; explain the race under that capability.

**(ii) MITM able to modify/drop.** Suppress CSBot’s genuine reply and substitute Mallory’s reply. This removes the race and gives reliable poisoning under the stated protocol.

**(iii) Off-path.** Construct the same self-consistent reply blindly and inject it when ARTBot is likely to have an outstanding lookup, possibly inducing such a lookup if the application allows it. Success depends on reachability, acceptance rules and timing. The protocol specifies no unpredictable transaction ID or signed challenge, so it gives no stated cryptographic freshness obstacle. It does not follow that every unsolicited packet will be accepted: identify the lookup-window assumption.

**Defense.** Pre-provision an authentic CSBot key, or validate an identity–key certificate against a pre-trusted CA. Have ARTBot send a fresh unpredictable nonce and require the signed response to cover `CSBot identity || phone number || nonce || protocol context`. Verify the identity, trusted key, signature and outstanding nonce before caching; bound cache lifetime. A nonce alone does not defeat an on-path key-substitution attacker who can see and sign that nonce with their own key.

**Exam tip.** State both missing bindings: identity-to-key and response-to-fresh-request. Adding “a stronger signature algorithm” does not supply either.
'''
answers['2023–24|4(c)'] = r'''
The figure is a **historical, simplified pre-TLS-1.3 handshake**, not a specification of current TLS.

**(i) Why plaintext hellos are acceptable.** The random nonces and offered/selected cipher suites are not secrets. They are included in each endpoint’s handshake transcript, which is authenticated by the Finished verification. If Mallory changes a hello in transit, the endpoints’ transcripts differ, so the keyed Finished checks fail, assuming sound negotiation and cryptography.

In the **authenticated DH case**, the server’s DH share/parameters are signed with the private key corresponding to its validated certificate. Mallory cannot replace them with her own usable shares while impersonating the server. The peers derive their shared secret and verify the transcript. In the **RSA key-transport case**, the client encrypts the premaster secret with the certificate-authenticated server key. Mallory cannot recover that secret or produce the required Finished authentication under derived keys. A certificate sent without chain/name validation provides no such assurance.

An attacker can still drop packets and cause failure. The claim is that plaintext hellos do not by themselves enable undetected session hijacking, not that TLS prevents all interference.

**(ii) Why separate directional keys.** If client and server use the same encryption/MAC keys and equivalent record encodings, an adversary may reflect a client’s valid record back as an apparently valid server record. Matching counters/nonces across directions can also reuse keystream or AEAD inputs under the same key. Separate keys, derived with role labels, isolate client→server and server→client cryptographic domains. Role/domain separation in authenticated encodings is also necessary design context.

**(iii) Remaining vulnerability in the shown application records.** The figure authenticates Mi but omits the record sequence number. An attacker can replay a valid encrypted record or change delivery order without forging its message MAC. Add a monotonically tracked per-direction sequence number to authenticated record data, along with record type/version/length or equivalent context:

$$
T=\operatorname{MAC}_{K_{\mathrm{dir}}}\!\left(\mathrm{seq}\parallel\mathrm{type}\parallel\mathrm{version}\parallel\mathrm{length}\parallel M\right).
$$

The receiver verifies the expected number and rejects replay/out-of-order records according to the protocol’s stream semantics. A number included only outside the MAC is editable and insufficient. The historical TLS record and Finished structures are specified in [RFC 5246, sections 6 and 7.4.9](https://www.rfc-editor.org/rfc/rfc5246).

**Exam tip.** Distinguish later authentication of earlier plaintext handshake messages from encryption of those messages. In part (iii), identify what the **given figure omits**, rather than listing unrelated TLS attacks.
'''
