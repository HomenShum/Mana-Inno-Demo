﻿# rag-a-thon
Use Cases Explored:
1. All Files Async Parallelized Processing
2. Our own querying method that involved sparse dense retrieval + parallel request merge responses + instructor pydantic class usage for raw text data transformation and transmission
3. Llama_index llama parser
4. Vectara Query
5. APIs deployed for fast and accurate parsing for SUPPORTED_EXTENSIONS =
[
    ".docx", ".doc", ".odt", ".pptx", ".ppt", ".xlsx", ".csv", ".tsv", ".eml", ".msg",
    ".rtf", ".epub", ".html", ".xml", ".pdf", ".png", ".jpg", ".jpeg", ".txt"
]

It works well for travel itinerary retrieva, meeting note retrieval, customer solution and product recommendation
The speed is faster than that of llama parser when scaled to dozens and hundreds of documents while maintaining precision in responses
Only key issue is complex table, which llama parser integration helped to ease on when the llama parser recursive retrieval result is integrated along with the input prompt.

Vectara integration was consuing at first with the three IDs, but eventually figured out.
BentoML integration was under going deployment, easy to use, love the interface.
