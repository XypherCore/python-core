# Day 01 Notes: Functions and Variables

## A function with no `return` gives `None`
Every call produces a value. If no `return` runs, that value is `None`
(type `NoneType`). `print()` writes to the screen as a side effect and does
not hand a value back, so `r = add(2, 3)` leaves `r` as `None` when `add`
only prints. Use `return` when the caller needs the result.

## Strings are immutable
String methods never change the original. They return a new string.
`s.strip()` on its own line creates a new string and discards it, so `s` is
unchanged. To keep the result, assign it: `s = s.strip()`. Method chaining
works because each method returns a new string for the next one to act on.

## Rounding
`round(2.5)` is 2 and `round(3.5)` is 4: Python 3 rounds exact halves to the
nearest even integer. JS `Math.round(2.5)` gives 3. Format specs like `:.3f`
round to the nearest value at that digit, so `f"{3.14159:.3f}"` is `3.142`.
Neither truncates.

## Scope
Assigning to a name inside a function creates a new local name that exists
only during the call and shadows any outer name. The outer variable is never
touched. A function can read names from enclosing scopes. Reading a local name
from outside raises `NameError`.

## `input()` returns `str`
Always. Convert with `int()` or `float()` before arithmetic. `"2" + "2"` is
`"22"`, `2 + 2` is `4`, and `"2" + 2` is a `TypeError`. Python never coerces
across `+` the way JS does.