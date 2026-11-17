import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="부산대 일물실 통합 자동화 플랫폼", page_icon="🧪", layout="wide"
)

st.title("🧪 부산대학교 일반물리학실험 통합 자동화 플랫폼")
st.markdown(
    "사이드바에서 원하는 실험 **챕터**를 선택하면 해당 실험의 데이터 시트 입력 칸과"
    " 오차율 계산기가 실시간으로 나타납니다."
)

# 📚 사이드바: 챕터 선택 메뉴
chapter = st.sidebar.selectbox(
    "📚 실험 챕터 선택",
    [
        "챕터 18. 유도 기전력",
        "챕터 1. 오차론 및 길이 측정 (추가 예시)",
        "챕터 19. 자기장 측정 (확장 템플릿)",
    ],
)

st.sidebar.divider()
st.sidebar.markdown(
    "💡 **사용 팁**\n- 실험실에서 스마트폰이나 노트북으로 이 주소에 접속한"
    " 뒤,\n  그날의 챕터만 톡 골라서 값을 바로 입력하고 계산하세요!"
)

# ⚡ [챕터 18] 유도 기전력 실험
if chapter == "챕터 18. 유도 기전력":
  st.subheader("📌 챕터 18: 유도 기전력 측정 실험")
  st.markdown(
      "패러데이 법칙에 따른 유도 기전력 실험 데이터를 입력하고 이론값과 비교합니다."
  )

  sub_mode = st.radio(
      "실험 세부 조건 선택",
      [
          "1. 이차코일 권수(N₂)에 따른 유도 기전력",
          "2. 주파수(f)에 따른 유도 기전력",
          "3. 1차 전류(I)에 따른 유도 기전력",
      ],
      horizontal=True,
  )

  if "권수" in sub_mode:
    st.markdown("#### 🔹 이차코일 권수($N_2$) 변화 실험")
    df_default = pd.DataFrame({
        "이차코일 권수 (N2)": [100, 200, 300, 400],
        "실험값 V_rms (V)": [0.12, 0.24, 0.36, 0.48],
    })
    edited_df = st.data_editor(
        df_default, num_rows="dynamic", use_container_width=True
    )

    if st.button("계산 및 오차 분석 실행", type="primary"):
      slope = (
          edited_df.iloc[0]["실험값 V_rms (V)"]
          / edited_df.iloc[0]["이차코일 권수 (N2)"]
      )
      edited_df["이론값 V_rms (V)"] = edited_df["이차코일 권수 (N2)"] * slope
      edited_df["오차율 (%)"] = (
          abs(edited_df["이론값 V_rms (V)"] - edited_df["실험값 V_rms (V)"])
          / edited_df["이론값 V_rms (V)"]
          * 100
      )

      st.success("✨ 계산이 완료되었습니다!")
      st.dataframe(edited_df, use_container_width=True)

      st.markdown("### 📈 권수 vs 유도 기전력 그래프")
      st.line_chart(
          edited_df.set_index("이차코일 권수 (N2)")[
              ["실험값 V_rms (V)", "이론값 V_rms (V)"]
          ]
      )

  elif "주파수" in sub_mode:
    st.markdown("#### 🔹 주파수($f$) 변화 실험")
    df_default = pd.DataFrame({
        "주파수 f (Hz)": [50, 100, 150, 200],
        "실험값 V_rms (V)": [0.20, 0.41, 0.60, 0.82],
    })
    edited_df = st.data_editor(
        df_default, num_rows="dynamic", use_container_width=True
    )

    if st.button("계산 및 오차 분석 실행", type="primary"):
      slope = (
          edited_df.iloc[0]["실험값 V_rms (V)"]
          / edited_df.iloc[0]["주파수 f (Hz)"]
      )
      edited_df["이론값 V_rms (V)"] = edited_df["주파수 f (Hz)"] * slope
      edited_df["오차율 (%)"] = (
          abs(edited_df["이론값 V_rms (V)"] - edited_df["실험값 V_rms (V)"])
          / edited_df["이론값 V_rms (V)"]
          * 100
      )

      st.success("✨ 계산이 완료되었습니다!")
      st.dataframe(edited_df, use_container_width=True)

      st.markdown("### 📈 주파수 vs 유도 기전력 그래프")
      st.line_chart(
          edited_df.set_index("주파수 f (Hz)")[
              ["실험값 V_rms (V)", "이론값 V_rms (V)"]
          ]
      )

  else:
    st.markdown("#### 🔹 1차 전류($I$) 변화 실험")
    df_default = pd.DataFrame({
        "1차 전류 I (A)": [0.2, 0.4, 0.6, 0.8],
        "실험값 V_rms (V)": [0.15, 0.31, 0.44, 0.60],
    })
    edited_df = st.data_editor(
        df_default, num_rows="dynamic", use_container_width=True
    )

    if st.button("계산 및 오차 분석 실행", type="primary"):
      slope = (
          edited_df.iloc[0]["실험값 V_rms (V)"]
          / edited_df.iloc[0]["1차 전류 I (A)"]
      )
      edited_df["이론값 V_rms (V)"] = edited_df["1차 전류 I (A)"] * slope
      edited_df["오차율 (%)"] = (
          abs(edited_df["이론값 V_rms (V)"] - edited_df["실험값 V_rms (V)"])
          / edited_df["이론값 V_rms (V)"]
          * 100
      )

      st.success("✨ 계산이 완료되었습니다!")
      st.dataframe(edited_df, use_container_width=True)

      st.markdown("### 📈 1차 전류 vs 유도 기전력 그래프")
      st.line_chart(
          edited_df.set_index("1차 전류 I (A)")[
              ["실험값 V_rms (V)", "이론값 V_rms (V)"]
          ]
      )

# 📏 [챕터 1] 오차론 및 길이 측정 (추가 예시)
elif chapter == "챕터 1. 오차론 및 길이 측정 (추가 예시)":
  st.subheader("📌 챕터 1: 오차론 및 측정값 통계 분석")
  st.markdown(
      "반복 측정값들의 평균과 표준오차를 계산하는 범용 데이터 시트입니다."
  )

  df_default = pd.DataFrame(
      {"회차": [1, 2, 3, 4, 5], "측정값": [10.1, 10.2, 10.0, 10.3, 10.1]}
  )
  edited_df = st.data_editor(
      df_default, num_rows="dynamic", use_container_width=True
  )

  if st.button("통계 분석 실행", type="primary"):
    vals = edited_df["측정값"].dropna()
    mean_val = np.mean(vals)
    std_val = np.std(vals, ddof=1)

    st.success("✨ 분석 완료!")
    c1, c2, c3 = st.columns(3)
    c1.metric("평균 (Mean)", f"{mean_val:.4f}")
    c2.metric("표준편차 (Std Dev)", f"{std_val:.4f}")
    c3.metric("데이터 개수 (N)", f"{len(vals)}개")

# 🚀 [기타 챕터 확장용 기본 템플릿]
else:
  st.subheader("📌 새로운 챕터 준비 중")
  st.markdown(
      "다음 실험 시간에 다룰 챕터 코드를 이 자리에 쏙쏙 붙여넣으면 됩니다!"
  )
