# pages/3_Transaction_Analyzer.py

import streamlit as st
import pandas as pd
import google.generativeai as genai
import io

st.set_page_config(layout="wide")
st.title("📂 Transaction Analyzer (Powered by Gemini)")

# 🔐 Load API key from Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Upload
uploaded_file = st.file_uploader("Upload your bank transactions (CSV or Excel)", type=["csv", "xlsx"])

if uploaded_file:
    # Read file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("🔍 Raw Transactions Preview")
    st.dataframe(df.head())

    expected_cols = {"Date", "Description", "Amount"}
    if not expected_cols.issubset(df.columns):
        st.error("❗ Required columns not found. Please include at least: Date, Description, Amount")
    else:
        st.success("✅ File is valid!")

        # Button to process with Gemini
        if st.button("🔮 Categorize with Gemini"):
            st.info("Sending to Gemini for analysis...")

            # Format for Gemini
            records = df[["Description", "Amount"]].astype(str).to_dict(orient="records")
            prompt = f"""
You are a helpful financial assistant. Categorize each transaction into one of the following budget categories:
- Groceries
- Dining
- Housing
- Utilities
- Shopping
- Entertainment
- Transport
- Misc

Return the original description and amount along with a new 'Category' column. Use CSV format.

Transactions:
{records}
"""

            try:
                model = genai.GenerativeModel("models/gemini-1.5-pro")

                # ⬅️ Prepare Gemini prompt
                response = model.generate_content(prompt)  # ✅ Move this line outside try to ensure it exists
                csv_output = response.text.strip()

                # Remove markdown formatting if present
                if csv_output.startswith("```csv"):
                    csv_output = csv_output.strip("`").replace("csv\n", "").replace("```", "").strip()

                # ✅ Try parsing the Gemini response
                df_categorized = pd.read_csv(io.StringIO(csv_output), skipinitialspace=True)

                st.success("✅ Gemini categorized your transactions!")

                # Show results
                st.subheader("📊 Categorized Transactions")
                st.dataframe(df_categorized)

                st.subheader("💵 Spending Summary by Category")
                st.write("📎 Parsed columns:", df_categorized.columns.tolist())
                
                # Ensure headers are clean
                df_categorized.columns = df_categorized.columns.str.strip()
                df_categorized["Amount"] = pd.to_numeric(df_categorized["Amount"], errors="coerce")

                # Show spending summary
                st.subheader("💵 Spending Summary by Category")
                summary = df_categorized.groupby("Category")["Amount"].sum().sort_values(ascending=False)
                st.bar_chart(summary)

                summary = df_categorized.groupby("Category")["Amount"].sum().sort_values(ascending=False)
                st.bar_chart(summary)

                st.download_button(
                    "⬇️ Download Categorized Transactions",
                    df_categorized.to_csv(index=False),
                    file_name="categorized_transactions.csv",
                    mime="text/csv"
                )

            except Exception as e:
                st.error("⚠️ Gemini failed to return properly formatted CSV.")
                try:
                    st.code(response.text)
                except:
                    st.warning("No Gemini response available.")
                st.exception(e)

