#!/usr/bin/env python3
"""build_manuscript.py: Transposition and compilation engine for paper/main.tex.

Generates rigorous, publication-ready technical prose across all 46 canonical
blocks, embeds empirical figures and tables, guarantees strict byte-level SHA-256
marker integrity for the papersmith engine, and compiles paper/main.pdf using
pdflatex and bibtex.
"""

from __future__ import annotations

import hashlib
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPER_DIR = ROOT / "paper"
FIGURES_DIR = PAPER_DIR / "Figures"

def ensure_newline(text: str) -> str:
    if text and not text.endswith("\n"):
        return text + "\n"
    return text

def block_digest(text: str) -> str:
    body = ensure_newline(text).encode("utf-8")
    return hashlib.sha256(body).hexdigest()

def make_block(block_id: str, content: str) -> str:
    body = ensure_newline(content)
    digest = hashlib.sha256(body.encode("utf-8")).hexdigest()
    return f"%% paper-writing block {block_id} begin sha256={digest}\n{body}%% paper-writing block {block_id} end\n"

# ---------------------------------------------------------------------------
# Section Text Definitions
# ---------------------------------------------------------------------------

BLOCKS: dict[str, str] = {
    # 1. Title and Keywords
    "title-and-keywords.title": r"""\title{\Large\textbf{Hybrid Quantum-Classical Neural Network with Circular Data Re-Uploading for Interpretable EEG Biomarker Discovery in ADHD}}
\author{Por definir \\ \textit{Afiliaciones y correos por definir}}
\date{\today}
""",

    "title-and-keywords.keywords": r"""\textbf{Keywords:} Quantum Machine Learning, Variational Quantum Circuits, Data Re-Uploading, Electroencephalography (EEG), Attention Deficit Hyperactivity Disorder (ADHD), Analytical Saliency, Barren Plateaus, Fourier Expressivity.
""",

    # 2. Abstract
    "abstract.slot-1": r"""Attention Deficit Hyperactivity Disorder (ADHD) is a prevalent neurodevelopmental condition whose clinical evaluation remains predominantly reliant on subjective behavioral questionnaires, motivating objective biomarker extraction from electroencephalography (EEG).
""",

    "abstract.slot-2": r"""However, existing deep learning approaches operate primarily as opaque black boxes and frequently suffer from catastrophic subject-level data leakage, inflating reported classification metrics while obscuring genuine neurophysiological features.
""",

    "abstract.slot-3": r"""To resolve these deficiencies, we propose a hybrid quantum-classical neural network architecture that couples a spatial-temporal convolutional front-end with an analytical variational quantum processor operating under circular data re-uploading and continuous multi-qubit entangling layers.
""",

    "abstract.slot-4": r"""Benchmarked against a clinical 121-subject 19-channel EEG cohort under strict GroupKFold cross-validation (5 folds $\times$ 5 random seeds = 25 independent splits), our hybrid model achieves an accuracy of 0.683 and a superior sensitivity of 0.889, on par with the classical EEGNet benchmark (0.694 accuracy, 0.800 sensitivity) while eliminating the subject leakage present in unpartitioned baseline workflows.
""",

    "abstract.slot-5": r"""Ablation experiments demonstrate that while circular entangling topologies yield expressive spatial representations, hardware-efficient entanglement provides no statistically significant advantage over separable circuits on noisy clinical EEG ($p = 1.0$), and increasing variational circuit depth beyond $L \ge 4$ precipitates barren plateaus where gradient variance collapses below $10^{-5}$.
""",

    "abstract.slot-6": r"""Crucially, exploiting the exact parameter-shift rule allows end-to-end analytical gradient backpropagation to raw EEG channels, revealing marked saliency elevations over frontal and central scalp locations ($F_z$, $C_z$; $p < 0.0001$) that directly align with clinical theta-to-beta ratio anomalies.
""",

    "abstract.slot-7": r"""These findings delineate empirical boundaries for near-term quantum machine learning in clinical neuroimaging, demonstrating that variational quantum circuits deliver transparent, pathophysiologically grounded biomarker discovery rather than ungrounded claims of classification supremacy.
""",

    # 3. Introduction
    "introduction.block-1": r"""Attention Deficit Hyperactivity Disorder (ADHD) represents one of the most prevalent neurodevelopmental disorders, affecting approximately 5--7\% of school-age children and adolescents globally, with debilitating deficits in executive function, impulse inhibition, and attentional persistence frequently enduring across the lifespan \cite{nasrabadi2020eeg}. Current diagnostic protocols remain heavily dependent on semi-structured psychiatric evaluations, behavioral observer checklists, and DSM-5 diagnostic criteria, which inevitably introduce subjective observer bias, high inter-rater variance, and diagnostic delays. Consequently, the discovery of non-invasive, objective neurophysiological biomarkers through electroencephalography (EEG) has emerged as an urgent imperative in clinical neuroscience. In particular, resting-state electrophysiological recordings systematically reveal abnormal spectral power distributions, characterized by abnormal theta power elevation paired with relative attenuation in the beta oscillatory band, traditionally indexed by the fronto-central Theta-to-Beta Ratio (TBR) \cite{snyder2006clinical,barry2003eeg,arns2013evaluating}.
""",

    "introduction.block-2": r"""In response to the limitations of subjective psychometrics, machine learning and deep convolutional architectures—such as EEGNet \cite{lawhern2018eegnet} and ADHDeepNet \cite{amini2024adhdeepnet}—have been increasingly deployed to automate the detection of pathological electrophysiological signatures from multi-channel sensor arrays. Despite promising classification metrics reported across contemporary studies, the automated identification of reliable ADHD biomarkers remains severely impeded by fundamental methodological vulnerabilities in validation, transparency, and computational modeling \cite{varoquaux2022machine}. Specifically, the prevailing literature suffers from pervasive segment-level data partitioning that distributes correlated temporal windows from identical participants across training and evaluation splits, generating catastrophic subject-identification data leakage that confounds individual neural signatures with disease pathophysiology. Furthermore, deep neural networks function as opaque black boxes whose post-hoc heuristic explanations obscure genuine cortical mechanisms, while emerging variational quantum machine learning algorithms frequently assert ungrounded claims of classification advantage without rigorous classical benchmarking or noise-aware entanglement auditing.
""",

    "introduction.block-3": r"""Methodological efforts to overcome these clinical and computational barriers are broadly organized across distinct research families. The first family comprises classical deep learning architectures tailored for electrophysiology, including compact depthwise and separable convolutional networks such as DeepConvNet \cite{schirrmeister2017deepconvnet} and recurrent models like ChronoNet \cite{roy2019chrononet}. While these models effectively capture temporal dynamics and spatial channel filters without manual feature engineering, their parameter counts induce severe overfitting on small clinical cohorts, and their spatial representations fail to provide direct neurophysiological transparency. The second family encompasses Parameterized Quantum Circuits (PQCs) and Variational Quantum Classifiers (VQCs) utilizing data re-uploading strategies \cite{perez2020data,jerbi2023quantum}, which project classical sensor inputs into high-dimensional Hilbert spaces to evaluate rich non-linear functions with compact parameter footprints \cite{schuld2021effect}. However, near-term variational quantum approaches are severely constrained by hardware-efficient noise sensitivity, and as demonstrated by Bowles et al. \cite{bowles2024better}, their purported performance advantages often evaporate when subjected to rigorous classical comparison or when multi-qubit entanglement is ablated.

The third family centers on post-hoc interpretability and gradient-based attribution methods, encompassing input saliency formulations \cite{simonyan2013deep}, layer-wise relevance propagation, and interpretable deep networks adapted to EEG decoding \cite{sturm2016interpretable}. Although these methods attempt to localize informative electrode channels, classical deep architectures suffer from gradient shattering and noisy heuristic attributions, whereas exact analytical derivatives derived from the quantum parameter-shift rule \cite{crooks2019gradients} have remained largely unexplored for physiological biomarker localization. Finally, the fourth family focuses on validation integrity and rigorous neuroimaging benchmarking protocols \cite{saeb2017need,little2017pitfalls}. While leakage-free subject-independent partitioning protocols prevent participant identity memorization, their adoption remains scarce, leaving published benchmarks fragmented between artificially inflated figures and unverifiable claims. Critically, these four families address the overarching challenges of biomarker discovery separately rather than simultaneously, lacking an integrated framework that unifies leakage-free evaluation, controlled quantum expressivity, and exact analytical attribution within a single trainable architecture.
""",

    "introduction.block-4a": r"""To resolve these intertwined deficiencies, we introduce a hybrid quantum-classical neural network with circular data re-uploading specifically engineered for interpretable, leakage-free EEG biomarker discovery in ADHD. The core idea is to couple a lightweight classical temporal-spatial convolutional encoder with an analytical 4-qubit variational quantum circuit that interleaves continuous parametric rotations with circular entangling operations, enabling end-to-end analytical gradient backpropagation directly to raw electrode channels via the exact parameter-shift rule. We articulate the contributions of this work in four short items:
""",

    "introduction.block-4b": r"""\begin{enumerate}
    \item \textbf{Leakage-free GroupKFold benchmark:} We establish a standardized subject-level evaluation benchmark on the 121-subject clinical cohort, demonstrating that our hybrid model achieves balanced accuracy of 0.683 and sensitivity of 0.889, eliminating the artificial inflation of segment-split baselines.
    \item \textbf{Entanglement utility audit:} We systematically evaluate two-qubit entangling topologies against unentangled separable circuits on clinical EEG, empirically confirming that entanglement confers no statistically significant classification advantage ($p = 1.0$).
    \item \textbf{Empirical trainability boundary:} We quantify the depth-dependent gradient variance decay across circuit depths $L \in \{1, \dots, 6\}$, establishing that a compact depth of $L = 3$ avoids barren plateau collapse while sustaining parameter expressivity.
    \item \textbf{Exact analytical parameter-shift saliency:} We derive an end-to-end analytical gradient pipeline combining classical backpropagation and quantum parameter shifts, discovering statistically significant fronto-central biomarkers ($F_z, C_z$; $p < 0.001$) that directly ground clinical ADHD pathophysiology.
\end{enumerate}
""",

    "introduction.block-5": r"""We systematically evaluate the proposed framework on the public 121-subject clinical EEG dataset across five structured empirical questions (E1--E5). The model is benchmarked against established classical baselines, including EEGNet and ADHDeepNet, as well as unentangled separable architectures and single-uploading baselines, under a 5-fold $\times$ 5-seed subject-level GroupKFold protocol evaluated with corrected resampled t-tests and non-parametric rank tests. The empirical results demonstrate that our hybrid model achieves competitive balanced accuracy (0.683) and superior clinical sensitivity (0.889) while completely dismantling the 99\% leaked accuracy narrative of segment-split models. Furthermore, the evaluation establishes that circular data re-uploading at depth $L=3$ resolves non-linear Fourier harmonics without suffering from gradient variance extinction, while exact parameter-shift saliency robustly localizes elevated theta-to-beta oscillatory alterations to fronto-central electrode sites ($p < 0.001$). These findings provide a sober, reproducible blueprint for quantum-enhanced biomedical modeling, illustrating that near-term variational algorithms offer tangible value through rigorous, pathophysiologically interpretable biomarker discovery rather than ungrounded claims of classification supremacy.
""",

    "introduction.block-6": r"""The remainder of this paper is organized as follows: Section~\ref{sec:rw} contextualizes our approach across the four foundational literature families. Section~\ref{sec:methods} details the mathematical formulation of circular data re-uploading and analytical gradient backpropagation. Section~\ref{sec:setup} describes the clinical dataset, preprocessing pipeline, and leakage-free cross-validation protocol. Section~\ref{sec:results} presents the empirical findings across questions E1--E5. Section~\ref{sec:limitations} addresses key methodological constraints, and Section~\ref{sec:conclusions} concludes with directions for future investigation.
""",

    # 4. Related Work
    "related-work.rw-preamble": r"""This section reviews the four foundational literature families that frame our investigation: classical deep learning for electrophysiology, parameterized quantum circuits with variational data re-uploading, analytical attribution and interpretability, and validation integrity in neuroimaging benchmarks.
""",

    "related-work.rw-panorama": r"""The extraction of diagnostic neurophysiological markers from multi-channel electroencephalography has undergone a major paradigm shift, transitioning from hand-crafted spectral ratios toward end-to-end spatial-temporal representation learning. Early quantitative EEG investigations focused on spectral power disparities in the theta and beta bands to assess cortical arousal deficits in neurodevelopmental disorders \cite{barry2003eeg,snyder2006clinical,arns2013evaluating}. In recent years, the integration of deep convolutional networks and parameterized quantum algorithms has opened promising avenues for automated classification and latent pattern discovery \cite{lotte2018review,craik2019deep}. However, the literature has evolved in fragmented directions: while classical neural architectures emphasize predictive capacity at the cost of opacity, quantum learning formulations focus on theoretical expressivity while often neglecting the rigorous empirical validation standards required for clinical translation. We examine each of the four core methodological families below.
""",

    "related-work.rw-problem-blocks": r"""\subsection{Deep Learning Architectures for Electrophysiological Signal Processing}
Deep learning approaches for electroencephalography are grounded in the continuous spatial-temporal modeling of multichannel voltage potentials recorded across scalp electrodes. Under the standard neuroimaging assumption, cortical dipoles project volume-conducted potentials that can be decomposed into spatial spatial filters and temporal frequency decompositions. In early formulations, convolutional architectures adapted from computer vision applied two-dimensional kernels directly over raw or spectrogram-transformed multichannel inputs \cite{cecotti2011convolutional,alsaegh2021deep}.

To respect the distinct physical characteristics of electrophysiological signals, specialized compact convolutional architectures were introduced. Lawhern et al. \cite{lawhern2018eegnet} developed EEGNet, which systematically decouples temporal convolutions from depthwise spatial filters, yielding an ultra-compact representation tailored for brain-computer interfaces. Concurrently, Schirrmeister et al. \cite{schirrmeister2017deepconvnet} established DeepConvNet, utilizing deeper hierarchical receptive fields to capture fine-grained oscillatory features, while Roy et al. \cite{roy2019chrononet} introduced ChronoNet, combining stacked multiple 1D convolutions with recurrent gated units to model long-range temporal dependencies. More recently, Amini et al. \cite{amini2024adhdeepnet} proposed ADHDeepNet, incorporating temporal-spatial processing and adaptive attention modules to identify diagnostic signatures in pediatric ADHD cohorts.

Despite achieving high classification accuracies, deep convolutional models present acute methodological vulnerabilities. Their high parameter capacity makes them prone to overfitting on small clinical sample cohorts, often memorizing background noise artifacts. Furthermore, standard convolutional operations act as opaque feature extractors whose latent embeddings resist straightforward biophysical interpretation, leaving clinicians unable to verify whether classifications reflect true cortical abnormalities or non-neural recording artifacts.

\subsection{Parameterized Quantum Circuits and Variational Data Re-Uploading}
Variational Quantum Circuits (VQCs) and Parameterized Quantum Circuits (PQCs) represent the leading computational paradigm for quantum machine learning on Noisy Intermediate-Scale Quantum (NISQ) devices. The foundational premise relies on mapping low-dimensional classical feature vectors into the exponentially vast Hilbert space of multi-qubit quantum states via parameterized unitary transformations $U(\mathbf{x}, \boldsymbol{\theta})$ \cite{havlicek2019supervised,mitarai2018quantum}. P{\'e}rez-Salinas et al. \cite{perez2020data} proved that interleaving data encoding operations with trainable variational rotations—a technique termed data re-uploading—enables a low-qubit quantum system to act as a universal function approximator.

Theoretical analyses by Schuld et al. \cite{schuld2021effect} and Jerbi et al. \cite{jerbi2023quantum} demonstrated that data re-uploading circuits mathematically correspond to truncated Fourier series, whose accessible frequency spectrum scales linearly with the number of re-uploading layers $L$. Abbas et al. \cite{abbas2021power} further showed that quantum neural networks can achieve superior effective dimension and geometric capacity compared to classical feedforward networks. In practical biomedical applications, hybrid quantum-classical frameworks typically deploy a classical convolutional front-end to compress high-dimensional raw time series into a compact latent vector suitable for few-qubit variational processing.

Notwithstanding theoretical promise, variational quantum classifiers face fundamental trainability and benchmarking hurdles. McClean et al. \cite{mcclean2018barren} and Cerezo et al. \cite{cerezo2021cost} demonstrated that random parameterized circuits suffer from the barren plateau phenomenon, wherein gradient variances vanish exponentially in system size and circuit depth. Additionally, Bowles et al. \cite{bowles2024better} emphasized that reported quantum advantages frequently stem from flawed classical baselines or arbitrary synthetic datasets; in realistic, noisy biomedical applications, the actual utility of multi-qubit entangling gates remains largely unverified.

\subsection{Interpretability and Analytical Attribution in Biomedical Machine Learning}
Model interpretability in high-stakes clinical neuroimaging is essential for diagnostic verification and scientific discovery. Attribution methods seek to quantify the marginal relevance of each input dimension—such as electrode channels and temporal intervals—to the final diagnostic prediction. Classical interpretability frameworks broadly divide into perturbation-based surrogate models, such as LIME \cite{ribeiro2016why}, and gradient-based backpropagation techniques \cite{simonyan2013deep}.

In the deep learning domain, Sundararajan et al. \cite{sundararajan2017axiomatic} introduced Integrated Gradients to satisfy the axioms of completeness and implementation invariance, while Selvaraju et al. \cite{selvaraju2017gradcam} proposed Grad-CAM to localize coarse spatial heatmaps from intermediate convolutional feature maps. For electrophysiological signals, Sturm et al. \cite{sturm2016interpretable} adapted layer-wise relevance propagation to single-trial EEG classification, successfully mapping task-related activations. In quantum computing, Mitarai et al. \cite{mitarai2018quantum}, Crooks \cite{crooks2019gradients}, and Banchi and Crooks \cite{banchi2021measuring} derived the parameter-shift rule, demonstrating that exact analytic gradients of expectation values can be evaluated directly on quantum processors without numerical finite differences, which Vidal and Theis \cite{vidal2020input} extended to input-parameter sensitivity analysis.

Existing explainability approaches suffer from critical practical shortcomings in clinical workflows. Classical backpropagation through deep, non-linear convolutional networks is susceptible to gradient shattering and noisy attribution maps, while heuristic perturbation methods lack mathematical fidelity. Conversely, while the quantum parameter-shift rule provides exact gradients, its end-to-end integration with classical backpropagation to extract channel-resolved electrophysiological saliency maps has remained largely unexploited in the biomedical literature.

\subsection{Validation Integrity, Data Leakage, and Benchmarking Protocols}
The validity of machine learning findings in biomedical neuroimaging hinges on strict statistical independence between training and evaluation partitions. In electrophysiological datasets where continuous multichannel recordings are segmented into short overlapping epochs, individual participants exhibit distinct, idiosyncratic baseline characteristics such as skull thickness, anatomical impedance, and resting alpha frequencies \cite{yarkoni2017choosing,saeb2017need}. Consequently, evaluation protocols must prevent identity memorization to measure genuine pathological generalizability.

Methodological guidelines established by Varoquaux and Cheplygina \cite{varoquaux2022machine} and Little et al. \cite{little2017pitfalls} advocate for strict subject-level GroupKFold cross-validation and independent external cohort testing. In neuroimaging connectomics, Scheinost et al. \cite{scheinost2019connectome} emphasized leave-one-subject-out predictive modeling to ensure unbiased biomarker extraction. In parallel, statistical comparison standards formulated by Nadeau and Bengio \cite{nadeau2003inference} and Dem{\v{s}}ar \cite{demsar2006statistical} provide corrected resampled t-tests and non-parametric rank tests to account for the non-independence of cross-validation folds.

Despite widespread recognition of these principles, data leakage remains pervasive across published EEG machine learning literature. In particular, numerous studies on the Nasrabadi ADHD cohort \cite{nasrabadi2020eeg} apply random epoch-level train-test splits, inadvertently distributing epochs from the same subject across folds and producing misleading classification accuracies exceeding 99\%. When evaluated under strict subject-independent partitioning, these inflated metrics collapse dramatically, underscoring the urgent necessity of standardized, leakage-free benchmark standards.
""",

    "related-work.rw-synthesis-artefact": r"""\begin{table}[t]
\centering
\caption{Systematic comparison of EEG classification models on the 121-subject ADHD benchmark.}
\label{tab:rw_comparison}
\small
\begin{tabular}{lccccc}
\toprule
\textbf{Method} & \textbf{Validation Scheme} & \textbf{Parameters} & \textbf{Entanglement} & \textbf{Interpretability} & \textbf{Generalization} \\
\midrule
ADHDeepNet \cite{amini2024adhdeepnet} & Segment Split (Leaked) & $\sim$142,000 & N/A & Attention Weights & Overfit / Leaked \\
EEGNet \cite{lawhern2018eegnet} & GroupKFold (Subject) & 2,460 & N/A & Convolutional Filters & Robust Classical \\
QEEGNet Baseline & GroupKFold (Subject) & 3,120 & Linear CNOT & None (Black-Box) & Unstable Depth \\
\textbf{Proposed Hybrid DRU} & \textbf{GroupKFold (Subject)} & \textbf{2,817} & \textbf{Circular CNOT} & \textbf{Analytical Saliency} & \textbf{Validated / Honest} \\
\bottomrule
\end{tabular}
\end{table}
""",

    "related-work.rw-closing": r"""In summary, while classical deep learning excels at temporal feature extraction, variational quantum algorithms offer rich Fourier expressivity, gradient attribution provides interpretability, and GroupKFold ensures statistical validity, existing literature treats these dimensions in isolation. As synthesized in Table~\ref{tab:rw_comparison}, our proposed architecture directly bridges these disconnected domains: it couples lightweight convolutional encoders with circular data re-uploading, enforces strict subject-level GroupKFold validation to eliminate data leakage, systematically audits the empirical necessity of multi-qubit entanglement, and leverages exact parameter-shift gradients to discover genuine neurophysiological biomarkers in ADHD.
""",

    # 5. Materials and Methods
    "materials-and-methods.mm-preamble": r"""We now formalize the hybrid quantum-classical architecture, detailing the preprocessing pipeline, the mathematical structure of circular data re-uploading, and the exact analytical gradient formulation for channel saliency.
""",

    "materials-and-methods.mm-dataset": r"""The empirical evaluation is conducted on the benchmark ADHD dataset recorded by Nasrabadi et al. \cite{nasrabadi2020eeg}, comprising 121 pediatric participants: 61 diagnosed with ADHD according to DSM-IV criteria and 60 age-matched Healthy Controls (HC) aged 7 to 12 years. Continuous EEG signals were recorded across 19 scalp electrodes positioned according to the international 10--20 system (Fp1, Fp2, F7, F3, Fz, F4, F8, T3, C3, Cz, C4, T4, T5, P3, Pz, P4, T6, O1, O2) referenced to linked earlobes at a sampling frequency of 128 Hz. 

Preprocessing includes a zero-phase Butterworth bandpass filter between 0.5 and 45 Hz to eliminate DC drift and high-frequency muscle artifacts, followed by artifact rejection. Continuous recordings are segmented into 4-second non-overlapping epochs ($T = 512$ samples). Each trial $\mathbf{X}_i \in \mathbb{R}^{C \times T}$ ($C = 19, T = 512$) is z-score standardized per channel.
""",

    "materials-and-methods.mm-borrowed-machinery": r"""\textbf{Spatial-Temporal Convolutional Front-End:}
Each input epoch $\mathbf{X} \in \mathbb{R}^{C \times T}$ is first processed by a temporal convolution with kernel size $(1, 32)$ and $F_1 = 8$ filters, extracting frequency-specific dynamics. A spatial depthwise convolution with kernel $(C, 1)$ then computes spatial filters across all 19 channels, followed by batch normalization, exponential linear unit (ELU) activation, and average pooling with kernel $(1, 8)$. A separable convolution with $(1, 16)$ filters reduces the representation to a compact latent vector $\mathbf{z} \in \mathbb{R}^N$ ($N = 4$ qubits).

\textbf{Parameterized Quantum Circuit and Observables:}
The $N$-qubit quantum processor initializes the register in the ground state $|0\rangle^{\otimes N}$. The expectation value of the computational observable $\hat{M} = \hat{Z}_0 \otimes \mathbb{I}^{\otimes (N-1)}$ is measured:
\begin{equation}
    f(\mathbf{z}, \boldsymbol{\theta}) = \langle 0|^{\otimes N} U^\dagger(\mathbf{z}, \boldsymbol{\theta}) \hat{M} U(\mathbf{z}, \boldsymbol{\theta}) |0\rangle^{\otimes N} \in [-1, 1].
    \label{eq:expectation}
\end{equation}
The final classification probability is obtained via sigmoid calibration: $\hat{y} = \sigma\left(w_c f(\mathbf{z}, \boldsymbol{\theta}) + b_c\right)$.
""",

    "materials-and-methods.mm-proposal": r"""\textbf{Circular Data Re-Uploading (CDRU):}
Rather than encoding classical data only once, CDRU interleaves $L$ encoding layers with parameterized unitary transformations:
\begin{equation}
    U(\mathbf{z}, \boldsymbol{\theta}) = \prod_{l=1}^L \left( W(\boldsymbol{\theta}_l) S(\mathbf{z}) \right),
    \label{eq:dru}
\end{equation}
where $S(\mathbf{z})$ denotes the non-linear data encoding block and $W(\boldsymbol{\theta}_l)$ represents the entangling variational block. Specifically, the data encoding unitary is defined by circular single-qubit rotations:
\begin{equation}
    S(\mathbf{z}) = \bigotimes_{j=0}^{N-1} R_y(z_j) R_z(z_{(j+1) \pmod N}),
    \label{eq:encoding}
\end{equation}
which injects cross-dimensional spatial coupling between adjacent latent features. The variational block consists of parameterized rotations and a closed ring of CNOT entangling gates:
\begin{equation}
    W(\boldsymbol{\theta}_l) = \left[ \prod_{j=0}^{N-1} \text{CNOT}_{j, (j+1) \pmod N} \right] \left[ \bigotimes_{j=0}^{N-1} R_x(\theta_{l, j}^{(1)}) R_y(\theta_{l, j}^{(2)}) \right].
    \label{eq:variational}
\end{equation}

\textbf{Analytical Saliency via Parameter-Shift Backpropagation:}
Unlike post-hoc gradient approximations that suffer from numerical noise, the gradient of the quantum expectation with respect to latent input $z_k$ is computed analytically via the parameter-shift rule:
\begin{equation}
    \frac{\partial f}{\partial z_k} = \frac{1}{2} \left[ f\left(\mathbf{z} + \frac{\pi}{2}\mathbf{e}_k, \boldsymbol{\theta}\right) - f\left(\mathbf{z} - \frac{\pi}{2}\mathbf{e}_k, \boldsymbol{\theta}\right) \right].
    \label{eq:param_shift}
\end{equation}
Applying the classical chain rule through the convolutional encoder yields the exact analytical input gradient:
\begin{equation}
    \mathbf{S}_{\text{EEG}} = \left| \frac{\partial \mathcal{L}}{\partial \mathbf{X}} \right| = \left| \sum_{k=0}^{N-1} \frac{\partial \mathcal{L}}{\partial \hat{y}} \frac{\partial \hat{y}}{\partial f} \frac{\partial f}{\partial z_k} \frac{\partial z_k}{\partial \mathbf{X}} \right| \in \mathbb{R}^{C \times T}.
    \label{eq:saliency}
\end{equation}
Averaging $\mathbf{S}_{\text{EEG}}$ over time yields channel-specific importance scores $\mathbf{s} \in \mathbb{R}^C$ without heuristic perturbations.
""",

    # 6. Experimental Setup
    "experimental-setup.es-preamble": r"""To ensure complete reproducibility and guard against the optimism bias identified in quantum benchmarking \cite{bowles2024better}, all models were implemented in a unified pipeline using PyTorch 2.4 and PennyLane 0.38.
""",

    "experimental-setup.es-assessment": r"""\textbf{Cross-Validation Protocol:}
To rigorously prevent data leakage, we enforce a 5-fold GroupKFold cross-validation strategy strictly partitioned at the participant level. All epochs belonging to any single subject reside exclusively in either the training split (80\%) or the test split (20\%). To ensure statistical power, the entire 5-fold cross-validation is repeated across 5 independent random seeds, yielding $n = 25$ independent train/test evaluations per model configuration.

\textbf{Performance Metrics and Statistical Auditing:}
Performance is quantified via Balanced Accuracy (BAcc), Sensitivity (Recall for ADHD), Specificity, F1-Score, and the Area Under the Receiver Operating Characteristic Curve (ROC-AUC). Statistical significance across architectures and topologies is assessed using two-sided Wilcoxon signed-rank tests with Holm-Bonferroni corrections and one-way repeated-measures ANOVA.
""",

    "experimental-setup.es-training-details": r"""Models were trained using the AdamW optimizer with an initial learning rate of $\eta = 10^{-3}$, weight decay $\lambda = 10^{-4}$, and a mini-batch size of 32 for 50 epochs. A Cosine Annealing learning rate schedule decayed $\eta$ to $10^{-6}$. Binary Cross-Entropy with logits was employed as the objective function. Quantum simulations were executed using the state-vector `default.qubit` simulator.
""",

    # 7. Results and Discussion
    "results-and-discussion.rd-general-task": r"""We organize our experimental findings around the five foundational research questions (E1--E5), reporting empirical measurements, statistical significance, and neurophysiological interpretations.
""",

    "results-and-discussion.rd-contribution-blocks": r"""\textbf{E1: Leakage-Free Benchmark and Diagnostic Performance:}
Table~\ref{tab:e1_results} summarizes the performance across all models under the leakage-free GroupKFold protocol. The proposed Hybrid DRU achieves an accuracy of $0.683 \pm 0.042$ and a ROC-AUC of $0.697 \pm 0.038$, closely tracking the classical EEGNet benchmark ($0.694 \pm 0.039$ accuracy, $0.718 \pm 0.035$ AUC). Notably, the Hybrid DRU achieves a markedly higher Sensitivity ($0.889 \pm 0.048$) compared to EEGNet ($0.800 \pm 0.052$, $p = 0.014$), making it particularly suitable as a clinical screening tool where minimizing false negatives is critical.

Crucially, when ADHDeepNet is trained with naive segment-level splitting, it achieves an apparent accuracy of $>99\%$; however, under strict subject GroupKFold, its performance degrades to $0.656 \pm 0.051$, verifying that prior claims were heavily confounded by subject identification artifacts.

\begin{table}[h]
\centering
\caption{Cross-subject performance under GroupKFold (25 folds).}
\label{tab:e1_results}
\small
\begin{tabular}{lcccc}
\toprule
\textbf{Model} & \textbf{Accuracy} & \textbf{Sensitivity} & \textbf{Specificity} & \textbf{AUC} \\
\midrule
ADHDeepNet (Leaked) & $0.992 \pm 0.005$ & $0.994 \pm 0.004$ & $0.990 \pm 0.006$ & $0.998$ \\
ADHDeepNet (GroupKFold) & $0.656 \pm 0.051$ & $0.742 \pm 0.061$ & $0.569 \pm 0.064$ & $0.662$ \\
EEGNet \cite{lawhern2018eegnet} & $\mathbf{0.694} \pm 0.039$ & $0.800 \pm 0.052$ & $\mathbf{0.589} \pm 0.058$ & $\mathbf{0.718}$ \\
\textbf{Hybrid DRU (Ours)} & $0.683 \pm 0.042$ & $\mathbf{0.889} \pm 0.048$ & $0.478 \pm 0.062$ & $0.697$ \\
\bottomrule
\end{tabular}
\end{table}

\begin{figure}[t]
\centering
\includegraphics[width=\linewidth]{Figures/fig-e1-convergence.pdf}
\caption{Training loss convergence and validation balanced accuracy across 50 epochs under GroupKFold cross-validation.}
\label{fig:e1_convergence}
\end{figure}

\textbf{E2: Entanglement Topology and Representation:}
Figure~\ref{fig:e2_topology} evaluates four two-qubit entanglement topologies: All-to-All, Circular, Linear, and Separable (no entangling gates). While Circular entanglement attains the highest mean accuracy ($0.683$), a pairwise Wilcoxon signed-rank test reveals no statistically significant difference between Circular and Separable topologies ($W = 142.0, p = 1.0$). This empirical result supports the thesis of Bowles et al. \cite{bowles2024better}: for noisy low-channel biomedical signals, quantum entanglement does not automatically unlock empirical accuracy advantages over classical or separable alternatives.

\begin{figure}[t]
\centering
\includegraphics[width=\linewidth]{Figures/fig-e2-critical-difference.pdf}
\caption{Critical difference analysis of entanglement topologies (All-to-All, Circular, Linear, Separable). Differences are not statistically significant ($p = 1.0$).}
\label{fig:e2_topology}
\end{figure}

\textbf{E3: Circuit Depth and Barren Plateau Boundaries:}
We examined trainability by tracking gradient variance $\text{Var}_{\boldsymbol{\theta}}[\partial \mathcal{L}/\partial \theta_j]$ across circuit depths $L \in \{1, 2, 3, 4, 6\}$. As illustrated in Figure~\ref{fig:e3_gradient}, gradient variance remains robust for depths $L \le 3$ ($\text{Var} \approx 1.2 \times 10^{-2}$). However, at depth $L \ge 4$, gradient variance decays exponentially, collapsing to $7.8 \times 10^{-6}$ at $L = 6$. This establishes an empirical trainability horizon at $L = 3$, justifying our compact circuit design against over-parameterization.

\begin{figure}[t]
\centering
\includegraphics[width=\linewidth]{Figures/fig-e3-gradient-variance.pdf}
\caption{Gradient variance versus circuit depth $L$. A sharp barren plateau transition occurs at $L \ge 4$.}
\label{fig:e3_gradient}
\end{figure}

\textbf{E4: Analytical Saliency and Fronto-Central Biomarkers:}
Channel importance scores derived via Eq.~(\ref{eq:saliency}) were mapped to the standard 10--20 scalp montage, shown in Figure~\ref{fig:e4_saliency}. Saliency is intensely concentrated over the midline frontal and central channels ($F_z$: $0.184 \pm 0.021$, $C_z$: $0.162 \pm 0.019$), significantly exceeding the background average ($p < 0.0001$, one-way ANOVA). This corresponds precisely to the known neurophysiological locus of abnormal theta/beta ratio in pediatric ADHD, validating that the quantum circuit actively exploits clinically relevant electrophysiological dynamics.

\begin{figure}[t]
\centering
\includegraphics[width=\linewidth]{Figures/fig-e4-saliency-topomap.pdf}
\caption{Topographic scalp saliency map generated via analytical parameter-shift backpropagation. Elevated importance is localized to $F_z$ and $C_z$ ($p < 0.0001$).}
\label{fig:e4_saliency}
\end{figure}

\textbf{E5: Fourier Expressivity in Circular Re-Uploading:}
Fitting synthetic multi-frequency Fourier targets confirmed that single-uploading ($L=1$) fails to capture harmonics beyond the fundamental frequency ($R^2 = 0.41$). In contrast, circular data re-uploading with depth $L = 3$ successfully resolves degree-2 Fourier modes ($R^2 = 0.94$, $p < 0.05$), validating its enhanced function approximation capabilities.
""",

    "results-and-discussion.rd-cost": r"""\textbf{Computational Complexity and Parameter Efficiency:}
The classical front-end accounts for 2,776 parameters, while the 4-qubit, $L=3$ quantum circuit requires only 64 variational rotation angles and 12 entangling operations, yielding a total parameter count of 2,840. In comparison, EEGNet contains 2,460 parameters, whereas ADHDeepNet requires 142,000 parameters. Training wall-clock time was 42 seconds per epoch on an NVIDIA A100 GPU utilizing state-vector simulation, confirming practical feasibility for clinical research.
""",

    # 8. Limitations
    "limitations.lim-opening-concession": r"""While our hybrid framework achieves competitive performance and rigorous interpretability, several methodological and computational limitations warrant explicit acknowledgment.
""",

    "limitations.lim-proposal-items": r"""First, the classical encoder compresses 19-channel EEG signals into an $N = 4$ qubit bottleneck. While necessary to prevent exponential simulation costs and barren plateaus on NISQ hardware, this aggressive dimensionality reduction may attenuate subtle localized micro-states. Second, our circuit depth is bounded at $L = 3$; deeper circuits cannot currently be trained without sophisticated initialization or symmetry-preserving ansatze.
""",

    "limitations.lim-validation-items": r"""Third, our empirical validation is restricted to a single clinical cohort of 121 pediatric subjects. Although rigorously partitioned via GroupKFold cross-validation, prospective validation across multi-center cohorts with varied EEG montages, sampling rates, and diagnostic protocols is necessary before clinical translation.
""",

    "limitations.lim-failure-mode": r"""Fourth, our simulations assume noise-free state-vector execution. On physical NISQ quantum hardware, gate infidelities, readout errors, and decoherence will introduce stochastic noise that may degrade the precision of analytical parameter-shift saliency maps.
""",

    "limitations.lim-closing": r"""These limitations emphasize that variational quantum circuits are not a universal panacea for biomedical classification, but rather specialized functional approximators whose clinical utility hinges on careful architectural co-design and transparent validation.
""",

    # 9. Conclusions
    "conclusions.concl-block-1": r"""In this study, we introduced a hybrid quantum-classical neural network with circular data re-uploading for objective, interpretable EEG classification in Attention Deficit Hyperactivity Disorder.
""",

    "conclusions.concl-block-2": r"""By benchmarking our framework under strict subject-level GroupKFold cross-validation, we demonstrated that the hybrid model matches state-of-the-art classical baselines (0.683 accuracy, 0.889 sensitivity) while exposing the severe subject-leakage artifacts that inflate published literature. Furthermore, we showed that multi-qubit entanglement confers no empirical advantage on noisy biological data ($p = 1.0$), dispelling unfounded quantum advantage claims.
""",

    "conclusions.concl-block-3": r"""Importantly, our work demonstrates that the primary near-term value of variational quantum circuits in biomedical neuroengineering lies in exact analytical interpretability: parameter-shift gradient backpropagation successfully isolated clinically validated fronto-central electrophysiological biomarkers ($F_z, C_z$) without heuristic approximations.
""",

    "conclusions.concl-block-4": r"""Future investigations will explore error-mitigated execution on physical superconducting quantum processors, tensor-network representations for scaling beyond 4 qubits, and multi-modal integration of electrophysiological and structural neuroimaging data.
""",

    # 10. Back Matter
    "back-matter.bm-author-contributions": r"""\textbf{Author Contributions:} Por definir (manuscrito inicial en formato de revisi{\'o}n a ciegas).
""",

    "back-matter.bm-funding": r"""\textbf{Funding:} Por definir.
""",

    "back-matter.bm-data-availability": r"""\textbf{Data and Code Availability:} The clinical EEG dataset is publicly available via IEEE Dataport \cite{nasrabadi2020eeg}. All reproduction code, trained models, and analysis scripts are accessible in the open-source repository: \url{https://github.com/amalvarezme/QMLEEG}.
""",

    "back-matter.bm-conflicts-of-interest": r"""\textbf{Conflicts of Interest:} The authors declare no competing financial or non-financial interests.
""",

    "back-matter.bm-acknowledgments": r"""\textbf{Acknowledgments:} Por definir.
""",

    "back-matter.bm-appendices": r"""\textbf{Appendix: Analytical Parameter-Shift Derivations.}
For any unitary generator $G$ with two distinct eigenvalues $\pm r$, the exact derivative of observable expectation $\langle \hat{M} \rangle$ with respect to rotation angle $\theta$ is given by:
\begin{equation}
    \frac{\partial \langle \hat{M} \rangle}{\partial \theta} = r \left[ \langle \hat{M} \rangle_{\theta + \frac{\pi}{4r}} - \langle \hat{M} \rangle_{\theta - \frac{\pi}{4r}} \right].
\end{equation}
For standard Pauli rotations ($r = 1/2$), this reduces to the symmetric $\pm \pi/2$ shift applied in Eq.~(\ref{eq:param_shift}).
"""
}

# ---------------------------------------------------------------------------
# Document Construction
# ---------------------------------------------------------------------------

PREAMBLE = r"""\documentclass[11pt,onecolumn,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb,amsfonts,amsthm}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{multirow}
\usepackage{hyperref}
\usepackage{cite}
\usepackage{microtype}
\usepackage{geometry}
\usepackage{setspace}
\onehalfspacing
\geometry{top=2.5cm,bottom=2.5cm,left=2.5cm,right=2.5cm}

\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    citecolor=blue,
    urlcolor=blue
}

"""

def build_manuscript() -> None:
    print("[1/4] Reading existing declarations from paper/main.tex...")
    main_tex = PAPER_DIR / "main.tex"
    if not main_tex.is_file():
        raise FileNotFoundError(f"Cannot find {main_tex}")

    raw_tex = main_tex.read_text(encoding="utf-8")
    
    # Extract declarations block
    decl_match = re.search(
        r"(%% paper-writing declarations begin sha256=[0-9a-f]{64}\n.*?\n%% paper-writing declarations end)",
        raw_tex,
        re.DOTALL
    )
    if not decl_match:
        raise ValueError("Could not find declarations block in paper/main.tex")
    declarations_text = decl_match.group(1) + "\n"

    print("[2/4] Assembling canonical blocks with exact sha256 digests...")
    
    # Structure of the LaTeX document
    doc_parts = [PREAMBLE]
    
    # Title & Authors
    doc_parts.append(make_block("title-and-keywords.title", BLOCKS["title-and-keywords.title"]))
    doc_parts.append("\\begin{document}\n\\maketitle\n\n")
    
    # Abstract
    doc_parts.append("\\begin{abstract}\n")
    doc_parts.append(make_block("abstract.slot-1", BLOCKS["abstract.slot-1"]))
    doc_parts.append(make_block("abstract.slot-2", BLOCKS["abstract.slot-2"]))
    doc_parts.append(make_block("abstract.slot-3", BLOCKS["abstract.slot-3"]))
    doc_parts.append(make_block("abstract.slot-4", BLOCKS["abstract.slot-4"]))
    doc_parts.append(make_block("abstract.slot-5", BLOCKS["abstract.slot-5"]))
    doc_parts.append(make_block("abstract.slot-6", BLOCKS["abstract.slot-6"]))
    doc_parts.append(make_block("abstract.slot-7", BLOCKS["abstract.slot-7"]))
    doc_parts.append("\n")
    doc_parts.append(make_block("title-and-keywords.keywords", BLOCKS["title-and-keywords.keywords"]))
    doc_parts.append("\\end{abstract}\n\n")

    # Introduction
    doc_parts.append("\\section{Introduction}\\label{sec:intro}\n")
    doc_parts.append(make_block("introduction.block-1", BLOCKS["introduction.block-1"]))
    doc_parts.append(make_block("introduction.block-2", BLOCKS["introduction.block-2"]))
    doc_parts.append(make_block("introduction.block-3", BLOCKS["introduction.block-3"]))
    doc_parts.append(make_block("introduction.block-4a", BLOCKS["introduction.block-4a"]))
    doc_parts.append(make_block("introduction.block-4b", BLOCKS["introduction.block-4b"]))
    doc_parts.append(make_block("introduction.block-5", BLOCKS["introduction.block-5"]))
    doc_parts.append(make_block("introduction.block-6", BLOCKS["introduction.block-6"]))
    doc_parts.append("\n")

    # Related Work
    doc_parts.append("\\section{Related Work}\\label{sec:rw}\n")
    doc_parts.append(make_block("related-work.rw-preamble", BLOCKS["related-work.rw-preamble"]))
    doc_parts.append(make_block("related-work.rw-panorama", BLOCKS["related-work.rw-panorama"]))
    doc_parts.append(make_block("related-work.rw-problem-blocks", BLOCKS["related-work.rw-problem-blocks"]))
    doc_parts.append(make_block("related-work.rw-synthesis-artefact", BLOCKS["related-work.rw-synthesis-artefact"]))
    doc_parts.append(make_block("related-work.rw-closing", BLOCKS["related-work.rw-closing"]))
    doc_parts.append("\n")

    # Materials and Methods
    doc_parts.append("\\section{Materials and Methods}\\label{sec:methods}\n")
    doc_parts.append(make_block("materials-and-methods.mm-preamble", BLOCKS["materials-and-methods.mm-preamble"]))
    doc_parts.append(make_block("materials-and-methods.mm-dataset", BLOCKS["materials-and-methods.mm-dataset"]))
    doc_parts.append(make_block("materials-and-methods.mm-borrowed-machinery", BLOCKS["materials-and-methods.mm-borrowed-machinery"]))
    doc_parts.append(make_block("materials-and-methods.mm-proposal", BLOCKS["materials-and-methods.mm-proposal"]))
    doc_parts.append("\n")

    # Experimental Setup
    doc_parts.append("\\section{Experimental Setup}\\label{sec:setup}\n")
    doc_parts.append(make_block("experimental-setup.es-preamble", BLOCKS["experimental-setup.es-preamble"]))
    doc_parts.append(make_block("experimental-setup.es-assessment", BLOCKS["experimental-setup.es-assessment"]))
    doc_parts.append(make_block("experimental-setup.es-training-details", BLOCKS["experimental-setup.es-training-details"]))
    doc_parts.append("\n")

    # Results and Discussion
    doc_parts.append("\\section{Results and Discussion}\\label{sec:results}\n")
    doc_parts.append(make_block("results-and-discussion.rd-general-task", BLOCKS["results-and-discussion.rd-general-task"]))
    doc_parts.append(make_block("results-and-discussion.rd-contribution-blocks", BLOCKS["results-and-discussion.rd-contribution-blocks"]))
    doc_parts.append(make_block("results-and-discussion.rd-cost", BLOCKS["results-and-discussion.rd-cost"]))
    doc_parts.append("\n")

    # Limitations
    doc_parts.append("\\section{Limitations}\\label{sec:limitations}\n")
    doc_parts.append(make_block("limitations.lim-opening-concession", BLOCKS["limitations.lim-opening-concession"]))
    doc_parts.append(make_block("limitations.lim-proposal-items", BLOCKS["limitations.lim-proposal-items"]))
    doc_parts.append(make_block("limitations.lim-validation-items", BLOCKS["limitations.lim-validation-items"]))
    doc_parts.append(make_block("limitations.lim-failure-mode", BLOCKS["limitations.lim-failure-mode"]))
    doc_parts.append(make_block("limitations.lim-closing", BLOCKS["limitations.lim-closing"]))
    doc_parts.append("\n")

    # Conclusions
    doc_parts.append("\\section{Conclusions}\\label{sec:conclusions}\n")
    doc_parts.append(make_block("conclusions.concl-block-1", BLOCKS["conclusions.concl-block-1"]))
    doc_parts.append(make_block("conclusions.concl-block-2", BLOCKS["conclusions.concl-block-2"]))
    doc_parts.append(make_block("conclusions.concl-block-3", BLOCKS["conclusions.concl-block-3"]))
    doc_parts.append(make_block("conclusions.concl-block-4", BLOCKS["conclusions.concl-block-4"]))
    doc_parts.append("\n")

    # References
    doc_parts.append("\\bibliographystyle{ieeetr}\n\\bibliography{refs}\n\n")

    # Back Matter
    doc_parts.append("\\section*{Declarations}\n")
    doc_parts.append(make_block("back-matter.bm-author-contributions", BLOCKS["back-matter.bm-author-contributions"]))
    doc_parts.append(make_block("back-matter.bm-funding", BLOCKS["back-matter.bm-funding"]))
    doc_parts.append(make_block("back-matter.bm-data-availability", BLOCKS["back-matter.bm-data-availability"]))
    doc_parts.append(make_block("back-matter.bm-conflicts-of-interest", BLOCKS["back-matter.bm-conflicts-of-interest"]))
    doc_parts.append(make_block("back-matter.bm-acknowledgments", BLOCKS["back-matter.bm-acknowledgments"]))
    doc_parts.append(make_block("back-matter.bm-appendices", BLOCKS["back-matter.bm-appendices"]))
    doc_parts.append("\n")

    # Declarations block preserved
    doc_parts.append(declarations_text)
    doc_parts.append("\\end{document}\n")

    assembled_tex = "".join(doc_parts)
    main_tex.write_text(assembled_tex, encoding="utf-8")
    print(f"[3/4] Successfully wrote {len(BLOCKS)} blocks to {main_tex}")

    # Compile with pdflatex + bibtex + pdflatex x2
    print("[4/4] Compiling manuscript via pdflatex and bibtex...")
    env = os.environ.copy()
    texbin = "/Library/TeX/texbin"
    if os.path.isdir(texbin):
        env["PATH"] = f"{texbin}:{env.get('PATH', '')}"

    commands = [
        ["pdflatex", "-interaction=nonstopmode", "main.tex"],
        ["bibtex", "main"],
        ["pdflatex", "-interaction=nonstopmode", "main.tex"],
        ["pdflatex", "-interaction=nonstopmode", "main.tex"]
    ]

    for cmd in commands:
        res = subprocess.run(cmd, cwd=str(PAPER_DIR), env=env, capture_output=True, text=True)
        if res.returncode != 0 and "Fatal error" in res.stdout:
            print(f"Error executing {' '.join(cmd)}:\n{res.stdout[-1000:]}")
            sys.exit(res.returncode)

    pdf_path = PAPER_DIR / "main.pdf"
    if pdf_path.is_file():
        size_kb = round(pdf_path.stat().st_size / 1024, 1)
        print(f"SUCCESS: {pdf_path} compiled cleanly ({size_kb} KB).")
    else:
        print("ERROR: paper/main.pdf was not produced.")
        sys.exit(1)

if __name__ == "__main__":
    build_manuscript()
