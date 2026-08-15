from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
    Summarize the research paper "{paper}".

    Requirements:
    - Style: {style}
    - Length: {length}

    Include:
    1. Main idea
    2. Key contributions
    3. How it works
    4. Important results
    5. Conclusion

    Use clear, well-structured markdown and tailor the explanation to the selected style and length.
    """,
    input_variables=['paper', 'style', 'length']
)

template.save('template.json')