import streamlit as st
import matplotlib.pyplot as plt

# 함수: 드레인 전류 계산 (단순 임계 동작 모델 사용)
def calculate_drain_current(Vg, Vth, k):
    if Vg < Vth:
        return 0
    else:
        return k * (Vg - Vth) ** 2

# Streamlit UI 구성
st.title("MOSFET 임계 전압(Vth) 시뮬레이터")

# 사용자 입력 받기
Vth = st.number_input("임계 전압 Vth (V)", min_value=0.0, max_value=10.0, value=2.0)
k = st.number_input("상수 k (전류 계수)", min_value=0.01, max_value=10.0, value=1.0)
start = st.number_input("시작 게이트 전압 Vg (V)", min_value=0.0, max_value=10.0, value=0.0)
end = st.number_input("끝 게이트 전압 Vg (V)", min_value=0.0, max_value=20.0, value=5.0)
step = st.number_input("증가 단위 (step)", min_value=0.01, max_value=5.0, value=0.1)

# 버튼 누르면 계산 시작
if st.button("시뮬레이션 시작"):
    Vg_values = []
    Id_values = []
    Vg = start

    while Vg <= end:
        Id = calculate_drain_current(Vg, Vth, k)
        Vg_values.append(round(Vg, 2))
        Id_values.append(Id)
        Vg += step

    # 결과 표로 출력
    st.subheader("시뮬레이션 결과")
    results = {"Vg (V)": Vg_values, "Id (A)": Id_values}
    st.dataframe(results)

    # 그래프로 출력
    st.subheader("드레인 전류(Id) vs 게이트 전압(Vg)")
    fig, ax = plt.subplots()
    ax.plot(Vg_values, Id_values, marker='o', linestyle='-', color='blue')
    ax.set_xlabel("Vg (V)")
    ax.set_ylabel("Id (A)")
    ax.set_title("MOSFET 드레인 전류 특성")
    ax.grid(True)
    st.pyplot(fig)
