from matplotlib_venn import venn2, venn2_circles
from matplotlib import pyplot as plt


def subsets(size=15, fill_color='skyblue', bg_color='white', font_size=20,
            title='Subsets', set_a='A', set_b='B', text_size=15):
    """
    Subsets Venn diagram

    parameters
    ---------- 

    size: Set the figure size. The default value is 15.
    fill_color: Set the filling color. The default value is 'skyblue'.
    bg_color: Set the background color. The default value is 'white'.
    font_size: Set the title font size. The default value is 20.
    title: Set the title. The default value is 'Subsets'.
    set_a: Set the set name for the left diagram. The default value is 'A'.
    set_b: Set the set name for the left diagram. The default value is 'B'.
    text_size: Set the text size. The default value is 15.

    example
    -------
    subsets()
    subsets(size=5, fill_color='#f5b705', bg_color='#f7edd0', font_size=20,
        title='Subsets of P', set_a='P', set_b='Q')

    """

    v = venn2(subsets=(5, 0, 2), set_labels=(set_a, set_b))
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
    plt.title(title, fontsize=font_size)
    ymin, ymax = plt.gca().get_ylim()
    plt.ylim(ymin - 0.1, ymax)
    plt.rc('font', size=text_size)
    plt.show()
