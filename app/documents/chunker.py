import re


def split_text(
    text: str,
    chunk_size: int = 800,
    overlap_units: int = 2
) -> list[str]:

    # 改行コードを統一
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    units = []

    # =====================================
    # 1. テキストをunitへ分割
    # =====================================

    for line in text.split("\n"):

        line = line.strip()

        if not line:
            continue

        # 日本語の句点の直後でも分割
        sentences = re.split(r"(?<=。)", line)

        for sentence in sentences:

            sentence = sentence.strip()

            if sentence:
                units.append(sentence)

    # =====================================
    # 2. unitをまとめてChunkを作る
    # =====================================

    chunks = []
    current_units = []

    for unit in units:

        # 現在のChunk + 新しいunit
        candidate_units = current_units + [unit]

        candidate = "\n".join(candidate_units)

        # chunk_size以内なら追加
        if len(candidate) <= chunk_size:

            current_units.append(unit)
            continue

        # 現在のChunkを確定
        if current_units:

            chunks.append(
                "\n".join(current_units)
            )

        # =====================================
        # 3. 最後のN unitをOverlap
        # =====================================

        if overlap_units > 0:

            current_units = current_units[
                -overlap_units:
            ]

        else:

            current_units = []

        # 新しいunitを追加
        current_units.append(unit)

    # =====================================
    # 4. 最後のChunk
    # =====================================

    if current_units:

        chunks.append(
            "\n".join(current_units)
        )

    return chunks