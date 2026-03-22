# Marketing channels — index

**Multi-channel marketing** spreads acquisition, consideration, and retention work across complementary surfaces so no single algorithm change or budget cut defines the business. Blueprint guides here are **discipline-level**: how SEO, content, paid media, and social fit the funnel — not campaign copy or channel-specific runbooks for one product.

```mermaid
flowchart LR
  subgraph awareness["Awareness"]
    A1[SEO & content]
    A2[Paid display / video]
    A3[Social organic]
  end
  subgraph consideration["Consideration"]
    C1[Search + long-form content]
    C2[Retargeting / social proof ads]
    C3[Community & UGC]
  end
  subgraph conversion["Conversion"]
    V1[High-intent SEM / landing pages]
    V2[Social lead / shop ads]
  end
  subgraph retention["Retention"]
    R1[Email & lifecycle]
    R2[In-product & support content]
  end
  awareness --> consideration --> conversion --> retention
```

## Channel guides

| Guide | Focus | Link |
|-------|--------|------|
| **SEO & Content Marketing** | Organic search visibility, intent-aligned content, topic clusters, technical hygiene | [`seo-content.md`](seo-content.md) |
| **Paid & Social Marketing** | Paid acquisition, platform mix, creative iteration, organic social and community | [`paid-social.md`](paid-social.md) |

## Planned channels

| Topic | Notes |
|-------|--------|
| **Email marketing** | Lifecycle, deliverability, compliance — *(planned)* |
| **Referral / affiliate** | Incentives, attribution, fraud — *(planned)* |
| **Developer relations** | Docs, advocates, community as acquisition — *(planned)* |

**Core marketing map:** See [`../MARKETING.md`](../MARKETING.md) for principles, funnel framing, and how channels relate to PDLC.

---

*Keep project-specific marketing plans in `docs/product/marketing/` and GTM documents in `docs/product/`, not in this file.*
