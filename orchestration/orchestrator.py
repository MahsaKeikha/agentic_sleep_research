ORDER=["study_context","signal_quality","sleep_metric","confounder_review","evidence_quality","human_review"]
def orchestrate(context): return {"workflow":ORDER,"context":context,"status":"review_required"}
