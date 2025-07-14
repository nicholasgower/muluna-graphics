#!/bin/bash

# Check for input argument
if [ $# -lt 1 ]; then
  echo "Usage: $0 input.png [output.png]"
  exit 1
fi

# Create output dir if needed
mkdir -p output

for f in "$@"; do
    INPUT="$f"
    # OUTPUT="${2:-adjusted_$INPUT}"

    # This fx expression remaps alpha as follows:
    # For example, it maps 0.5 (50%) to 0.2 (20%), linearly scales around it.
    # You can tweak the expression for other mappings.
    convert "$INPUT" \
    -channel A \
    -fx 'a<=0.5 ? a*(0.8/0.5) : 0.8 + (a-0.5)*(0.2/0.5)' \
    "output/$f"

    echo "Saved adjusted file to $OUTPUT"
done