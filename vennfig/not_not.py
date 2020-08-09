from matplotlib_venn import venn2, venn2_circles
from matplotlib import pyplot as plt


def not_not(subs=1, size=15, fill_color='skyblue', bg_color='white', font_size=20,
            title_a='NOT A', title_b='NOT B', set_a='A', set_b='B'):
    """
    NOT A, NOT B Venn diagram

    parameters
    ----------
    subs: 
        1: default(both)
        2: NOT A 
        3: NOT B
    size: default 15
    fill_color: default 'skyblue'
    bg_color: default 'white'
    font_size: default 20
    title_a: default 'A'
    title_b: default 'B'
    set_a: default 'A'
    set_b: default 'B'

    example
    -------
    not_not()
    not_not(subs=3, size=5, fill_color='#e8e815', bg_color='#f2f2aa', font_size=25, 
        title_b='NOT Q', set_a='P', set_b='Q')

    """

    if subs == 1:
        figure, (ax1, ax2) = plt.subplots(1, 2, figsize=(size, size))
    elif subs == 2:
        figure, ax1 = plt.subplots(1, 1, figsize=(size, size))
    else:
        figure, ax2 = plt.subplots(1, 1, figsize=(size, size))

    if subs == 1 or subs == 2:
        # NOT A
        ax1.set_title(title_a, fontsize=font_size)

        v1 = venn2(subsets=(3, 3, 1), set_labels=(set_a, set_b), ax=ax1)
        c1 = venn2_circles(subsets=(3, 3, 1), ax=ax1)
        ax1.set_axis_on()
        ax1.set_facecolor(fill_color)
        ymin, ymax = ax1.get_ylim()
        ax1.set_ylim(ymin - 0.1, ymax)

        for area in ['01', '10', '11']:
            color = fill_color if area == '01' else bg_color
            v1.get_patch_by_id(area).set_color(color)
            v1.get_patch_by_id(area).set_alpha(1)
            txt = v1.get_label_by_id(area)
            if txt:
                txt.set_text('')

    if subs == 1 or subs == 3:
        # NOT B
        ax2.set_title(title_b, fontsize=font_size)

        v2 = venn2(subsets=(3, 3, 1), set_labels=(set_a, set_b), ax=ax2)
        c2 = venn2_circles(subsets=(3, 3, 1), ax=ax2)
        ax2.set_axis_on()
        ax2.set_facecolor(fill_color)
        ymin, ymax = ax2.get_ylim()
        ax2.set_ylim(ymin - 0.1, ymax)

        for area in ['01', '10', '11']:
            color = fill_color if area == '10' else bg_color
            v2.get_patch_by_id(area).set_color(color)
            v2.get_patch_by_id(area).set_alpha(1)
            txt = v2.get_label_by_id(area)
            if txt:
                txt.set_text('')

    plt.show()
