Reflection answers
1. Which issues were the easiest to fix, and which were the hardest? Why?

ANS: The easiest issues to fix were unused imports, unused variables, and formatting problems because they required only small changes. The hardest issues were removing eval(), improving PIN generation, and correcting error handling because these changes affected security and program behaviour. I had to ensure that the program continued to calculate fines correctly and manage book copies properly after the changes.

2. Did the static analysis tools report any false positives? If so, describe one example.

ANS: The static analysis tools reported potential issues that needed to be checked against the actual code. The MD5 warning is relevant if the hash is used for security-sensitive purposes, although the original program used it to generate a digest of a patron identifier. Therefore, its severity depends on how the digest is used. I replaced MD5 with SHA-256, but I would not consider a warning a false positive without checking the program's intended behaviour and the specific finding.

3. How would you integrate static analysis tools into your actual software development workflow?

ANS: I would run Flake8 and Pylint during development and before committing code. I would use Bandit to check for potential security issues, especially when handling user input, files, commands, or sensitive information. I would also configure these tools to run automatically in a CI workflow whenever a pull request is created. This would help detect problems before code is merged.

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

ANS: The revised program avoids arbitrary expression evaluation, uses secure temporary PIN generation, and removes the shell command used for status output. It also handles invalid book IDs and fine inputs more explicitly and avoids a mutable default argument. File writing and logging have been improved, and the program runs its demonstration through a main execution guard. Consistent naming and formatting make the code easier to read, review, and maintain.
