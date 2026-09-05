

class NTNChoices:
    INDIVIDUAL = 'individual'
    COMPANY = 'company'

ntn_choices = [
    (NTNChoices.INDIVIDUAL, 'Individual'),
    (NTNChoices.COMPANY, 'Company'),
]

def calculate_tax(salary):
    salary = float(salary)
    if salary <= 600000:
        return {"tax_slab": "0 \u2013 600,000", "tax_rate": "0%", "tax_owed": 0}
    elif salary <= 1200000:
        tax = (salary - 600000) * 0.05
        return {"tax_slab": "600,001 \u2013 1,200,000", "tax_rate": "5% on amount exceeding 600,000", "tax_owed": int(tax)}
    elif salary <= 2200000:
        tax = 30000 + (salary - 1200000) * 0.15
        return {"tax_slab": "1,200,001 \u2013 2,200,000", "tax_rate": "Rs. 30,000 + 15% on amount exceeding 1,200,000", "tax_owed": int(tax)}
    elif salary <= 3200000:
        tax = 180000 + (salary - 2200000) * 0.25
        return {"tax_slab": "2,200,001 \u2013 3,200,000", "tax_rate": "Rs. 180,000 + 25% on amount exceeding 2,200,000", "tax_owed": int(tax)}
    elif salary <= 4100000:
        tax = 430000 + (salary - 3200000) * 0.30
        return {"tax_slab": "3,200,001 \u2013 4,100,000", "tax_rate": "Rs. 430,000 + 30% on amount exceeding 3,200,000", "tax_owed": int(tax)}
    else:
        tax = 700000 + (salary - 4100000) * 0.35
        return {"tax_slab": "Above 4,100,000", "tax_rate": "Rs. 700,000 + 35% on amount exceeding 4,100,000", "tax_owed": int(tax)}

def calculate_zakat(asset_value):
    asset_value = float(asset_value)
    # Silver standard: 612.36 grams
    # Using rough mid-2024 price of PKR 245.7 per gram. Note: update this value periodically since silver prices fluctuate.
    silver_price_per_gram = 245.7
    nisab_threshold = int(612.36 * silver_price_per_gram) # approx 150456
    
    if asset_value >= nisab_threshold:
        return {
            "nisab_threshold": nisab_threshold,
            "meets_nisab": True,
            "zakat_due": int(asset_value * 0.025)
        }
    else:
        return {
            "nisab_threshold": nisab_threshold,
            "meets_nisab": False,
            "zakat_due": 0
        }