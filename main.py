# MD-Tax-Master: Precision Maryland Tax Estimator
# Project: 400-mission portfolio

def run_tax_mission():
    # 1. DATA: Local "Piggyback" Tax Rates for MD Counties
    county_rates = {
        "annapolis": 0.0281,
        "anne arundel": 0.0281,
        "baltimore city": 0.032,
        "baltimore county": 0.032,
        "montgomery": 0.032,
        "frederick": 0.0296,
        "prince georges": 0.032,
        "howard": 0.032,
        "carroll": 0.0303,
        "harford": 0.0306
    }

    print("--- MD-TAX-MASTER: MISSION START ---")
    print("This tool calculates Maryland State + Local Taxes.")
    print("---------------------------------------------")

    try:
        # 2. INPUT: Get the raw data from the user
        income = float(input("Enter your annual gross income (e.g., 50000): "))
        county = input("Enter your MD county (e.g., Montgomery): ").strip().lower()

        # 3. LOGIC: Calculate the specific rates
        # Maryland state tax is roughly 4.75% for most earners
        state_rate = 0.0475
        
        # Look up county rate; if not found, use a safe average of 3%
        local_rate = county_rates.get(county, 0.030)
        
        total_tax_rate = state_rate + local_rate
        final_tax = income * total_tax_rate

        # 4. REPORT: Detailed inspection output
        print("\n--- TAX INSPECTION REPORT ---")
        print(f"Gross Income:      ${income:,.2f}")
        print(f"County:            {county.title()}")
        print(f"Combined Tax Rate: {total_tax_rate * 100:.2f}%")
        print("-----------------------------")
        print(f"TOTAL MD TAX DUE:  ${final_tax:,.2f}")
        print("-----------------------------")

    except ValueError:
        print("ERROR: Invalid data detected. Please enter a number for income.")

if __name__ == "__main__":
    run_tax_mission()