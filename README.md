# Python for JS/MERN Developers → AI/GenAI Engineer Roadmap

You already know JavaScript/Node/React/Express/MongoDB. This repo teaches you
Python **by constantly comparing it to JS**, then bridges you into the
libraries you'll actually use as an AI/GenAI engineer (NumPy, Pandas,
scikit-learn, and LLM/GenAI API patterns).

## How to use this repo

1. Go folder by folder, in order (01 → 10).
2. Every `.py` file is runnable on its own: `python 03_data_structures/01_lists_vs_arrays.py`
3. Read the comments — they explain the "why", not just the "what", and
   call out interview-favorite gotchas (`# INTERVIEW:`).
4. Try the `# TODO (practice)` blocks yourself before checking the answer.

## Folder map

| Folder | Topic | JS equivalent you already know |
|---|---|---|
| 01_basics | variables, types, operators, strings | `let/const`, template literals |
| 02_control_flow | if/else, loops | `if/else`, `for`, `while` |
| 03_data_structures | list/dict/tuple/set | Array, Object, Map, Set |
| 04_functions | functions, lambda, *args/**kwargs | function, arrow fn, spread/rest |
| 05_oop | classes, inheritance | ES6 classes |
| 06_modules_and_packages | import/export, pip | import/export, npm |
| 07_file_handling | reading/writing files | fs module |
| 08_error_handling | try/except | try/catch |
| 09_advanced | decorators, generators, context managers, async | HOFs, iterators, `async/await` |
| 10_ai_genai_intro | NumPy, Pandas, scikit-learn, LLM API calls | closest thing: no direct JS equivalent |
| 11_numpy_pandas_deep_dive | broadcasting, linear algebra, data cleaning, groupby/merge/pivot, mini project | closest thing: MongoDB aggregation pipelines |
| 12_ml_concepts | training vs inference, train/test split & overfitting, evaluation metrics, embeddings | no direct JS equivalent |
| 13_llm_fundamentals | tokens, context windows/memory, temperature/sampling, system prompts, prompt engineering | closest thing: Express middleware (system prompt), stateless REST calls (context) |

## Interview prep checklist (Python specific)

- Mutable vs immutable types (list vs tuple, and why dict keys must be immutable)
- List comprehensions (Python's most-loved interview topic)
- `*args` / `**kwargs` and unpacking
- Difference between `is` and `==`
- GIL (Global Interpreter Lock) — what it is, why it matters for concurrency
- Decorators — how they work under the hood (functions returning functions)
- Generators vs normal functions (`yield` vs `return`) — memory efficiency
- Shallow copy vs deep copy
- `__init__`, `self`, dunder/magic methods (`__str__`, `__repr__`, `__eq__`)

## Path to AI/GenAI Engineer

1. **Python fundamentals** (this repo, folders 1-9) — 1-2 weeks if you're consistent
2. **NumPy + Pandas** (folder 10) — data manipulation, the backbone of ML/AI work
3. **Math refresher** — linear algebra basics, probability (Khan Academy is enough)
4. **scikit-learn** — classical ML (regression, classification) to understand ML fundamentals
5. **PyTorch or TensorFlow** — deep learning
6. **LLM/GenAI tooling** — OpenAI/Anthropic SDKs, LangChain, vector databases (Pinecone/Chroma),
   RAG (Retrieval Augmented Generation), prompt engineering
7. **Build projects** — a chatbot, a RAG app over your own docs, a fine-tuned classifier

Folder `10_ai_genai_intro` gives you a taste of steps 2-6 so you know what's coming.
Folders `11_numpy_pandas_deep_dive` and `12_ml_concepts` go deeper into steps 2-3 —
real data cleaning, aggregation, and the core ML vocabulary (training/inference,
overfitting, precision/recall, embeddings) you need before touching LLM/RAG work.
Folder `13_llm_fundamentals` covers step 4 — tokens, context windows, temperature,
system prompts, and prompt engineering patterns — the exact vocabulary and
mental models you need before calling real LLM APIs and building RAG pipelines.

Note: `13_llm_fundamentals/01` and `02` use the `tiktoken` package to count
real tokens. It downloads its encoding file from the internet on first use —
if that's blocked on your network, the files automatically fall back to an
approximation so they still run and still teach the concept.
