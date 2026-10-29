"""Sec B component found while auditing both printed sections of each paper."""
answers={}
answers['2023–24|3(a)']=r'''
**HTTPS plus a firewall/NIDS cannot always prevent reflected XSS.** The vulnerable application can copy attacker-controlled input into a response as executable browser content. TLS can then deliver that response faithfully to the victim; it does not make the response safe. The script executes with the vulnerable page's origin and can perform actions available to that origin.

A network IDS outside TLS termination normally cannot inspect the encrypted HTTP payload. Inspection at or after termination improves visibility, but a generic filtering rule still does not guarantee correct interpretation of every application output context. A passive NIDS may only alert rather than block anything.

The primary repair is **safe rendering at the application**: apply encoding appropriate to the HTML, attribute, URL or script context; use safe templating and DOM APIs; and avoid interpreting untrusted input as executable markup or script. If rich HTML is genuinely required, use a suitable sanitizer with an explicit policy. A restrictive Content Security Policy can reduce impact as an additional layer. Neither the same-origin policy nor transport encryption repairs an injection already executing in the trusted page's origin.

**Exam tip.** Explain the layer boundary: authenticated transport and packet filtering do not guarantee that the application's response is safe to execute.
'''
