# vennfig

`vennfig` is a Python package and is a wrapper for [`matplotlib_venn`](https://github.com/konstantint/matplotlib-venn)

You can draw simple Venn diagrams with 2 lines of code.

## Installation:

```
pip install vennfig
```

On Jupyter:

```
!pip install vennfig
```

## Examples

### A, B

```
import vennfig as v
<!-- default -->
v.a_b()

<!-- using params -->
v.a_b(subs=2, size=6, fill_color='#f5b705', bg_color='#f7edd0', 
    font_size=25, title_a='P', set_a='P', set_b='Q')
```

![A, B](image/a_b.png)

### A AND B, A NAND B

```
import vennfig as v
<!-- default -->
v.and_nand()

<!-- using params -->
v.and_nand(subs=2, size=5, fill_color='#f55faa', bg_color='#f2e4eb', 
         font_size=25, title_a='P and Q', title_b='a nand b', set_a='P', set_b='Q')
```

![A AND B, A nand B](image/and_nand.png)

### TRUE, FALSE

```
import vennfig as v
<!-- default -->
v.true_false()

<!-- using params -->
v.true_false(subs=2, size=5, fill_color='#d0f7f3', bg_color='#13edd7', title_a='P, Q, TRUE',
           font_size=25, set_a='P', set_b='Q')
```

![TRUE, FALSE](image/true_false.png)

### OR, NOR

```
import vennfig as v
<!-- default -->
v.or_nor()

<!-- using params -->
v.or_nor(subs=3, size=5, fill_color='#88f77c', bg_color='#daf5d7', font_size=25,
      title_b='P NOR Q', set_a='P', set_b='Q')
```

![OR, NOR](image/or_nor.png)

### XOR, XNOR

```
import vennfig as v
<!-- default -->
v.xor_xnor()

<!-- using params -->
v.xor_xnor(subs=2, size=5, fill_color='#fa8069', bg_color='#fae5e1', 
         font_size=25, title_a='P XOR Q', set_a='P', set_b='Q')
```

![XOR, XNOR](image/xor_xnor.png)

### NOT A, NOT B

```
import vennfig as v
<!-- default -->
v.not_not()

<!-- using params -->
v.not_not(subs=3, size=5, fill_color='#e8e815', bg_color='#f2f2aa', font_size=25, 
        title_b='NOT Q', set_a='P', set_b='Q')
```

![NOT A, NOT B](image/nota_notb.png)

### A NOT B, B NOT A

```
import vennfig as v
<!-- default -->
v.x_not_y()

<!-- using params -->
v.x_not_y(subs=3, size=5, fill_color='#d4812f', bg_color='#e3dad1', font_size=25, 
        title_b='P NOT Q', set_a='P', set_b='Q')
```

![A NOT B, B NOT A](image/anotb.png)


### Implication

```
import vennfig as v
<!-- default -->
v.implication()

<!-- using params -->
v.implication(subs=3, size=5, fill_color='#5ba870', bg_color='#d7f5df', font_size=25, 
        title_b='Q ⇒ P', set_a='P', set_b='Q')
```

![Implication](image/impl.png)

### Mutually exclusive

```
import vennfig as v
<!-- default -->
v.mut_exclusive()

<!-- using params -->
v.mut_exclusive(size=10, fill_color='#2d5c91', bg_color='#e1e8f0', font_size=25, 
        title='Mutually exclusive: P∩Q=∅', set_a='P', set_b='Q')
```

![Mutually exclusive](image/mutual.png)

### Complement

```
import vennfig as v
<!-- default -->
v.complement()

<!-- using params -->
v.complement(subs=2, size=5, fill_color='#3eacb5', bg_color='#c1d9db', font_color='#d40f19', 
           font_size=25, title_a='Complement P', set_a='P', set_b="P'")
```

![Complement](image/complement.png)

### Subsets

```
import vennfig as v
<!-- default -->
v.subsets()

<!-- using params -->
v.subsets(size=5, fill_color='#f5b705', bg_color='#f7edd0', font_size=20,
        title='Subsets of P', set_a='P', set_b='Q')
```

![Subsets](image/subsets.png)
