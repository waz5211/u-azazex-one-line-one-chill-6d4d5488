"""One line of horror for make.fun's "One Line, One Chill" bounty.

The scare: a child casually treats an unseen presence as a normal
member of the household, and the morning evidence — an empty plate and
a chair still warm — quietly confirms the presence is real, was sitting
at the table, and ate. The dread comes from the domestic routine
absorbing the impossible, and from the implication that the thing in
the walls is not only hungry but already being served, night after
night, by a family that has stopped asking questions.
"""

import os

LINE = (
    "My son has started setting a place at the table for the boy who lives "
    "in the walls, and this morning the plate was empty and the chair was "
    "still warm."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    assert "\n" not in LINE, "line must be a single line"
    assert LINE.count(".") == 1 and LINE.endswith("."), (
        "line must be exactly one sentence"
    )
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
