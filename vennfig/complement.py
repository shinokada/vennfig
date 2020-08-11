from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt


def complement(subs=1, size=15, fill_color='skyblue', bg_color='white', font_color='#000',
               font_size=20, title_a='Complement A', title_b="Complement A'",
               set_a="A", set_b="A'", text_size=15):
    """
    Complement Venn diagram

    parameters
    ----------

    subs: 
        1 shows the both diagram.(default)
        2 shows A filled diagram.
        3 shows A' filled diagram.

    size: Set the figure size. The default value is 15.
    fill_color: Set the tfilling color. The default value is 'skyblue'.
    bg_color: Set the background color. The default value is 'white'.
    font_size: Set the title font size. The default value is 20.
    title_a: Set the title value for the left diagram. The default value is 'Complement A'.
    title_b: Set the title value for the left diagram. The default value is "Complement A'".
    set_a: Set the set name for the left diagram. The default value is 'A'.
    set_b: Set the set name for the left diagram. The default value is 'B'.
    text_size: Set the text size. The default value is 15.

    example
    -------
    complement()
    complement(subs=2, size=5, fill_color='#3eacb5', bg_color='#c1d9db', font_color='#d40f19', 
           font_size=25, title_a='Complement P', set_a='P', set_b="P'")

    """

    if subs == 1:
        figure, (ax1, ax2) = plt.subplots(1, 2, figsize=(size, size))
    elif subs == 2:
        figure, ax1 = plt.subplots(1, 1, figsize=(size, size))
    else:
        figure, ax2 = plt.subplots(1, 1, figsize=(size, size))

    if subs == 1 or subs == 2:
        # A filled
        v1 = venn3(subsets=(1, 1, 0, 1, 0, 0, 0),
                   set_labels=('', '', ''), ax=ax1)
        c1 = venn3_circles(subsets=(1, 1, 0, 1, 0, 0, 0), ax=ax1)
        c1[0].set_lw(0)
        c1[2].set_lw(0)

        for area in ['001', '100']:
            v1.get_patch_by_id(area).set_color(bg_color)
            txt = v1.get_label_by_id(area)
            if txt:
                txt.set_text('')

        v1.get_patch_by_id('010').set_color(fill_color)
        v1.get_patch_by_id('010').set_alpha(1)
        v1.get_label_by_id('010').set_text(set_a)
        v1.get_label_by_id('010').set_fontsize(font_size)
        v1.get_label_by_id('010').set_color(font_color)
        v1.get_label_by_id('001').set_text(set_b)
        v1.get_label_by_id('001').set_fontsize(font_size)
        v1.get_label_by_id('001').set_color(font_color)

        ax1.set_axis_on()
        ax1.set_facecolor(bg_color)
        ax1.text(-1, 0.2, r'U', fontsize=font_size)
        ax1.set_title(title_a, fontsize=font_size)

    if subs == 1 or subs == 3:
        # A' filled
        v2 = venn3(subsets=(1, 1, 0, 1, 0, 0, 0),
                   set_labels=('', '', ''), ax=ax2)
        c2 = venn3_circles(subsets=(1, 1, 0, 1, 0, 0, 0), ax=ax2)
        c2[0].set_lw(0)
        c2[2].set_lw(0)

        for area in ['001', '100']:
            v2.get_patch_by_id(area).set_color(fill_color)
            txt = v2.get_label_by_id(area)
            if txt:
                txt.set_text('')

        v2.get_patch_by_id('010').set_color(bg_color)
        v2.get_patch_by_id('010').set_alpha(1)
        v2.get_label_by_id('010').set_text(set_a)
        v2.get_label_by_id('010').set_fontsize(font_size)
        v2.get_label_by_id('010').set_color(font_color)
        v2.get_label_by_id('001').set_text(set_b)
        v2.get_label_by_id('001').set_fontsize(font_size)
        v2.get_label_by_id('001').set_color(font_color)

        ax2.set_axis_on()
        ax2.set_facecolor(fill_color)
        ax2.text(-1, 0.2, r'U', fontsize=font_size)
        ax2.set_title(title_b, fontsize=font_size)

    plt.rc('font', size=text_size)
    plt.show()
