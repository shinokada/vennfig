from matplotlib_venn import venn2, venn2_circles
from matplotlib import pyplot as plt


def implication(subs=1, size=15, fill_color='skyblue', bg_color='white', font_size=20,
                title_a='A ⇒ B', title_b='B ⇒ A', set_a='A', set_b='B', text_size=15):
    """
    Implication A ⇒ B, B ⇒ A Venn diagram

    parameters
    ----------

    subs: 
        1 shows the both diagram.(default)
        2 shows the A ⇒ B diagram.
        3 shows the B ⇒ A diagram.

    size: Set the figure size. The default value is 15.
    fill_color: Set the tfilling color. The default value is 'skyblue'.
    bg_color: Set the background color. The default value is 'white'.
    font_size: Set the title font size. The default value is 20.
    title_a: Set the title value for the left diagram. The default value is 'A ⇒ B'.
    title_b: Set the title value for the left diagram. The default value is 'B ⇒ A'.
    set_a: Set the set name for the left diagram. The default value is 'A'.
    set_b: Set the set name for the left diagram. The default value is 'B'.
    text_size: Set the text size. The default value is 15.

    example
    -------
    implication()
    implication(subs=3, size=5, fill_color='#5ba870', bg_color='#d7f5df', font_size=25, 
        title_b='Q ⇒ P', set_a='P', set_b='Q')

    """

    if subs == 1:
        figure, (ax1, ax2) = plt.subplots(1, 2, figsize=(size, size))
    elif subs == 2:
        figure, ax1 = plt.subplots(1, 1, figsize=(size, size))
    else:
        figure, ax2 = plt.subplots(1, 1, figsize=(size, size))

    if subs == 1 or subs == 2:
        # A ⇒ B
        ax1.set_title(title_a, fontsize=font_size)

        v1 = venn2(subsets=(3, 3, 1), set_labels=(set_a, set_b), ax=ax1)
        c1 = venn2_circles(subsets=(3, 3, 1), ax=ax1)
        ax1.set_axis_on()
        ax1.set_facecolor(fill_color)
        ymin, ymax = ax1.get_ylim()
        ax1.set_ylim(ymin - 0.1, ymax)

        for area in ['01', '10', '11']:
            color = fill_color if area != '10' else bg_color
            v1.get_patch_by_id(area).set_color(color)
            v1.get_patch_by_id(area).set_alpha(1)
            txt = v1.get_label_by_id(area)
            if txt:
                txt.set_text('')

    if subs == 1 or subs == 3:
        # B ⇒ A
        ax2.set_title(title_b, fontsize=font_size)

        v2 = venn2(subsets=(3, 3, 1), set_labels=(set_a, set_b), ax=ax2)
        c2 = venn2_circles(subsets=(3, 3, 1), ax=ax2)
        ax2.set_axis_on()
        ax2.set_facecolor(fill_color)
        ymin, ymax = ax2.get_ylim()
        ax2.set_ylim(ymin - 0.1, ymax)

        for area in ['01', '10', '11']:
            color = fill_color if area != '01' else bg_color
            v2.get_patch_by_id(area).set_color(color)
            v2.get_patch_by_id(area).set_alpha(1)
            txt = v2.get_label_by_id(area)
            if txt:
                txt.set_text('')

    plt.rc('font', size=text_size)
    plt.show()
