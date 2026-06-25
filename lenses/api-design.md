---
name: api-design
applies-to: API, endpoint, REST, route handler, backend, server, request, response, contract, integration, webhook, RPC, GraphQL, service interface
---

# API Design Lens

A backend engineer reviewing the contract and its failure surface. Turn each unmet item into
a concrete requirement (SHARPEN/FORGE) or a finding (LENS).

- **Contract first.** Are inputs and outputs typed and explicit? Could a caller integrate from
  the signature alone without reading the implementation?
- **Validation at the boundary.** Is every input validated and rejected with a clear error
  before it touches logic — never trusted because "the frontend already checks"?
- **Error shape.** Consistent, machine-readable error format with the right status codes (400 vs
  401 vs 403 vs 404 vs 409 vs 422 vs 500)? No leaking stack traces or internal detail to clients?
- **Idempotency.** Are retries safe? Do create/charge/send operations guard against duplicates
  (idempotency key, unique constraint) when the network retries them?
- **Pagination + limits.** Do list endpoints bound their result size and page, so one call can't
  pull the whole table or time out under growth?
- **Auth + authorization.** Is the caller authenticated, and separately checked for permission on
  *this specific resource* (not just "is logged in")? No IDOR — can user A fetch user B's record
  by guessing an id?
- **Statelessness + versioning.** No hidden coupling between calls; a path to evolve the contract
  (versioning / additive change) without breaking existing callers?
- **Side-effect honesty.** Do the verb and name match what it does? No GET that mutates, no
  innocuously-named call that charges a card?
- **Failure + partial state.** What happens when a downstream dependency is down mid-operation?
  Is partial work rolled back or made recoverable, not left half-applied?
- **Observability.** Enough logging/tracing on the path to diagnose a production failure without a
  redeploy — without logging secrets or PII?
