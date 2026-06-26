# Newline Formatter

This program reads a text file named `input.txt` and creates a new file named `output.txt`.

The output file is the same as the input file, except that it inserts a blank line after every **145 lines**.

---

## Requirements

You need **Python 3** installed on your computer.

### Windows

1. Go to https://www.python.org/downloads/

2. Download the latest version of Python 3.

3. Run the installer.

4. **Important:** On the first installation screen, check the box that says:

   ```
   Add Python to PATH
   ```

5. Click **Install Now**.

6. When the installation finishes, close the installer.

---

## Files

Place these files in the same folder:

* `script.py`
* `input.txt`

Your folder should look something like this:

```
MyFolder/
│
├── script.py
└── input.txt
```

---

## Running the Program

### Windows

1. Open the folder containing the files.

2. Click in the address bar at the top of File Explorer.

3. Type:

   ```
   cmd
   ```

4. Press **Enter**.

A Command Prompt window will open.

5. Type:

   ```
   python script.py
   ```

6. Press **Enter**.

If that doesn't work, try:

```
py script.py
```

---

## Output

When the program finishes, you'll see a message similar to:

```
Done! Output written to output.txt
```

A new file named `output.txt` will appear in the same folder.

---

## Changing the Input or Output File Names

At the top of `script.py` are these lines:

```python
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
```

You can change these if you want the program to use different file names.

---

## Troubleshooting

### "python is not recognized"

Python is either not installed or was installed without selecting **Add Python to PATH**.

Try:

```
py script.py
```

If that also fails, reinstall Python and make sure **Add Python to PATH** is checked during installation.

---

### "FileNotFoundError: input.txt"

The program could not find `input.txt`.

Make sure:

* `input.txt` exists.
* It is in the same folder as `script.py`.
* The file name is spelled exactly `input.txt`.

---

## Need to Process a Different Number of Lines?

Open `script.py` and change this line:

```python
LINES_PER_GROUP = 145
```

Replace `145` with any number you want.
