# United States State-Law Assessment

Status: **ACTIVE LAUNCH ASSESSMENT / BLOCKED**

Launch posture: United States, adults-only beta

Last source check: 2026-07-15

United States availability does not create one uniform privacy rule. This file is
a gate to a current state-by-state applicability matrix; it is not a claim that
AgentKip is below every threshold or exempt from every obligation.

## Applicability matrix required before launch

Create one row for every state and the District of Columbia, using current
statutes, regulations, effective dates, thresholds, exemptions, and regulator
guidance. At minimum record:

| Field | Required decision |
|---|---|
| Law/effective date | Current comprehensive, health, biometric, child, AI, breach, consumer, and data-broker rules |
| Applicability | Revenue/data thresholds, targeting, business role, exemptions, and look-back period |
| Rights | Access, correction, deletion, portability, opt-out, appeal, authorized agent, and response timing |
| Sensitive data | Definition, consent/authorization, geofencing, health, biometric, precise location, children |
| Sale/share/targeted ads | Definitions and whether current or planned behavior qualifies |
| Universal opt-out | Signals and technical/notice requirements, including current recognized mechanisms |
| Profiling/AI | Opt-out, assessment, notice, appeal, and consequential-decision requirements |
| Assessments/contracts | Data protection/risk assessment, processor agreement, retention/security duties |
| Enforcement | Agency, cure period if any, penalties, and private right of action if any |
| Evidence | Official source, reviewer, date, product/configuration evidence |

Do not copy a static blog list. State coverage and regulations are changing, and
some obligations apply even below comprehensive-privacy-law thresholds.

## Product controls to verify

- [ ] No sale, targeted advertising, cross-context behavioral advertising, or
      data-broker activity occurs in code, SDKs, providers, or contracts.
- [ ] Global Privacy Control and other legally recognized universal opt-out
      mechanisms are detected and honored where required; the privacy notice
      explains the behavior.
- [ ] Sensitive-data and consumer-health scope is assessed for free-form prompts,
      voice, images/files, diagnostics, device identifiers, model outputs, and
      integrations.
- [ ] AI-provider consent is specific and separate from Terms acceptance.
- [ ] Access, correction, deletion, export, appeal, consent withdrawal, and
      authorized-agent workflows are implemented where applicable.
- [ ] State-specific response timing, verification, recordkeeping, and appeal
      notices are operational.
- [ ] Data protection/risk assessments cover AI inference, profiling, provider
      transfers, sensitive data, diagnostics, and autonomous tool actions.
- [ ] Processor/provider contracts contain required instructions, confidentiality,
      security, deletion/return, assistance, audit, and subprocessor terms where
      applicable.
- [ ] Retention is purpose-limited and technically enforced.

## California and Colorado minimum source checks

- [ ] Evaluate CCPA/CPRA applicability using the current monetary and data
      thresholds, definitions, regulations, and exemptions.
- [ ] Verify notices at collection, privacy policy, rights methods, sensitive-data
      controls, service-provider/contractor terms, and opt-out preference signals
      if applicable.
- [ ] Evaluate whether California's current cybersecurity audit, risk assessment,
      or automated decisionmaking regulations apply.
- [ ] Evaluate Colorado Privacy Act applicability, consent for sensitive data,
      assessments, rights/appeals, and current universal opt-out requirements.
- [ ] Recheck both agencies' final rules at each release; proposals are not treated
      as operative requirements.

## Other state-law layers

- [ ] State breach-notification laws and incident contacts.
- [ ] Unfair/deceptive-practices and consumer-protection laws, including Michigan.
- [ ] Biometric identifiers/information and voiceprint/face/hand data rules.
- [ ] Consumer-health data laws and geofencing restrictions.
- [ ] Call/audio recording consent laws for diagnostics or support.
- [ ] Automatic-renewal, subscription, pricing, refund, and cancellation laws if
      payments are enabled.
- [ ] Electronic-signature/record retention and accessible-copy requirements.
- [ ] Children's and teen rules notwithstanding the product's 18+ restriction;
      test that underage users are not knowingly admitted.

## Current blockers

1. A dated 51-jurisdiction applicability matrix does not exist.
2. Company metrics needed to evaluate thresholds are not recorded.
3. Rights, deletion, appeals, retention, diagnostics, and provider evidence are
   incomplete.
4. Universal opt-out and sensitive-data handling are not tested.
5. State breach, biometric, health-data, AI/profiling, and subscription overlays
   are not fully assessed.

Official starting points:

- [California Privacy Protection Agency laws and regulations](https://cppa.ca.gov/regulations/)
- [Colorado Attorney General privacy resources](https://coag.gov/resources/colorado-privacy-act/)
- [Colorado universal opt-out guidance](https://coag.gov/opt-out/)
- [Michigan Consumer Protection](https://www.michigan.gov/ag/consumer-protection)
