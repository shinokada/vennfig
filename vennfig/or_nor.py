from matplotlib_venn import venn2, venn2_circles
from matplotlib import pyplot as plt


def or_nor(subs=1, size=15, fill_color='skyblue', bg_color='white', font_size=20,
           title_a='A OR B', title_b='A NOR B', set_a='A', set_b='B'):
    """
    OR, NOR Venn diagram

    parameters
    ----------
    subs: 
        1: default(both)
        2: OR 
        3: NOR
    size: default 15
    fill_color: default 'skyblue'
    bg_color: default 'white'
    font_size: default 20
    title_a: default 'A OR B'
    title_b: default 'A NOR B'
    set_a: default 'A'
    set_b: default 'B'

    example
    -------
    or_nor()
    or_nor(subs=3, size=5, fill_color='#88f77c', bg_color='#daf5d7', font_size=25,
      title_b='P NOR Q', set_a='P', set_b='Q')

    """

    if subs == 1:
        figure, (ax1, ax2) = plt.subplots(1, 2, figsize=(size, size))
    elif subs == 2:
        figure, ax1 = plt.subplots(1, 1, figsize=(size, size))
    else:
        figure, ax2 = plt.subplots(1, 1, figsize=(size, size))

    if subs == 1 or subs == 2:
        # A OR B
        ax1.set_title(title_a, fontsize=font_size)

        v1 = venn2(subsets=(3, 3, 1), set_labels=(set_a, set_b), ax=ax1)
        c1 = venn2_circles(subsets=(3, 3, 1), ax=ax1)
        ax1.set_axis_on()
        ax1.set_facecolor(bg_color)
        ymin, ymax = ax1.get_ylim()
        ax1.set_ylim(ymin - 0.1, ymax)

        for area in ['01', '10', '11']:
            v1.get_patch_by_id(area).set_color(fill_color)
            v1.get_patch_by_id(area).set_alpha(1)
            txt = v1.get_label_by_id(area)
            if txt:
                txt.set_text('')

    if subs == 1 or subs == 3:
        # A NOR B
        ax2.set_title(title_b, fontsize=font_size)

        v2 = venn2(subsets=(3, 3, 1), set_labels=(set_a, set_b), ax=ax2)
        c2 = venn2_circles(subsets=(3, 3, 1), ax=ax2)
        ax2.set_axis_on()
        ax2.set_facecolor(fill_color)
        ymin, ymax = ax2.get_ylim()
        ax2.set_ylim(ymin - 0.1, ymax)

        for area in ['01', '10', '11']:
            v2.get_patch_by_id(area).set_color(bg_color)
            v2.get_patch_by_id(area).set_alpha(1)
            txt = v2.get_label_by_id(area)
            if txt:
                txt.set_text('')

    plt.show()
