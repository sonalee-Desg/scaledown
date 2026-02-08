## Policy Document Navigator 🇮🇳
A government policy analysis tool designed to help citizens, students, and researchers understand long and complex policy documents using AI-inspired techniques.


## Problem
Government policies are often 50–200+ pages long, written in complex legal language, making them inaccessible to the public.


## Solution

This project ingests large Government of India policy PDFs and:
\- Extracts and processes policy text
\- Compresses content using a ScaleDown approach
\- Generates plain-language summaries
\- Analyzes stakeholder impact across multiple policies


## Features

\- Policy PDF ingestion (60–120 pages tested)
\- ScaleDown summaries (plain language)
\- Stakeholder impact analysis
\- Multi-policy comparison support
\- Focus on Indian student education policies


## Project Scope & Constraints

- This is a prototype-level GenAI system focused on document understanding, not policy enforcement.
- Summaries are informational and not legally binding.
- The system prioritizes readability over legal precision.
- Full RAG and live API deployment were kept out of scope due to time constraints.

  
## Tech Stack

\- Python
\- PyPDF2


## My Contribution & Learning

I personally selected Government of India student education policies and designed the overall workflow of the system.

My work included:
- Structuring the end-to-end pipeline
- Testing policy ingestion on real 60–120 page PDFs
- Verifying extracted text correctness
- Applying ScaleDown-style summarization logic
- Mapping stakeholder impact manually and validating AI-generated outputs

Through this project, I learned how GenAI systems can be responsibly applied to civic and public-interest use cases, especially in contexts where transparency and accessibility matter more than automation.


## AI Assistance Disclosure

AI tools were used for guidance and conceptual understanding. All policy selection, pipeline structuring, testing on real PDFs, validation of outputs, and documentation were performed by me based on my own understanding.


\## Author

Sonali Maity





