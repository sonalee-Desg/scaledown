import os

DATA_DIR = "data"

stakeholders = {
    "Students": "Access to education, scholarships, reduced financial burden",
    "Government": "Policy implementation, budget allocation, governance",
    "Educational Institutions": "Infrastructure funding, compliance, quality standards",
    "Teachers": "Training programs, recruitment, job stability",
    "Society": "Literacy rate improvement, skilled workforce"
}

print("\nSTAKEHOLDER IMPACT ANALYSIS\n")

for file in os.listdir(DATA_DIR):
    if file.endswith(".pdf"):
        print(f"Policy: {file}")
        print("-" * 40)

        for k, v in stakeholders.items():
            print(f"{k}: {v}")

        print("\n")
