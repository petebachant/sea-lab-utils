import matplotlib.pyplot as plt


def get_fonts(usetex=True):
    """Use a LaTeX-like serif font style for plots.

    usetex=True renders all text with LaTeX, which needs MiKTeX or TeX Live
    installed. usetex=False uses the STIX fonts and math renderer that ship
    with Matplotlib, so no TeX install is needed. Math like $\\alpha$ still
    works, but text outside $...$ is not LaTeX, so write % rather than \\%.
    """
    if usetex:
        plt.rcParams.update({"font.family": "serif", "text.usetex": True})
    else:
        plt.rcParams.update(
            {
                "font.family": "STIXGeneral",
                "mathtext.fontset": "stix",
                "text.usetex": False,
            }
        )
