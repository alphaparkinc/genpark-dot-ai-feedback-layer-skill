class DotAiFeedbackLayerClient:
    def parse_feedback(self, original_output_id: str, rating_score: int, text_correction: str) -> dict:
        action = f"Revise output {original_output_id}." if rating_score < 4 else "Keep as is."
        instruction = f"Action: {action} Adjustments required: {text_correction}"
        return {"revised_prompt_instructions": instruction}