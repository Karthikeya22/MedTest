from dialer import call_parent

row = {
    "patient_name": "Test Baby",
    "parent_name": "Test Parent",
    "visit_label": "Newborn (3-5 Days)",
    "insurance_type": "ACA",
    "parent_phone": "+1YOUR_VERIFIED_CELL"
}

if __name__ == "__main__":
    call_parent(row)