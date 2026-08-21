"""
ASYNC / AWAIT — Python vs Node.js

Since you know Node, this will feel familiar. The keywords are IDENTICAL
(`async`, `await`), but the execution model differs slightly.

JS/Node:
    async function fetchData() {
      const res = await fetch(url);
      const data = await res.json();
      return data;
    }
    fetchData().then(data => console.log(data));

Node's event loop is BUILT IN and runs automatically.
Python's event loop must be explicitly STARTED via asyncio.
"""

import asyncio

# --- Basic async function ---
async def say_hello():
    print("Hello...")
    await asyncio.sleep(1)     # JS: await new Promise(r => setTimeout(r, 1000))
    print("...World")

# You CANNOT just call say_hello() like a normal function — it returns a
# "coroutine" object, not the result. You must run it via the event loop:
asyncio.run(say_hello())        # JS: just calling an async function auto-runs it

# --- Running multiple async tasks CONCURRENTLY ---
# JS: await Promise.all([fetchUser(), fetchPosts(), fetchComments()])
async def fetch_user():
    await asyncio.sleep(1)
    return "user data"

async def fetch_posts():
    await asyncio.sleep(2)
    return "posts data"

async def main():
    # gather() = Python's Promise.all()
    results = await asyncio.gather(fetch_user(), fetch_posts())
    print(results)   # ['user data', 'posts data'] -- total time ~2s, not 3s (they run concurrently)

asyncio.run(main())

# --- Real-world relevance for AI/GenAI engineers ---
# Calling LLM APIs (OpenAI, Anthropic) is I/O-bound (waiting on network),
# exactly like calling a Node API. Async matters a LOT when you need to:
#   - call an LLM API for many prompts in parallel
#   - stream tokens back to a user as they're generated
#   - handle many concurrent requests in a FastAPI backend (Python's Express equivalent)

async def call_llm_mock(prompt: str) -> str:
    """Pretend this calls an LLM API (e.g. Anthropic's Messages API)."""
    await asyncio.sleep(1)              # simulate network latency
    return f"AI response to: {prompt}"

async def process_many_prompts():
    prompts = ["Explain AI", "Explain Python", "Explain GenAI"]
    # Runs all 3 API calls CONCURRENTLY, not one after another
    responses = await asyncio.gather(*[call_llm_mock(p) for p in prompts])
    for r in responses:
        print(r)

asyncio.run(process_many_prompts())

# INTERVIEW: "Why can't you just call an async function directly?"
# -> It returns a coroutine object (a "recipe" for the work), which only
# executes once it's scheduled on the event loop via asyncio.run(),
# await, or asyncio.gather/create_task.

# NOTE: FastAPI (Python's most popular API framework, very Express-like)
# is built entirely around `async def` route handlers.

# TODO (practice): write an async function `download_all(urls)` that uses
# asyncio.gather to "download" (simulate with asyncio.sleep) multiple
# URLs concurrently and prints how long the total operation took.
