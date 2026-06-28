"""
AI Evaluation Pipeline - Main Entry Point
Loads test cases, sends to LLM, evaluates responses, prints results
"""

import json
from src.llm_client import mock_llm
from src.evaluator import evaluate_response


def load_test_cases(filepath="data/test_cases.json"):
    """Load test cases from JSON file"""
    with open(filepath, "r") as f:
        return json.load(f)


def run_evaluation():
    """Main evaluation pipeline"""
    print("=" * 60)
    print("AI EVALUATION PIPELINE")
    print("=" * 60)
    
    # Load test cases
    test_cases = load_test_cases()
    print(f"\nLoaded {len(test_cases)} test cases\n")
    
    results = []
    
    # Run each test case
    for i, test_case in enumerate(test_cases, 1):
        prompt = test_case["prompt"]
        expected = test_case["expected_answer"]
        category = test_case["category"]
        
        print(f"Test {i}: {category}")
        print(f"Prompt: {prompt}")
        print(f"Expected: {expected}")
        
        # Get LLM response (using mock)
        model_output = mock_llm(prompt)
        print(f"Model Output: {model_output}")
        
        # Evaluate response
        score = evaluate_response(expected, model_output)
        print(f"Score: {score:.2f}\n")
        
        results.append({
            "test_id": i,
            "category": category,
            "score": score
        })
    
    # Summary
    print("=" * 60)
    print("EVALUATION SUMMARY")
    print("=" * 60)
    avg_score = sum(r["score"] for r in results) / len(results)
    print(f"Average Score: {avg_score:.2f}")
    print(f"Total Tests: {len(results)}")
    print("=" * 60)


if __name__ == "__main__":
    run_evaluation()
