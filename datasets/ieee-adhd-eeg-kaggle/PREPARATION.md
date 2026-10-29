# Official preparation of `ieee-adhd-eeg-kaggle` (version 2)

The single preparation the proof of concept and the full experiments both read.
Change it here, never in an experiment's own code.

## Source

- File: `datasets/ieee-adhd-eeg-kaggle/derived/adhdata-no-v56p.csv`
- sha256: `99d713cdadc09d289a816a2a1196f9129b73f0eba06689cf4317d06219f057c7`
- Rows: 2152244; groups (ID): 120

## Steps

1. Read `datasets/ieee-adhd-eeg-kaggle/derived/adhdata-no-v56p.csv`; check its sha256 against the value above and refuse on mismatch.
2. For each of 5 repetitions, assign every `ID` to one of 5 folds by stratified group k-fold on `Class`, taking the groups largest first in size strata of 5 that its seed shuffles; no subject appears in two folds of one repetition.
3. A row's fold in a repetition is its group's fold there, read from `splits.json` (`repetitions[i].assignment`); the first repetition is also `assignment`.

## Parameters

| Parameter | Value |
|---|---|
| label | `Class` |
| group | `ID` |
| folds | 5 |
| seeds | 42, 123, 456, 789, 1024 |

## Folds, seed 42

| Fold | Rows | Groups | Classes |
|---|---|---|---|
| 0 | 421532 | 23 | {"ADHD": 239492, "Control": 182040} |
| 1 | 439904 | 25 | {"ADHD": 248135, "Control": 191769} |
| 2 | 429410 | 24 | {"ADHD": 240471, "Control": 188939} |
| 3 | 431243 | 24 | {"ADHD": 239991, "Control": 191252} |
| 4 | 430155 | 24 | {"ADHD": 238980, "Control": 191175} |

## Folds, seed 123

| Fold | Rows | Groups | Classes |
|---|---|---|---|
| 0 | 428841 | 24 | {"ADHD": 239467, "Control": 189374} |
| 1 | 430418 | 24 | {"ADHD": 239162, "Control": 191256} |
| 2 | 421510 | 23 | {"ADHD": 239697, "Control": 181813} |
| 3 | 440288 | 25 | {"ADHD": 248528, "Control": 191760} |
| 4 | 431187 | 24 | {"ADHD": 240215, "Control": 190972} |

## Folds, seed 456

| Fold | Rows | Groups | Classes |
|---|---|---|---|
| 0 | 421345 | 23 | {"ADHD": 239568, "Control": 181777} |
| 1 | 431409 | 24 | {"ADHD": 239608, "Control": 191801} |
| 2 | 439732 | 25 | {"ADHD": 248476, "Control": 191256} |
| 3 | 429300 | 24 | {"ADHD": 240250, "Control": 189050} |
| 4 | 430458 | 24 | {"ADHD": 239167, "Control": 191291} |

## Folds, seed 789

| Fold | Rows | Groups | Classes |
|---|---|---|---|
| 0 | 430836 | 24 | {"ADHD": 239408, "Control": 191428} |
| 1 | 440142 | 25 | {"ADHD": 248301, "Control": 191841} |
| 2 | 430388 | 24 | {"ADHD": 239278, "Control": 191110} |
| 3 | 421912 | 23 | {"ADHD": 240370, "Control": 181542} |
| 4 | 428966 | 24 | {"ADHD": 239712, "Control": 189254} |

## Folds, seed 1024

| Fold | Rows | Groups | Classes |
|---|---|---|---|
| 0 | 430515 | 24 | {"ADHD": 239452, "Control": 191063} |
| 1 | 431581 | 24 | {"ADHD": 239747, "Control": 191834} |
| 2 | 429447 | 24 | {"ADHD": 240285, "Control": 189162} |
| 3 | 439924 | 25 | {"ADHD": 248556, "Control": 191368} |
| 4 | 420777 | 23 | {"ADHD": 239029, "Control": 181748} |

## Derivation and decisions

- **Source file.** `datasets/ieee-adhd-eeg-kaggle/raw/adhdata.csv` (267,279,775 bytes, 2,166,383 data rows, 121 IDs: 61 ADHD, 60 Control), sha256 `c9a7262cefc70688247db248a2defee3c63ab3e3c2ad0e3189c394caf2281d73`, downloaded on 2026-10-27 with the official `kaggle` client from the Kaggle dataset `danizo/eeg-dataset-for-adhd`.
- **Filter rule.** Drop every row whose `ID` is `v56p` (trailing `\r` stripped before comparing), per experiments v06 (kept in v08). The header and all other rows are copied byte for byte (CRLF line endings, same columns). 14,139 rows were dropped. The derived file `datasets/ieee-adhd-eeg-kaggle/derived/adhdata-no-v56p.csv` (265,487,808 bytes, sha256 above) holds 2,152,244 data rows and 120 IDs: 61 ADHD and 59 Control.
- **Duplicate rows kept.** `qc` reports 45 duplicate rows. They are kept by the operator's decision: in a time series, identical consecutive samples are valid data.
- **Channels by name, never by position.** The mirror's column order is Fp1, Fp2, F3, F4, C3, C4, P3, P4, O1, O2, F7, F8, T7, T8, P7, P8, Fz, Cz, Pz, using the T7/T8/P7/P8 names. The official source's order is Fz, Cz, Pz, C3, T3, C4, T4, Fp1, Fp2, F3, F4, F7, F8, P3, P4, T5, T6, O1, O2, using T3/T4/T5/T6. Code must select channels by column name. The mirror's name-to-signal mapping has not yet been checked against an official `.mat` file, and that check is required before E4.
- **Official split and repetitions (version 2).** Five repetitions of stratified group k-fold on `Class` grouped by `ID`, 5 folds each, seeds 42, 123, 456, 789 and 1024 (`prepare --seeds`, papersmith 0.29.0): every repetition takes the subjects largest first in size strata of 5 that its seed shuffles, so each seed gives its own split, and the experiments read every repetition from `splits.json` (`repetitions`) rather than re-splitting. Version 1 (a single split, seed 42) is superseded: its procedure sorted subjects by size after the seeded shuffle, so on this dataset, where every subject has a different size, any seed gave that same split, and five repetitions would have been one split repeated.
- **License basis.** The official source is IEEE DataPort, DOI 10.21227/rzfh-zn36, under CC BY 4.0, with credit to Nasrabadi, Allahverdy, Samavati and Mohammadi. The `kaggle` client reports the mirror's license as `other`. The mirror is not redistributed.
- **Saturation (stdlib domain check in `qc.json`, verdict pass).** Per channel, samples equal to that channel's global max or min. Across all 19 channels, 127 of 40,892,636 channel samples are at a rail (fraction 3e-06), between 3 and 11 per channel. 41 of 120 subjects touch a rail at least once, and 0 subjects have more than 1% of their samples at a rail.
