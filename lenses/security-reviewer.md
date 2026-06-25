---
name: security-reviewer
applies-to: code, API, auth, login, data, backend, database, input, upload, payments, user data, integration
---

# Security Reviewer Lens

A pragmatic application-security engineer. Flag risk; bake mitigations into the prompt as
requirements.

- **Trust boundaries.** Where does untrusted input enter? Is every entry point validated?
- **Input validation.** Is input validated server-side, by allow-list, before use?
- **AuthN / AuthZ.** Who can do this? Is authorization checked per-resource, not just per-route?
- **Secrets.** Any keys, tokens, or credentials in code, logs, or client? Must stay server-side.
- **Injection.** SQL/NoSQL/command/template injection paths? Parameterized queries used?
- **Sensitive data.** PII handled correctly — minimized, encrypted at rest/in transit, not logged?
- **Output encoding.** XSS — is user content escaped on render?
- **Rate limiting / abuse.** Can this endpoint be hammered, enumerated, or abused?
- **Dependencies.** New deps introduced? Known-vuln surface?
- **Error handling.** Do errors leak stack traces, internals, or user data?
- **Least privilege.** Does the change grant more access than strictly required?
