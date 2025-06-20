import streamlit as st
import matplotlib.pyplot as plt

# 설정 값
Vth = 2.0  # 임계 전압
k = 1.5    # 전도 계수
MAX_VGS = 20
MAX_VDS = 55
MAX_ID = 49

# 전류 계산 함수
def calculate_current(Vgs, Vds):
    if Vgs < Vth:
        return 0
    else:
        return k * (Vgs - Vth)**2

# 고장 판단 함수
def check_fault(Vgs, Vds, Id):
    if abs(Vgs) > MAX_VGS:
        return "⚠️ 게이트 전압이 너무 높습니다!"
    elif Vds > MAX_VDS:
        return "⚠️ 드레인 전압이 너무 높습니다!"
    elif Id > MAX_ID:
        return "⚠️ 과전류가 발생했습니다!"
    elif Id == 0:
        return "MOSFET이 꺼진 상태입니다."
    else:
        return "✅ 정상 작동 중입니다."

# Streamlit UI 구성
st.title("🔌 MOSFET 시뮬레이터")
st.markdown("Vgs (게이트 전압)와 Vds (드레인 전압)를 조절하여 전류 흐름을 확인해보세요.")

Vgs = st.slider("게이트-소스 전압 Vgs (V)", 0.0, 25.0, 5.0, step=0.1)
Vds = st.slider("드레인-소스 전압 Vds (V)", 0.0, 60.0, 10.0, step=0.1)

Id = calculate_current(Vgs, Vds)
status = check_fault(Vgs, Vds, Id)

st.subheader("📊 결과")
st.write(f"전류 \( I_D \): {Id:.2f} A")
st.write(f"상태: {status}")

# 그래프 출력
vgs_range = [i / 10 for i in range(0, 250)]
id_values = [calculate_current(v, Vds) for v in vgs_range]

fig, ax = plt.subplots()
ax.plot(vgs_range, id_values, label=f"Vds = {Vds}V")
ax.axvline(x=Vth, color='gray', linestyle='--', label="임계 전압 Vth")
ax.axhline(y=MAX_ID, color='red', linestyle=':', label="최대 전류")
ax.set_xlabel("Vgs (V)")
ax.set_ylabel("Id (A)")
ax.set_title("MOSFET 전류-전압 특성")
ax.grid(True)
ax.legend()
st.pyplot(fig)
