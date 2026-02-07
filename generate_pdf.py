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
story.append(Spacer(1, 20))

story.append(Paragraph("<i>Generated: February 2026</i>", styles['Body']))

doc.build(story)
print("PDF created successfully!")
