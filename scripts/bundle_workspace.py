import os
from pathlib import Path

def generate_bundle():
    root = Path(__file__).resolve().parent.parent
    output_file = root / "GEMINI_NOTEBOOK_WORKSPACE_CONTEXT.md"

    files_to_bundle = [
        "README.md",
        "AGENTS.md",
        "SOUL.md",
        "USER.md",
        "MEMORY.md",
        "00-project/PROJECT.md",
        "00-project/TIMELINE.md",
        "00-project/PITCH-DECK.md",
        "10-pedoman/CHECKLIST-PEDOMAN.md",
        "20-literatur/EVIDENCE-LEDGER.md",
        "30-riset/CLAIM-MATRIX.md",
        "30-riset/EXPERIMENT-LOG.md",
        "40-naskah/OUTLINE.md",
        "50-review/REVIEWER-RUBRIC.md",
        "50-review/REVIEW-LOG.md",
    ]

    # Add all skills from skills/ directory
    for skill_file in sorted(root.glob("skills/*/SKILL.md")):
        rel = skill_file.relative_to(root).as_posix()
        if rel not in files_to_bundle:
            files_to_bundle.append(rel)

    content = [
        "# PKM-KC 2027 WORKSPACE — FULL CONSOLIDATED CONTEXT",
        "> **Sumber Kebenaran Repositori PKM-KC 2027** untuk diintegrasikan ke **Gemini Notebook (NotebookLM / Google AI Studio)** menggunakan model **Gemini 4 Neon** (1M Token Context Window).",
        "> Dokumen ini memuat seluruh kontrak operasional, profil tim, ide karsa cipta, pitch deck, regulasi Belmawa 2026, matriks bukti empiris, dan 10 modul skill otomasi agen riset.",
        "",
        "---",
        ""
    ]

    bundled_count = 0
    for rel_path in files_to_bundle:
        p = root / rel_path
        if p.exists():
            text = p.read_text(encoding="utf-8")
            content.append("<!-- ======================================================== -->")
            content.append(f'<workspace_file path="{rel_path}">')
            content.append(text.strip())
            content.append("</workspace_file>\n")
            bundled_count += 1
            print(f"Bundled: {rel_path} ({len(text)} chars)")
        else:
            print(f"Warning: {rel_path} not found!")

    output_file.write_text("\n".join(content), encoding="utf-8")
    size_kb = output_file.stat().st_size / 1024
    print(f"\n[OK] Success! Generated: {output_file.name} ({bundled_count} files, {size_kb:.2f} KB)")

if __name__ == "__main__":
    generate_bundle()
