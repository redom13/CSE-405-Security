"""Worked answers in Markdown with canonical LaTeX math."""
answers = {}
answers['2022–23|5(a)'] = r'''
For block size n, let E be a secure block cipher and D its inverse.

$$
\begin{aligned}\mathrm{ECB}:\quad C_i&=E_K(P_i),\\\mathrm{CBC}:\quad C_0&=IV,\quad C_i=E_K(P_i\oplus C_{i-1}),\\P_i&=D_K(C_i)\oplus C_{i-1},\\\mathrm{CTR}:\quad Z_i&=E_K(N\parallel i),\\C_i&=P_i\oplus Z_i,\quad P_i=C_i\oplus Z_i.\end{aligned}
$$

![CBC and CTR structure](assets/modes.svg)

| Property | ECB | CBC | CTR |
|---|---|---|---|
| IND-CPA | No: deterministic, exposes block equality | Yes under appropriate unpredictable IV and secure-block-cipher assumptions | Yes when every nonce/counter input under a key is unique, within security limits |
| Parallel encryption | Yes | No | Yes |
| Parallel decryption | Yes | Yes | Yes |
| Padding | Needed for arbitrary byte lengths | Needed | Not needed for a final partial block |
| Reuse consequence | No IV; repeated blocks always visible | Reused IV exposes equal starting plaintext blocks up to divergence | Repeated keystream gives C XOR C′ = P XOR P′ |

CBC encryption depends on the preceding ciphertext, so it cannot parallelize across a message. Its decryption uses only received ciphertext blocks, so D calls can run simultaneously. CTR keystream blocks are independent computations; encryption and decryption use E, not D.

For CBC, the IV should be unpredictable at encryption time in the usual chosen-plaintext model; merely incrementing a public IV is not a general substitute. For CTR, uniqueness is the central requirement, so a correctly managed deterministic nonce/counter allocation can work. In both cases authenticate transmitted parameters and ciphertext to stop active modification.

**Exam tip.** “IND-CPA secure” needs conditions. Correctly used CBC and CTR provide confidentiality; neither plain mode independently guarantees integrity.
'''
answers['2022–23|5(b)'] = r'''
Assume Enc is a secure randomized encryption scheme, MAC is unforgeable, message encodings are unambiguous, and—as expressly granted in this question—using K in both primitives creates no cross-protocol interaction.

| Scheme sent | Confidentiality against Eve | Integrity against Mallory |
|---|---|---|
| 1. C1=Enc(K,m), C2=Hash(C1) | Yes, if Enc is secure; the hash is publicly computable from already visible C1 | No: replace C1 with altered ciphertext and recompute its hash |
| 2. C1=Enc(K,m), C2=MAC(K,m) | Not guaranteed generically; the deterministic plaintext tag leaks equality across transmissions | Yes for fresh message forgery, if Bob decrypts and verifies the tag on the recovered m |
| 3. C1=Enc(K,m), C2=MAC(K,C1) | Yes under the granted composition assumptions | Yes for ciphertext forgery; verify before decryption |

**Why scheme 2 needs a careful answer.** A keyed HMAC is not a public plaintext hash, so Eve cannot necessarily hash candidate passwords herself without K. Nevertheless, the MAC is deterministic: repeated m gives repeated tags even when the randomized ciphertext changes. This defeats general indistinguishability across messages/oracle access. Thus the scheme does not inherit a general confidentiality guarantee from encryption alone. It may hide a single unpredictable message in a weaker, restricted setting; do not confuse that with IND-CPA.

Schemes 2 and 3 do not automatically reject a previously valid packet replay. Add authenticated freshness and receiver state if integrity includes replay resistance. In practical design use independent derived keys even though this paper temporarily assumes shared-key interactions away.

**Exam tip.** Distinguish a keyed MAC from an unkeyed hash and tamper detection from freshness. State the paper’s special same-key assumption before applying generic composition reasoning.
'''
answers['2022–23|5(c)'] = r'''
**(i) CSRF.** Ordinary Domain/Path cookie matching is insufficient: an attacker can induce a request **to the legitimate target**, and the target’s own cookie matches that request. The browser authenticates the account, not the user’s intention. SameSite can limit cross-site attachment; unpredictable session-bound CSRF tokens and appropriate Origin/Referer checks provide additional protection. A Secure or HttpOnly flag alone does not stop CSRF.

**(ii) XSS session hijacking.** Injected script runs as the victim site, so the domain/origin isolation boundary does not exclude it. If a session cookie is script-readable, XSS can read it and export it. HttpOnly blocks that specific reading path. However, the script can still make same-origin requests that automatically include the cookie, so HttpOnly does not cure XSS. Use contextual output encoding/safe DOM APIs and CSP as defense in depth.

**(iii) Stored-cookie confidentiality.** Domain/Path rules govern browser delivery, not disk encryption. Secure protects network transmission; HttpOnly restricts page scripts. Neither promises protection from someone who can read the browser profile or compromise its user account. OS/browser storage protection, device security, token expiration and server-side revocation address different parts of that threat.

**Exam tip.** Organize the answer by the three threat locations: unwanted request, hostile script inside a trusted page, and local storage access. Cookie policy is not a complete defense against all three.
'''
answers['2022–23|6(a)'] = r'''
**Unauthenticated exchange.** Alice publishes A=$g^{a}$; Bob publishes B=$g^{b}$; each obtains $g^{ab}$. A passive observer sees g,p,A,B but, under the relevant DH assumption, cannot recover the secret. An active Mallory replaces A/B, establishes independent keys with each party, and relays traffic.

![DH MITM](assets/dh-mitm.svg)

**RSA-signature repair.** Before this protocol, Alice and Bob must possess authentic RSA verification keys for one another, obtained through certificates, pinning or an authenticated fingerprint comparison. Then:

```text
1. A → B: Alice, Bob, nonceA, A=g^a
2. B → A: nonceB, B=g^b,
          Sig_B("DH/server" || Alice || Bob || nonceA || nonceB || A || B)
3. A → B: Sig_A("DH/client" || Alice || Bob || nonceA || nonceB || A || B)
```

Each verifies the signature using the corresponding authenticated public key and checks identities, shares and freshness. In lecture notation $\operatorname{Sig}_X(T)=H(T)^{d_X}\bmod N_X$, verified by raising to eX. Derive a session key from $g^{ab}$ and the transcript using a KDF; optional key-confirmation MACs prove both endpoints obtained it.

Mallory cannot change a share or identity without invalidating a signature. Replaying a signature on an old share fails the nonce/transcript checks. If signatures are verified against untrusted keys attached by Mallory, the fix fails for exactly the same reason as unauthenticated DH.

**Exam tip.** The essential extra assumption is authentic signing keys. Signing just a bare share without peer/role/freshness context leaves avoidable replay and identity-binding problems.
'''
answers['2022–23|6(b)'] = r'''
The vulnerable statement is:

```sql
INSERT INTO cart(session,item) VALUES ('S','ITEM')
```

Here S denotes Alice’s actual session token. Since ITEM is interpolated as SQL text, Alice can end its first tuple and append more tuples **inside the same INSERT**. One pen is inserted by the original tuple; add 99 more for a total of 100.

The following constructs the POST body, rather than printing 99 nearly identical tuples:

```python
from urllib.parse import urlencode
S = "ALICES_ACTUAL_SESSION_TOKEN"
extra = ",".join("('" + S + "','pen')" for _ in range(99))
item = "pen')," + extra + " -- "
body = urlencode({"item": item})
```

Send `body` in an `application/x-www-form-urlencoded` POST to the cart’s existing add-item endpoint, with Alice’s normal session cookie. The resulting SQL is:

```sql
INSERT INTO cart(session,item) VALUES
('S','pen'),('S','pen'), ... 100 total tuples ... -- ')
```

The illustration assumes a database supporting multi-row VALUES and `-- ` comments, and Alice knows her own session value. The question does not supply a literal endpoint name. The original three-item UI restriction is bypassed because a single backend call inserts many rows.

**Prevent SQL injection** with `INSERT INTO cart(session,item) VALUES (?,?)` and bound values. Enforce the **business rule** independently: check the resulting cart quantity server-side, using a transaction/locking or an appropriate database constraint so concurrent requests cannot bypass it. A client-side limit is insufficient even after SQL injection is fixed.

**Exam tip.** Count 1 original row + 99 injected rows. “Only one SQL statement” does not prevent this; no semicolon or stacked statement is needed.
'''
answers['2022–23|6(c)'] = r'''
HMAC-DRBG holds secret state (K,V). It expands a high-entropy seed into pseudorandom output using HMAC, then updates state so compromising today’s state does not reveal earlier output.

A standard form initializes K to zero bytes and V to 0x01 bytes, each as long as the HMAC output. With seed material s:

```text
Update(s):
    K = HMAC(K, V || 0x00 || s)
    V = HMAC(K, V)
    if s is nonempty:
        K = HMAC(K, V || 0x01 || s)
        V = HMAC(K, V)

Generate(n):
    out = empty
    while length(out) < n:
        V = HMAC(K,V)
        out = out || V
    Update(empty)
    return first n bits of out
```

Instantiate by calling Update(seed material); reseed by Update(new entropy and any allowed additional data). The lecture’s initialization shorthand differs from the standard’s V bytes, so state the convention rather than mixing traces. See [NIST SP 800-90A Rev. 1, HMAC-DRBG](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf).

**Security explanation.** With unpredictable hidden state and a secure HMAC pseudorandom-function construction, generated blocks should be computationally indistinguishable from random. More output does not create more initial entropy; sufficient seeding matters. Rollback resistance depends on the irreversible state updates and erasing obsolete state: knowing the current (K,V) should not allow inversion to earlier states/output.

This does not imply that state compromise cannot predict future output. Without new secret entropy, an attacker who has the state can generally follow deterministic future transitions. Reseeding is necessary to recover from compromise. Also, “HMAC is collision resistant” alone is not the full security assumption for this generator.

**Exam tip.** Separate unpredictability, protection of past output after compromise, and recovery of future security after reseeding.
'''
answers['2022–23|7(a)'] = r'''
**(i) Why it works.** On a legitimate page the server creates an unpredictable token T bound to the authenticated session and includes it in a hidden field. A submitted state-changing POST must carry both the session cookie and T. The attacker can induce a cookie-bearing request, but cannot read the victim’s page token across origins. A token obtained in the attacker’s own session does not validate for the victim.

![CSRF and token check](assets/csrf.svg)

The server compares the submitted token with the expected session-bound value before changing state. Cookies alone are automatic; the additional token is not automatically copied into a forged form. A b-bit uniform token permits roughly $2^{-b}$ success per independent guess, with rate limiting further bounding attempts.

“No special browser support” means no new CSRF-specific browser feature is required. The reasoning still assumes baseline browser origin isolation, no XSS/token leakage, authenticated transport where needed, and server validation. A hidden field is not secret from the user or same-origin JavaScript; its protection is from the remote attacker.

**(ii) Refresh only on POST versus GET and POST.** Rotating on every GET can invalidate forms in other tabs or cause a cross-site image/link request to invalidate a pending form, creating usability and denial-of-service problems. Rotating after an accepted state-changing POST reduces such accidental invalidation. GET must not change protected state, so it normally needs no token-consuming operation.

Per-POST rotation still creates multi-tab/back-button races if the server stores only one current token. A well-designed per-session token or multiple valid per-request tokens may offer a better balance. Rotation is not what fundamentally blocks CSRF: unpredictability, session binding and validation are. If a GET performs a sensitive change, leaving GET unprotected is a vulnerability, regardless of refresh policy.

**Exam tip.** Explain the attacker’s missing information, then discuss usability. Do not claim that more frequent refresh always means stronger practical security.
'''
answers['2022–23|7(c)'] = r'''
**Stored XSS:** an attacker submits active content to persistent storage, such as a comment or profile. Later victims receive it as part of a trusted page and their browsers execute it. No new crafted request from the attacker is required for each victim.

**Reflected XSS:** attacker input arrives in the victim’s request and is immediately echoed into the response as executable content. The attacker usually lures the victim to a crafted URL or form submission.

```text
Stored:    attacker → stored entry → server page → victim executes
Reflected: crafted link → victim request → echoed response → victim executes
```

Both exploit unsafe interpretation of input as code and execute in the browser under the affected page’s origin. Use output encoding suitable for the HTML/attribute/JavaScript context, safe DOM operations and sanitization for permitted rich HTML; CSP adds defense in depth.

**Exam tip.** The database is not the execution environment. A stored payload is stored at the server but normally executes in a victim’s browser.
'''
answers['2022–23|8(a)'] = r'''
Assume the attacker may alter writable file contents and header fields, but not the user’s secret key k. Treat F as the protected **content excluding its stored tag field**; otherwise hashing a file containing its own tag is underspecified.

**(i) Writable file plus unkeyed hash: insecure.** Replace F by any F′ and replace its header value by H(F′). No collision is needed. Collision resistance only prevents finding matching outputs when the trusted comparison digest cannot itself be changed.

**(ii) Writable file plus MAC: secure against fresh content substitution under the stated model.** Store T=MAC(k,F), then on open verify T against F. The attacker cannot change F to a new F′ and produce the corresponding tag without forging the MAC. Include file identity and relevant metadata in the authenticated encoding to avoid cross-file substitution.

**(iii) MAC tag in read-only memory: secure for detecting a changed content version**, assuming the key remains protected and a valid fixed tag uniquely binds the intended file content except with negligible probability. The attacker cannot replace the tag or forge a different matching message. A securely fixed unkeyed digest could also detect changes under an appropriate second-preimage assumption; the important additional property is a trusted comparison value.

**Freshness caveat.** With the tag writable in (ii), an attacker who saved an old valid (F,T) pair can restore both. A MAC alone does not detect rollback. Read-only storage fixes an intended version but complicates authorized updates. If freshness is required, authenticate a version counter whose current value is independently trusted.

**Exam tip.** Explain the attacker’s action on both content and tag. “Hashes detect tampering” is incomplete without saying where the expected hash is trusted.
'''
answers['2022–23|8(b)'] = r'''
**SMS 2FA helps against a stolen password alone, but does not reliably defeat interactive phishing.** A relay phishing site asks for the password, immediately submits it to the genuine service, asks the victim for the SMS code, and forwards that code before it expires. The real service sees valid factors and issues a session to the attacker.

![Phishing relay](assets/relay.svg)

An expiring or one-time code reduces replay but not live forwarding. SMS also inherits phone-account and delivery-channel risks; those are separate from the phishing mechanism asked here.

A stronger defense is an origin-bound authenticator such as WebAuthn used correctly: the authenticator’s response is bound to the legitimate relying party, so the phishing origin cannot simply request a response valid for a different site. The site still needs sound session management.

**Exam tip.** Avoid a bare yes/no. Name the threat it stops—password-only compromise—and show why a live relay can still succeed.
'''
answers['2022–23|8(c)'] = r'''
**(i) Fake subscription button above a purchase action.** Eve embeds WorstPay in an iframe and positions its real buy button under a visible “free Getflix” button. The frame is transparent and lies above the decoy in the click stack, so the user’s click reaches the purchase button. An authenticated victim may complete an action they did not intend. Eve need not read or modify the cross-origin iframe’s DOM; knowing the button’s approximate screen position is enough.

![Clickjacking overlay](assets/clickjacking.svg)

**(ii) Twitter, Facebook, then the real results.** Eve places two transparent links over the apparent submit button, one above the other. On the first click the top link opens Twitter and is removed; on the second the next opens Facebook and is removed; on the third the unobstructed iframe receives the click and performs its normal result request. For example:

```html
<!-- All layers positioned over the iframe's submit-button coordinates. -->
<a class="overlay top" href="https://twitter.com/" target="_blank"
   rel="noopener" onclick="this.remove()"></a>
<a class="overlay lower" href="https://facebook.com/" target="_blank"
   rel="noopener" onclick="this.remove()"></a>
<iframe src="RESULT_SITE_URL"></iframe>
```

The anchors’ z-index values order the first two clicks; each has a transparent hit area. Use new tabs/windows so Eve’s page and filled iframe remain available for subsequent clicks. Exact navigation behavior and button coordinates are assumptions, not a right to inspect the frame across origins.

**Defense.** The framed target sends an appropriate CSP `frame-ancestors` policy, optionally with X-Frame-Options for older clients. Sensitive-action confirmation can reduce damage. A parent page cannot undo a correctly enforced target framing restriction. [OWASP’s framing-defense guidance](https://cheatsheetseries.owasp.org/cheatsheets/Clickjacking_Defense_Cheat_Sheet.html).

**Exam tip.** Show the click order and where the event actually lands. Cross-origin framing may be allowed even though cross-origin DOM reading is forbidden.
'''
answers['2022–23|2(a)'] = r'''
**The prompt needs assumptions for a numerical answer.** It gives minimum length 10 but no maximum, no count of permitted special symbols, and no required success probability. An exhaustive guarantee over all permitted lengths has no finite fixed search space. The conventional exam estimate uses exactly ten uniformly chosen characters and a 30-day month.

Assume 26 uppercase + 26 lowercase + 10 digits + 32 non-space special characters, giving alphabet size A=94. A common coarse estimate is:

$$
\begin{aligned}N&=94^{10}=53\,861\,511\,409\,489\,970\,176,\\T&=30\cdot24\cdot3600=2\,592\,000\ \mathrm{s},\\r_{\mathrm{worst}}&=\frac{N}{T}\approx2.078\times10^{13}\ \mathrm{guesses/s},\\r_{\mathrm{mean}}&=\frac{N}{2T}\approx1.039\times10^{13}\ \mathrm{guesses/s}.\end{aligned}
$$

**If the policy requires at least one character from every class**, count valid ten-character strings rather than all $94^{10}$. Inclusion–exclusion gives:

$$
\begin{aligned}N_{\mathrm{valid}}&=\sum_{S\subseteq\{U,L,D,S_p\}}(-1)^{|S|}\left(94-\sum_{c\in S}|c|\right)^{10}\\&=32\,333\,391\,317\,360\,640\,000,\\(|U|,|L|,|D|,|S_p|)&=(26,26,10,32).\end{aligned}
$$

The two 26-sized classes are distinct subsets even though their sizes coincide. Then:

$$
\begin{aligned}\frac{N_{\mathrm{valid}}}{T}&\approx1.247\times10^{13}\ \mathrm{guesses/s},\\\frac{N_{\mathrm{valid}}}{2T}&\approx6.237\times10^{12}\ \mathrm{guesses/s}.\end{aligned}
$$

For a uniform space of N candidates and no repeated guesses, success after g guesses is approximately min(g/N,1). Thus a target success fraction α requires roughly αN/T guesses/s; “crack within one month” must identify whether α is average-case or near certainty. Human-selected passwords are not uniform, so dictionary guessing may cost far less.

**Exam tip.** Write the assumptions and distinguish N/T from N/(2T). A monthly reset policy does not specify the attacker’s desired success probability.
'''
