# Comma Code

A simple Python script that takes a list of strings and formats it into a single string, separating items with commas and inserting "and" before the last item. This is a common practice project often referred to as "Comma Code."

---

## How It Works

- Takes a list of strings as input.
- Joins items with a comma and a space.
- Inserts "and" before the last item in the list.
- **Handles single-item lists:** If there's only one item, it returns just that item (e.g., `['apple']` becomes `'apple'`).
- **Handles empty lists:** Returns an empty string if the list is empty.

---

## Example

```
Enter the number of list entries: 4
Enter the string-1: apples
Enter the string-2: bananas
Enter the string-3: tofu
Enter the string-4: cats
apples, bananas, tofu, and cats
```

---

## File

- `comma.py` — contains the logic for formatting the list and handling user input.

---

## Note

This is a practice task from the book **"Automate the Boring Stuff with Python" by Al Sweigart.**
