import streamlit as st
import numpy as np
import pandas as pd

st.title("MOSFET 전류 계산기")

Vgs = st.number_input("Vgs (게이트-소스 전압, V)를 입력하세요:", value=2.0)
Vds = st.number_input("Vds (드레인-소스 전압, V)를 입력하세요:", value=5.0)
Kn = st.number_input("Kn (MOSFET 성능 수치, mA/V^2)를 입력하세요:", value=0.5)
Vth = st.number_input("Vth (임계 전압, V)를 입력하세요:", value=1.0)

def calculate_current(Vgs, Vds, Kn, Vth):
    if Vgs <= Vth:
        return 0
    elif Vds < Vgs - Vth:
        return Kn * ((Vgs - Vth) * Vds - (Vds ** 2) / 2)
    else:
        return (Kn / 2) * (Vgs - Vth) ** 2

Id = calculate_current(Vgs, Vds, Kn, Vth)
st.write(f"계산된 드레인 전류 Id는 {Id:.3f} mA 입니다.")

Vds_values = np.linspace(0, 10, 200)
Id_values = [calculate_current(Vgs, v, Kn, Vth) for v in Vds_values]

df = pd.DataFrame({
    'Vds': Vds_values,
    'Id': Id_values
}).set_index('Vds')

st.line_chart(df)
