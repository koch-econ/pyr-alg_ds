# %% [markdown]
#  ## Инвариант цикла
#
#   См примеры
#   https://www.maths.tcd.ie/~odunlain/u11601/online_notes/pdf_invariants.pdf
#
#  Инвариант используется:
#
#  * для доказательства правильности программ "по индукции"
#  * для придумывания цикла
#
# обоснование факта gcd(𝑏,𝑎)=gcd(𝑏,𝑎 % 𝑏), если b>0
# https://math.stackexchange.com/questions/95799/why-gcdb-qbr-gcdb-r-so-gcdb-a-gcdb-a-bmod-b



# %%


def euclid_gcd(m, n):
    x = m
    y = n
    while y > 0:
        z = x % y
        x = y
        y = z
    return x
#%%
euclid_gcd(6,15)
# %%
