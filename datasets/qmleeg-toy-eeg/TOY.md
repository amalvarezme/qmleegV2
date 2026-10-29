# Toy dataset `qmleeg-toy-eeg`

Seeded synthetic data for the proof of concept. Same parameters, same bytes.

| Parameter | Value |
|---|---|
| kind | eeg |
| seed | 42 |
| n_subjects | 20 |
| n_per_subject | 24 |
| channels | 19 |
| label_per | subject |
| length | 256 |
| sfreq | 128.0 |
| profile | theta-beta |

- File: `qmleeg-toy-eeg.csv` (480 rows, 4867 columns)
- sha256: `cec99326fbf85e5b10703208df24f0e13f7f641c0be3bda342611c49d47025fb`
- Labels: one class per subject, balanced across subjects (subject-level protocols).
- Signal: a 10 Hz sinusoid per channel whose band power depends on the class (amplitude 1.0 vs 0.4, times a per-subject gain), plus Gaussian noise (sd 0.3).

Regenerate: `python3 skills/datasets/scripts/datasets_cli.py synth --slug qmleeg-toy-eeg --kind eeg --seed 42 --n-subjects 20 --n-per-subject 24 --channels 19 --label-per subject --length 256 --sfreq 128.0 --profile theta-beta --force`
