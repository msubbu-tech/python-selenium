from fpdf import FPDF

# Create PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "OSPF Interview Cheat Sheet – Senior Network Engineer", ln=True, align="C")
pdf.ln(10)

# Section 1: Basic
pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, "Section 1: Basic Scenarios", ln=True)
pdf.set_font("Arial", "", 12)
basic_questions = [
    ("1. OSPF Neighbors Not Forming",
     "Check Area ID, Hello/Dead timers, subnet match, MTU, and authentication. Use 'show ip ospf neighbor' and 'debug ip ospf adj'."),
    ("2. OSPF 2-Way State",
     "Normal on broadcast networks for non-DR/BDR routers. Only DR/BDR form FULL adjacency."),
    ("3. Missing OSPF Routes",
     "Check LSDB using 'show ip ospf database', verify area type and route filters."),
    ("4. OSPF Network Type",
     "Point-to-point avoids DR election, broadcast elects DR/BDR, NBMA requires manual neighbors."),
    ("5. OSPF Passive Interface",
     "Prevents adjacency on interfaces where you don't want hello packets sent. 'passive-interface G0/1'")
]
for q, a in basic_questions:
    pdf.multi_cell(0, 8, f"{q}\n→ {a}\n")

# Section 2: Intermediate
pdf.add_page()
pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, "Section 2: Intermediate Scenarios", ln=True)
pdf.set_font("Arial", "", 12)
intermediate_questions = [
    ("6. OSPF Route Redistribution",
     "Use 'redistribute static subnets'. Stub areas block Type-5 LSAs; use NSSA for redistribution."),
    ("7. OSPF Summarization",
     "At ABR: 'area 1 range 10.10.0.0 255.255.0.0'. At ASBR: 'summary-address 172.16.0.0 255.255.0.0'."),
    ("8. OSPF LSA Types",
     "Type-1 (Router), Type-2 (Network), Type-3 (Summary), Type-4 (ASBR Summary), Type-5 (External), Type-7 (NSSA)."),
    ("9. OSPF DR/BDR Election",
     "Highest priority wins, then highest router ID. Use 'ip ospf priority 0' to exclude router from election."),
    ("10. OSPF Authentication Issues",
     "Check matching authentication type and key on both ends. 'ip ospf authentication message-digest'.")
]
for q, a in intermediate_questions:
    pdf.multi_cell(0, 8, f"{q}\n→ {a}\n")

# Section 3: Advanced
pdf.add_page()
pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, "Section 3: Advanced Scenarios", ln=True)
pdf.set_font("Arial", "", 12)
advanced_questions = [
    ("11. OSPF Route Preference Order",
     "Intra-area > Inter-area > E1 > E2. Verify 'show ip route' for AD and LSA origin."),
    ("12. OSPF Stub and NSSA Areas",
     "Stub blocks Type-5 LSAs. NSSA allows Type-7 LSAs converted to Type-5 by ABR."),
    ("13. OSPF Virtual Link",
     "Used to connect a non-backbone area to Area 0. 'area 20 virtual-link 2.2.2.2'."),
    ("14. OSPF SPF Optimization",
     "Use throttling: 'timers throttle spf 5 100 5000' to limit SPF recalculations."),
    ("15. OSPF External Route Type",
     "E1 adds internal cost; E2 (default) static external cost. 'redistribute static metric-type 1'."),
    ("16. ABR and ASBR Identification",
     "ABR: connects Area 0 & non-0 area. ASBR: redistributes external routes. Verify with 'show ip ospf border-routers'."),
    ("17. LSA Flooding Troubleshooting",
     "Check LSA age, seq num, and DB sync using 'show ip ospf database'. Adjust 'timers pacing flood 33'."),
    ("18. OSPF Design Best Practices",
     "Use hierarchical design, summarization, and stub areas to reduce LSDB and SPF overhead."),
    ("19. OSPF Cost Manipulation",
     "Adjust interface cost to influence path: 'ip ospf cost 100'. Lower cost = preferred path."),
    ("20. OSPF Multi-Area Summarization",
     "Perform summarization at ABRs only; use proper address aggregation to minimize LSAs."),
    ("21. OSPF Route Flapping",
     "Caused by unstable links; use BFD or interface dampening and SPF throttling."),
    ("22. OSPF Default Route Advertisement",
     "ABR: 'area 0 stub no-summary' + 'default-information originate'. External: redistribute default route."),
    ("23. OSPF Over GRE/IPSec",
     "Use point-to-point network type to avoid DR election; ensure OSPF multicast is permitted."),
    ("24. OSPF LSDB Size Optimization",
     "Summarize and use stub areas to reduce LSA count and memory load."),
    ("25. OSPF Troubleshooting Commands",
     "'show ip ospf neighbor', 'show ip ospf interface', 'show ip ospf database', 'debug ip ospf adj'.")
]
for q, a in advanced_questions:
    pdf.multi_cell(0, 8, f"{q}\n→ {a}\n")

pdf.output("OSPF_Interview_CheatSheet_Senior.pdf")
print("✅ PDF generated: OSPF_Interview_CheatSheet_Senior.pdf")
