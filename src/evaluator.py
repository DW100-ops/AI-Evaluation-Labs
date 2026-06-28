"""
Evaluator Module
Compares expected answers vs model outputs and returns scores
"""


def evaluate_response(expected, model_output):
    """
    Evaluate model response against expected answer.
    Returns a score between 0 and 1.
    
    Scoring logic:
    - Exact match: 1.0
    - Keyword overlap: partial score (0.5 - 0.9)
    - No match: 0.0
    """
    
    # Convert to lowercase for comparison
    expected_lower = expected.lower()
    output_lower = model_output.lower()
    
    # Exact match
    if expected_lower == output_lower:
        return 1.0
    
    # Check for substring match (partial credit)
    if expected_lower in output_lower or output_lower in expected_lower:
        return 0.9
    
    # Check keyword overlap
    expected_words = set(expected_lower.split())
    output_words = set(output_lower.split())
    
    if expected_words and output_words:
        overlap = expected_words.intersection(output_words)
        overlap_ratio = len(overlap) / len(expected_words)
        
        if overlap_ratio > 0.7:
            return 0.8
        elif overlap_ratio > 0.5:
            return 0.6
        elif overlap_ratio > 0.2:
            return 0.3
    
    # No match
    return 0.0
