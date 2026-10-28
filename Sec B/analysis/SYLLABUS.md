# Syllabus derived from the supplied Sec B material

This is a syllabus reconstructed from the files in this repository, not an official instructor-issued syllabus. It includes all eleven lecture decks, the handwritten notes, and the CT 4 revision guide. Read this first, then use [the question-frequency report](FINAL_EXAM_TOPIC_ANALYSIS.md).

PDF page numbers below start at 1 and refer to the physical pages in the named file. Revision sheets and lecture recap slides repeat earlier topics; they do not create additional syllabus units.

## Repository map

```text
CSE405-Security_Merged.pdf                 shared past finals, at repo root
Sec B/
  README.md                               section overview
  slides/                                 Lectures 02–12, in one folder
  notes/                                  handwritten notes and CT4 revision guide
  analysis/                               syllabus, frequency report, question index
  solutions/                              PDF, LaTeX, Markdown, HTML and figures
  scripts/                                reproducible document builders
```

There is no Lecture 1 file. There are **637 lecture pages**, **66 handwritten-note pages**, and **69 supplementary-guide pages**. The root past-paper PDF is separate. The handwritten document complements the decks and includes additional JWT/session-fixation annotations.

## 1. Lecture 2 — Intro to Cryptography

Source: [slide deck](<../slides/lecture-02-intro-to-cryptography.pdf>). Handwritten companion: pp. 1–12.

### Foundations and security models — deck pp. 3–22

- Secure communication over insecure channels; modern cryptography’s goals.
- Alice/Bob, passive Eve and active Mallory; attacker capabilities.
- Confidentiality, integrity and authenticity; integrity versus authenticity.
- Plaintext, ciphertext, keys, encryption, decryption, tags and signatures.
- Symmetric shared keys versus asymmetric public/private key pairs.
- Kerckhoff’s principle and Shannon’s maxim; key secrecy versus algorithm secrecy.
- Key generation, storage, transmission, rotation and destruction.
- Ciphertext-only, chosen-plaintext, chosen-ciphertext and combined attack models.
- Cryptographic roadmap: confidentiality tools, integrity/authentication tools, hashes, PRNGs, key exchange and key/password management.

### Symmetric encryption and IND-CPA — deck pp. 25–41

- KeyGen, Enc and Dec; correctness, efficiency and confidentiality.
- Security as learning no additional plaintext information.
- Indistinguishability game; encryption-oracle queries; challenge messages and guessing.
- Proving insecurity by constructing an adversary; universal quantification in a security claim.
- Equal-length challenge messages and permitted length leakage.
- Polynomial attacker runtime, negligible advantage and practical security parameters.

### Classical cryptography — deck pp. 43–68

- Caesar cipher: key space, encryption/decryption, brute force and chosen-plaintext recovery.
- General substitution ciphers; permutation keys; frequency analysis and chosen-plaintext attacks.
- Monoalphabetic versus polyalphabetic substitution.
- Enigma: rotors, reflector, plugboard, settings, self-mapping weakness and cryptanalysis history.
- Additive cipher and modular additive inverses.
- Multiplicative cipher; coprimality and modular multiplicative inverses.
- Hill cipher: block/matrix representation, key invertibility, encryption and decryption modulo 26.
- Worked Hill examples: ACT with key GYBNQKURP; ATTACK practice problem.
- Extended Euclidean/Diophantine-equation background for modular inversion.
- Determinism and known-plaintext key recovery in classical schemes.
- **Handwritten extension, pp. 7–11:** affine cipher from additive/multiplicative operations; modular arithmetic and worked matrix inverses.

### Confusion and diffusion — deck pp. 69–70

- Hide the key–ciphertext relationship through confusion.
- Spread plaintext changes across ciphertext through diffusion.
- Connection to block-cipher design and statistical cryptanalysis.

## 2. Lecture 3 — One-Time Pads and Block Ciphers

Source: [slide deck](<../slides/lecture-03-one-time-pads-and-block-ciphers.pdf>). Handwritten companion: pp. 12–15.

### One-time pads — deck pp. 6–22

- XOR truth table, cancellation, associativity and algebra.
- Random message-length keys; encryption/decryption by XOR.
- Correctness proof and perfect-secrecy intuition.
- Two-time pads: XOR of ciphertexts reveals XOR of plaintexts.
- Known/guessed plaintext consequences of key reuse.
- Key generation/distribution costs and practical limitations.
- Number stations, spy use and VENONA as examples.

### Block-cipher foundations — deck pp. 25–31, 42–45

- Key length versus block length; fixed-size permutations.
- Encryption/decryption functions and their domains.
- Bijectivity as a correctness requirement.
- Security as indistinguishability from a random permutation.
- Brute-force work factors for 128-bit/256-bit keys.
- Efficient implementation using XOR, shifts and lookups.
- Why deterministic raw block encryption is not IND-CPA secure.
- Why modes of operation are needed for long messages and randomized encryption.

### DES and AES — deck pp. 32–41

- DES parameters, design history and short-key brute-force weakness.
- AES selection and parameters: 128-bit blocks; 128/192/256-bit keys.
- Round counts and round keys.
- SubBytes, ShiftRows, MixColumns and AddRoundKey.
- Invertibility of the round operations.
- Confusion/diffusion from repeated rounds.
- Final-round difference and the security assumption behind AES.

Detailed DES rounds, multiple-DES meet-in-the-middle analysis and custom P-box/S-box tracing appear in old questions but are not fully taught by this deck.

## 3. Lecture 4 — Block Cipher Modes of Operation

Source: [slide deck](<../slides/lecture-04-block-cipher-modes.pdf>). Handwritten companion: pp. 16–20 and 66.

### ECB — deck pp. 5–9

- Split messages into blocks and encrypt independently.
- Pattern/equality leakage; deterministic encryption; failure of IND-CPA.

### CBC — deck pp. 10–23

- Chaining and random IVs.
- Encryption/decryption equations and block diagrams.
- Sequential encryption versus parallel decryption.
- Padding requirements; ambiguity in naive padding.
- A 1 bit followed by zeros; PKCS#7 and full-block padding.
- Security conditions and IV-reuse leakage of common message prefixes.

### CTR — deck pp. 24–42

- Pseudorandom block-cipher output as an XOR keystream.
- Nonce/counter construction; public nonce, secret key.
- Unique nonce/counter combinations under one key.
- Encryption/decryption using block-cipher encryption only.
- Parallel encryption/decryption; no block padding required.
- Nonce reuse as a two-time-pad failure.
- Counter limits and avoiding repeated keystream.

### Mode comparison, CFB and integrity — deck pp. 43–55

- IV versus nonce; uniqueness, unpredictability and reuse consequences.
- Performance, padding, parallelism and misuse robustness.
- CFB feedback idea and its tradeoffs.
- Confidentiality versus integrity/authenticity.
- CTR bit flipping and chosen plaintext modification.
- CBC corruption propagation and the limits of unauthenticated encryption.
- **Handwritten extension, p. 66:** equations/attack for the custom two-IV chaining construction from the 2023–24 final.

## 4. Lecture 5 — Cryptographic Hashes and MACs

Source: [slide deck](<../slides/lecture-05-hashes-and-macs.pdf>). Handwritten companion: pp. 20–29.

### Cryptographic hashes — deck pp. 13–26, 48

- Arbitrary input length, fixed output length, determinism and efficiency.
- Preimage resistance, second-preimage resistance and collision resistance.
- Pigeonhole principle: collisions exist even for secure hashes.
- Birthday attacks and the n/2-bit collision-security bound.
- MD5, SHA-1, SHA-2 and SHA-3 as examples in the slides.
- Merkle–Damgård: blocks, compression, chaining and padding.
- Length extension; extending a known hash without the original message.
- Secret-prefix hashing and why it can be vulnerable.
- When a trusted hash can detect tampering; why an attacker-editable message/hash pair cannot authenticate data.

### MACs, NMAC and HMAC — deck pp. 27–39, 49

- Shared-key tag generation and verification.
- Correctness, efficiency and existential unforgeability under chosen-message/plaintext queries, called EU-CPA in the deck.
- MAC forgery game and restrictions on previously queried messages.
- Nested hashing/NMAC and defense against length extension.
- HMAC: inner/outer pads, key handling and construction.
- Integrity, shared-key authenticity and absence of confidentiality.
- MACs versus digital signatures; limits on non-repudiation.

### Authenticated encryption — deck pp. 40–47, 50

- Combine confidentiality with integrity/authenticity.
- Encrypt-and-MAC, MAC-then-encrypt and encrypt-then-MAC.
- Evaluate confidentiality/integrity of candidate compositions.
- Independent keys and key reuse.
- Verify-before-decrypt reasoning and implementation side channels.
- Lucky 13 as the slide’s case study.
- Dedicated authenticated-encryption/AEAD modes at overview level.

## 5. Lecture 6 — PRNGs and Diffie–Hellman Key Exchange

Source: [slide deck](<../slides/lecture-06-prngs-and-diffie-hellman.pdf>). Handwritten companion: pp. 30–36.

### Randomness and PRNGs — deck pp. 8–28

- Random/unpredictable values, entropy and uniform distributions.
- Physical entropy sources; bias, cost and combining sources.
- Deterministic generators; seed, reseed, generate and state.
- Computational indistinguishability from randomness; next-output prediction.
- Seed length as a limit on possible output streams.
- Rollback/backtracking resistance after state compromise.
- CTR-DRBG at construction level.
- HMAC-DRBG internal K/V state, seeding/reseeding/generation and state updates.
- Why one-way updates protect previous states/output.
- UUIDs and unpredictable object identifiers.
- Case studies: Bitcoin-wallet entropy, slot machines, Debian OpenSSL, password-reset links, Rust RNG examples and the XZ supply-chain example.

### Stream ciphers — deck pp. 30–37

- PRNG output as an OTP-style keystream.
- Key/IV seeding and encryption of multiple messages.
- AES-CTR as a stream cipher.
- IND-CPA assumptions, limits and counter reuse.
- Streaming and seeking; random access in CTR versus sequential HMAC-DRBG output.

### Diffie–Hellman — deck pp. 41–55, 58

- Public p/g, private exponents, exchanged powers and shared secret.
- Discrete logarithms and the Diffie–Hellman assumption.
- Modular exponentiation, primitive roots, cyclic groups and element order.
- Why generator choice affects the space of possible secrets.
- Euler-totient background and modular inverse/exponentiation practice in the notes.
- Numerical public-key/shared-secret calculations.
- Ephemeral DH, fresh exponents, deletion and forward secrecy.
- MITM exchange diagram; absent authentication and its consequences.
- Active-protocol requirement that both parties participate online.

### ECDH — deck pp. 56–57

- Generalize DH to cyclic groups of elliptic-curve points.
- Elliptic-curve discrete-log intuition and smaller keys.
- Detailed point arithmetic/enumeration is not developed in the deck.

## 6. Lecture 7: Public-Key Encryption and Digital Signatures

Source: [slide deck](<../slides/lecture-07-public-key-encryption-and-signatures.pdf>). Handwritten companion: pp. 36–45. Revision guide: pp. 3–27, 59–61.

### Public-key encryption — deck pp. 6–9

- Public/private key generation, encryption/decryption and correctness.
- Public-key versus shared-key assumptions and costs.
- Number-theoretic message representation.

### ElGamal encryption — deck pp. 12–17

- Derivation from Diffie–Hellman and asynchronous message delivery.
- Public key g^b; fresh random exponent r.
- Ciphertext pair (g^r, M×B^r); inverse-based decryption.
- Correctness and security assumptions.
- Message-space restrictions; IND-CPA discussion in the slides.
- Multiplicative malleability and ciphertext modification.
- Numerical exercise and the modified-private-key exercise.

### RSA encryption and hybrid encryption — deck pp. 20–26

- Primes p/q, modulus N, totient φ(N), public exponent e and private exponent d.
- Coprimality and modular inverses/extended Euclid.
- Encryption/decryption and message-size restriction.
- Correctness via Fermat’s little theorem and the Chinese remainder theorem.
- Factoring/RSA assumptions; determinism and lack of raw-RSA IND-CPA security.
- Small-message/exponent, multiple-recipient and timing-attack issues.
- Probabilistic padding as a requirement at overview level.
- Hybrid encryption: encrypt data symmetrically and wrap the symmetric key asymmetrically.
- **Notes/guide extension:** Euler’s theorem, repeated totients and old modular-equation questions.

### Digital signatures — deck pp. 29–41

- Sign/Verify and signing versus verification keys.
- Integrity/authenticity without a shared signing secret.
- Correctness, efficiency and unforgeability.
- Hash-then-sign for arbitrary-length messages.
- RSA signing/verification equations.
- Security analysis of sending an encryption plus a separate signature.
- Non-repudiation and signature-key trust, expanded in the revision guide.
- DSA/ECDSA overview; fresh secret per-signature k.
- Key exposure from repeated, predictable or short k.
- PS3, Android Bitcoin and Chromebook U2F case studies.
- **Guide extension, pp. 26–27:** full ElGamal signature scheme and nonce-reuse analysis; this is distinct from ElGamal encryption and is not fully given in the lecture.

## 7. Lecture 8: Certificates, Password Hashing, and Case Studies

Source: [slide deck](<../slides/lecture-08-certificates-password-hashing-and-case-studies.pdf>). Handwritten companion: pp. 46–53. Revision guide: pp. 41–53, 65–66.

### Certificates and public-key trust — deck pp. 5–20

- Public-key substitution/MITM and the circularity of self-authenticating keys.
- Trust anchors and trust on first use/SSH.
- Certificates as signed identity–key bindings.
- Trusted-directory model, scalability and single points of failure.
- Root/intermediate CAs, delegated trust and certificate chains.
- Multiple trust anchors and offline certificate issuance.
- Erroneous certificates; expiration and renewal tradeoffs.
- Revocation lists, signatures, stale information and availability tradeoffs.
- X.509 complexity and web-of-trust/OpenPGP alternatives.

### Password storage and attacks — deck pp. 23–30

- Why plaintext storage and reversible encryption are problematic.
- Hash-based verification; determinism and one-wayness.
- Common passwords, dictionary/brute-force attacks and rainbow tables.
- Per-user public random salts; verification with salts.
- Unsalted versus salted attack-cost comparison.
- Slow hashes and practical work factors.
- PBKDF2 inputs, PRF, iterations, output length and uses.
- Memory-cost alternatives mentioned in the slides.
- Offline versus online guessing and suitable defenses.
- **Revision-guide extension, pp. 49–53:** numerical password-space/time calculations and password-reset security questions.

### Case studies and parameters — deck pp. 32–36

- Traffic analysis and metadata versus message content.
- Implementation side channels.
- Spy/number-station example.
- Nothing-up-my-sleeve constants and transparent parameter selection.

## 8. Lecture 9: Introduction to the Web

Source: [slide deck](<../slides/lecture-09-introduction-to-the-web.pdf>). Handwritten companion: pp. 53–54. Revision guide: pp. 62–64.

### Web architecture and URLs — deck pp. 4–22

- Static/active content; Java and JavaScript history; web versus Internet.
- Browsers, servers, data/services and backend computation.
- Scheme, hostname, optional username/port, path, query and fragment.
- Query name/value pairs and client-only fragments.
- URL escaping/encoding and obfuscation.

### HTTP and webpage components — deck pp. 25–43

- Request/response model; HTTP versus HTTPS.
- Methods, paths, query parameters, request bodies and headers.
- GET versus POST in the course model.
- Status codes, response headers and returned data.
- HTML links, forms, images and iframes.
- CSS for presentation.
- Client-side JavaScript: DOM modification, popups and HTTP requests.
- DOM parsing/rendering and browser execution.
- Sandboxed language versus vulnerabilities in interpreters/JIT implementations.

### Web security, origins and privacy — deck pp. 45–59

- Server security, browser sandboxing and website isolation as separate problems.
- Origin = scheme + hostname + port; exact equality and default ports.
- Same-origin policy and frame isolation.
- Origin of externally fetched scripts.
- Cross-origin image loading; CORS and postMessage at overview level.
- Tracking pixels and privacy leakage.

This deck supplies prerequisites for many questions; no question in the collection directly asks a standalone URL/HTTP/DOM/SOP definition exercise.

## 9. Lecture 10: Cookies and CSRF

Source: [slide deck](<../slides/lecture-10-cookies-and-csrf.pdf>). Handwritten companion: pp. 55–63. Revision guide: pp. 28–40, 54–58.

### Cookies and cookie policy — deck pp. 8–29, 71

- State across HTTP requests; Set-Cookie and JavaScript creation.
- Browser storage and automatic cookie attachment.
- Name/value, Domain, Path, Secure, HttpOnly and Expires.
- Domain hierarchy and restrictions on setting cookies.
- Domain/path matching and sending rules.
- URL/cookie matrices including HTTPS and path checks.
- Cookie policy versus same-origin policy.
- Duplicate-name cookie ambiguity and missing attribute information at the server.

### Spectre and isolation — deck pp. 30–35

- Tab/process design; multiple origins in one process.
- Branch prediction, speculative execution and cache/timing side channels.
- Cross-origin data exposure and site/process isolation.
- Isolation’s performance/memory costs.

### Session authentication — deck pp. 37–43, 72

- Login, random secret session tokens and server-side associations.
- Cookie-based subsequent requests, logout and expiration.
- Stolen tokens as independent authentication credentials.
- Secure token generation and restrictive cookie attributes.
- **Handwritten extension, pp. 57–60:** session IDs versus JWTs; token header/payload/signature, verification, expiry and logout/revocation limitations; session fixation and token renewal.

### CSRF — deck pp. 44–59, 73

- Authentication versus user intent.
- Automatic cookies on attacker-induced requests.
- Attack sequence and victim/attacker/server roles.
- GET requests via links/images and POST requests via forms/JavaScript.
- IoT, malvertising and social-network examples.
- CSRF versus XSS, expanded in handwritten pp. 61–63.

### CSRF defenses — deck pp. 61–70, 74

- Session-bound unpredictable CSRF tokens.
- Hidden form fields and explicit submission outside an automatically attached cookie.
- Why the attacker cannot read a victim’s token.
- Referer checking; missing headers, privacy and usability tradeoffs.
- SameSite Strict/Lax/None and cross-site cookie restrictions.
- Cookie attributes’ limits against XSS and local cookie theft.

## 10. Lecture 11 — XSS and UI Attacks

Source: [slide deck](../slides/lecture-11-xss-and-ui-attacks.pdf), **79 pages**. Handwritten companion: pp. 61–64.

### XSS mechanisms — deck pp. 8–25

- Review of origin isolation, JavaScript execution and its trusted page context.
- Untrusted data becoming executable HTML/script through string formatting or concatenation.
- Vulnerable Go HTTP-handler examples.
- Stored/persistent XSS: injecting content retained by the server and executed by later visitors.
- Reflected XSS: request content copied into a response; crafted-link and POST delivery.
- Cookie/data theft and authenticated actions from the trusted origin.
- Reflected XSS versus CSRF; where code executes and what the attacker controls.
- CalNet example and constructing a cross-site request to trigger reflection.

### XSS defenses — deck pp. 26–29, 76–77

- Output escaping and sanitization; control characters versus data.
- Safe templates/APIs and the difficulty of requiring programmers to escape every use.
- Content Security Policy and permitted script/resource origins.
- Why HttpOnly is only a partial mitigation for script execution.

### Clickjacking and other UI attacks — deck pp. 30–51, 78

- Misleading visible controls and trust in user clicks.
- Invisible target iframes, visible frames with invisible overlays, partial overlays.
- Temporal attacks and cursorjacking.
- Visual integrity, temporal integrity, framing restrictions and confirmation.

### Phishing, homographs and second factors — deck pp. 52–75, 79

- Deceptive messages/pages and credential collection.
- URL recognition limits, lookalike/homograph characters and browser-in-browser attacks.
- Human factors and why users cannot reliably inspect every UI cue.
- 2FA factors and their protection against password-only compromise.
- Live phishing/relay attacks and phone-provider social engineering.
- Authentication tokens versus origin-bound security keys.

**Question attribution update:** XSS, clickjacking/phishing/homograph and 2FA questions now point to this deck as their main source, rather than only to handwritten notes. Their historical exam counts are unchanged.

## 11. Lecture 12 — SQL Injection and CAPTCHAs

Source: [slide deck](../slides/lecture-12-sql-injection-and-captchas.pdf), **66 pages**. Handwritten companion: pp. 64–65.

### Web services and SQL foundations — deck pp. 5–28

- Browser, web server and database responsibilities.
- Tables, rows, columns and query results.
- SELECT, constants, WHERE predicates, INSERT INTO, UPDATE and DELETE.
- CREATE/DROP and UNION compatibility.
- SQL string delimiters, comments and statement separators.

### SQL injection — deck pp. 29–40, 55

- Vulnerable query formatting in a Go handler.
- Syntax errors as clues, tautology predicates and stacked-statement examples.
- Query modification, data disclosure and database changes within granted privileges.
- Blind SQL injection and response/error/timing feedback.
- Automated attack tools as case studies.
- Sanitization/escaping limitations.
- Prepared statements: separating fixed query syntax from bound data; driver-specific APIs.

### Command injection — deck pp. 41–45

- Data and commands mixed in shell strings.
- C system() example with attacker-controlled regular-expression input.
- Safe APIs that pass executable and arguments separately; shell parsing and its risks.

### CAPTCHAs — deck pp. 46–56

- Automated abuse, spam, brute force and resource consumption.
- Human/computer challenge definition; text, image and audio examples.
- Machine learning and the changing difficulty of recognition tasks.
- Accessibility and the difference between benign bots and malicious automation.
- Human-outsourcing attacks and the economics of bypassing challenges.

### Worked SQLi walkthrough — deck pp. 57–66

- Start from the SQL interpreter’s actual input.
- Specify the intended altered result, compare syntax and construct an injected UNION query.
- Balance quotes and comments; debug the resulting query rather than guessing payloads.

**Question attribution update:** SQL injection, blind injection and prepared-statement questions now point to this deck. CAPTCHA and command injection remain syllabus topics without standalone questions in the gathered index.

## 12. Handwritten notes and the revision guide

[Handwritten notes](../notes/handwritten-notes.pdf), 66 pages, accompany the lecture material. Additional annotations include JWT header/payload/signature and revocation tradeoffs (pp. 57–59), session fixation (pp. 59–60), and custom-mode practice (p. 66). XSS/UI/SQL topics in those notes are now also covered by Lectures 11–12.

[CT4 revision guide](../notes/ct4-revision-guide.pdf), 69 pages, remains a supplementary historical revision document. Its source material now lives in the common slides folder. It expands digital signatures (pp. 3–10), DH (11–15), RSA/number theory (16–21), ElGamal (22–27), cookies (28–33), CSRF (34–40), certificates (41–47), passwords (48–53), sessions (54–58), key models/TLS (59–61), web foundations (62–64), side channels (65–66) and reference sheets (67–69).

The repository-derived syllabus records what the supplied files teach, not an official current examination exclusion list. The handwritten DSA exclusion annotation and the DSA slides are both retained as source context.
