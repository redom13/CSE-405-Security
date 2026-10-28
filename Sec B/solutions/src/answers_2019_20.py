"""Worked answers in Markdown with canonical LaTeX math."""
answers = {}
answers['2019–20|1(a)'] = r'''
Alice signs a message using a private signing key known only to her. A verifier uses her **authentic public key**, so unlike a MAC the verifier does not need a shared signing secret and cannot create the same kind of signature merely because they can verify it.

```text
Alice:      h=H(M); s=Sign(SKA, context || M)
Send:       (M,s, Alice's certificate if needed)
Verifier:   validate identity/key binding; Verify(PKA,context||M,s)
```

![Signature creation and public verification](assets/signature.svg)

If the signature is valid, the key is correctly bound to Alice, the algorithm is unforgeable and the private key has remained under Alice’s control, a third party has evidence that the holder of Alice’s signing key endorsed the exact signed content. Alice cannot plausibly claim that Bob generated the signature merely because Bob knew how to verify it.

Hashing binds the signature to arbitrary-length content; signing an encoded context helps avoid interpreting the same signature as authorization for another purpose. Certificates, timestamps, key-protection records and revocation status can matter in a real dispute.

**Limit.** A signature proves a cryptographic relationship to a key, not by itself the human’s intent or absence of key theft. Non-repudiation relies on identity and operational assumptions in addition to the equation. A MAC lacks the same third-party attribution because both participants can generate it.

**Exam tip.** Explain why verification is transferable evidence and contrast it with a shared-key MAC. Include the authentic public-key assumption.
'''
answers['2019–20|1(c)'] = r'''
This is **account takeover through weak knowledge-based account recovery**, aided by impersonation/social engineering. The attackers did not need to brute-force the existing password: they exploited an alternate reset path that treated publicly discoverable facts as identity proof.

Birthday, ZIP code and biographical/security-question answers can have low effective entropy or be directly searchable. Several such questions are not independent strong secrets when all answers come from the same public biography. The account’s effective security is limited by the weakest route that can issue a fresh credential.

A stronger recovery design uses previously enrolled recovery channels/codes, short-lived single-use unpredictable reset tokens, appropriate rate limits, audit/notification, and additional verification for sensitive accounts. The delivery channel itself must be protected. Avoid user-enumeration leaks and revoke relevant old sessions after recovery. High-entropy stored answers help if a service forces security questions, but do not fix a support workflow that can bypass them.

**Exam tip.** Name the recovery-path failure rather than calling this password brute force. An excellent normal password cannot compensate for a publicly guessable reset mechanism.
'''
answers['2019–20|2(b)'] = r'''
There are 128 choices at each of ten positions, with repetition allowed:

$$
\begin{aligned}N&=128^{10}=(2^7)^{10}=2^{70}\\&=1\,180\,591\,620\,717\,411\,303\,424,\\r&=\frac1{10^{-6}}=10^6\ \mathrm{guesses/s}.\end{aligned}
$$

Assuming the target is uniform and the attacker tries distinct candidates in some order, the expected position is (N+1)/2, effectively N/2 here:

$$
\begin{aligned}t_{\mathrm{avg}}&\approx\frac{N}{2\cdot10^6}\\&\approx5.902958\times10^{14}\ \mathrm{s}\\&\approx1.8705\times10^7\ \mathrm{years}\approx18.7\text{ million years}.\end{aligned}
$$

The near-worst-case exhaustive time is approximately 37.4 million years. Converting uses 365.25 days/year; choosing 365 changes only rounding.

The result is conditional on the paper’s full 128-character alphabet and uniform selection. Real text inputs may reject control characters, and human choices are nonuniform. The paper fixes the rate, so do not silently replace it with a different hardware assumption.

**Exam tip.** Convert one microsecond to $10^{-6}$ seconds and apply the average-case factor 1/2. Write the exact password count before converting time units.
'''
answers['2019–20|6(a)'] = r'''
**Binary OTP.** For an n-bit message M and an independently uniform secret n-bit pad P used only once:

$$
\begin{aligned}C&=M\oplus P,\\C\oplus P&=M\oplus P\oplus P=M.\end{aligned}
$$

XOR cancellation makes the identical pad usable for encryption and decryption. A fixed observed C is compatible with every possible M through exactly one pad P=C XOR M, so a uniform secret pad leaks no message information beyond length. Reusing P on two messages exposes $C_1\oplus C_2=M_1\oplus M_2$.

**Transposition cipher.** It reorders symbol positions without changing their values. For block length n, represent the permutation by an n×n matrix Π with one 1 in each row and column and zeros elsewhere. Then $C=\Pi M\pmod{26}$ is a Hill cipher with key Π.

Example, swap the first two symbols of a three-symbol block:

$$
\Pi\begin{pmatrix}m_1\\m_2\\m_3\end{pmatrix}=\begin{pmatrix}0&1&0\\1&0&0\\0&0&1\end{pmatrix}\begin{pmatrix}m_1\\m_2\\m_3\end{pmatrix}=\begin{pmatrix}m_2\\m_1\\m_3\end{pmatrix}\pmod{26}.
$$

$\Pi^{-1}=\Pi^{\mathsf T}$, and $\det(\Pi)=\pm1$, always invertible modulo 26. Therefore transposition ciphers form a restricted subset of Hill transformations, which permit more general invertible matrices.

**Exam tip.** Show a permutation matrix instead of only asserting the relationship. OTP pad “P” is a bitstring here, while Hill plaintext symbols are residues; do not conflate the notation.
'''
answers['2019–20|6(b)'] = r'''
**Ideal-hash properties.** Efficient deterministic evaluation, fixed output size, preimage resistance, second-preimage resistance and collision resistance. Hash outputs should not expose useful algebraic structure.

- **Weak collision resistance / second-preimage resistance:** given x, hard to find x′≠x with H(x′)=H(x).
- **Strong collision resistance:** hard to find any distinct pair x,x′ with equal hashes, both chosen by the attacker.

For the supplied toy hash over unrestricted integers:

$$
\begin{aligned}H(4)&=(5\cdot4+11)\bmod19=12,\\H(23)&=(5\cdot23+11)\bmod19=12.\end{aligned}
$$

Since 23≠4, this is a direct second preimage. More generally H(x+19t)=H(x). If the domain were restricted to 0,…,18, multiplication by 5 is invertible and this particular collision would not be in-domain; the question’s conclusion assumes the unrestricted/longer input domain.

**Merkle–Damgård construction.** Pad the message with an unambiguous length-encoding scheme, split it into fixed-size blocks m1,…,mt, set h0 to a fixed public IV, and iterate:

$$
h_i=f(h_{i-1},m_i),\qquad H(M)=h_t.
$$

![Merkle–Damgård chaining](assets/merkle-damgard.svg)

Why does compression collision resistance matter? If two distinct inputs to f produce the same chaining state, subsequent identical suffix blocks produce identical final hashes. Under the construction’s proper length strengthening and conditions, a collision in the iterated hash can be traced back to a collision in the compression function. Thus weak compression security undermines the composed hash. This is a collision-resistance statement, not protection against every misuse such as naive secret-prefix length extension.

**Exam tip.** Give the specific second preimage 23 and distinguish the attacker’s freedom in weak versus strong collision games. Include padding and the fixed IV in the diagram.
'''
answers['2019–20|7(a)'] = r'''
Euler’s totient φ(n) counts integers from 1 through n that are coprime to n. For prime p, φ(p)=p−1; for distinct primes p,q, φ(pq)=(p−1)(q−1).

**Euler’s theorem:** if gcd(a,n)=1, then $a^{\varphi(n)}\equiv1\pmod n$. Splitting off one factor gives:

$$
\begin{aligned}a\cdot a^{\varphi(n)-1}&\equiv1\pmod n,\\a^{-1}&\equiv a^{\varphi(n)-1}\pmod n.\end{aligned}
$$

Example: n=10, a=3 and φ(10)=4. Then inverse $3^3=27\equiv7\pmod{10}$, and 3·7≡1. For an RSA-related example φ(160)=64, so $7^{63}\bmod160=23$, since 7·23=161≡1.

If gcd(a,n)≠1, the inverse does not exist, so the formula must not be applied. In practice extended Euclid finds an inverse without needing φ(n): find x,y with ax+ny=1; then x is the inverse modulo n.

**Exam tip.** State the coprimality condition with the theorem. Computing φ(n) may require factorization; Euler’s expression is mathematically illuminating but not always the most efficient inverse algorithm.
'''
answers['2019–20|7(b)'] = r'''
**(i) $x^{8}$≡9 mod 13.** Check residues x=1,…,12 by repeated squaring; x=0 plainly fails:

| x | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| $x^{2}$ mod 13 | 1 | 4 | 9 | 3 | 12 | 10 | 10 | 12 | 3 | 9 | 4 | 1 |
| $x^{4}$ mod 13 | 1 | 3 | 3 | 9 | 1 | 9 | 9 | 1 | 9 | 3 | 3 | 1 |
| $x^{8}$ mod 13 | 1 | 9 | 9 | 3 | 1 | 3 | 3 | 1 | 3 | 9 | 9 | 1 |

**Solutions: x≡2,3,10,11 mod 13.** Checking all residue classes proves completeness.

**(ii) $x^{2}$≡2 mod 13.** The squares in the table are `{1,3,4,9,10,12}`, with 0 added for x=0. None equals 2. **No solution.**

**(iii) $3^{128}$ mod 7.** Fermat gives $3^{6}$≡1 mod 7. Since 128=21·6+2:

$$
3^{128}\equiv(3^6)^{21}\cdot3^2\equiv9\equiv2\pmod7.
$$

**Exam tip.** Solve for residue classes, not merely ordinary integer roots. “Take an eighth root” is not a valid modular solution method without more group reasoning.
'''
answers['2019–20|7(c)'] = r'''
**System A:** p=83, q=101, N=8383.

$$
\begin{aligned}\varphi(N)&=82\cdot100=8200,\\8200&=2^3\cdot5^2\cdot41,\\\varphi(\varphi(N))&=\varphi(8200)=4\cdot20\cdot40=3200,\\ed&=3\cdot5467=16401=2\cdot8200+1.\end{aligned}
$$

Therefore e is coprime to φ(N) and d is its inverse modulo φ(N). The factors are distinct primes, so the RSA key relationships are valid.

**System B:** p=17, q=11, N=187.

$$
\begin{aligned}\varphi(N)&=16\cdot10=160=2^5\cdot5,\\\varphi(\varphi(N))&=\varphi(160)=16\cdot4=64,\\ed&=7\cdot23=161=160+1.\end{aligned}
$$

Again d is the required modular inverse. Encrypt M=3:

$$
C=3^7\bmod187=2187\bmod187=130.
$$

A decryption check gives $130^{23}\bmod187=3$.

**Exam tip.** φ(φ(N)) is not φ(N)−1 unless φ(N) happens to be prime, which it is not here. Factor the intermediate totient. Mathematical key validity does not make these tiny classroom moduli secure.
'''
answers['2019–20|8(a)'] = r'''
**ElGamal encryption.** In a specified cyclic group written multiplicatively, publish generator g and public key y=$g^{x}$; keep x private. To encrypt group element M, choose fresh random r and send:

$$
C_1=g^r,\qquad C_2=My^r.
$$

Decrypt $M=C_2(C_1^x)^{-1}$. Correctness is:

$$
C_2(C_1^x)^{-1}=Mg^{xr}g^{-rx}=M.
$$

For a small arithmetic example modulo 11, let g=2,x=4, so y=5. Encrypt M=7 with r=3: C1=8 and C2=7·$5^{3}$ mod 11=6. Bob computes $C1^{x}$=$8^{4}$ mod 11=4, whose inverse is 3, giving M=6·3 mod 11=7. State the group and message-encoding assumptions when discussing confidentiality; the correctness equation itself is not a security proof.

**Birthday attack on hash-based signatures.** Suppose signatures authenticate H(M). An attacker prepares many benign contract variants Bi and many malicious variants Aj, using harmless formatting/metadata variations within each semantic category. Search for a cross-pair with H(Bi)=H(Aj). Ask the signer to approve Bi, then attach the resulting signature to Aj: verification sees the same digest.

For an ideal b-bit digest, two sets of roughly $2^{b/2}$ variants give a constant probability of a cross-collision because there are about $2^{b}$ cross-comparisons. A toy 32-bit digest would need on the order of $2^{16}$ variants in each set, making the problem practical. A large collision-resistant digest makes this infeasible.

**Exam tip.** The attack does not forge the private-key operation. It substitutes a different message with the same signed digest, and it needs flexibility to prepare both candidate sets before obtaining the signature.
'''
answers['2019–20|8(b)'] = r'''
**DH steps.** Agree public p,g. Alice chooses a and sends A=$g^{a}$ mod p. Bob chooses b and sends B=$g^{b}$ mod p. Alice computes $B^{a}$ and Bob computes $A^{b}$, both giving $g^{ab}$ mod p.

**MITM steps.** Mallory intercepts A and sends X=$g^{x}$ to Bob; intercepts B and sends Y=$g^{y}$ to Alice. Alice’s key becomes $Y^{a}$=$A^{y}$; Bob’s key becomes $X^{b}$=$B^{x}$. Mallory computes both from her own x,y and the intercepted A,B.

![DH exchange and substitution](assets/dh-mitm.svg)

Mallory decrypts Alice’s traffic using the Alice–Mallory key, optionally modifies it, and re-encrypts under the Mallory–Bob key. Neither party has authenticated the claimed owner of the received DH contribution. This is why discrete-log hardness against a passive observer does not prevent the attack.

Authenticate fresh shares/transcripts through signatures verified against trusted keys, a pre-shared secret, or an independent authenticated comparison. Bind both identities and roles to prevent misassociation. Merely encrypting application messages under the resulting keys cannot retrospectively authenticate the exchange.

**Exam tip.** Show Mallory’s two calculable secrets explicitly. Multiplying A by B produces $g^{a+b}$, not the desired $g^{ab}$.
'''
