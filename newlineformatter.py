INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
CHARS_PER_LINE = 10

print(f"Looking for {INPUT_FILE}...")
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    text = f.read()

print("File found!")    

print("Length of input:", len(text))
print("First 200 characters:")
print(repr(text[:200]))

print("Removing whitespace characters before starting...")
text = text.replace("\r", "").replace("\n", "")
print("Length after removing newlines:", len(text))

print("Writing results to output file...")
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for i in range(0, len(text), CHARS_PER_LINE):
        f.write(text[i:i + CHARS_PER_LINE] + "\n")

print("Done!")
input("Press Enter to exit...")
