"""
AI service for generating explanations for quiz answers.
Uses a rule-based approach for generating explanations.
"""
import random

# Fallback explanations when AI is not available
FALLBACK_EXPLANATIONS = {
    True: "This answer is correct. The selected option matches the expected answer for this question.",
    False: "This answer is incorrect. Please review the related material and try again."
}

# Explanation templates for different scenarios
EXPLANATION_TEMPLATES = {
    True: [
        "Excellent! You selected the correct answer. {correct_answer} is indeed the right choice because it accurately addresses the question.",
        "Well done! The answer {correct_answer} is correct. This demonstrates your understanding of the concept.",
        "Correct! {correct_answer} is the right answer. You've shown good knowledge of this topic.",
        "That's right! {correct_answer} is the correct answer. Your selection shows you understand the key principles involved."
    ],
    False: [
        "Not quite. The correct answer is {correct_answer}, not {user_answer}. Review this topic to better understand the concept.",
        "That's incorrect. You selected {user_answer}, but the correct answer is {correct_answer}. Consider reviewing this material.",
        "Your answer {user_answer} is not correct. The right answer is {correct_answer}. This is an important distinction to understand.",
        "Unfortunately, {user_answer} is incorrect. The correct answer is {correct_answer}. This is a common misconception."
    ]
}


class AIExplanationService:
    """Service for generating rule-based explanations for quiz answers"""
    
    def __init__(self):
        self.is_initialized = True
    
    def initialize(self):
        """Initialize the service - simple for rule-based approach"""
        return True
    
    def generate_explanation(self, question_text, correct_answer, user_answer, is_correct):
        """Generate an explanation for a quiz answer using templates"""
        
        # Choose a random template based on whether the answer is correct
        templates = EXPLANATION_TEMPLATES[is_correct]
        template = random.choice(templates)
        
        # Fill in the template with the specific details
        explanation = template.format(
            correct_answer=correct_answer,
            user_answer=user_answer
        )
        
        return explanation


# Singleton instance
explanation_service = AIExplanationService()
