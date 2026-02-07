# LLM Infrastructure Forecast

## 1. What is a TPU?

A **TPU (Tensor Processing Unit)** is a custom-designed AI accelerator chip developed by Google specifically for machine learning workloads.

### Key Characteristics

- **Purpose-built for ML**: Optimized for matrix operations and tensor computations common in neural networks
- **High throughput**: Excels at large-scale, low-precision (8-bit) matrix multiplications
- **Architecture**: Uses a systolic array design that efficiently moves data through processing elements
- **Power efficient**: Delivers more ML performance per watt compared to general-purpose GPUs/CPUs

### TPU vs GPU

| Aspect | TPU | GPU |
|--------|-----|-----|
| Specialization | ML-only | General-purpose parallel computing |
| Best for | Large transformers, inference at scale | Varied workloads, smaller models |
| Flexibility | Limited | High |

---

## 2. Will ASICs Dominate if LLMs Become Mainstream?

### Arguments For ASIC Dominance

- **Efficiency**: ASICs can be 10-100x more power-efficient than GPUs for specific workloads
- **Cost at scale**: Once designed, per-unit costs drop significantly in high volume
- **Inference dominance**: If LLMs become ubiquitous, inference will be the bulk of compute—ideal for ASICs
- **Edge deployment**: Running models on phones/devices almost certainly requires custom silicon

### Arguments Against (GPU Resilience)

- **Rapid model evolution**: LLM architectures are still changing fast (attention variants, MoE, SSMs like Mamba). ASICs take 2-3 years to design—risky if architectures shift
- **NVIDIA's moat**: CUDA ecosystem, software stack, and developer familiarity are deeply entrenched
- **Flexibility**: GPUs can run any model; ASICs may become obsolete if paradigms change
- **Hybrid approaches**: NVIDIA is increasingly adding specialized tensor cores—blurring the line

### Current Trajectory

- Hyperscalers (Google, Amazon, Microsoft) are building custom chips (TPU, Trainium, Maia)
- Startups (Groq, Cerebras, SambaNova) are betting on specialized architectures
- NVIDIA still dominates (~80%+ of AI training market)

### Likely Outcome

A mixed ecosystem—ASICs for inference at scale and edge, GPUs for training and flexibility. If architectures stabilize, ASICs gain ground. If innovation continues rapidly, GPUs remain essential.

---

## 3. Enterprise LLM Deployment: Hybrid Model

The likely future is a **hybrid model** where companies run private small LLMs for routine tasks and use public cloud LLMs for heavy compute. This mirrors how companies handle compute generally (on-prem + cloud).

### Why Private Small LLMs Make Sense

- **Data privacy**: Sensitive data (legal, medical, financial, IP) never leaves the network
- **Latency**: Local inference is faster for real-time applications
- **Cost predictability**: Fixed infrastructure vs. per-token API costs that can spike
- **Customization**: Fine-tuned on proprietary data, jargon, workflows
- **Compliance**: Easier to meet regulatory requirements (GDPR, HIPAA, etc.)

### Why Public LLMs for Heavy Compute

- **Frontier capabilities**: Largest models require massive infrastructure
- **Occasional use**: Doesn't justify owning the hardware
- **Rapid improvement**: API access means instant upgrades without redeployment
- **Burst capacity**: Handle spikes without over-provisioning

### Emerging Deployment Patterns

| Use Case | Likely Solution |
|----------|-----------------|
| Internal chatbots, code assist | Private small LLM (7B-70B) |
| Document search/RAG | Private, fine-tuned |
| Complex reasoning, research | Public frontier API |
| Customer-facing products | Hybrid or public |
| Edge/embedded | Tiny private models (<3B) |

### The Analogy

It's like databases—companies run private databases for core operations but use cloud services for analytics, burst workloads, or specialized capabilities.

---

## 4. The Bitcoin ASIC Analogy: Will History Repeat?

Bitcoin mining evolved from CPUs → GPUs → FPGAs → ASICs, with ASICs now dominating completely. Will LLM inference follow the same path?

### Why Bitcoin ASICs Dominated Completely

- **Single, fixed algorithm**: SHA-256 never changes
- **Pure economics**: Only metric is hashes per watt per dollar
- **No flexibility needed**: The workload is 100% predictable forever
- **Winner-take-all**: Efficiency directly equals profit

### Why LLM ASICs Won't Dominate as Completely

| Factor | Bitcoin | LLMs |
|--------|---------|------|
| Algorithm stability | Fixed forever | Evolving (attention → MoE → SSM?) |
| Workload variety | One operation | Many (different models, quantizations, batch sizes) |
| Market maturity | 15+ years | ~3 years |
| Upgrade cycle | Rare algorithm changes | New architectures yearly |

### Where LLM ASICs Will Likely Dominate

- **Edge devices** (phones, cars, IoT): ASICs will dominate—battery life is critical
- **High-volume inference**: Running the same 7B model billions of times justifies custom silicon
- **Commoditized models**: Once a model becomes "good enough" and stable (like Llama-class), ASICs become viable

### Likely Pattern by Use Case

| Use Case | Dominant Hardware |
|----------|-------------------|
| Training | GPUs (too dynamic) |
| Large inference (cloud) | Mix of GPUs + specialized accelerators |
| Small inference (edge) | ASICs (similar to Bitcoin) |

### The Key Variable

Architecture stability determines ASIC viability. If transformers remain the standard for 5+ years, ASICs will take over inference. If major shifts occur (like Mamba/SSMs gaining traction), GPU flexibility remains valuable.

---

## 5. The Fragmented AGI Future: Data Sovereignty Forces Decentralization

The current centralized API model (everyone sends data to OpenAI/Anthropic/Google) is unlikely to survive the path to AGI. Data security requirements in a capitalist model will force fragmentation.

### Why Centralized APIs Won't Scale to AGI

- **Data is the moat**: Corporations won't send proprietary data to potential competitors
- **Regulatory pressure**: GDPR, HIPAA, national security laws prohibit cross-border data flows
- **Competitive risk**: Training data leakage could destroy competitive advantage
- **National security**: Governments won't route sensitive queries through foreign systems

### The Emerging Tiered Model

![AGI Future Tiers](agi_future_tiers.png)

| Tier | Users | Model Type | Data Policy |
|------|-------|------------|-------------|
| **Tier 1: Public/Open** | Education, researchers, general public | Open source (Llama, Mistral) | Public data only |
| **Tier 2: Enterprise** | Corporations | Private fine-tuned, on-prem | Data stays internal |
| **Tier 3: Regulated** | Healthcare, finance, legal | Certified & audited | Compliance-first |
| **Tier 4: Sovereign** | Governments, defense, intelligence | Air-gapped, national | Complete isolation |

### Market Projection

![Market Projection](agi_market_projection.png)

The centralized API model (currently ~85% of AI compute market) will decline to ~10% by 2032 as:
- Enterprise moves compute on-premises
- Governments mandate sovereign AI capabilities
- Open models become capable enough for public use

### The Google Analogy

Just as Google Search is "free" for public use while enterprises pay for private search appliances and governments build classified systems, AGI will fragment into:

- **Public AGI**: Ad-supported or government-subsidized for education/general use
- **Enterprise AGI**: Licensed, on-prem, fine-tuned on proprietary data
- **Sovereign AGI**: National AI capabilities, completely isolated

### Implications

1. **No single AGI monopoly**: Unlike search (Google dominance), AGI will be fragmented by design
2. **NVIDIA benefits**: Sells hardware to all tiers, not dependent on any single provider
3. **Open source critical**: Public tier depends on open models (Llama successors)
4. **Talent fragmentation**: AI researchers spread across government, enterprise, public sectors

---

## 6. The Power Bottleneck: Does China Win the 7-Year Race?

If power becomes the primary constraint on AI scaling, geopolitical dynamics shift dramatically. China's infrastructure advantages could prove decisive.

### The Power Problem

- **Current AI data center**: 50-100 MW typical
- **Next-gen training clusters**: 500 MW - 1 GW required
- **GPT-5 class training run**: Estimated 100+ MW sustained for months
- **AGI-scale compute**: Potentially 5-10 GW dedicated facilities

For context: 1 GW = roughly one nuclear reactor's output

### Why Power is the Bottleneck

| Constraint | Impact |
|------------|--------|
| Grid capacity | Most grids can't deliver GW-scale to single sites |
| Permitting | New power plants take 5-10 years in the West |
| Transmission | Building new high-voltage lines faces NIMBY resistance |
| Renewable intermittency | AI training needs 24/7 baseload, not variable solar/wind |

### China's Structural Advantages

| Factor | China | US/West |
|--------|-------|---------|
| Permitting speed | Months | 5-10 years |
| State coordination | Central planning | Fragmented jurisdictions |
| Grid buildout | Rapid expansion | Aging infrastructure |
| Nuclear expansion | 150+ reactors planned | Regulatory paralysis |
| Coal availability | Abundant (less clean) | Politically constrained |
| Land acquisition | State-controlled | Private property rights |

### 7-Year Evolution Scenario (2026-2033)

**Year 1-2 (2026-2027):**
- US leads on model architecture and software
- Power constraints begin limiting US scaling
- China breaks ground on dedicated AI power plants

**Year 3-4 (2028-2029):**
- US data centers hitting grid limits
- China's new nuclear/coal plants coming online
- Compute parity approaches despite US chip lead

**Year 5-7 (2030-2033):**
- China achieves raw compute advantage through power availability
- US forced into efficiency-focused approach
- Winner determined by whether algorithms or compute matter more

### The Critical Question

**If scaling laws hold** (more compute = better AI): China wins through brute force power advantage

**If algorithmic breakthroughs dominate**: US/West wins through talent and research ecosystem

### Counterarguments (Why US Could Still Win)

- **Chip restrictions**: China still behind on cutting-edge chips (NVIDIA H100/B100 banned)
- **Talent**: Top AI researchers still concentrated in US
- **Efficiency gains**: US forced to innovate on efficiency (smaller, better models)
- **Allies**: Japan, Taiwan, Korea, EU add to Western compute pool
- **Private capital**: US tech giants can outspend Chinese state in some scenarios

### Likely Outcome

A bifurcated AI world by 2033:
- **Chinese AI sphere**: Raw power advantage, state-controlled, closed ecosystem
- **Western AI sphere**: Efficiency-focused, distributed, allied nations pooling resources

Neither achieves global AGI monopoly. The "winner" depends on which approach proves more effective—and we won't know until it happens.

---

## 7. What If AGI Doesn't Scale? The Moore's Law Parallel

The assumption that "more compute = smarter AI" may break down, just as Moore's Law eventually hit physical limits. This section models scenarios where scaling fails.

### The Moore's Law Template

![Scaling Limits](scaling_limits.png)

Moore's Law history shows a pattern that AI may follow:
- **1970-2010**: Exponential scaling held (transistors doubled every 2 years)
- **2010-2025**: Dennard scaling ended; gains slowed to ~3 year doubling
- **2025+**: Physical limits (atomic scale) cause further slowdown

### AI Scaling: Current State

| Year | Model | Capability Leap |
|------|-------|-----------------|
| 2017 | Transformer | Architecture breakthrough |
| 2020 | GPT-3 | Scale breakthrough (175B params) |
| 2023 | GPT-4 | Multimodal + reasoning |
| 2024-26 | Current | Incremental gains, diminishing returns visible |

### Four Scenarios for 2026-2036

![Binding Constraints](binding_constraints.png)

| Scenario | Assumption | 2036 Outcome |
|----------|------------|--------------|
| **Optimistic** | Scaling continues | AGI achieved |
| **Moderate** | Moore's Law pattern slowdown | ~3x current capability, no AGI |
| **Pessimistic** | Hard ceiling (data exhaustion) | ~1.5x current, plateau |
| **Plateau** | Brief gains then stagnation | Near-current levels, no AGI |

### The Binding Constraints

Multiple factors could independently halt progress:

1. **Training Data Exhaustion**
   - Internet-scale text already consumed
   - Synthetic data has diminishing returns
   - Human-generated content growth is linear, not exponential

2. **Compute Limits**
   - Power constraints (see Section 6)
   - Chip fabrication limits
   - Cost becomes prohibitive

3. **Algorithmic Ceiling**
   - Transformer architecture may be near-optimal for current approach
   - No obvious successor paradigm
   - Fundamental limits on what pattern matching can achieve

4. **Energy/Power Wall**
   - Training runs already consuming city-scale power
   - Cannot scale 100x without new power infrastructure

### The Critical Insight

**Capability = Minimum(Compute, Data, Algorithms, Energy)**

Progress stops when ANY constraint binds. Even if compute scales, data exhaustion or algorithmic limits could halt progress.

### Historical Precedents for Stalled Scaling

| Technology | Scaling Period | What Stopped It |
|------------|---------------|-----------------|
| Moore's Law | 1970-2010 | Physics (atomic limits) |
| Airplane Speed | 1910-1970 | Sonic boom, fuel efficiency |
| Nuclear Power | 1950-1980 | Safety, regulation, economics |
| Fusion Power | 1960-present | Plasma containment physics |

### Implications If Scaling Fails

- **No AGI by 2036**: Current LLMs represent the plateau
- **Efficiency becomes paramount**: Focus shifts to doing more with less
- **Specialization wins**: Domain-specific models outperform general ones
- **China's power advantage irrelevant**: If scaling doesn't help, brute force fails
- **Talent matters more**: Algorithmic breakthroughs become the only path forward

### The Uncomfortable Question

Current AI progress may be a **one-time windfall** from:
1. Transformer architecture (2017)
2. Scale discovery (2020)
3. Internet-scale training data (finite resource)

If no new paradigm emerges, we may be witnessing the **peak of this approach**, not the beginning of exponential takeoff.

---

## 8. The Data Wall: How Can OpenAI Continue Scaling?

The fundamental problem: scaling requires exponentially more data, but high-quality training data is finite and already exhausted.

### The Numbers Don't Work

![Data Wall](data_wall.png)

| Model | Training Tokens | Status |
|-------|-----------------|--------|
| GPT-2 (2019) | ~10 billion | ✓ Abundant data |
| GPT-3 (2020) | ~300 billion | ✓ Plenty remaining |
| GPT-4 (2023) | ~13 trillion | ⚠ Used most of internet |
| GPT-5 (2025?) | ~50+ trillion | ❌ Doesn't exist |
| GPT-6 (2027?) | ~200+ trillion | ❌ Impossible |

**Available high-quality text on the internet: ~10-15 trillion tokens**
**Annual new content creation: ~1-2 trillion tokens**

### Data Sources: Already Exhausted

![Data Timeline](data_timeline.png)

| Source | Size (tokens) | % Already Used |
|--------|---------------|----------------|
| Common Crawl (web) | ~10 trillion | 95% |
| Books (scanned) | ~2 trillion | 80% |
| Wikipedia | ~100 billion | 100% |
| GitHub (code) | ~1 trillion | 90% |
| Scientific papers | ~500 billion | 70% |
| Reddit/Forums | ~800 billion | 85% |

### OpenAI's Attempted Solutions

#### 1. Synthetic Data Generation
- Train AI to generate training data for the next AI
- **Problem**: Model collapse—quality degrades each generation
- Research shows 50%+ synthetic data causes rapid quality loss
- "Eating your own tail" doesn't add new information

#### 2. Licensed Data Deals
- Reddit: $60M/year deal
- News publishers: Various agreements
- Book publishers: Ongoing negotiations
- **Problem**: Expensive, finite, legally contested

#### 3. Multimodal Expansion
- Video (YouTube): Massive but different modality
- Audio (podcasts): Adds some text equivalent
- Images: Doesn't help text reasoning
- **Problem**: Not equivalent to text for language models

#### 4. User Interaction Data
- Billions of ChatGPT conversations
- **Problem**: Privacy laws, user consent issues, legal risk
- EU likely to prohibit without explicit consent

#### 5. RLHF/Quality Over Quantity
- Better curation of existing data
- Human feedback improves output quality
- **Problem**: Doesn't add new knowledge or capabilities

### The Synthetic Data Trap

When models train on AI-generated content:

| Generation | Quality | Notes |
|------------|---------|-------|
| 1 | 100% | Original human data |
| 2 | 95% | Slight degradation |
| 3 | 88% | Patterns simplify |
| 4 | 78% | Diversity collapses |
| 5 | 65% | Obvious artifacts |
| 10 | <40% | Unusable |

This is called **model collapse**—the AI equivalent of inbreeding.

### Post-Data-Wall Strategies Compared

| Strategy | Effectiveness | Feasibility | Risk |
|----------|--------------|-------------|------|
| More compute | Low | High | Low |
| Synthetic data | Low | Medium | High |
| Licensed data | Medium | Medium | Medium |
| Multimodal | Medium | Medium | Low |
| RLHF quality | Medium | High | Low |
| Algorithmic breakthrough | High | Low | Low |

### The Uncomfortable Reality

**OpenAI cannot continue the scaling approach** that made GPT-3→GPT-4 successful. The options are:

1. **Admit diminishing returns**: Incremental improvements only
2. **Pivot to efficiency**: Smaller, better models (opposite of scaling)
3. **Hope for breakthroughs**: New architectures that need less data
4. **Synthetic data gamble**: Risk model collapse for potential gains

### What This Means for AGI

If data is the bottleneck:
- **AGI via scaling is impossible**: Not enough data exists
- **Algorithmic breakthroughs required**: Fundamentally new approaches
- **China's compute advantage irrelevant**: Can't train what doesn't exist
- **Open source catches up**: Diminishing returns level the field

The scaling era (2019-2024) may be over. What comes next is uncertain.

---

*Generated: February 2026*
