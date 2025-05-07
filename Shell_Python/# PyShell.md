# PyShell — A Minimalist Python Shell

**Author:** John-Michael Barron  
**Version:** 1.0  
**License:** MIT

---

## Overview

PyShell is a lightweight, Python-based shell interpreter designed to mimic basic functionality of a Unix shell. It supports:

- Command execution
- `cd` and environment variable expansion
- Piping (`|`)
- Output redirection (`>`, `>>`)
- Input redirection (`<`)
- Background job handling (`&`)
- Command history (`history`)

Built for educational purposes, PyShell is ideal for learning how shells work under the hood using Python’s standard libraries.

---

## Features

- Change directories (`cd`)
- Use environment variables like `$HOME` or `$USER`
- Chain commands with pipes: `ls | grep .py`
- Redirect output/input: `echo hello > file.txt`, `cat < file.txt`
- Run background tasks: `sleep 5 &`
- View command history: `history`

---

## How to Run

```bash
git clone https://github.com/yourusername/pyshell.git
cd pyshell
python shell.py
