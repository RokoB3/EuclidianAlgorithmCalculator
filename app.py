import streamlit as st

st.write("""
# The Euclidian Algorithm Calculator!
Input ***A*** and ***B*** to compute the gcd and find ***r*** and ***s*** such that **gcd = Ar + Bs**
""")

a = st.number_input("Enter A", min_value=1, format='%i')
b = st.number_input("Enter B", min_value=1, format='%i')
if a<b:
    c = b
    b = a 
    a = c

az = [a]
bs = [b]
qs = []
rs = []

qs.append(int(az[-1]/bs[-1]))
rs.append(az[-1] - (bs[-1]*qs[-1]))

while rs[-1] != 0:
    az.append(bs[-1])
    bs.append(rs[-1])
    qs.append(int(az[-1]/bs[-1]))
    rs.append(az[-1] - (bs[-1]*qs[-1]))

print(f'\ngcd of {a} and {b} is {bs[-1]}')
gcd = bs[-1]
counts = [0]*len(az)

if len(az) == 1:
    print(f"\n{gcd} = 0*{az[0]} + 1*{bs[0]}")
    st.write(f"""
    > ### The gcd of {a} and {b} is **{gcd}**

    > ### {gcd} = (0\*{az[0]}) + (1\*{bs[0]})
    > #### r = 0
    > #### s = 1
    """)


if len(az) >= 2:
    counts[1] = 1
    counts[0] = -qs[-2]
    i = 0
    while counts[-1] == 0:
        counts[i+2] = counts[i]
        counts[i+1] += counts[i]*-qs[-(3+i)]
        counts[i] = 0
        i+=1
    print(f"\n{gcd} = {counts[-1]}*{az[0]} + {counts[-2]}*{bs[0]}")

    st.write(f"""
    > ### The gcd of {a} and {b} is **{gcd}**

    > ### {gcd} = ({counts[-1]}\*{az[0]}) + ({counts[-2]}\*{bs[0]})
    > #### r = {counts[-1]}
    > #### s = {counts[-2]}
    """)
