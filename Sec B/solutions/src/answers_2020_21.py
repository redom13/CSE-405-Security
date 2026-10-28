"""Worked answers in Markdown with canonical LaTeX math."""
answers = {}
answers['2020–21|5(a)'] = r'''
**A visible bearer cookie alone is insufficient.** If an observer can copy a token that is accepted as the only credential, they can replay it or impersonate its holder. Likewise, using the public cookie value itself as an HMAC key lets the observer forge tags. The goal permits cleartext content, not exposure of the authentication secret.

**One complete construction: authenticated session establishment plus MACed datagrams.** Assume the client and service establish a secret session key K by an authenticated exchange—for example, signed ephemeral DH with a pre-trusted server verification key, or a pre-shared secret. This is possible without running TLS, but cannot dispense with all initial trust. Derive separate directional keys Kcs/Ksc using a KDF. The server gives the client a session identifier/cookie sid and expiry, binding sid to the session and identity.

For a client→server message:

```text
packet = (sid, direction, seq, payload, tag)
tag = HMAC(Kcs, encode(sid,direction,seq,payload))
```

The server looks up the appropriate secret key from sid, validates the tag, checks expiry, then rejects any seq already accepted. Use a replay bitmap/window if UDP reordering must be tolerated. Reverse direction uses Ksc and its own sequence-number space. Record the accepted counter atomically after successful verification.

- **Impersonation:** an observer can copy sid but cannot compute new valid tags without the secret key.
- **Alteration:** payload and associated fields are MAC-covered, so modification invalidates the tag.
- **Replay:** an old valid packet is rejected by the tracked sequence number; a MAC alone would accept it again.
- **Confidentiality:** payload can remain unencrypted, as permitted by the question.

A signed/self-authenticating cookie can reduce server state for the cookie’s integrity, but replay detection still needs state or a carefully specified freshness mechanism. If no shared secret is possible, digital signatures on datagrams plus an authentic verification key and sequence checking are another authentication approach.

**Exam tip.** Raw UDP does not automatically carry HTTP cookies. Treat the cookie as an application token field, state how secret keys are established, and explicitly include replay protection. Sending a fresh MAC key in cleartext defeats the design even if the application content need not be confidential.
'''
answers['2020–21|5(b)'] = r'''
**Restricting the backend to one SQL statement does not prevent injection within that statement.** The question supplies a password-change form but no exact query, so state a conventional vulnerable implementation:

```sql
UPDATE users SET password='NEW'
WHERE username='CURRENT_USER' AND password='OLD'
```

Put the following in the new-password field (and anything in old password):

```text
chosen_password' WHERE 1=1 -- 
```

After interpolation:

```sql
UPDATE users SET password='chosen_password' WHERE 1=1 -- '
WHERE username='CURRENT_USER' AND password='anything'
```

The comment suppresses the intended WHERE restriction; every row is updated by the **same UPDATE statement**. The trailing space after `--` is relevant for MySQL-style comments. This assumes the application trusts that one query as its password check/update, with no prior independent verification. Different query placement may require a different payload; without source, no unique byte-for-byte input is guaranteed.

**Repair:** look up the current authenticated user with a bound identifier, verify the old password against its stored hash, then update only that user’s password hash through a prepared statement. Scope the update using the server’s authenticated user identity, not an arbitrary submitted username. Database privileges should limit damage.

**Exam tip.** Show the expanded statement and how its predicate changes. Do not use a semicolon followed by a second UPDATE—the prompt explicitly removes that avenue.
'''
answers['2020–21|6(a)'] = r'''
**Part (i): forge the visitor’s friend request.** Trudy serves a page containing:

```html
<img hidden
 src="http://www.networksocial.com/action/friends/add?friend=20">
```

When logged-in A visits, the browser sends the GET to NS. Under the paper’s vulnerable cookie/CSRF assumptions it includes A’s session cookie, so NS interprets the action as A adding Trudy. The image need not successfully display; sending the request is sufficient.

**Part (ii): store active content in A’s homepage using CSRF.** Trudy’s page also auto-submits a form to NS’s profile-update endpoint, setting A’s homepage field to the same malicious image (or equivalent script). For example, where the paper omits endpoint/field names:

```html
<form id="change" method="POST" action="PROFILE_UPDATE_ENDPOINT">
  <input type="hidden" name="HOMEPAGE_FIELD"
    value='&lt;img src="http://www.networksocial.com/action/friends/add?friend=20"&gt;'>
</form>
<script>document.getElementById('change').submit();</script>
```

`PROFILE_UPDATE_ENDPOINT` and `HOMEPAGE_FIELD` must be replaced by NS’s actual authenticated profile-edit interface; the prompt does not name them. HTML entity decoding gives the submitted field its literal `<img ...>` markup. A’s browser attaches A’s cookie to that update. With no CSRF checks, the server stores it; with no XSS/output-encoding defense, later profile viewers receive active content. Each logged-in viewer’s browser sends its own friend-add request to Trudy.

![CSRF and stored-XSS propagation](assets/xss.svg)

This is a CSRF initial profile change followed by persistent HTML/script injection. If the stored content also copies itself into every viewer’s profile, it becomes a self-propagating worm; replication is an optional extension, not needed to meet the stated “every visitor adds Trudy” requirement.

Defenses: CSRF tokens on profile changes; no state-changing GETs; contextual output encoding/sanitization; CSP and appropriate cookie restrictions. The example assumes the legacy vulnerable behavior specified in the paper, not every modern browser’s default SameSite configuration.

**Exam tip.** Distinguish whose cookie authenticates each step: A for the profile update, then each later viewer for that viewer’s own friend request.
'''
answers['2020–21|6(b)'] = r'''
**ElGamal signatures are different from ElGamal encryption.** Choose prime p, generator g, private x and public y=$g^{x}$ mod p. Hash M to an integer h. Choose a fresh secret k with gcd(k,p−1)=1.

$$
\begin{aligned}r&=g^k\bmod p,\\s&=(h-xr)k^{-1}\bmod(p-1),\\\mathrm{signature}&=(r,s),\\\mathrm{verify:}\quad g^h&\equiv y^r r^s\pmod p.\end{aligned}
$$

Correctness follows because $xr+ks\equiv h\pmod{p-1}$, hence $y^rr^s=g^{xr+ks}\equiv g^h\pmod p$.

**Nonce reuse.** Two signatures with the same k have the same r. Let h1/h2 be message hashes:

$$
\begin{aligned}s_1k&\equiv h_1-xr\pmod{p-1},\\s_2k&\equiv h_2-xr\pmod{p-1},\\(s_1-s_2)k&\equiv h_1-h_2\pmod{p-1}.\end{aligned}
$$

Solve this linear congruence for k, then solve $rx\equiv h_1-s_1k\pmod{p-1}$ for x. Check candidates using $g^k=r$ and $g^x=y$. Because p−1 is composite, the coefficients may not be invertible: do **not** blindly divide as in a prime-order DSA formula.

**Worked small example.** Let p=23, g=5, x=6, y=8, and reused k=7, so r=17. For h1=13 and h2=3, signatures have s1=3 and s2=11. Subtraction gives:

$$
\begin{aligned}14k&\equiv10\pmod{22},\\7k&\equiv5\pmod{11}\quad\Longrightarrow\quad k\equiv7\pmod{11}.\end{aligned}
$$

Candidates modulo 22 are 7 and 18. k=18 is not coprime to 22 and also fails the r check; k=7 remains. Then $17x\equiv13-3\cdot7\equiv14\pmod{22}$, giving x=6 and the public-key check $5^{6}$≡8. The attacker has recovered the long-term signing key and can forge signatures.

**Exam tip.** Show both congruences and explain why k is secret and fresh. State gcd conditions before taking inverses.
'''
answers['2020–21|7(a)'] = r'''
Let plaintext blocks be n-dimensional column vectors over Z26. Caesar adds the same shift s to every component, then Hill multiplies by invertible K:

$$
\begin{aligned}C&=K(P+s\mathbf1)=KP+b\pmod{26},\\b&=sK\mathbf1.\end{aligned}
$$

The result is an **affine transformation**, not a strong nonlinear substitution–permutation cipher. The linear structure is exploitable.

**Chosen-plaintext attack.** Ask for the encryption of the zero vector P=0. Its result C0=b. For each basis vector ei (a single 1 in position i), get Ci. Then:

$$
C_i-C_0=Ke_i=\text{column }i\text{ of }K.
$$

After n+1 chosen blocks the attacker knows K and b, computes $K^{-1}$ and decrypts every block using $P=K^{-1}(C-b)\pmod{26}$. It is unnecessary to recover the original Caesar shift separately.

**Known-plaintext version.** Subtract a reference pair: $C_j-C_0=K(P_j-P_0)$. If n chosen differences form an invertible matrix X over Z26, form the corresponding Y and compute K=$YX^{-1}$. Then recover b=C0−KP0. Since Z26 is not a field, explicitly require an invertible difference matrix; arbitrary sample blocks do not guarantee one.

**Exam tip.** Confusion/diffusion terminology does not prove resistance to algebraic attacks. Exhibit the affine equation and an actual recovery procedure.
'''
answers['2020–21|7(b)'] = r'''
**Correction to the earlier index:** the scanned paper marks Cookie 2 **non-secure**, not secure. Its explicit Domain is docs.example.com and Path is /test. Cookies 1 and 3 have Domain=example.com (a leading dot is immaterial here), are Secure, and have paths / and /print respectively.

| Requested URL | C1 main | C2 test | C3 print |
|---|---:|---:|---:|
| (i) http://print.example.com/print | 0 | 0 | 0 |
| (ii) https://docs.example.com/ | 1 | 0 | 0 |
| (iii) http://example.com/test | 0 | 0 | 0 |
| (iv) https://example.com/print/test | 1 | 0 | 1 |
| (v) https://docs.example.com/test/print | 1 | 1 | 0 |

(i): C1/C3 fail HTTPS and C2 fails domain. (ii): C1 matches; neither /test nor /print matches root path /. (iii): C2 would permit HTTP but **example.com is not docs.example.com**, so it is absent; the Secure cookies fail. (iv): C1/C3 match; C2’s domain does not. (v): C1/C2 match; /print is not a prefix of /test/print.

All cookies have the same name `file`. When two match, both values may be transmitted; the question asks which cookies qualify, not which one “wins.” Do not infer a safe server-side choice from the name alone. The Secure correction does not change any of these five matrix cells, but it matters for hypothetical HTTP requests to docs.example.com/test.

**Exam tip.** Check flags from the scan and test domain/path independently. A child-domain cookie is not sent upward to its parent domain.
'''
answers['2020–21|8(b)'] = r'''
**The b/2 bound concerns collision finding**, not preimage finding. An ideal b-bit hash has N=$2^{b}$ possible outputs. After q independent random outputs, the probability of no collision is:

$$
\begin{aligned}\Pr[\text{no collision}]&=\prod_{i=0}^{q-1}\left(1-\frac{i}{N}\right)\\&\approx\exp\!\left(-\frac{q(q-1)}{2N}\right),\\\Pr[\text{collision}]&\approx1-\exp\!\left(-\frac{q(q-1)}{2N}\right).\end{aligned}
$$

For a constant collision probability, the exponent must be of order 1, so $q^{2}$/N is of order 1:

$$
q=\Theta(\sqrt N)=\Theta(2^{b/2}).
$$

At 50% probability, solve q(q−1)/(2N)≈ln 2, giving $q\approx\sqrt{2\ln2}\,2^{b/2}\approx1.177\,2^{b/2}$. Therefore a generic collision attack takes about $2^{b/2}$ work, giving b/2 bits of collision security. SHA-256’s ideal generic collision target is approximately 128-bit work, while an ideal specified-output preimage target is approximately 256-bit work.

**Exam tip.** Name the attack goal. It is incorrect to say all attacks on a b-bit hash cost only $2^{b/2}$.
'''
answers['2020–21|8(c)'] = r'''
**The session cookie is an independent credential.** Updating a password changes the condition for obtaining a new session; it does not automatically invalidate tokens already accepted by the server. An attacker who stole a valid year-long session can continue authenticating without knowing the new password.

Example: a user logs in on a shared computer, forgets to log out, then changes their password elsewhere. Unless the old session is revoked, that browser remains logged in. The same issue applies to a token stolen through XSS or a compromised device.

**Required repair:** invalidate all old sessions for that account on a security-sensitive password reset/change, then optionally issue a fresh session to the user who completed reauthentication. Deleting or replacing only the current browser’s cookie is insufficient; the server must reject copies of old tokens.

For opaque session IDs, delete/revoke the account’s session-table entries. For signed/JWT tokens, enforce short expiry and a revocation/version mechanism, such as a per-user session epoch included in the signed token and checked against the current server-side epoch. **An epoch check requires state**; it is not fully stateless revocation. A token’s own signature and expiration cannot learn that a password changed elsewhere.

**Exam tip.** Separate browser cookie removal, server-side invalidation and fresh-token issuance. Revocation is the key part of the answer.
'''
