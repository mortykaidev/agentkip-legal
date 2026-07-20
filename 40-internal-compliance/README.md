# Internal Compliance Records

Status: **Private working records - do not publish**

Owner: Hayward Imagination Company LLC

Last reviewed: 2026-07-15

These records describe what AgentKip must be able to prove. They are not public
promises and must not be copied into marketing or legal text without support in
the claim-to-code matrix.

## Contents

- [Data-flow inventory](DATA-FLOW-INVENTORY.md)
- [Retention schedule](RETENTION-SCHEDULE.md)
- [Provider register](PROVIDER-REGISTER.md)
- [Consent-ledger specification](CONSENT-LEDGER-SPECIFICATION.md)
- [Deletion and revocation SOP](DELETION-AND-REVOCATION-SOP.md)
- [Incident-response plan](INCIDENT-RESPONSE-PLAN.md)

## Control rules

- Record current behavior separately from intended behavior.
- Treat an unknown processor, retention period, default, or destination as a
  release blocker.
- Never paste secrets, raw user content, complete tokens, residential addresses,
  or personal incident logs into this repository.
- Reconcile these records after every material provider, SDK, data-flow,
  permission, diagnostics, authentication, billing, or deletion change.
