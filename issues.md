# Lab 5: Static Code Analysis - Issues and Fixes

| Issue | Type | Original Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Mutable default argument | Bug | 15 | Using an empty list as a default argument can cause data to be shared between function calls. | Changed the default argument to `None` and initialized a new list inside the function. |
| Bare exception | Code quality | 26 | A bare `except` can hide unexpected errors. | Removed the bare exception and handled invalid book IDs explicitly. |
| Use of `eval()` | Security | 42 | Evaluating arbitrary expressions can execute unintended code. | Replaced expression evaluation with validated numeric inputs and direct arithmetic. |
| Weak MD5 hash | Security | 47 | MD5 is not suitable for security-sensitive hashing. | Replaced MD5 with SHA-256. |
| Insecure PIN generation | Security | 51 | The `random` module is not suitable for security-sensitive random values. | Used `secrets` to generate a temporary PIN. |
| Shell command execution | Security | 58 | Using `os.system()` with a filename can introduce command-injection risks. | Removed shell execution and used logging. |
| Unused imports and variables | Code quality | Various | Some imports and variables were never used. | Removed the unused imports and variables. |
| File handling | Code quality | 55 | The original code opened a file without a context manager or explicit encoding. | Used `Path.write_text()` with UTF-8 encoding. |
| Function naming | Style | 15 | The original function used camelCase instead of snake_case. | Renamed `issueBook()` to `issue_book()`. |

## Verification

- Ran Pylint, Bandit, and Flake8 on the original program.
- Fixed issues identified by the static analysis tools.
- Reran all three tools on the updated program.
- Checked the final reports to verify the fixes.
