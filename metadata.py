from pathlib import Path

DATA_DIR = Path("data")

metadata_map = {
    "letter": {
        "category": "entry_clue",
        "priority": 10,
        "memory_type": "intro",
        "retrieval_mode": "always",
        "volatility": "stable"
    },
    "newspaper": {
        "category": "public_record",
        "priority": 7,
        "memory_type": "official_version",
        "retrieval_mode": "context",
        "volatility": "stable"
    },
    "diary": {
        "category": "visitor_account",
        "priority": 8,
        "memory_type": "witness",
        "retrieval_mode": "clue",
        "volatility": "stable"
    },
    "eastern_wing": {
        "category": "restricted_area",
        "priority": 9,
        "memory_type": "investigation",
        "retrieval_mode": "clue",
        "volatility": "stable"
    },
    "head_librarian_journal": {
        "category": "core_testimony",
        "priority": 10,
        "memory_type": "primary_witness",
        "retrieval_mode": "truth",
        "volatility": "stable"
    },
    "archivist_rowan_statement": {
        "category": "contradictory_testimony",
        "priority": 10,
        "memory_type": "witness",
        "retrieval_mode": "truth",
        "volatility": "stable"
    },
    "missing_visitor_fragment": {
        "category": "corrupted_memory",
        "priority": 10,
        "memory_type": "hidden_truth",
        "retrieval_mode": "revelation",
        "volatility": "unstable"
    },
    "lower_door_transcript": {
        "category": "final_revelation",
        "priority": 10,
        "memory_type": "ending",
        "retrieval_mode": "final_truth",
        "volatility": "impossible"
    }
}

def has_frontmatter(text):
    return text.startswith("---\n")

for md_file in DATA_DIR.glob("*.md"):
    name = md_file.stem
    text = md_file.read_text(encoding="utf-8")

    if has_frontmatter(text):
        print(f"Skipped existing metadata: {md_file}")
        continue

    meta = metadata_map.get(name, {
        "category": "general",
        "priority": 5,
        "memory_type": "general",
        "retrieval_mode": "query_only",
        "volatility": "medium",
    })

    frontmatter_lines = ["---"]
    frontmatter_lines.append(f"title: {name}")

    for key, value in meta.items():
        frontmatter_lines.append(f"{key}: {value}")

    frontmatter_lines.append("source_type: markdown_memory")
    frontmatter_lines.append("---")
    frontmatter_lines.append("")

    frontmatter = "\n".join(frontmatter_lines) + "\n"

    md_file.write_text(frontmatter + text, encoding="utf-8")
    print(f"Added metadata: {md_file}")