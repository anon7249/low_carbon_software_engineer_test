# Take-Home Task: Junior Software Engineer, Low Carbon

## Before you start

- **Time budget:** Please spend no more than **2-3 hours** across all three parts below. We are not expecting a polished production system. We want to see how you think, investigate, and communicate. If you find yourself going beyond 3 hours, please stop where you are and submit what you have, noting what you'd do next.
- **AI tools are allowed and expected.** Use tooling that you have available to you and that you are comfortable using (Copilot, ChatGPT, Claude, etc.). We are specifically interested in how you use them. Submissions that show no evidence of judgement about AI-assisted output (i.e. everything is unreviewed AI output, or AI use is undisclosed) will be marked down. Please see the "AI usage and assumptions" section below for more detail.
- **The dataset is entirely synthetic** and was generated for this exercise. It's structured similarly to real operational data but the domain (a fleet of vending machines) is deliberately unrelated to what Low Carbon actually does, so nothing here reflects real company data or systems.
- You do **not** need an Azure, Fabric, or any cloud account for this. Everything should run locally.
- **Notebooks are accepted.** If Jupyter is your normal way of working, submit a `.ipynb` file instead of (or alongside) a `.py`/`.sql` file if you prefer. If submitting a notebook, run it through fully before you submit, so we can read your outputs without needing to execute anything ourselves.

## The dataset

`data/readings.csv` contains hourly telemetry from six vending machines over two weeks:

| Column | Description |
|---|---|
| `machine_id` | Machine identifier |
| `timestamp` | Reading time (hourly) |
| `internal_temp_c` | Internal temperature, °C |
| `stock_level_units` | Current stock level |
| `door_open_count` | Number of times the door was opened that hour |
| `transaction_count` | Number of vending transactions that hour |
| `total_sales_gbp` | Revenue that hour, GBP |
| `connectivity_status` | `online` or `offline` |

`data/machines.csv` contains one row per machine, with its site name and `capacity_units` (maximum stock level).

This is representative of a real-world, messy dataset. **Some of the issues are described below.** We've deliberately left some issues unflagged. 

## Part 1: Data quality checks

Build and test a check for each of the following **three known issue types**:

1. **Duplicate readings** - rows that shouldn't both be there.
2. **Missing or blank readings** - data that's absent or null when it shouldn't be. Think about this one in more than one way, as a reading can be missing in more than one sense.
3. **Implausible values** - readings that are physically or logically impossible, in any of the columns.

For each of the three checks, write either a Python function or a SQL query that implements it (you're welcome to do both for a given check, but you don't need to).

**Across your three checks as a whole, at least one must be a SQL query and at least one a Python function**. Beyond this minimum, the choice per check is yours.

For each check, write at least one test that meaningfully proves it works: feed it input containing the issue it's meant to catch, and assert on the specific result you expect. A test that would still pass even if the check did nothing, or wasn't there at all, doesn't count.  For a Python check, this could be a worked example using sample inputs or an automated test (e.g. a `pytest` test). For a SQL check, a worked example is enough: show a small set of input rows and the output your query should produce against them, with a line on why. You don't need to actually execute your SQL to satisfy this, but if you'd like to verify it yourself, use any local SQL engine you're comfortable with (DuckDB is a good default if you don't have a preference, as it can query the CSV directly with no load step).

Whichever format you use (`.py` script/`.sql` file/`.ipynb` notebook), each check should be a properly defined function or query, not loose exploration. If you're working in a notebook, that means each check should still live in its own cell(s) as a real, callable function, not scattered across ad hoc exploration cells.

As you go, keep a short running note of anything else you notice in the data that isn't covered by the three checks above. You don't need to build a tested check for these, just tell us what you found, how you came to find it (e.g. the query you executed) and why you think it matters. Save these notes as `FINDINGS.md`. We're not expecting you to find everything; a well-reasoned list of what you noticed beyond the flagged items is sufficient.

## Part 2: Write it up as a pull request

Write a pull request (PR) description for the code you produced in Part 1, as if you were submitting it for review to a teammate who hasn't seen it yet. Save it as `PULL_REQUEST.md`.

We're deliberately not giving you a template or a list of sections to include. Deciding what a reviewer actually needs to know is part of what we're looking at. We're not expecting a real git repository or commit history; this is about the write-up itself.

## Part 3: A helpful visual

Produce **one** visual that would help an Operations Team understand data quality across the fleet. Some suggested visualisation formats are below. Pick whichever format you're most comfortable with, we are assessing what the visual represents and why it is useful, rather than how it was produced. 

- **A Power BI** `.pbix` file, if you have access to Power BI Desktop.
- **A static HTML page**, self-contained (inline CSS/JS, no server or build step needed).
- **A single PNG image**, generated via Python (e.g. matplotlib).

Alongside the visual itself, please include:
- **The source behind it, where applicable.** For example, please provide the Python script if you produced a PNG (or generated the HTML page programmatically). For a hand-written HTML page, the page itself is the source. A `.pbix` file already contains its own model and query logic, so nothing extra is needed there.
- **A short description (2-4 sentences)** of what the visual shows and why you chose that particular view, saved as `VISUAL.md`.

We may follow up on this in an interview conversation, so be ready to talk through the choices you made.

## AI usage and assumptions

Include a separate `AI_USAGE.md` file stating which AI tools you used, for which specific parts of the task, and where you used AI-generated code or text. Let us know what you changed, kept, or rejected, and why. Please be specific; generic statements such as "used ChatGPT for the whole thing" is not sufficient.

Also note in this file any assumptions you made during the assignment, in a short paragraph. For example, what "implausible" means to you for a column we haven't defined or how you interpreted "missing" beyond blanks.

## What to submit

Please submit a zipped folder containing:
- Your Python and/or SQL source files or notebook, including your three checks with tests or worked examples
- `FINDINGS.md` - anything you noticed in the data, beyond the three flagged checks
- `PULL_REQUEST.md` - your write-up of code produced in Part 1, for a code reviewer who hasn't seen it
- Your Part 3 visual (`.pbix`, `.html`, or `.png`), alongside its source script if applicable
- `VISUAL.md` - your description of what the visual shows and why
- `AI_USAGE.md` - your description of which AI tools you used, for what, and the assumptions you made


Submissions should be made by email to Charlie.Jessop@lowcarbon.com by 23:59 BST Wednesday 23rd September, with subject line: 'Junior Software Engineer - {Your name as it appears on your application}'.

If for any reason you require an extension to the deadline, please let us know at your earliest convenience.

## How this will be assessed

For Part 1, we are evaluating whether your three required checks are correct, the quality of your SQL and Python, and your articulation of any further data findings.

In Part 2, we're assessing how clearly you write up your work for a teammate to review.

Part 3 is about producing a meaningful visual, with good reasoning behind it. We are not assessing visual design or formatting polish on the output, beyond it being clear and readable.

Across the whole assignment, we will also be evaluating your judgement about when and how to use AI tools.

If anything in this brief is ambiguous, please make a reasonable assumption, note it, and move on, as we're also interested in how you handle ambiguity. If you are genuinely stuck and cannot move forward, please contact Charlie.Jessop@lowcarbon.com, and we will get back to you as soon as possible.
