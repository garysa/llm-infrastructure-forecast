#!/usr/bin/env python3
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors

doc = SimpleDocTemplate(
    "/home/grs/Projects/adhoc/llm_forecast/llm_forecast_discussion.pdf",
    pagesize=letter,
    rightMargin=0.75*inch,
    leftMargin=0.75*inch,
    topMargin=0.75*inch,
    bottomMargin=0.75*inch
)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='H1', fontSize=18, spaceAfter=12, spaceBefore=6, textColor=colors.darkblue, fontName='Helvetica-Bold'))
styles.add(ParagraphStyle(name='H2', fontSize=14, spaceAfter=10, spaceBefore=12, textColor=colors.darkblue, fontName='Helvetica-Bold'))
styles.add(ParagraphStyle(name='H3', fontSize=12, spaceAfter=8, spaceBefore=10, fontName='Helvetica-Bold'))
styles.add(ParagraphStyle(name='Body', fontSize=10, spaceAfter=6, leading=14))
styles.add(ParagraphStyle(name='MyBullet', fontSize=10, spaceAfter=4, leftIndent=20, bulletIndent=10, leading=14))

story = []

story.append(Paragraph("LLM Infrastructure Forecast", styles['H1']))
story.append(Spacer(1, 12))

# Section 1
story.append(Paragraph("1. What is a TPU?", styles['H2']))
story.append(Paragraph("A <b>TPU (Tensor Processing Unit)</b> is a custom-designed AI accelerator chip developed by Google specifically for machine learning workloads.", styles['Body']))
story.append(Spacer(1, 6))

story.append(Paragraph("Key Characteristics", styles['H3']))
story.append(Paragraph("• <b>Purpose-built for ML</b>: Optimized for matrix operations and tensor computations common in neural networks", styles['MyBullet']))
story.append(Paragraph("• <b>High throughput</b>: Excels at large-scale, low-precision (8-bit) matrix multiplications", styles['MyBullet']))
story.append(Paragraph("• <b>Architecture</b>: Uses a systolic array design that efficiently moves data through processing elements", styles['MyBullet']))
story.append(Paragraph("• <b>Power efficient</b>: Delivers more ML performance per watt compared to general-purpose GPUs/CPUs", styles['MyBullet']))
story.append(Spacer(1, 6))

story.append(Paragraph("TPU vs GPU", styles['H3']))
data = [
    ['Aspect', 'TPU', 'GPU'],
    ['Specialization', 'ML-only', 'General-purpose parallel computing'],
    ['Best for', 'Large transformers, inference at scale', 'Varied workloads, smaller models'],
    ['Flexibility', 'Limited', 'High'],
]
t = Table(data, colWidths=[1.5*inch, 2.5*inch, 2.5*inch])
t.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
]))
story.append(t)
story.append(Spacer(1, 12))

# Section 2
story.append(Paragraph("2. Will ASICs Dominate if LLMs Become Mainstream?", styles['H2']))

story.append(Paragraph("Arguments For ASIC Dominance", styles['H3']))
story.append(Paragraph("• <b>Efficiency</b>: ASICs can be 10-100x more power-efficient than GPUs for specific workloads", styles['MyBullet']))
story.append(Paragraph("• <b>Cost at scale</b>: Once designed, per-unit costs drop significantly in high volume", styles['MyBullet']))
story.append(Paragraph("• <b>Inference dominance</b>: If LLMs become ubiquitous, inference will be the bulk of compute—ideal for ASICs", styles['MyBullet']))
story.append(Paragraph("• <b>Edge deployment</b>: Running models on phones/devices almost certainly requires custom silicon", styles['MyBullet']))
story.append(Spacer(1, 6))

story.append(Paragraph("Arguments Against (GPU Resilience)", styles['H3']))
story.append(Paragraph("• <b>Rapid model evolution</b>: LLM architectures are still changing fast. ASICs take 2-3 years to design—risky if architectures shift", styles['MyBullet']))
story.append(Paragraph("• <b>NVIDIA's moat</b>: CUDA ecosystem, software stack, and developer familiarity are deeply entrenched", styles['MyBullet']))
story.append(Paragraph("• <b>Flexibility</b>: GPUs can run any model; ASICs may become obsolete if paradigms change", styles['MyBullet']))
story.append(Paragraph("• <b>Hybrid approaches</b>: NVIDIA is adding specialized tensor cores—blurring the line", styles['MyBullet']))
story.append(Spacer(1, 6))

story.append(Paragraph("Current Trajectory", styles['H3']))
story.append(Paragraph("• Hyperscalers (Google, Amazon, Microsoft) are building custom chips (TPU, Trainium, Maia)", styles['MyBullet']))
story.append(Paragraph("• Startups (Groq, Cerebras, SambaNova) are betting on specialized architectures", styles['MyBullet']))
story.append(Paragraph("• NVIDIA still dominates (~80%+ of AI training market)", styles['MyBullet']))
story.append(Spacer(1, 6))

story.append(Paragraph("Likely Outcome", styles['H3']))
story.append(Paragraph("A mixed ecosystem—ASICs for inference at scale and edge, GPUs for training and flexibility. If architectures stabilize, ASICs gain ground. If innovation continues rapidly, GPUs remain essential.", styles['Body']))
story.append(Spacer(1, 12))

# Section 3
story.append(Paragraph("3. Enterprise LLM Deployment: Hybrid Model", styles['H2']))
story.append(Paragraph("The likely future is a <b>hybrid model</b> where companies run private small LLMs for routine tasks and use public cloud LLMs for heavy compute. This mirrors how companies handle compute generally (on-prem + cloud).", styles['Body']))
story.append(Spacer(1, 6))

story.append(Paragraph("Why Private Small LLMs Make Sense", styles['H3']))
story.append(Paragraph("• <b>Data privacy</b>: Sensitive data never leaves the network", styles['MyBullet']))
story.append(Paragraph("• <b>Latency</b>: Local inference is faster for real-time applications", styles['MyBullet']))
story.append(Paragraph("• <b>Cost predictability</b>: Fixed infrastructure vs. per-token API costs", styles['MyBullet']))
story.append(Paragraph("• <b>Customization</b>: Fine-tuned on proprietary data, jargon, workflows", styles['MyBullet']))
story.append(Paragraph("• <b>Compliance</b>: Easier to meet regulatory requirements (GDPR, HIPAA, etc.)", styles['MyBullet']))
story.append(Spacer(1, 6))

story.append(Paragraph("Why Public LLMs for Heavy Compute", styles['H3']))
story.append(Paragraph("• <b>Frontier capabilities</b>: Largest models require massive infrastructure", styles['MyBullet']))
story.append(Paragraph("• <b>Occasional use</b>: Doesn't justify owning the hardware", styles['MyBullet']))
story.append(Paragraph("• <b>Rapid improvement</b>: API access means instant upgrades", styles['MyBullet']))
story.append(Paragraph("• <b>Burst capacity</b>: Handle spikes without over-provisioning", styles['MyBullet']))
story.append(Spacer(1, 6))

story.append(Paragraph("Emerging Deployment Patterns", styles['H3']))
data2 = [
    ['Use Case', 'Likely Solution'],
    ['Internal chatbots, code assist', 'Private small LLM (7B-70B)'],
    ['Document search/RAG', 'Private, fine-tuned'],
    ['Complex reasoning, research', 'Public frontier API'],
    ['Customer-facing products', 'Hybrid or public'],
    ['Edge/embedded', 'Tiny private models (<3B)'],
]
t2 = Table(data2, colWidths=[2.5*inch, 3*inch])
t2.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
]))
story.append(t2)
story.append(Spacer(1, 12))

story.append(Paragraph("The Analogy", styles['H3']))
story.append(Paragraph("It's like databases—companies run private databases for core operations but use cloud services for analytics, burst workloads, or specialized capabilities.", styles['Body']))
story.append(Spacer(1, 12))

# Section 4
story.append(Paragraph("4. The Bitcoin ASIC Analogy: Will History Repeat?", styles['H2']))
story.append(Paragraph("Bitcoin mining evolved from CPUs → GPUs → FPGAs → ASICs, with ASICs now dominating completely. Will LLM inference follow the same path?", styles['Body']))
story.append(Spacer(1, 6))

story.append(Paragraph("Why Bitcoin ASICs Dominated Completely", styles['H3']))
story.append(Paragraph("• <b>Single, fixed algorithm</b>: SHA-256 never changes", styles['MyBullet']))
story.append(Paragraph("• <b>Pure economics</b>: Only metric is hashes per watt per dollar", styles['MyBullet']))
story.append(Paragraph("• <b>No flexibility needed</b>: The workload is 100% predictable forever", styles['MyBullet']))
story.append(Paragraph("• <b>Winner-take-all</b>: Efficiency directly equals profit", styles['MyBullet']))
story.append(Spacer(1, 6))

story.append(Paragraph("Why LLM ASICs Won't Dominate as Completely", styles['H3']))
data3 = [
    ['Factor', 'Bitcoin', 'LLMs'],
    ['Algorithm stability', 'Fixed forever', 'Evolving (attention → MoE → SSM?)'],
    ['Workload variety', 'One operation', 'Many (models, quantizations, batch sizes)'],
    ['Market maturity', '15+ years', '~3 years'],
    ['Upgrade cycle', 'Rare algorithm changes', 'New architectures yearly'],
]
t3 = Table(data3, colWidths=[1.5*inch, 2*inch, 2.5*inch])
t3.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
]))
story.append(t3)
story.append(Spacer(1, 6))

story.append(Paragraph("Where LLM ASICs Will Likely Dominate", styles['H3']))
story.append(Paragraph("• <b>Edge devices</b> (phones, cars, IoT): ASICs will dominate—battery life is critical", styles['MyBullet']))
story.append(Paragraph("• <b>High-volume inference</b>: Running the same 7B model billions of times justifies custom silicon", styles['MyBullet']))
story.append(Paragraph("• <b>Commoditized models</b>: Once a model becomes stable (like Llama-class), ASICs become viable", styles['MyBullet']))
story.append(Spacer(1, 6))

story.append(Paragraph("Likely Pattern by Use Case", styles['H3']))
data4 = [
    ['Use Case', 'Dominant Hardware'],
    ['Training', 'GPUs (too dynamic)'],
    ['Large inference (cloud)', 'Mix of GPUs + specialized accelerators'],
    ['Small inference (edge)', 'ASICs (similar to Bitcoin)'],
]
t4 = Table(data4, colWidths=[2.5*inch, 3*inch])
t4.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
]))
story.append(t4)
story.append(Spacer(1, 6))

story.append(Paragraph("The Key Variable", styles['H3']))
story.append(Paragraph("Architecture stability determines ASIC viability. If transformers remain the standard for 5+ years, ASICs will take over inference. If major shifts occur (like Mamba/SSMs gaining traction), GPU flexibility remains valuable.", styles['Body']))
story.append(Spacer(1, 12))

# Section 5
story.append(Paragraph("5. The Fragmented AGI Future: Data Sovereignty Forces Decentralization", styles['H2']))
story.append(Paragraph("The current centralized API model (everyone sends data to OpenAI/Anthropic/Google) is unlikely to survive the path to AGI. Data security requirements in a capitalist model will force fragmentation.", styles['Body']))
story.append(Spacer(1, 6))

story.append(Paragraph("Why Centralized APIs Won't Scale to AGI", styles['H3']))
story.append(Paragraph("• <b>Data is the moat</b>: Corporations won't send proprietary data to potential competitors", styles['MyBullet']))
story.append(Paragraph("• <b>Regulatory pressure</b>: GDPR, HIPAA, national security laws prohibit cross-border data flows", styles['MyBullet']))
story.append(Paragraph("• <b>Competitive risk</b>: Training data leakage could destroy competitive advantage", styles['MyBullet']))
story.append(Paragraph("• <b>National security</b>: Governments won't route sensitive queries through foreign systems", styles['MyBullet']))
story.append(Spacer(1, 6))

story.append(Paragraph("The Emerging Tiered Model", styles['H3']))
data5 = [
    ['Tier', 'Users', 'Model Type', 'Data Policy'],
    ['Tier 1: Public', 'Education, researchers, public', 'Open source (Llama, Mistral)', 'Public data only'],
    ['Tier 2: Enterprise', 'Corporations', 'Private fine-tuned, on-prem', 'Data stays internal'],
    ['Tier 3: Regulated', 'Healthcare, finance, legal', 'Certified & audited', 'Compliance-first'],
    ['Tier 4: Sovereign', 'Governments, defense', 'Air-gapped, national', 'Complete isolation'],
]
t5 = Table(data5, colWidths=[1.3*inch, 1.5*inch, 1.8*inch, 1.4*inch])
t5.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 8),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
]))
story.append(t5)
story.append(Spacer(1, 6))

story.append(Paragraph("Market Projection", styles['H3']))
story.append(Paragraph("The centralized API model (currently ~85% of AI compute market) will decline to ~10% by 2032 as enterprise moves compute on-premises, governments mandate sovereign AI capabilities, and open models become capable enough for public use.", styles['Body']))
story.append(Spacer(1, 6))

story.append(Paragraph("The Google Analogy", styles['H3']))
story.append(Paragraph("Just as Google Search is 'free' for public use while enterprises pay for private search appliances and governments build classified systems, AGI will fragment into:", styles['Body']))
story.append(Paragraph("• <b>Public AGI</b>: Ad-supported or government-subsidized for education/general use", styles['MyBullet']))
story.append(Paragraph("• <b>Enterprise AGI</b>: Licensed, on-prem, fine-tuned on proprietary data", styles['MyBullet']))
story.append(Paragraph("• <b>Sovereign AGI</b>: National AI capabilities, completely isolated", styles['MyBullet']))
story.append(Spacer(1, 6))

story.append(Paragraph("Implications", styles['H3']))
story.append(Paragraph("• <b>No single AGI monopoly</b>: Unlike search (Google dominance), AGI will be fragmented by design", styles['MyBullet']))
story.append(Paragraph("• <b>NVIDIA benefits</b>: Sells hardware to all tiers, not dependent on any single provider", styles['MyBullet']))
story.append(Paragraph("• <b>Open source critical</b>: Public tier depends on open models (Llama successors)", styles['MyBullet']))
story.append(Paragraph("• <b>Talent fragmentation</b>: AI researchers spread across government, enterprise, public sectors", styles['MyBullet']))
story.append(Spacer(1, 20))

story.append(Spacer(1, 12))

# Section 6
story.append(Paragraph("6. The Power Bottleneck: Does China Win the 7-Year Race?", styles['H2']))
story.append(Paragraph("If power becomes the primary constraint on AI scaling, geopolitical dynamics shift dramatically. China's infrastructure advantages could prove decisive.", styles['Body']))
story.append(Spacer(1, 6))

story.append(Paragraph("The Power Problem", styles['H3']))
story.append(Paragraph("• <b>Current AI data center</b>: 50-100 MW typical", styles['MyBullet']))
story.append(Paragraph("• <b>Next-gen training clusters</b>: 500 MW - 1 GW required", styles['MyBullet']))
story.append(Paragraph("• <b>GPT-5 class training</b>: Estimated 100+ MW sustained for months", styles['MyBullet']))
story.append(Paragraph("• <b>AGI-scale compute</b>: Potentially 5-10 GW dedicated facilities", styles['MyBullet']))
story.append(Spacer(1, 6))

story.append(Paragraph("China's Structural Advantages", styles['H3']))
data6 = [
    ['Factor', 'China', 'US/West'],
    ['Permitting speed', 'Months', '5-10 years'],
    ['State coordination', 'Central planning', 'Fragmented jurisdictions'],
    ['Grid buildout', 'Rapid expansion', 'Aging infrastructure'],
    ['Nuclear expansion', '150+ reactors planned', 'Regulatory paralysis'],
]
t6 = Table(data6, colWidths=[1.5*inch, 2*inch, 2*inch])
t6.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
]))
story.append(t6)
story.append(Spacer(1, 6))

story.append(Paragraph("7-Year Scenario (2026-2033)", styles['H3']))
story.append(Paragraph("• <b>2026-2027</b>: US leads on architecture; power constraints emerge; China builds power plants", styles['MyBullet']))
story.append(Paragraph("• <b>2028-2029</b>: US hits grid limits; China's new plants come online; compute parity approaches", styles['MyBullet']))
story.append(Paragraph("• <b>2030-2033</b>: China achieves raw compute advantage; US forced into efficiency focus", styles['MyBullet']))
story.append(Spacer(1, 6))

story.append(Paragraph("The Critical Question", styles['H3']))
story.append(Paragraph("<b>If scaling laws hold</b> (more compute = better AI): China wins through brute force power advantage", styles['Body']))
story.append(Paragraph("<b>If algorithmic breakthroughs dominate</b>: US/West wins through talent and research ecosystem", styles['Body']))
story.append(Spacer(1, 6))

story.append(Paragraph("Likely Outcome", styles['H3']))
story.append(Paragraph("A bifurcated AI world by 2033: Chinese AI sphere (raw power, state-controlled, closed) vs Western AI sphere (efficiency-focused, distributed, allied nations pooling resources). Neither achieves global AGI monopoly.", styles['Body']))
story.append(Spacer(1, 20))

story.append(Spacer(1, 12))

# Section 7
story.append(Paragraph("7. What If AGI Doesn't Scale? The Moore's Law Parallel", styles['H2']))
story.append(Paragraph("The assumption that 'more compute = smarter AI' may break down, just as Moore's Law eventually hit physical limits.", styles['Body']))
story.append(Spacer(1, 6))

story.append(Paragraph("The Moore's Law Template", styles['H3']))
story.append(Paragraph("• <b>1970-2010</b>: Exponential scaling held (transistors doubled every 2 years)", styles['MyBullet']))
story.append(Paragraph("• <b>2010-2025</b>: Dennard scaling ended; gains slowed to ~3 year doubling", styles['MyBullet']))
story.append(Paragraph("• <b>2025+</b>: Physical limits (atomic scale) cause further slowdown", styles['MyBullet']))
story.append(Spacer(1, 6))

story.append(Paragraph("Four Scenarios for 2026-2036", styles['H3']))
data7 = [
    ['Scenario', 'Assumption', '2036 Outcome'],
    ['Optimistic', 'Scaling continues', 'AGI achieved'],
    ['Moderate', "Moore's Law pattern", '~3x current, no AGI'],
    ['Pessimistic', 'Hard ceiling', '~1.5x current, plateau'],
    ['Plateau', 'Brief gains then stagnation', 'Near-current, no AGI'],
]
t7 = Table(data7, colWidths=[1.5*inch, 2*inch, 2*inch])
t7.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
]))
story.append(t7)
story.append(Spacer(1, 6))

story.append(Paragraph("The Binding Constraints", styles['H3']))
story.append(Paragraph("Capability = Minimum(Compute, Data, Algorithms, Energy). Progress stops when ANY constraint binds:", styles['Body']))
story.append(Paragraph("• <b>Training data exhaustion</b>: Internet-scale text already consumed", styles['MyBullet']))
story.append(Paragraph("• <b>Compute limits</b>: Power constraints, chip fab limits, prohibitive costs", styles['MyBullet']))
story.append(Paragraph("• <b>Algorithmic ceiling</b>: Transformer may be near-optimal, no successor paradigm", styles['MyBullet']))
story.append(Paragraph("• <b>Energy wall</b>: Training runs consuming city-scale power", styles['MyBullet']))
story.append(Spacer(1, 6))

story.append(Paragraph("The Uncomfortable Question", styles['H3']))
story.append(Paragraph("Current AI progress may be a <b>one-time windfall</b> from: (1) Transformer architecture, (2) Scale discovery, (3) Internet-scale training data. If no new paradigm emerges, we may be witnessing the <b>peak of this approach</b>, not the beginning of exponential takeoff.", styles['Body']))
story.append(Spacer(1, 20))

story.append(Spacer(1, 12))

# Section 8
story.append(Paragraph("8. The Data Wall: How Can OpenAI Continue Scaling?", styles['H2']))
story.append(Paragraph("The fundamental problem: scaling requires exponentially more data, but high-quality training data is finite and already exhausted.", styles['Body']))
story.append(Spacer(1, 6))

story.append(Paragraph("The Numbers Don't Work", styles['H3']))
data8 = [
    ['Model', 'Training Tokens', 'Status'],
    ['GPT-2 (2019)', '~10 billion', 'Abundant data'],
    ['GPT-3 (2020)', '~300 billion', 'Plenty remaining'],
    ['GPT-4 (2023)', '~13 trillion', 'Used most of internet'],
    ['GPT-5 (2025?)', '~50+ trillion', "Doesn't exist"],
]
t8 = Table(data8, colWidths=[1.5*inch, 1.5*inch, 2*inch])
t8.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
    ('BACKGROUND', (0, 1), (-1, 3), colors.beige),
    ('BACKGROUND', (0, 4), (-1, 4), colors.lightcoral),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
]))
story.append(t8)
story.append(Paragraph("<b>Available high-quality internet text: ~10-15 trillion tokens. Annual new content: ~1-2 trillion.</b>", styles['Body']))
story.append(Spacer(1, 6))

story.append(Paragraph("OpenAI's Attempted Solutions", styles['H3']))
story.append(Paragraph("• <b>Synthetic data</b>: AI generates training data → model collapse risk, quality degrades", styles['MyBullet']))
story.append(Paragraph("• <b>Licensed deals</b>: Reddit ($60M/yr), publishers → expensive, finite, legally contested", styles['MyBullet']))
story.append(Paragraph("• <b>Multimodal</b>: Video/audio → different modality, doesn't help text reasoning", styles['MyBullet']))
story.append(Paragraph("• <b>User data</b>: ChatGPT conversations → privacy laws, consent issues", styles['MyBullet']))
story.append(Paragraph("• <b>RLHF quality</b>: Better curation → doesn't add new knowledge", styles['MyBullet']))
story.append(Spacer(1, 6))

story.append(Paragraph("The Uncomfortable Reality", styles['H3']))
story.append(Paragraph("<b>OpenAI cannot continue the scaling approach</b> that made GPT-3→GPT-4 successful. Options: admit diminishing returns, pivot to efficiency, hope for algorithmic breakthroughs, or gamble on synthetic data.", styles['Body']))
story.append(Spacer(1, 6))

story.append(Paragraph("What This Means for AGI", styles['H3']))
story.append(Paragraph("• <b>AGI via scaling is impossible</b>: Not enough data exists", styles['MyBullet']))
story.append(Paragraph("• <b>Algorithmic breakthroughs required</b>: Fundamentally new approaches needed", styles['MyBullet']))
story.append(Paragraph("• <b>China's compute advantage irrelevant</b>: Can't train what doesn't exist", styles['MyBullet']))
story.append(Paragraph("• <b>Open source catches up</b>: Diminishing returns level the field", styles['MyBullet']))
story.append(Spacer(1, 6))

story.append(Paragraph("The scaling era (2019-2024) may be over. What comes next is uncertain.", styles['Body']))
story.append(Spacer(1, 20))

story.append(Paragraph("<i>Generated: February 2026</i>", styles['Body']))
story.append(Paragraph("<i>See PNG files for all visualizations</i>", styles['Body']))

doc.build(story)
print("PDF created successfully!")
