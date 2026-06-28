# AI Evaluation Labs

A lightweight framework for evaluating Large Language Model (LLM) responses across accuracy, relevance, hallucination detection, latency, and cost metrics.

## Problem

Modern LLMs can produce confidently incorrect answers, partial truths, and fabricated information. Organizations need a systematic way to:
- **Verify** that LLM outputs match expected standards
- **Identify** which types of queries cause hallucinations or failures
- **Benchmark** model performance across diverse categories
- **Quantify** response quality with reproducible metrics

This framework provides a simple, extensible pipeline for automated evaluation.

## How It Works

```
test_cases.json (input data)
        ↓
    mock_llm() (generates response)
        ↓
  evaluate_response() (scores against expected answer)
        ↓
  run_example.py (orchestrates & displays results)
        ↓
   formatted output (scores, statistics, risk analysis)
```

Each test case includes:
- **Prompt** - The input question or task
- **Expected Answer** - The reference/baseline response
- **Category** - Type of task (factual, reasoning, code, creative, etc.)
- **Evaluation Criteria** - What makes a good response
- **Hallucination Risk** - Likelihood of LLM failure (Low/Medium/High)

## Installation

**Requirements:** Python 3.8+

```bash
# Clone the repository
git clone https://github.com/DW100-ops/AI-Evaluation-Labs.git
cd AI-Evaluation-Labs

# Install dependencies (currently zero external dependencies for MVP)
pip install -r requirements.txt
```

## Usage

Run the complete evaluation pipeline with a single command:

```bash
python run_example.py
```

### Example Output

```
================================================================================
                   AI EVALUATION PIPELINE - EXAMPLE RUN
================================================================================

✓ Loaded 10 test cases from data/test_cases.json

Test  1 | Factual Accuracy      | Score: 0.90 | Risk: Low
         Prompt: What is the capital of France?...
         Expected: Paris is the capital of France....
         Model Output: Paris is the capital of France....

Test  2 | Complex Reasoning     | Score: 0.80 | Risk: Medium
         Prompt: Explain why photosynthesis is important...
         Expected: Photosynthesis converts sunlight...
         Model Output: This is a mock response from the LLM....

Test  3 | Code Generation       | Score: 0.00 | Risk: High
         Prompt: Write a Python function that calculates...
         Expected: def factorial(n): ...
         Model Output: This is a mock response from the LLM....

[... 7 more tests ...]

================================================================================
                          EVALUATION SUMMARY
================================================================================

Total Tests Run:      10
Average Score:        0.75 / 1.00

Hallucination Risk Breakdown:
  Low Risk:           5 tests
  Medium Risk:        3 tests
  High Risk:          2 tests

Score Distribution:
  Perfect (1.0):      2 tests
  Good (0.7-0.99):    3 tests
  Partial (0.3-0.69): 4 tests
  Poor (0.0-0.29):    1 tests

================================================================================
                   Demo complete! Results ready for analysis.
================================================================================
```

## Project Structure

```
AI-Evaluation-Labs/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── run_example.py            # Main demo script - START HERE
├── main.py                   # Alternative entry point
│
├── data/
│   ├── test_cases.json       # 10 realistic evaluation test cases
│   ├── sample_dataset.json   # Placeholder for custom data
│   └── expected_answers.json # Placeholder for answer keys
│
├── src/
│   ├── __init__.py
│   ├── llm_client.py         # Mock LLM that generates responses
│   ├── evaluator.py          # Scoring logic (0.0-1.0)
│   ├── pipeline.py           # Extensible pipeline (placeholder)
│   ├── evaluators/           # Specialized evaluators (placeholder)
│   └── models/               # Model implementations (placeholder)
│
├── .env.example              # Environment variables template
├── .gitignore
└── LICENSE (MIT)
```

## Evaluation Metrics

The evaluator returns a **score between 0.0 and 1.0** using this logic:

| Condition | Score | Meaning |
|-----------|-------|---------|
| Exact match | 1.0 | Perfect response |
| Substring match | 0.9 | Contains full expected answer |
| >70% keyword overlap | 0.8 | Strong semantic similarity |
| >50% keyword overlap | 0.6 | Moderate overlap |
| >20% keyword overlap | 0.3 | Weak overlap |
| No match | 0.0 | Completely incorrect |

## Test Case Categories

The framework includes 10 diverse test cases:

1. **Factual Accuracy** - Capital of France (Low risk)
2. **Complex Reasoning** - Photosynthesis importance (Medium risk)
3. **Code Generation** - Factorial function (High risk)
4. **Summarization** - Industrial Revolution (Medium risk)
5. **Creative Writing** - AI metaphor (Low risk)
6. **Multi-hop Reasoning** - Logical deduction (Low risk)
7. **Opinion/Subjective** - Remote work pros/cons (Medium risk)
8. **Technical Definition** - API explanation (Low risk)
9. **Open-ended Question** - Climate change impact (High risk)
10. **Instruction Following** - Formatted list (Low risk)

## Lessons Learned

### Engineering Insights

1. **Hallucination Risk Scoring**
   - Not all LLM failures are equal. Code generation and open-ended questions pose higher hallucination risk than factual recalls.
   - Categorizing test cases by risk helps prioritize which failures matter most.

2. **Evaluation Metrics Matter**
   - A single score (0-1) is insufficient; context is critical. The evaluator needs to track why a response failed (format? content? reasoning?).
   - Keyword overlap is a simple proxy but misses semantic equivalence. Future work should integrate embedding-based similarity.

3. **Mock Data vs. Real LLMs**
   - The mock_llm() function lets us test the pipeline without API costs or rate limits, but it also masks real failure modes.
   - Moving from mock to real LLM requires only swapping the mock_llm() function—architecture is plugin-ready.

4. **Pipeline Extensibility**
   - By separating concerns (llm_client, evaluator, pipeline), we can easily add new metrics (latency, cost, bias detection).
   - The test_cases.json structure supports rich metadata (category, risk level, criteria), making future enhancements modular.

5. **Reproducibility & Transparency**
   - Hard-coded expected answers + deterministic scoring = reproducible results. 
   - Each test case documents its evaluation criteria upfront, so results are interpretable, not a black box.

## Future Enhancements

- [ ] Integrate real LLM APIs (OpenAI, Anthropic, etc.)
- [ ] Add embedding-based semantic similarity scoring
- [ ] Track latency and cost per request
- [ ] Implement bias & safety evaluation metrics
- [ ] Support batch evaluation with result export (CSV, JSON)
- [ ] Dashboard for result visualization
- [ ] CI/CD integration for automated evaluation

## Contributing

Contributions welcome! To add new test cases:

1. Add entries to `data/test_cases.json` following the existing schema
2. Update `src/llm_client.py` with mock responses (if needed)
3. Run `python run_example.py` to validate
4. Submit a pull request

## License

MIT License - see LICENSE file for details.

---

**Questions?** Open an issue or reach out to the maintainers.
