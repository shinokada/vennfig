from matplotlib_venn import venn2, venn2_circles
from matplotlib import pyplot as plt


def mut_exclusive(size=15, fill_color='skyblue', bg_color='white', font_size=20,
                  title='Mutually exclusive: A∩B=∅', set_a='A', set_b='B', text_size=15):
    """
    Mutually exclusive Venn diagram

    parameters
    ----------

    size: Set the figure size. The default value is 15.
    fill_color: Set the filling color. The default value is 'skyblue'.
    bg_color: Set the background color. The default value is 'white'.
    font_size: Set the title font size. The default value is 20.
    title: Set the title. The default value is 'Mutually exclusive: A∩B=∅'
    set_a: Set the set name for the left diagram. The default value is 'A'.
    set_b: Set the set name for the left diagram. The default value is 'B'.
    text_size: Set the text size. The default value is 15.

    example
    -------
    mut_exclusive()
    mut_exclusive(size=10, fill_color='#2d5c91', bg_color='#e1e8f0', font_size=25, 
        title='Mutually exclusive: P∩Q=∅', set_a='P', set_b='Q')

    """

    figure, ax = plt.subplots(1, 1, figsize=(size, size))

    ax.set_title(title, fontsize=font_size)

    v = venn2(subsets=(3, 3, 0), set_labels=(set_a, set_b))
    c = venn2_circles(subsets=(3, 3, 0))
    ax.set_axis_on()
    ax.set_facecolor(bg_color)
    ymin, ymax = ax.get_ylim()
    ax.set_ylim(ymin - 0.1, ymax)

    for area in ['01', '10', '11']:
        if area != '11':
            v.get_patch_by_id(area).set_color(fill_color)
            v.get_patch_by_id(area).set_alpha(1)
        txt = v.get_label_by_id(area)
        if txt:
            txt.set_text('')

    plt.rc('font', size=text_size)
    plt.show()
