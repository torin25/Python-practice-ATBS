# Character Picture Grid

A Python script that prints a text-based image from a 2D grid of characters.

## How It Works

- Takes a 2D list of characters as input (a list of lists).
- Treats each element as a pixel.
- Transposes the grid to print the image column by column, producing a rotated text-based picture.

---

## Example

```
Enter the number of lists in the main list: 3
Enter the number of entries in each list: 3

Number of lists in the main list: 3
Number of entries in each list: 3

Enter the entry 1 for list 1: o
Enter the entry 2 for list 1: .
Enter the entry 3 for list 1: o

Enter the entry 1 for list 2: .
Enter the entry 2 for list 2: o
Enter the entry 3 for list 2: .

Enter the entry 1 for list 3: o
Enter the entry 2 for list 3: .
Enter the entry 3 for list 3: o

Grid formed: [['o', '.', 'o'], ['.', 'o', '.'], ['o', '.', 'o']]

The image grid:
o.o
.o.
o.o
```

---

## Files

- `picture_grid.py` — contains the logic, user input handling, and grid printing.

## Note

This is a practice task from the book  
**"Automate the Boring Stuff with Python" by Al Sweigart.**
