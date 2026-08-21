"""
ERROR HANDLING — Python vs JS

JS:
    try {
      riskyCode();
    } catch (error) {
      console.log(error.message);
    } finally {
      cleanup();
    }
"""

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:      # Python catches SPECIFIC error types (best practice)
        print("Error:", e)
        return None
    except TypeError as e:
        print("Type error:", e)
        return None
    else:
        # `else` runs ONLY if no exception occurred — no direct JS equivalent
        print("Division succeeded!")
        return result
    finally:
        # same as JS finally — ALWAYS runs, error or not
        print("Division attempt finished")

print(divide(10, 2))
print(divide(10, 0))

# --- Catching multiple exception types at once ---
try:
    x = int("not a number")
except (ValueError, TypeError) as e:
    print("Caught:", e)

# --- Raising your own errors (JS: throw new Error("message")) ---
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")   # JS: throw new Error("Insufficient funds")
    return balance - amount

try:
    withdraw(100, 500)
except ValueError as e:
    print("Withdrawal failed:", e)

# --- Custom exception classes (JS: class InsufficientFundsError extends Error {}) ---
class InsufficientFundsError(Exception):
    """Custom exception for banking operations."""
    pass

def withdraw_v2(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"Cannot withdraw {amount}, balance is {balance}")
    return balance - amount

try:
    withdraw_v2(100, 500)
except InsufficientFundsError as e:
    print("Custom error caught:", e)

# INTERVIEW: catching bare `except:` (no type) is BAD practice — it catches
# EVERYTHING including KeyboardInterrupt/SystemExit. Always specify the type,
# or at minimum use `except Exception as e:`

# TODO (practice): write a function `safe_get_item(lst, index)` that returns
# None instead of raising IndexError when the index is out of range.
