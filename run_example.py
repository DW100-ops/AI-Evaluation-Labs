"""
run_example.py - Simple end-to-end demo of the AI Evaluation Pipeline

Usage: python run_example.py

This script:
1. Loads realistic test cases from data/test_cases.json
2. Passes each prompt through the mock LLM and evaluator
3. Displays formatted results for review
4. Serves as a working example of the complete system
"""

import json
import sys
from src.llm_client import mock_llm
from src.evaluator import evaluate_response


def load_test_cases(filepath="data/test_cases.json"):
    """Load test cases from JSON file."""
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"ERROR: Could not find {filepath}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"ERROR: {filepath} is not valid JSON")
        sys.exit(1)


def run_evaluation_demo():
    """Run the complete evaluation pipeline with formatted output."""
    
    print("\n" + "=" * 80)
    print("AI EVALUATION PIPELINE - EXAMPLE RUN".center(80))
    print("=" * 80)
    
    # Load test cases
    test_cases = load_test_cases()
    print(f"\n✓ Loaded {len(test_cases)} test cases from data/test_cases.json\n")
    
    results = []
    
    # Run each test case
    for i, test_case in enumerate(test_cases, 1):
        prompt = test_case["prompt"]
        expected = test_case["expected_answer"]
        category = test_case["category"]
        criteria = test_case.get("evaluation_criteria", {})
        
        # Get LLM response (using mock)
        model_output = mock_llm(prompt)
        
        # Evaluate response
        score = evaluate_response(expected, model_output)
        
        # Store result
        result = {
            "test_id": i,
            "category": category,
            "score": score,
            "hallucination_risk": criteria.get("hallucination_risk", "Unknown")
        }
        results.append(result)
        
        # Print formatted output for this test
        print(f"Test {i:2d} | {category:25s} | Score: {score:.2f} | Risk: {criteria.get('hallucination_risk', 'N/A'):6s}")
        print(f"         Prompt: {prompt[:60]}{'...' if len(prompt) > 60 else ''}")
        print(f"         Expected: {expected[:60]}{'...' if len(expected) > 60 else ''}")
        print(f"         Model Output: {model_output[:60]}{'...' if len(model_output) > 60 else ''}")
        print()
    
    # Print summary statistics
    print("=" * 80)
    print("EVALUATION SUMMARY".center(80))
    print("=" * 80)
    
    avg_score = sum(r["score"] for r in results) / len(results) if results else 0
    high_risk = sum(1 for r in results if "High" in r["hallucination_risk"])
    medium_risk = sum(1 for r in results if "Medium" in r["hallucination_risk"])
    low_risk = sum(1 for r in results if "Low" in r["hallucination_risk"])
    
    print(f"\nTotal Tests Run:      {len(results)}")
    print(f"Average Score:        {avg_score:.2f} / 1.00")
    print(f"\nHallucination Risk Breakdown:")
    print(f"  Low Risk:           {low_risk} tests")
    print(f"  Medium Risk:        {medium_risk} tests")
    print(f"  High Risk:          {high_risk} tests")
    
    # Score distribution
    perfect_scores = sum(1 for r in results if r["score"] == 1.0)
    good_scores = sum(1 for r in results if 0.7 <= r["score"] < 1.0)
    partial_scores = sum(1 for r in results if 0.3 <= r["score"] < 0.7)
    poor_scores = sum(1 for r in results if 0.0 <= r["score"] < 0.3)
    
    print(f"\nScore Distribution:")
    print(f"  Perfect (1.0):      {perfect_scores} tests")
    print(f"  Good (0.7-0.99):    {good_scores} tests")
    print(f"  Partial (0.3-0.69): {partial_scores} tests")
    print(f"  Poor (0.0-0.29):    {poor_scores} tests")
    
    print("\n" + "=" * 80)
    print("Demo complete! Results ready for analysis.".center(80))
    print("=" * 80 + "\n")


if __name__ == "__main__":
    run_evaluation_demo()
