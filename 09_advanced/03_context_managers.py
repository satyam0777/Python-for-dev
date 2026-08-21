"""
CONTEXT MANAGERS — the `with` keyword.
No exact JS equivalent — closest concept is try/finally used for cleanup,
but Python formalizes this pattern with `with`.

You already used this in 07_file_handling — now let's see how it works.
"""

# --- How `with open(...) as f:` works under the hood ---
# It's equivalent to:
#     f = open("file.txt")
#     try:
#         # do stuff with f
#     finally:
#         f.close()
# `with` guarantees cleanup happens automatically, even if an exception occurs.

# --- Building your OWN context manager (class-based) ---
class Timer:
    def __enter__(self):              # runs when entering the `with` block
        import time
        self.start = time.time()
        return self                    # this becomes the `as X` value

    def __exit__(self, exc_type, exc_value, traceback):   # ALWAYS runs on exit, even on error
        import time
        elapsed = time.time() - self.start
        print(f"Elapsed: {elapsed:.4f}s")
        # returning False (or None) lets exceptions propagate normally;
        # returning True would SUPPRESS the exception (rarely what you want)

with Timer() as t:
    total = sum(range(1000000))
print("Sum computed:", total)

# --- Simpler way: @contextmanager decorator (function-based, less boilerplate) ---
from contextlib import contextmanager

@contextmanager
def timer_simple():
    import time
    start = time.time()
    yield                      # code inside the `with` block runs HERE
    elapsed = time.time() - start
    print(f"Elapsed (simple): {elapsed:.4f}s")

with timer_simple():
    total = sum(range(1000000))

# --- Practical real-world use: database connections, locks, API sessions ---
# Example pattern you'll see constantly in AI/backend code:
#
#     with db.session() as session:
#         session.query(...)
#     # connection auto-closed here, even if query() throws
#
#     with requests.Session() as session:
#         session.get(url)
#     # HTTP connection pool cleaned up automatically

# INTERVIEW: "Why use `with` instead of manually calling close()?"
# -> Guarantees resource cleanup (files, sockets, locks, DB connections)
# even when an exception is raised, without needing explicit try/finally.

# TODO (practice): write a context manager `suppress_errors()` that
# catches and silently ignores any exception raised inside the `with` block.
