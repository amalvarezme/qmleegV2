# Official preparation of `qmleeg-toy-eeg` (version 1)

The single preparation the proof of concept and the full experiments both read.
Change it here, never in an experiment's own code.

## Source

- File: `datasets/qmleeg-toy-eeg/qmleeg-toy-eeg.csv`
- sha256: `cec99326fbf85e5b10703208df24f0e13f7f641c0be3bda342611c49d47025fb`
- Rows: 480; groups (subject): 20

## Steps

1. Read `datasets/qmleeg-toy-eeg/qmleeg-toy-eeg.csv`; check its sha256 against the value above and refuse on mismatch.
2. Assign every `subject` to one of 5 folds by stratified group k-fold on `label` (seed 42); no subject appears in two folds.
3. A row's fold is its group's fold, read from `splits.json` (`assignment`).

## Parameters

| Parameter | Value |
|---|---|
| label | `label` |
| group | `subject` |
| folds | 5 |
| seed | 42 |

## Folds

| Fold | Rows | Groups | Classes |
|---|---|---|---|
| 0 | 96 | 4 | {"0": 48, "1": 48} |
| 1 | 96 | 4 | {"0": 48, "1": 48} |
| 2 | 96 | 4 | {"0": 48, "1": 48} |
| 3 | 96 | 4 | {"0": 48, "1": 48} |
| 4 | 96 | 4 | {"0": 48, "1": 48} |
