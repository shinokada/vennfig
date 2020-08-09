from matplotlib_venn import venn2, venn2_circles
from matplotlib import pyplot as plt


def true_false(subs=1, size=15, fill_color='skyblue', bg_color='white', font_size=20,
               title_a='TRUE', title_b='FALSE', set_a='A', set_b='B'):
    """
    TRUE, FALSE Venn diagram

    parameters
    ----------
    subs: 
        1: default(both)
        2: TRUE
        3: FALSE
    size: default 15,15
    fill_color: default 'skyblue'
    bg_color: default 'white'
    font_size: default 20
    title_a: default 'TRUE'
    title_b: default 'FALSE'
    set_a: default 'A'
    set_b: default 'B'

    example
    -------
    true_false()
    true_false(subs=2, size=5, fill_color='#d0f7f3', bg_color='#13edd7', title_a='P, Q, TRUE',
           font_size=25, set_a='P', set_b='Q')

    """

    if subs == 1:
        figure, (ax1, ax2) = plt.subplots(1, 2, figsize=(size, size))
    elif subs == 2:
        figure, ax1 = plt.subplots(1, 1, figsize=(size, size))
    else:
        figure, ax2 = plt.subplots(1, 1, figsize=(size, size))

    if subs == 1 or subs == 2:
        # TRUE
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
        # FALSE
        ax2.set_title(title_b, fontsize=font_size)

        v2 = venn2(subsets=(3, 3, 1), set_labels=(set_a, set_b), ax=ax2)
        c2 = venn2_circles(subsets=(3, 3, 1), ax=ax2)
        ax2.set_axis_on()
        ax2.set_facecolor(bg_color)
        ymin, ymax = plt.gca().get_ylim()
        ax2.set_ylim(ymin - 0.1, ymax)

        for area in ['01', '10', '11']:
            v2.get_patch_by_id(area).set_color(bg_color)
            v2.get_patch_by_id(area).set_alpha(1)
            txt = v2.get_label_by_id(area)
            if txt:
                txt.set_text('')

    plt.show()
