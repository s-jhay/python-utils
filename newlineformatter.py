INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
LINES_PER_GROUP = 145

with open(INPUT_FILE, "r", encoding="utf-8") as infile:
    lines = infile.readlines()

with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:
    for i, line in enumerate(lines):
        outfile.write(line.rstrip("\n"))  # Remove existing newline
        outfile.write("\n")               # Write the line back

        # Add an extra blank line after every 145 lines
        if (i + 1) % LINES_PER_GROUP == 0:
            outfile.write("\n")

print(f"Done! Output written to {OUTPUT_FILE}")
