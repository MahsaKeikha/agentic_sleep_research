def clinical_gate(context): return {"allowed": not any(k in context for k in ["diagnosis","treatment_decision"]),"requires_human_review":True}
