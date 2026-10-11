# A User's Guide to Hypervector Linear Transdimensional Algebra (HTLA)

## 1. Introduction: What is HTLA?

Hypervector Linear Transdimensional Algebra (HTLA) is the mathematical foundation of the Hyperdimensional Vector Database (HVD). It is a novel framework designed to perform linear algebra on data that resides in spaces of different dimensions. In the real world, data is messy and heterogeneous; it comes from different sources, modalities, and scales (e.g., text embeddings, image features, sensor readings).

Traditional linear algebra requires data to be in a single, uniform vector space. This often forces developers to flatten, pad, or concatenate data, which can destroy important structural information. HTLA solves this "curse of heterogeneity" by providing a unified calculus for operating on multi-modal data while preserving the unique identity and dimensionality of each component.

This guide will walk you through the core concepts, key operations, and practical applications of HTLA.

## 2. Core Concepts

### 2.1. Hypervectors and Hypervector Spaces

The fundamental object in HTLA is the **hypervector**. A hypervector is a tuple of vectors, where each vector component belongs to a vector space of a potentially different dimension. Each component is identified by a unique **dimension label**.

Formally, a hypervector space `H` is the direct sum of several real vector spaces:

H = ⨁_{ℓ∈L} ℝ^{n_ℓ}

Where:
- `L` is the set of dimension labels (e.g., 'text', 'image', 'audio').
- `n_ℓ` is the dimension of the vector space associated with label `ℓ`.

An individual hypervector `H` is a collection of vectors `(H_ℓ)` for each label `ℓ` in `L`.

**In practice (Python implementation):**

A hypervector can be represented as a dictionary where keys are the dimension labels and values are NumPy arrays.

```python
import numpy as np

class HyperVector:
    """Represents a hypervector as a collection of components indexed by dimension labels."""
    def __init__(self, components: dict[str, np.ndarray]):
        self.components = components
        self.labels = list(components.keys())

    def __repr__(self):
        comp_str = ', '.join([f'{label}: {comp.shape}' for label, comp in self.components.items()])
        return f"HyperVector({comp_str})"

# Example: A hypervector with text and image components
hv = HyperVector({
    'text': np.random.randn(128),  # 128-dimensional text embedding
    'image': np.random.randn(512) # 512-dimensional image feature vector
})

print(hv)
# Output: HyperVector(text: (128,), image: (512,))
```

### 2.2. Transdimensional Operators

A **transdimensional operator** is a linear map that operates on hypervectors. These operators are represented as **block matrices**, where each block defines a linear transformation from a source component space to a target component space.

An operator `L` mapping a source hypervector space `H_s` to a target space `H_t` is defined by a collection of blocks `L_{t,s}`, where each block is a standard matrix that maps the vector for source label `s` to the vector for target label `t`.

**In practice (Python implementation):**

A block operator can be represented as a nested dictionary.

```python
class BlockOperator:
    """Represents a transdimensional operator as a block matrix."""
    def __init__(self, blocks: dict[str, dict[str, np.ndarray]]):
        self.blocks = blocks

    def apply(self, hv: HyperVector) -> HyperVector:
        # (Implementation details omitted for brevity, see full code examples below)
        pass

# Example: An operator that fuses 'text' and 'image' data into a 'fusion' space
fusion_operator = BlockOperator({
    'fusion': {
        'text': np.random.randn(64, 128),  # Maps 128-D text to 64-D fusion
        'image': np.random.randn(64, 512) # Maps 512-D image to 64-D fusion
    }
})
```

### 2.3. Graded Inner Product and Label Kernels

To measure similarity between hypervectors, HTLA uses a **graded inner product**. This is a weighted version of the standard Euclidean inner product, where the contribution of each component is scaled by a weight. These weights are defined by a **label kernel**.

The graded inner product is defined as:

⟨H, K⟩_w = ∑_{ℓ∈L} w_ℓ ⟨H_ℓ, K_ℓ⟩

The weights `w_ℓ` allow you to incorporate semantic knowledge into the system. For example, you can assign higher weights to more important modalities. The label kernel is often defined based on a "distance" between labels, allowing you to model relationships between different components.

## 3. Key Operations in HTLA

### 3.1. Operator Application

Applying a `BlockOperator` to a `HyperVector` involves a block-wise matrix-vector multiplication. For each target component, the contributions from all relevant source components are computed and summed.

HTLA also formally incorporates **noise injection** during operator application, acknowledging that real-world operations are imperfect.

### 3.2. Operator Taxonomy

HTLA provides a clear classification of operators based on their structure and function. This taxonomy helps in designing complex multi-modal systems. The four main types are:

| Type      | Block Structure | Rank Property                  | Example Use Case       |
|-----------|-----------------|--------------------------------|------------------------|
| Ascension | `[A; 0]`        | `rank(A) = p_s`                  | Dimension expansion    |
| Reduction | `[B, C]`        | `rank([B,C]) <= p_s1 + p_s2`   | Feature fusion         |
| **Fusion**    | `[D | E]`         | `rank(D)+rank(E) >= rank([D E])` | Multi-modal input      |
| **Splitting** | `[F; G]`        | `ker(F) ∩ ker(G) = {0}`          | Multi-task output      |

- **Fusion**: Combines multiple input streams (e.g., text and image features) into a single, unified representation.
- **Splitting**: Takes a single representation and maps it to multiple output streams, often for different tasks (e.g., generating a caption and a classification label from an image).

### 3.3. Transdimensional System Solving

HTLA provides a mechanism for solving for an input hypervector `H` given an operator `L` and a target hypervector `b` in the system `LH = b`. This is achieved by flattening the block operator into a single large matrix and using a **regularized pseudoinverse**. This technique allows for stable solutions even when the system is ill-conditioned or rank-deficient.

## 4. Comprehensive Code Examples

The following Python code provides a complete, executable implementation of the core HTLA concepts.

```python
import numpy as np
from scipy.linalg import svd
from sklearn.random_projection import GaussianRandomProjection
from typing import Dict, List, Tuple, Union

# --- Core Classes (HyperVector, BlockOperator) ---

class HyperVector:
    """Represents a hypervector as a collection of components indexed by dimension labels."""
    def __init__(self, components: Dict[str, np.ndarray]):
        self.components = components
        self.labels = list(components.keys())

    def __add__(self, other: 'HyperVector') -> 'HyperVector':
        result = {}
        for label in set(self.labels) | set(other.labels):
            v1 = self.components.get(label, np.zeros_like(next(iter(self.components.values()))))
            v2 = other.components.get(label, np.zeros_like(v1))
            result[label] = v1 + v2
        return HyperVector(result)

    def norm(self, weights: Dict[str, float]) -> float:
        total = 0.0
        for label, vec in self.components.items():
            w = weights.get(label, 1.0)
            total += w * np.dot(vec, vec)
        return np.sqrt(total)

    def inner_product(self, other: 'HyperVector', weights: Dict[str, float]) -> float:
        total = 0.0
        all_labels = set(self.labels) | set(other.labels)
        for label in all_labels:
            w = weights.get(label, 1.0)
            v1 = self.components.get(label, np.zeros_like(next(iter(self.components.values()))))
            v2 = other.components.get(label, np.zeros_like(v1))
            total += w * np.dot(v1, v2)
        return total

    def flatten(self) -> np.ndarray:
        return np.concatenate([v for v in self.components.values()])

class BlockOperator:
    """Represents a transdimensional operator as a block matrix."""
    def __init__(self, blocks: Dict[str, Dict[str, np.ndarray]]):
        self.blocks = blocks
        self.source_labels = set().union(*[b.keys() for b in blocks.values()])
        self.target_labels = set(blocks.keys())

    def apply(self, hv: HyperVector, noise_level: float = 0.0) -> HyperVector:
        result = {}
        for t_label, t_ops in self.blocks.items():
            components = []
            for s_label, mat in t_ops.items():
                if s_label in hv.components:
                    comp = mat @ hv.components[s_label]
                    if noise_level > 0:
                        comp += noise_level * np.random.randn(*comp.shape)
                    components.append(comp)
            if components:
                result[t_label] = np.sum(components, axis=0)
        return HyperVector(result)

    def pseudoinverse(self, regularization: float = 0.1) -> 'BlockOperator':
        source_dims = {label: next(iter(self.blocks.values()))[label].shape[1] for label in self.source_labels}
        target_dims = {label: self.blocks[label][next(iter(self.blocks[label].keys()))].shape[0] for label in self.target_labels}
        full_matrix = np.zeros((sum(target_dims.values()), sum(source_dims.values())))
        row_start = 0
        for t_label in self.target_labels:
            t_dim = target_dims[t_label]
            col_start = 0
            for s_label in self.source_labels:
                s_dim = source_dims[s_label]
                block = self.blocks[t_label].get(s_label, np.zeros((t_dim, s_dim)))
                full_matrix[row_start:row_start+t_dim, col_start:col_start+s_dim] = block
                col_start += s_dim
            row_start += t_dim
        U, S, Vt = svd(full_matrix, full_matrices=False)
        S_inv = np.diag(S / (S**2 + regularization))
        pseudo = Vt.T @ S_inv @ U.T
        blocks = {}
        row_start = 0
        for t_label in self.target_labels:
            t_dim = target_dims[t_label]
            blocks[t_label] = {}
            col_start = 0
            for s_label in self.source_labels:
                s_dim = source_dims[s_label]
                blocks[t_label][s_label] = pseudo[col_start:col_start+s_dim, row_start:row_start+t_dim].T
                col_start += s_dim
            row_start += t_dim
        return BlockOperator(blocks)

# --- Use Case Examples ---

def example_fusion_and_splitting():
    print("\\n--- Example: Fusion and Splitting Operators ---")
    # Define dimensions
    dims = {'text': 128, 'image': 256, 'fusion': 64, 'task1_out': 10, 'task2_out': 1}

    # 1. Fusion Operator
    fusion_op = BlockOperator({
        'fusion': {
            'text': np.random.randn(dims['fusion'], dims['text']),
            'image': np.random.randn(dims['fusion'], dims['image'])
        }
    })
    source_hv = HyperVector({'text': np.random.randn(dims['text']), 'image': np.random.randn(dims['image'])})
    fused_hv = fusion_op.apply(source_hv)
    print(f"Source HyperVector: text({dims['text']}), image({dims['image']})")
    print(f"Fused HyperVector: fusion({fused_hv.components['fusion'].shape[0]})")

    # 2. Splitting Operator
    splitting_op = BlockOperator({
        'task1_out': {'fusion': np.random.randn(dims['task1_out'], dims['fusion'])},
        'task2_out': {'fusion': np.random.randn(dims['task2_out'], dims['fusion'])}
    })
    split_hv = splitting_op.apply(fused_hv)
    print(f"Split HyperVector: task1({split_hv.components['task1_out'].shape[0]}), task2({split_hv.components['task2_out'].shape[0]})")

def example_system_solving():
    print("\\n--- Example: Transdimensional System Solving ---")
    system = BlockOperator({
        'out1': {'in': np.array([[1, 0, 2], [0, 1, 1]])},
        'out2': {'in': np.array([[1, 1, 0]])}
    })
    target = HyperVector({'out1': np.array([4, 3]), 'out2': np.array([2])})
    pseudo_op = system.pseudoinverse(regularization=0.1)
    solution = pseudo_op.apply(target)
    print(f"Solved Input: {solution.components['in']}")
    reconstructed = system.apply(solution)
    error = np.linalg.norm(reconstructed.flatten() - target.flatten())
    print(f"Reconstruction Error: {error:.4f}")

if __name__ == '__main__':
    example_fusion_and_splitting()
    example_system_solving()
```

## 5. Theoretical Guarantees

HTLA is not just a set of convenient operations; it is backed by rigorous mathematical theorems that provide guarantees about its behavior.

-   **Capacity Bound**: This theorem quantifies the information storage capacity of hypervectors, showing how many patterns can be stored and distinguished. It demonstrates that capacity scales with the total dimensionality across all labels.
-   **Concentration of Measure**: This theorem proves that in high-dimensional spaces, the properties of hypervectors (like their inner products) are very stable and robust to noise. Small perturbations in individual components are unlikely to have a major impact on the overall result.
-   **Operator Convergence**: This theorem guarantees that iterative algorithms that learn or refine HTLA operators will converge to stable solutions, which is crucial for building machine learning models based on HTLA.

## 6. Further Reading

This guide provides a high-level overview of HTLA. For a complete, in-depth theoretical treatment, please refer to the original technical paper: [Hypervector Linear Transdimensional Algebra.txt](./Hypervector%20Linear%20Transdimensional%20Algebra.txt).
