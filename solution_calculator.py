
import streamlit as st
import pandas as pd

def solution_calculator():

    st.title("🧪 Solution Preparation Calculator")

    st.write(
        "Calculate solution mass, molarity and dilution."
    )

    choice = st.selectbox(
        "Choose a calculation",
        [
            "Solution Preparation",
            "Dilution Calculation",
            "Molarity Calculation"
        ]
    )

    st.divider()

    if choice == "Solution Preparation":

        st.subheader("⚗️ Solution Preparation")

        chemicals = {
            "Sodium Chloride (NaCl)": 58.44,
            "Glucose": 180.156,
            "Sucrose": 342.296,
            "Potassium Chloride (KCl)": 74.551,
            "Custom Chemical": None
        }

        chemical = st.selectbox(
            "Select Chemical",
            list(chemicals.keys())
        )

        if chemicals[chemical] is None:
            mw = st.number_input(
                "Molecular Weight (g/mol)",
                min_value=0.001,
                value=100.0
            )
        else:
            mw = chemicals[chemical]
            st.info(f"Molecular Weight: {mw} g/mol")

        M = st.number_input(
            "Required Molarity (mol/L)",
            min_value=0.001,
            value=0.1
        )

        V = st.number_input(
            "Final Volume (mL)",
            min_value=0.1,
            value=100.0
        )

        if st.button("Calculate Mass"):

            moles = M * V / 1000
            mass = moles * mw

            st.success(f"Required Mass: {mass:.4f} g")

            st.write(f"Number of moles: {moles:.5f} mol")

    elif choice == "Dilution Calculation":

        st.subheader("💧 Dilution Calculator")

        M1 = st.number_input(
            "Stock Concentration (M)",
            min_value=0.001,
            value=1.0
        )

        M2 = st.number_input(
            "Required Concentration (M)",
            min_value=0.001,
            value=0.1
        )

        V2 = st.number_input(
            "Final Volume (mL)",
            min_value=0.1,
            value=100.0
        )

        if st.button("Calculate Dilution"):

            if M2 > M1:
                st.error("Required concentration cannot exceed stock concentration.")
            else:
                V1 = (M2 * V2) / M1

                st.success(
                    f"Stock Solution Required: {V1:.3f} mL"
                )

                st.info(
                    f"Final volume: {V2:.3f} mL. "
                    f"Add suitable solvent until this final volume is reached."
                )

                st.latex(r"M_1V_1=M_2V_2")

    elif choice == "Molarity Calculation":

        st.subheader("📊 Molarity Calculator")

        mass = st.number_input(
            "Mass of Solute (g)",
            min_value=0.001,
            value=5.844
        )

        mw = st.number_input(
            "Molecular Weight (g/mol)",
            min_value=0.001,
            value=58.44
        )

        V = st.number_input(
            "Solution Volume (mL)",
            min_value=0.1,
            value=100.0
        )

        if st.button("Calculate Molarity"):

            molarity = (mass / mw) / (V / 1000)

            st.success(
                f"Molarity: {molarity:.5f} M"
            )

    st.divider()

    st.caption("Chemistry Virtual Laboratory")


if __name__ == "__main__":
    solution_calculator()
