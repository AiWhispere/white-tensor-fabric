white-tensor-fabric/
├── README.md
├── pyproject.toml
├── LICENSE
├── docs/
│   ├── architecture_spec.md
│   └── metric_tensor_mechanics.md
├── examples/
│   ├── basic_resonance.py
│   └── dynamic_contraction_loop.py
├── tests/
│   ├── test_metric.py
│   ├── test_wave_superposition.py
│   └── test_thermodynamics.py
└── white_tensor_fabric/
    ├── __init__.py
    ├── core/
    │   ├── __init__.py
    │   ├── metric.py            # Dynamic metric tensor g_mu_nu & volume elements
    │   ├── syntax.py            # Metric-weighted Einstein summation contractions
    │   └── invariants.py        # Boundary checks & thermodynamic invariants
    ├── dynamics/
    │   ├── __init__.py
    │   ├── wave.py              # Standing wave memory bank & phase-locking
    │   ├── interference.py      # Multi-branch wave superposition & cross-terms
    │   └── thermodynamics.py    # Local energy conservation & metric dilation
    └── engine/
        ├── __init__.py
        ├── membrane.py          # Elastic membrane unifying metric & wave banks
        └── runtime.py           # Master execution loop & state commit logic
