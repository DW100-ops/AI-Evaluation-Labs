"""
Mock LLM Client
Returns deterministic fake responses without real API calls
"""


def mock_llm(prompt):
    """
    Mock LLM function that returns a fake response based on the prompt.
    No API calls - just for testing the pipeline.
    """
    # Simple deterministic responses for demo purposes
    responses = {
        "capital": "Paris is the capital of France.",
        "inventor": "Thomas Edison invented the light bulb.",
        "planet": "Mars is known as the Red Planet.",
        "language": "Python is a popular programming language.",
        "scientist": "Albert Einstein developed the theory of relativity."
    }
    
    # Check if prompt contains keywords and return matching response
    prompt_lower = prompt.lower()
    
    for key, response in responses.items():
        if key in prompt_lower:
            return response
    
    # Default fallback response
    return "This is a mock response from the LLM."
