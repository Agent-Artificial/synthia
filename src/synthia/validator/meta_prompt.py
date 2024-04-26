import random
from dataclasses import dataclass


@dataclass
class Criteria:
    subject_type: str
    specificity: str
    target_audience: str
    detail: str
    abstraction: str
    field: str


def get_fields() -> list[str]:
    """
    Returns a list of fields related to various academic disciplines.
    """
    return [
        "Higher Order Logic",
        "Complexity theory",
        "Fractal information theory",
        "Geometrical music theory",
        "Concurrency theory",
        "Recursive function theory",
        "Calculus",
        "Graph rewrites",
        "Hopf algebra",
        "Programming language theory",
        "Financial Derivatives",
        "Coordination mechanisms",
        "Incentive Design",
        "linear logic",
        "category theory",
        "lambda calculus",
        "Parallel computing",
        "Zero-Knowledge proofs",
        "Functional programming",
        "Formal verification",
        "Interaction Combinators",
        "Automated theorem proving",
        "Type Theory",
        "distributed ledgers",
        "distributed systems",
        "natural language processing",
        "Active Inference",
        "Bioformation",
        "Evolutionary Emergence",
        "Internet",
        "Cryptocurrency",
        "Organizational behavior",
        "Management science",
        "Ontology",
        "Free Energy Principle",
        "Adaptivity",
        "Emergent behavior",
        "Cybernetics",
        "Self-organization",
        "Organizational Psychology",
        "Evolutionary epistemology",
        "Complex Systems",
        "Network economics",
        "Agent-based modeling",
        "Co-evolution",
        "Media theory",
        "Monetary economics",
        "Swarm intelligence",
        "Organizational Ecology",
        "Organizational Cybernetics",
        "Semantic web",
        "Autopoiesis",
        "Stigmergy",
        "Memetics",
        "Synergetics",
        "Resilience Theory",
        "Formal systems",
        "Abstract models of computation",
        "Models of computation",
        "Functional computing",
        "Molecular Biology",
        "Neuroscience",
        "Quantum Physics",
        "Artificial Intelligence",
        "Cryptography",
        "Nanotechnology",
        "Astrophysics",
        "Genetics",
        "Robotics",
        "Bioinformatics",
        "Cognitive Science",
        "Computational Linguistics",
        "Game Theory",
        "Network Science",
        "Organic Chemistry",
        "Particle Physics",
        "Evolutionary Biology",
        "Immunology",
        "Materials Science",
        "Nuclear Physics",
        "Operations Research",
        "Quantum Computing",
        "Systems Biology",
        "Behavioral Economics",
        "Biomedical Engineering",
        "Computational Neuroscience",
        "Data Science",
        "Epidemiology",
        "Fluid Dynamics",
        "Information Theory",
        "Machine Learning",
        "Mathematical Biology",
        "Nonlinear Dynamics",
        "Plasma Physics",
        "Tensor Calculus",
        "Quantum Chemistry",
        "Statistical Mechanics",
        "Theoretical Computer Science",
        "Topology",
        "Computational Fluid Dynamics",
        "Econometrics",
        "Environmental Science",
        "Fractional Calculus",
        "Geophysics",
        "High Energy Physics",
        "Knot Theory",
        "Mathematical Logic",
        "Number Theory",
        "Philosophy",
        "Pharmacology",
        "Macroeconomics",
        "Quantum Field Theory",
        "Relativity",
        "Stochastic Processes",
        "Theoretical Ecology",
        "Thermodynamics",
        "Algebraic Geometry",
        "Astrobiology",
        "Bayesian Statistics",
        "Biophysics",
        "Combinatorics",
        "Computational Geometry",
        "Cosmology",
        "Developmental Biology",
        "Differential Equations",
        "Experimental Psychology",
        "Functional Analysis",
        "Gauge Theory",
        "Harmonic Analysis",
        "Integrable Systems",
        "Mathematical Finance",
        "Metamaterials",
        "Nonequilibrium Thermodynamics",
        "Numerical Analysis",
        "Optimal Control Theory",
        "Partial Differential Equations",
        "Quantum Optics",
        "Representation Theory",
        "Spectral Theory",
        "String Theory",
        "Theoretical Neuroscience",
        "Computational Social Science",
        "Dynamical Systems",
        "Epigenetics",
        "Evolutionary Game Theory",
        "Extremal Combinatorics",
        "Fractal Geometry",
        "Geometric Topology",
        "Gödel's Incompleteness Theorems",
        "Homotopy Theory",
        "Inverse Problems",
        "Lie Algebras",
        "Mathematical Epidemiology",
        "Measure Theory",
        "Operator Algebras",
        "Random Matrix Theory",
        "Soliton Theory",
        "Symplectic Geometry",
        "Additive Combinatorics",
        "Algebraic Topology",
        "Analytic Number Theory",
        "Arithmetic Geometry",
        "Epistemology",
        "Bifurcation Theory",
        "Coding Theory",
        "Combinatorial Game Theory",
        "Computational Topology",
        "Conformal Field Theory",
        "Control Theory",
        "Discrete Geometry",
        "Ergodic Theory",
        "Geometric Measure Theory",
        "Geometric Group Theory",
        "Graph Theory",
        "Harmonic Maps",
        "Computational Storage",
        "Homological Algebra",
        "Kinetic Theory",
        "Large Deviations",
        "Modular Forms",
        "Percolation Theory",
        "Persistent Homology",
        "Probabilistic Number Theory",
        "Quantum Gravity",
        "Quantum Groups",
        "Quantum Information Theory",
        "Quantum Topology",
        "Quasicrystals",
        "Applied Graph Theory",
        "Rational Homotopy Theory",
        "Rough Path Theory",
        "Spectral Graph Theory",
        "Stochastic Differential Equations",
        "Stochastic Geometry",
        "Stochastic Partial Differential Equations",
        "Symbolic Dynamics",
        "Topological Data Analysis",
        "Topological Dynamics",
        "Topological Recursion",
        "Von Neumann Algebras",
        "Algorithmic Information Theory",
        "Algorithmic Randomness",
        "Analytic Combinatorics",
        "Arithmetic Combinatorics",
        "Arithmetic Dynamics",
        "Automata Groups",
        "Braid Groups",
        "Cluster Algebras",
        "Combinatorial Species",
        "Computable Analysis",
        "Computational Algebraic Geometry",
        "Computational Complexity Theory",
        "Computational Group Theory",
        "Computational Number Theory",
        "Computational Topology",
        "Constructive Mathematics",
        "Set Theory",
        "Mathematical Biology",
        "Differential Topology",
        "Discrete Differential Geometry",
        "Acoustic Metamaterials",
        "Adiabatic Quantum Computation",
        "Affective Computing",
        "Agent-Based Computational Economics",
        "Algebraic Coding Theory",
        "Algebraic Quantum Field Theory",
        "Algorithmic Algebraic Geometry",
        "Algorithmic Game Theory",
        "Algorithmic Trading",
        "Analytic Topology",
        "Applied Cryptography",
        "Arithmetic Circuit Complexity",
        "Arithmetic of Function Fields",
        "Artificial Life",
        "Asymptotic Geometric Analysis",
        "Atmospheric Physics",
        "Automorphic Forms",
        "Behavioral Game Theory",
        "Biogeography",
        "Biolinguistics",
        "Biomechanics",
        "Biostatistics",
        "Cellular Automata",
        "Chemical Graph Theory",
        "Chemical Reaction Network Theory",
        "Coalgebra",
        "Cognitive Neurodynamics",
        "Collective Intelligence",
        "Combinatorial Commutative Algebra",
        "Combinatorial Geometry",
        "Combinatorial Matrix Theory",
        "Combinatorial Optimization",
        "Combinatorial Representation Theory",
        "Comparative Genomics",
        "Computational Algebraic Statistics",
        "Computational Astrophysics",
        "Computational Biology",
        "Computational Creativity",
        "Computational Geometry",
        "Computational Intelligence",
        "Computational Materials Science",
        "Computational Mechanics",
        "Computational Musicology",
        "Computational Photography",
        "Computational Psycholinguistics",
        "Computational Semantics",
        "Computational Sociolinguistics",
        "Computational Statistics",
        "Synthetic Biology",
        "Computational Systems Biology",
        "Computer Vision",
        "Condensed Matter Physics",
        "Conformal Geometry",
        "Constraint Programming",
        "Constructive Approximation Theory",
        "Contact Topology",
        "Contextual Bandits",
        "Convex Algebraic Geometry",
        "Cryobiology",
        "Cryptographic Protocols",
        "Electrical Engineering",
        "Cyber-Physical Systems",
        "Data Mining",
        "Decision Theory",
        "Deep Learning",
        "Delay Differential Equations",
        "Diophantine Approximation",
        "Discrete Differential Geometry",
        "Discrete Integrable Systems",
        "Discrete Optimization",
        "DNA Computing",
        "Dynamical Systems",
        "Economic Complexity",
        "Econophysics",
        "Embodied Cognition",
        "Sympoiesis",
        "Evolutionary Computation",
        "Evolutionary Psychology",
        "Explainable Artificial Intelligence",
        "Teleodynamics",
    ]


def get_explination_types() -> list[str]:
    """
    Returns a list of explanation types.

    :return: A list of strings representing different types of explanations.
    :rtype: list[str]
    """
    return [
        "causal",
        "by example",
        "analogies",
        "heuristic",
        "inductive",
        "deductive",
        "functional",
        "teleological",
        "historical",
        "reductionist",
        "storytelling",
        "from first principles",
    ]


def get_subject_types() -> list[str]:
    """
    Returns a list of subject types.

    :return: A list of strings representing different types of subjects.
    :rtype: list[str]
    """

    return [
        "phenomena",
        "process",
        "principles",
        "concepts",
        "methods",
        "systems",
        "theories",
        "patterns",
        "trends",
    ]


def get_levels():
    """
    Returns a list of different levels ranging from "slight" to "very high".
    """
    return [
        "slight",
        "mild",
        "tangible",
        "modest",
        "moderate",
        "substantial",
        "strong",
        "high",
        "intense",
        "very high",
    ]


def get_target_audience():
    """
    Returns a list of target audiences for educational content.

    :return: A list of strings representing different target audiences.
    :rtype: list[str]
    """
    return [
        "middle school student",
        "high school student",
        "layperson",
        "casual reader",
        "enthusiast",
        "hobbyist",
        "undergraduate student",
        "graduate student",
        "early career researcher",
        "experienced researcher",
        "industry expert",
        "academic expert",
        "expert scientist",
        "lead professor",
    ]


def explanation_prompt() -> tuple[str, Criteria]:
    """
    Generates a prompt for a user to pick a specific subject in a random subject type with a random specificity level of esotericity in a random field, 
    that they consider interesting and provide a insightful semantically dense explanation, targetting a random target audience. 
    The user's goal is their comprehension of the explanation, according to their background expertise. The user follows a random abstraction level and a random detail level of detail. 
    The user starts by titling the subject they've picked in quotation marks.

    Returns:
        tuple[str, Criteria]: A tuple containing the generated prompt and a Criteria object containing the subject type, specificity, target audience, detail level, abstraction level, and field.
    """
    subject_types = random.choice(get_subject_types())
    specificity = random.choice(get_levels())
    target_audiences = random.choice(get_target_audience())
    detail = random.choice(get_levels())
    abstraction = random.choice(get_levels())
    fields = random.choice(get_fields())

    criteria = Criteria(
        subject_type=subject_types,
        specificity=specificity,
        target_audience=target_audiences,
        detail=detail,
        abstraction=abstraction,
        field=fields,
    )

    prompt = (
        f"Pick a specific subject in {subject_types} with a {specificity} level of esotericity in the field of {fields}, "
        "you consider interesting and provide a insightful semantically dense explanation, "
        f"targetting a {target_audiences}. "
        "Your goal is their comprehension of the explanation, according to their background expertise. "
        f"Follow a {abstraction} abstraction level and a {detail} level of detail. "
        "Start by titling the subject you've picked in quotation marks."
    )

    return prompt, criteria


def get_miner_prompt(criteria: Criteria, sample_subject: str, sample_length: int):
    """
    Generates a prompt for a miner to provide an insightful and semantically dense explanation of a given subject.

    Args:
        criteria (Criteria): The criteria for the miner's expertise in the field and the target audience.
        sample_subject (str): The subject of the explanation.
        sample_length (int): The target length of the explanation in words.

    Returns:
        str: The generated prompt for the miner.

    """
    return f"You are a top expert in the field of {criteria.field} with deep knowledge on the subject {[sample_subject]}. Provide an insightful semantically dense explanation of the {[sample_subject]} that will be read by a {[criteria.target_audience]}. Your goal is their comprehension of the explanation, according to their background expertise. Follow a {[criteria.abstraction]} level of abstraction and a {[criteria.detail]} level of detail. Target a length of approximately [{sample_length}] words."
