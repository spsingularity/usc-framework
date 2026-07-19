#!/usr/bin/env python3
"""Figure for Paper V (USC framework): the unification schematic — three faces sharing one
entropy clock, the shared vertex, and the NESS character. Matches PROGRAM_MAP."""
import os
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = os.path.join(os.path.dirname(__file__), "..", "paper", "figures")
os.makedirs(OUT, exist_ok=True)

def fig_unification():
    fig, ax = plt.subplots(figsize=(9.2, 5.6)); ax.set_xlim(0, 12); ax.set_ylim(0, 9); ax.axis("off")
    def box(x, y, w, h, t, c, fc, fs=8.6):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.04,rounding_size=0.10",
                     lw=1.7, edgecolor=c, facecolor=fc)); ax.text(x+w/2, y+h/2, t, ha="center", va="center", fontsize=fs)
    def arr(x1, y1, x2, y2, c="0.45", style="-|>"):
        ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style, mutation_scale=13, lw=1.4, color=c))

    # the clock at the top
    box(3.6, 8.0, 4.8, 0.85, r"entropy clock  $\mathcal{D}_E=\dot\Theta_E/H=\frac{3}{2}(1-w)$", "#e67e22", "#fef5e7", 9.5)

    faces = [
        (0.3, "#2980b9", "#eaf2f8", "DUSK — dark energy (SEDE)", "H-linear volume-law;\nΔDIC = −3.5 vs ΛCDM;\n+2–3% fσ8", "I·II·III·IV"),
        (4.3, "#c0392b", "#fdedec", "DAWN — matter genesis (ECCG)", "co-genesis; f_B=28/79;\nΣmν 59–64 meV;\nμ from transmutation", "VI·VII"),
        (8.3, "#27ae60", "#eafaf1", "GALACTIC — MOND (APDM)", "rate branch a₀∝H(z);\nworldline cot-kernel;\ncoefficient open", "VIII"),
    ]
    for x, c, fc, title, body, papers in faces:
        box(x, 5.4, 3.4, 1.9, title + "\n\n" + body, c, fc)
        ax.text(x+1.7, 5.15, papers, ha="center", fontsize=7.5, color=c, style="italic")
        arr(6.0, 8.0, x+1.7, 7.3, c)   # clock -> each face

    # shared structures band
    box(0.3, 3.2, 11.4, 1.2,
        "SHARED:  (1) clock-halves sum to 3 (exact identity)   ·   (2) one vertex $T^{\\mu\\nu}\\nabla_\\mu X_{a\\nu}$ "
        "(dusk injection = galactic inertia)\n(3) all faces are driven non-equilibrium steady states — never KMS-thermal   ·   "
        "(4) scale chain $\\alpha_s(M_{\\rm Pl})\\to\\Lambda_h\\to\\mu\\to a_0$", "#7f8c8d", "#f4f6f6", 8.4)
    for x, c, *_ in faces: arr(x+1.7, 5.4, x+1.7, 4.4, c)

    box(2.0, 1.3, 8.0, 0.95,
        "frozen falsifier matrix P1–P20 (hash-committed 2026-07-16)  ·  two no-gos: clock never sources matter ($R_0=0$, spurion)",
        "#8e44ad", "#f5eef8", 8.4)
    arr(6.0, 3.2, 6.0, 2.25, "#8e44ad")

    ax.set_title("USC: three faces of one entropy clock (a framework, with its falsifier matrix)", fontsize=11.5)
    fig.tight_layout(); p = f"{OUT}/fig1_unification.png"; fig.savefig(p, dpi=170); plt.close(fig); print("wrote", p)

if __name__ == "__main__":
    fig_unification()
