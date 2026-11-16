# Integer Sum

Requires Python 3. No external dependencies are needed.

Application code lives in `src/`, and tests live in `tests/`.

Run the program from the repository root:

```sh
python3 src/sum_integers.py
```

The program prints the running total after each addition, from
`After adding 1: 1` through `After adding 100: 5050`, followed by
the final result, `5050`.

Run the tests using Python's built-in `unittest` framework:

```sh
python3 -m unittest discover -s tests -v
```
