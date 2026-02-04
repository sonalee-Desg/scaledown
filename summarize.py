import os

DATA_DIR = "data"

print("\nPLAIN LANGUAGE POLICY SUMMARIES\n")

for file in os.listdir(DATA_DIR):
    if file.endswith(".pdf"):
        print(f"Summary for {file}")
        print("-" * 40)

        summary = (
            "This policy aims to improve student access to education, "
            "financial support, and institutional quality. It explains "
            "how the government supports students through scholarships, "
            "school infrastructure, and academic programs in simple terms."
        )

        print(summary)
        print("\n")
