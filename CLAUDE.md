# qmleegV2 — Claude Code Entrypoint

This standalone paper workspace is managed by `papersmith` 0.67.0.

## Canonical context

- **Workspace configuration**: `papersmith.yaml`
- **Domain guidelines**: `guidance/paper-guide/`
- **Available capabilities**: `skills/*/SKILL.md`
- **Research topic**: Quantum Machine Learning for EEG (QMLEEG)

## Canonical agents

- `ai-auditor` — Audits a manuscript draft or block for writing quality (monotone cadence, overused academic phrasing, lexical diversity, connector use, sentence openings, redundancy) using `paper_ai_metrics`, and verifies strict adherence to F5 invariants. A readability check, never an AI detector. Never invoked by any code path; `write` and `humanize` reconcile your account against the real draft, they never trust either from you.
- `audit-report` — One stretch: audit a subject that enumerates a closed set — accepted operations, subcommands, error codes, shipped assets — for the gap between what its running code accepts and what its own documentation claims. Derives both halves independently rather than reading either, and arrives at the report. Reports; never repairs.
- `contract-auditor` — Reads a contract's `## Disqualifiers` bullets verbatim and judges a drafted block against each one, returning fires/clear/undecidable per bullet with a quoted span for every `fires`. Never invoked by any code path; `write` reconciles your account against the real bullets and the real draft, it never trusts either from you.
- `dataset-curator` — One stretch of the datasets flow, from a dataset need to its arrival: a toy set and a licensed, checked, prepared dataset that the proof of concept and the full experiments both read, published privately only on the operator's consent. Synthesize the seeded toy set, fetch a source whose license is already allowed, measure it with `qc`, write the one official subject-wise preparation with `prepare`, and run `publish` for real only with the operator's own consent tokens. Stages: toy, checked, prepared, published.
- `dataset-scout` — One stretch of the datasets flow, from a stated research question or paper to ranked dataset candidates whose source licenses are already decided: search the paper's official repository and data statement on the web, run the skill's own `search` verb across the remote dataset hosts, and record a `license` decision per candidate. Stages: sourced, licensed. Never downloads data it cannot license, and never uploads anything.
- `deliberation-publish` — One stretch of proposal-deliberation, beginning where the operator accepted a change and ending at the successor revision published and current, which is the only form the mathematics travels in. Resolve the entry, compose the replacement by substituting inside it rather than handing back a bare block, and publish. The deliberation itself is not in this stretch and may not be: nothing but the operator closes that.
- `diagram-author` — Authors one standalone TikZ diagram (<id>.tex plus <id>.diagram.json) and drives its own compile loop through render, up to the repair budget. Never draws a chart from measured numbers -- that is a separate verb (place) this agent never calls.
- `experimental-publish` — One stretch of experimental-deliberation, beginning where the operator accepted a change and ending at the successor revision published and current, which is the only form the experiments travel in. Resolve the entry, compose the replacement by substituting inside it rather than handing back a bare block, and publish. The deliberation itself is not in this stretch and may not be: nothing but the operator closes that.
- `experimental-validation` — One stretch of experimental-deliberation, the `validated` stage: search for the area's standard evaluation protocol, its accepted metrics, its current baselines, the dataset the plan runs on, and the seeds, repetitions and significance test the area expects, then verify each baseline's own repository and venue year and tag every external URL with the date a search actually reached it. Ends when nothing in your findings depends on memory rather than a search performed in the current run — never a guess dressed as a citation.
- `experiments-build` — One stretch of experimental-implementation, between two of the operator's gates: from an approved map of the protocol's declared steps to runnable commands, up through every measurement the protocol declares having a place to land. Materialize what the protocol needs, wire each declared step to a runnable command, and instrument every measurement so it can actually be run and read back. Decides nothing and asks nothing — it ends by reporting what it found and what establishing it cost.
- `experiments-reviewer` — One stretch of experimental-implementation, between two of the operator's gates: from an instrumented implementation — every measurement the protocol declares already has a place to land — to a findings report the operator reads before any rehearsal or launch. Review the code against the bound experiments protocol on four dimensions: code quality, optimisation of the simulation and data path, remote GPU use, and the statistical tests the protocol declares. Reads and runs the target's own tests and linters only; never repairs, never launches — it ends by reporting what it measured.
- `experiments-tutor` — One turn of the experiments tutor: begins with the operator's message, a mode and a decision area from the dashboard's experiments panel, ends at one structured turn — one hint grounded in the protocol, approvals, code and results it read, one question, an assessment of the design with quoted evidence, the risks it sees, and any change of decision drafted for /experimental-deliberation. Reads; never writes the workspace.
- `experiments-walk` — One stretch of experimental-implementation, between two of the operator's gates: from per-step placement decisions already taken to the launch they must authorize. Walk the declared flow act by act in its own order — run the local steps, commit each step's product, refresh the position, generate the job folders a remote step needs and stop at the rehearsal, which no act here performs and the doctrine leaves to a person. Stops at the launch and has no path to submitting a campaign.
- `figure-auditor` — Audits one standalone TikZ diagram against the prose that describes it: runs `figure audit` for the semantic verdict, runs `figure-review probe` to measure whether the visual half is answerable and bounds it to that skill's checklist only when the probe resolves a link, checks typographic parity, and reports measured findings. Never repairs the figure, never re-derives a verdict by eye, and never invents a visual one.
- `figure-visual-reviewer` — One visual pass over one rendered diagram whose mechanical audit already passed: reads a preview of at most 1400 px once and judges what no script can -- legibility at print scale, centring and balance, overlaps and crowding, labels and arrows reading correctly. Returns PASS, or FAIL with concrete fixes, and PASS plus an UNCERTAINTY line when unsure. Never edits a file.
- `implementation-build` — One stretch of proposal-implementation, between two of the operator's gates: from an approved object-to-module map to the findings report they decide on. Materialize the object scaffolding, write one module per mathematical object with its provenance and invariant tests, sweep the declared configurations, rule on each remedy's admissibility BEFORE measuring it, and validate what was admitted. Decides nothing and asks nothing — it ends by reporting what it found and what establishing it cost.
- `implementation-walk` — One stretch of proposal-implementation, between two of the operator's gates: from per-step placement decisions already taken to the launch they must authorize. Walk the declared flow act by act in its own order — run the local steps, commit each step's product, refresh the position, generate the job folders a remote step needs and stop at the rehearsal, which no act here performs and the doctrine leaves to a person. Stops at the launch and has no path to submitting a campaign.
- `insumos-observer` — Reads the paper's four declared input sources — proposals/, experiments/, the target implementation repository's code, and its own run outputs — and reports, for each of the five observable facts, whether it is satisfied and by what evidence. Never decides a value and never runs `declare`; its report is what a human reads before running `declare` themselves.
- `math-tutor` — One turn of the Socratic math tutor: begins with the reader's message and any hand-written images they attached in the dashboard's math panel, ends at one structured turn — the image read back as LaTeX and parts, one hint, one question, and an assessment of understanding quoted from the reader's own words — always tied to why the paper's novelty holds. Reads; never writes the workspace.
- `novelty-screener` — One stretch of the plausibility flow: discuss the stated hypothesis against the scout pool's abstracts, grade each claim's novelty and conceptual plausibility with quoted evidence — every grade provisional until ingestion — rank the top 5 references for the later ingestion stage, and close with one plausibility paragraph on where the proposal stands. Ends at the report; publishes nothing, writes nothing, ingests nothing, and deliberates nothing.
- `paper-ingestion` — Turn a paper into the form it can actually be used in — equations as LaTeX, tables as tables, figures as files — and arrive at a document a person can read and a later session can cite, which a PDF is not. Stages: filed, extracted, readable. Nothing here is a person's decision: ingestion asks nobody.
- `paper-replicator` — One stretch of proposal-implementation, the `fidelity` stage for a referenced method (a comparison or baseline paper): first search for the paper's published code; when it exists, adopt it pinned to a commit and audit that it corresponds to the paper and is implemented correctly, and only when it does not, reimplement the method from the paper's ingested Markdown (and the cited papers it depends on, when ingested). Either way it ends at code inside the target repository's layout, a REPLICATION.md correspondence table, invariant tests and a toy-set smoke run. Search, then audit or plan, analyze, code, verify. Never invents a result, never claims fidelity it did not test, and never launches a remote run — it ends by reporting what it wrote and measured.
- `paper-reviewer` — Reviews the assembled paper the way a main-track reviewer of a top machine-learning conference would: fills every field of the official review form (summary, contribution type, strengths and weaknesses on quality, clarity, significance and originality, the four 1-4 ratings, 3-5 actionable questions, limitations, overall 1-6, confidence 1-5, ethics flag, formatting concerns), backs each originality, pertinence and coherence judgement with a quoted passage from the paper and from the workspace's own SOTA pool or ingested references, and audits adjusted novelty concordance between problem, title, abstract, introduction and verified empirical findings. Ends at the review report the operator reads before revising; never edits the paper, never submits it, and never claims a lack of novelty without naming the reference that holds the idea.
- `redactor` — Drafts one contract block's LaTeX from exactly five inputs — the contract's own prose (verbatim), the block's evidence set, its mode, its style set (empty is valid), and its own bound source sections (empty is valid) — and hands back a binding map beside the draft, naming every sentence's source. Never invoked by any code path; `write` judges what you return, it never calls you.
- `section-grounding-auditor` — Reads a transposition block's own bound source section, verbatim, and judges each subject sentence's support against it, returning supported/unsupported/undecidable per sentence with a quoted span for every supported. Never invoked by any code path; write re-derives both the subject sentences and the section bytes independently and reconciles your account against them, it never trusts either from you.
- `sota-grapher` — One stretch: map the scout pool to its solar-system constellation — one system per paper grouped by family, at most 20 planets each, links running between planets of different systems — as sota-pool/atlas.json plus the single sota-pool/atlas.html, and drive the skill's own checker and renderer until both run green. Ends at the HTML plus the green runs; judges truth never, repairs nothing outside sota-pool/.
- `sota-scout` — One stretch: scout a stated research idea across the open literature — at most 25 resolved references with verbatim abstracts, each in exactly one primary family, 3 to 7 families per pool, and a provisional plausibility note — as sota-pool/candidates.json. Ends at the pool; ingests nothing, grades nothing as final, files nothing into guidance/.
- `style-sampler` — Resolves the equivalent block, whole, from each guidance/ folder the registry classes style-reference — and returns it verbatim, never excerpted. What you return becomes R, the only material any later overlap check may compare a styled draft against.
- `venue-adapter` — Reads a chosen journal's author guidelines and document template and measures the manuscript against them: writes the venue's requirements (each one a quoted passage and the url it came from), alerts on sections that must be adjusted, sections the venue needs and smith lacks, and every inconsistency between smith's base template and the venue's, and proposes an adjustment plan only when one is prudent, iterating it with the operator until the operator approves its exact text. Ends at an approved plan (or an audit that needs none) and a built paper/venues/<slug>/main.tex; never changes a word of the paper, never invents a requirement, and never submits.

The `.claude/agents/` tree is the single source of truth for agent
definitions. Other harness documents are generated projections; do not fork
their instructions manually.

## Slash commands

Every top-level skill under `skills/` is also generated as a slash command in
`.claude/commands/<name>.md`, so it can be invoked directly. Each command body
loads that skill's `SKILL.md` and passes your text through as `$ARGUMENTS`. The
directory is a framework artifact: `smith audit --check-drift` reports drift
and `smith upgrade` restores it, so do not edit it by hand.

## Language

Reply to the human in the language they write in (Spanish or English).
Everything else stays English regardless of the conversation language: skills,
agent definitions, delegations and messages between agents, tool inputs, and
every generated artifact (code, comments, docs, commit messages, the data files
the dashboard displays under `.papersmith/` and `sota-pool/`, and paper
internals unless the paper declares another language). The dashboard's language
selector translates its own labels, never a workspace file, so a file written in
Spanish shows Spanish under English; only the conversation with an agent
follows the human's language.

## Paper construction flow

These are the eleven phases the command center (`smith ui`) shows under
"Pipeline y Avance", in order. Each phase card runs its stage: a slash command
`/<skill> <text>` typed into an agent, a `smith` command, or a link to the
panel that owns the work. The dashboard locks each phase until the one before
it is verified from its evidence on disk, with an explicit override, and every
skill refuses when its input is missing.

1. **Harness**: `smith status .` and `smith audit . --check-drift`;
   `/upgrade-project` when the workspace runs an older release.
2. **Plausibility**: `/plausibility <the idea in at least two sentences>`. It
   scouts about 25 SOTA references, draws `sota-pool/atlas.html` and grades the
   claims. Nothing is ingested until the operator accepts the report.
3. **Ingestion**: `/paper-ingestion <PDF or URL>` (or `smith ingest`)
   turns the accepted top 5 into Markdown under `guidance/`, with equations
   as LaTeX.
4. **Proposal deliberation**: `/proposal-deliberation` keeps managed revisions
   `proposals/research-concept-<slug>-rNN.md` (or slugless
   `research-concept-rNN.md`), built in this order: the
   central problem and its pillars, then the hypotheses each pillar predicts,
   then the mathematics in `$$ … \tag{N} $$` display blocks. Each step stays
   locked until the one before it exists on disk; the dashboard's
   Mapa Conceptual & Modelo tab shows the three steps with a "Generar y
   deliberar" button that types the step's `/proposal-deliberation` into the
   agent.
   - **Concept map and mathematics**: before implementing a revision, discuss
     its pillars, hypotheses and concept layers and its equations with
     `/math-tutor`, the Socratic tutor that also reads hand-written pages.
   - **Concept trees**: `novelty.problem_tree` in
     `.papersmith/model_spec.json` holds the central problem, its 2 to 3
     direct causes and their effects; at least 2 pillars each reach a
     hypothesis through its `pillars` field. Every statement and citation
     reason is in English; the central problem fits in 400
     characters, every other statement in 300. The central problem and the
     causes state a negative condition, never "Lack of", "No", "Need for",
     "Requires" or an infinitive. The problem, each cause, each pillar and
     each hypothesis cite Q1 or Q2 journal articles at most 4 years old,
     checked against `sota-pool/journal-ranks.json`, which `python
     skills/_core/results/citations_cli.py rank --root .` writes from the SJR
     table. A preprint also counts when an author belongs to an accepted lab,
     found in OpenAlex or confirmed by the operator with `citations_cli.py lab`.
     The fourth step stays open until both trees hold.
   - **SOTA citations**: every pillar, hypothesis, concept-map layer and
     numbered equation is justified by 2 to 5 references of
     `sota-pool/candidates.json`, each with its reason and a verbatim quote of its abstract that holds the idea, in
     `.papersmith/citations.json`, and shown beside the idea. This is the
     phase's fourth step, launched from its button in the stepper; `python
     skills/_core/results/citations_cli.py check --root .` says what is owed. The quote is 20 to 300 characters of the pool record's
     abstract, verbatim and starting and ending on word boundaries, so a
     reference without an abstract cannot be cited; `python
     skills/_core/results/citations_cli.py routes --root .` prints each
     reference with the ideas it is cited for and their quotes. Each reference the ideas cite must also be drawn in the SOTA constellation: `smith atlas coverage .` lists the ones it is not.
   - **Contribution type**: once the hypotheses are discussed and the
     mathematics and the novelty proposed, the `paper-reviewer` agent
     classifies the proposal's contribution type
     (`contribution_type` in `.papersmith/model_spec.json`), shown right after
     the hypotheses. This judge-reviewer is the phase's fifth step: the
     "Lanzar el juez-revisor" button, on that card and in the stepper, launches
     it, and Phase 5 stays locked until it records a type.
5. **Proof of concept and experiments**, in this order:
   `/experimental-deliberation` writes the protocol in `experiments/`; a toy
   set (`/datasets synth`); replication of the comparison methods;
   the proof of concept (`/proposal-implementation`), done when its
   `Results/discussion.json` is complete; the operator's verification of
   that proof of concept (G-EXP-POC: its results and contrasted hypotheses,
   in the Novedad & Hallazgos tab or with `smith novelty approve --gate
   poc`); a timing estimate; an optional hyperparameter search
   (`/hyperparameter-search`); the full experiments
   (`/experimental-implementation`), locked until G-EXP-POC passes; the code
   review (`experiments-reviewer`); the remote rehearsal; and the operator's
   launch. The Experimentos tab steps through SOTA citations → proof of
   concept → verify → full experiment with one button each.
   - **Experiment citations**: every experiment of the latest protocol carries
     its 2 to 5 SOTA citations in `.papersmith/citations.json`, launched from
     the Experimentos tab. Until then `/proposal-implementation` and
     `/experimental-implementation` stay locked and G-EXP-POC refuses its
     approval (`SOTA_CITATIONS_OWED`). Then `smith atlas coverage .` lists the
     cited references the SOTA constellation does not draw yet.
   - **Data**: `/datasets synth|search|license|qc|prepare|publish` gives both
     stages a seeded toy set always and one official dataset (agents
     `dataset-scout`, `dataset-curator`): license checked, quality measured,
     one subject-wise preparation, published privately only with the
     operator's consent.
   - **Replication of comparison methods**: `/proposal-implementation` hands
     each baseline paper to `paper-replicator`, which looks for the paper's
     published code first, adopts it pinned and audits it against the paper,
     and reimplements the method only when no code exists.
   - **Timing and placement**: a short timing probe in `Results/timing.json`
     before the pilot and again before the full run; the dashboard's
     Experimentos tab lists the local, Kaggle and Colab options, and
     `/remote-parallelism` (`estimate`, then `assess --owners <distinct
     owners>`) decides whether to split a campaign. A run whose local
     estimate exceeds 20 minutes runs on Colab or Kaggle, never locally, and
     a proof of concept is sized to at most 5 hours where it runs.
   - **Hyperparameter search** (only when the deliberation judged it
     worthwhile): `/hyperparameter-search plan|report|status` runs an
     Optuna search nested inside each outer fold, with the same trial
     budget for every arm and a declared importance evaluator; its contour
     and importance plots land in `Results/hpo/` and the Experimentos tab
     shows them. It runs remotely like the full runs.
   - **Experiment diagrams**: when the proof of concept is approved
     (`AGREED.md`) and again when the full experiments are
     (`Experimental_AGREED.md`), `/experiment-diagrams poc` and then
     `/experiment-diagrams experiments` (or the Experimentos tab's
     "Generar diagrama") draw each one as a TikZ figure. The operator
     validates each one in that tab ("Validar diagrama") or by approving it
     explicitly in the conversation, which the agent then records with
     `diagram_cli.py validate` (the operator's words verbatim and the hash
     of the PNG shown); `submit` refuses `DIAGRAM_NOT_VALIDATED` until then,
     and drawing it again asks again.
   - **Experiments tutor**: in the Experimentos tab, `/experiments-tutor`
     explains, questions and evaluates each design decision (architecture,
     hyperparameters, ablations, significance tests, the toy set, training,
     upper bounds, baselines and their implementation) from the protocol,
     the approvals, the code and the results; it never invents a number, and
     a change of decision goes back to `/experimental-deliberation`.
   - **Remote runs**: accounts associated with distinct emails
     (`smith team add … [--email <email>] --attest`), `/kaggle-accounts validate`, then
     `/remote-execution`: generate-job → submit --smoke → fetch --smoke /
     smoke record → readiness → gate → submit → status / poll → fetch.
   - **Findings and novelty**: once a stage's discussion is complete, the
     `paper-reviewer` agent classifies the contribution type of its
     findings (`contribution_type` in `Results/discussion.json`). The
     Novedad & Hallazgos tab launches that judge from a button on its
     contribution-type card, and G-EXP-POC and G-NOVELTY refuse their approval
     (`JUDGE_REVIEW_OWED`) while a complete discussion of that stage has no
     type. The tab contrasts the hypothesis verdicts with the SOTA
     pool and the operator records `G-NOVELTY` (`smith novelty approve` or
     `iterate`) before the paper is written.
   Only the operator authorizes a launch. The phase passes only with a
   published protocol with every experiment cited, a proof of concept
   discussed and verified, and a full
   experiment discussed.
6. **Scaffolding**: `/paper-writing` opens the `paper/` tree and its section
   contracts.
7. **Declarations**: `/paper-writing mark …` records each decision of the
   paper (authorship, funding, data and code, ethics, language, style).
8. **Writing**: `/paper-writing` writes one named block at a time. Every
   claim needs a source that holds it (`resolve`). `refs.bib` comes from
   `bib build`, never from hand edits. After the citations change, run
   `resolve --references`: it stores each cited paper's metadata and abstract
   in `paper/.paper-writing/references.json`, and `verify` fails while a cited
   key has no record there. A paper it cannot resolve, offline included, keeps
   a record and passes with a note. Then `smith atlas coverage .` lists the cited papers the SOTA constellation draws only as placeholders: their abstracts go to the pool (`sota-scout`) and their systems to the constellation (`sota-grapher`).
9. **Figures**: `/figure-review <figure id>` checks a compiled
   `paper/Figures/<id>.pdf`.
10. **Paper**: compile `paper/main.tex` to `paper/main.pdf` (dashboard:
    the PDF preview tab, whose style and redundancy panel scores each
    section from 0 to 100).
11. **Audit** (transversal): `smith audit .` and `/skill-audit <subject>`.
    Audits report; they never repair.

The human gates are plausibility acceptance, proposal and experimental
acceptance, the proof-of-concept verification (G-EXP-POC), the novelty
decision (G-NOVELTY) and launch authorization. An agent never passes a gate
on the operator's behalf.
