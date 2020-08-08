from matplotlib_venn import venn2, venn2_circles
from matplotlib import pyplot as plt


def subsets(size=15, fill_color='skyblue', bg_color='white', font_size=20):
    """
    Subsets Venn diagram

    parameters
    size: figsuze, default 15,15
    fill_color: default skyblue
    bg_color: default white
    font_size: default 20

    example
    subsets()
    subsets(size=5, fill_color='#f5b705', bg_color='#f7edd0', font_size=20)

    """

    v = venn2(subsets=(5, 0, 2))
    c = venn2_circles(subsets=(5, 0, 2))

    for area in ['01', '10', '11']:
        v.get_patch_by_id(area).set_color(fill_color)
        v.get_patch_by_id(area).set_alpha(1)
        txt = v.get_label_by_id(area)
        if txt:
            txt.set_text('')

    plt.text(-0.6, 0.5, r'U', fontsize=font_size)
    plt.gca().set_axis_on()
    plt.gca().set_facecolor(bg_color)
    plt.title("Subsets", fontsize=font_size)
    ymin, ymax = plt.gca().get_ylim()
    plt.ylim(ymin - 0.1, ymax)
    plt.show()
