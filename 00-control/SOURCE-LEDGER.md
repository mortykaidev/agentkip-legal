# Source Ledger

Last primary-source verification: **2026-07-15**

This ledger is research provenance, not a substitute for legal advice. Use primary government,
platform, and vendor sources. Before approving a material change, re-open every source marked
`release` because platform rules and service terms change.

## Law, enforcement, and risk guidance

| ID | Authority | Primary URL | Used for | Refresh |
|---|---|---|---|---|
| `US-ESIGN-7001` | U.S. House Office of the Law Revision Counsel | https://uscode.house.gov/view.xhtml?req=%28title%3A15+section%3A7001+edition%3Aprelim%29 | Electronic records, consumer disclosure, retention, and effect of signatures | Material change |
| `MI-UETA-450.838` | Michigan Legislature | https://www.legislature.mi.gov/documents/mcl/pdf/mcl-Act-305-of-2000.pdf | Retainable electronic records and Michigan electronic transactions | Material change |
| `MI-CONSUMER` | Michigan Department of Attorney General | https://www.michigan.gov/ag/consumer-protection | Michigan consumer-protection and truthful-disclosure baseline | Release |
| `MI-CONSUMER-LAWS` | Michigan Consumer Protection Team | https://www.michigan.gov/consumerprotection/protect-yourself/michigan-consumer-laws | Official index to Michigan consumer statutes | Release |
| `FTC-AI` | U.S. Federal Trade Commission | https://www.ftc.gov/industry/technology/artificial-intelligence | Truthful, substantiated AI and automation representations | Release |
| `FTC-AI-COMPLY` | U.S. Federal Trade Commission | https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes | Enforcement examples for deceptive or unsupported AI claims | Material change |
| `FTC-VOICE-DATA` | U.S. Federal Trade Commission | https://www.ftc.gov/business-guidance/blog/2023/06/hey-alexa-what-are-you-doing-my-data | Data retention, deletion, and representation risks for voice/AI products | Material change |
| `NIST-AI-RMF` | National Institute of Standards and Technology | https://www.nist.gov/itl/ai-risk-management-framework | Voluntary AI risk-governance vocabulary; not represented as law | Annual |

## Apple distribution

| ID | Authority | Primary URL | Used for | Refresh |
|---|---|---|---|---|
| `APPLE-REVIEW` | Apple Developer | https://developer.apple.com/app-store/review/guidelines/ | Privacy policy access, third-party AI consent, accurate metadata, TestFlight, account and safety requirements | Every submission |
| `APPLE-DELETE` | Apple Developer | https://developer.apple.com/support/offering-account-deletion-in-your-app/ | In-app deletion for apps that support account creation | Every submission |
| `APPLE-PRIVACY` | Apple Developer | https://developer.apple.com/app-store/app-privacy-details/ | App Privacy data-type and purpose worksheet | Every submission |
| `APPLE-MANIFEST` | Apple Developer | https://developer.apple.com/documentation/bundleresources/privacy-manifest-files | Privacy manifest structure and bundle requirements | Every SDK/bundle change |
| `APPLE-STANDARD-EULA` | Apple Legal | https://www.apple.com/legal/internet-services/itunes/dev/stdeula/ | Relationship between Apple's standard EULA and supplemental service Terms | Release |

## GitHub authorization and connected content

| ID | Authority | Primary URL | Used for | Refresh |
|---|---|---|---|---|
| `GITHUB-PERMISSIONS` | GitHub Docs | https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app | Least-privilege installation and repository permission design | Integration change |
| `GITHUB-AUTHORIZATION` | GitHub Docs | https://docs.github.com/en/apps/using-github-apps/authorizing-github-apps | GitHub App/user authorization and revocation flow | Integration change |
| `GITHUB-TOS` | GitHub | https://docs.github.com/en/site-policy/github-terms/github-terms-of-service | User responsibility for connected repositories and service terms | Release |

## Declared website and service providers

Provider entries establish which official notices must be reviewed; they do not prove which
deployment, data location, retention period, or contractual option is active.

| ID | Provider | Primary URL | Product evidence |
|---|---|---|---|
| `CLERK-PRIVACY` | Clerk | https://clerk.com/legal/privacy | Website dependency and server authentication code |
| `CLERK-DPA` | Clerk | https://clerk.com/legal/dpa | Processor terms and subprocessor review |
| `NEON-PRIVACY` | Neon | https://neon.tech/privacy-policy | Neon/Drizzle website storage code |
| `NEON-DPA` | Neon | https://neon.tech/dpa | Processor terms and subprocessor review |
| `STRIPE-PRIVACY` | Stripe | https://stripe.com/privacy | Billing/customer/entitlement implementation |
| `STRIPE-SERVICES` | Stripe | https://stripe.com/legal/ssa | Services agreement and merchant responsibilities |
| `VERCEL-PRIVACY` | Vercel | https://vercel.com/legal/privacy-policy | Website hosting and Blob dependency |
| `VERCEL-DPA` | Vercel | https://vercel.com/legal/dpa | Processor and transfer review |
| `OPENAI-PRIVACY` | OpenAI | https://openai.com/policies/privacy-policy/ | Optional user-selected model provider disclosure |
| `OPENAI-BUSINESS-TERMS` | OpenAI | https://openai.com/policies/business-terms/ | Optional API provider terms |
| `ANTHROPIC-PRIVACY` | Anthropic | https://www.anthropic.com/legal/privacy | Optional user-selected model provider disclosure |
| `ANTHROPIC-COMMERCIAL-TERMS` | Anthropic | https://www.anthropic.com/legal/commercial-terms | Optional API provider terms |

## Source-use rules

- Cite only what the source supports; do not convert guidance into a false statement of law.
- Record the access date and relevant section in the drafting PR when a source materially changes
  text or product requirements.
- Vendor policies support disclosure wording but never establish the product's actual runtime
  configuration; deployment evidence belongs in `CLAIM-TO-CODE-MATRIX.md` and the provider register.
- If an automated link check is blocked by a provider, manually open the canonical URL and record
  the check in the PR. Do not replace it with an unaffiliated summary.
