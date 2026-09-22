
class Patient:
    def __init__(self, patient_id, name, treatment_cost):
        self.patient_id = patient_id
        self.name = name
        self.treatment_cost = treatment_cost
        self.category = self.categorize()

    def categorize(self):
        if self.treatment_cost > 10000:
            return "Special"
        return "General"

    def __str__(self):
        return (f"ID: {self.patient_id:<6} | Name: {self.name:<20} | "
                f"Cost: ₹{self.treatment_cost:<10.2f} | Category: {self.category}")


class Hospital:

    def __init__(self, name="City Hospital"):
        self.name = name
        self.patients = []

    def add_patient(self, patient_id, name, treatment_cost):

        if any(p.patient_id == patient_id for p in self.patients):
            print(f"  Patient ID {patient_id} already exists. Use a unique ID.\n")
            return

        if treatment_cost < 0:
            print("  Treatment cost cannot be negative.\n")
            return

        patient = Patient(patient_id, name, treatment_cost)
        self.patients.append(patient)
        print(f"✅ Patient '{name}' added successfully as '{patient.category}' patient.\n")

    def display_all_records(self):
        """Display all patient records in a formatted table."""
        if not self.patients:
            print("No patient records found.\n")
            return

        print(f"\n{'='*80}")
        print(f"{self.name} - Patient Records")
        print(f"{'='*80}")
        for patient in self.patients:
            print(patient)
        print(f"{'='*80}\n")

    def display_by_category(self, category):
        """Display patients filtered by category (General/Special)."""
        filtered = [p for p in self.patients if p.category.lower() == category.lower()]
        if not filtered:
            print(f"No '{category}' patients found.\n")
            return

        print(f"\n--- {category} Patients ---")
        for patient in filtered:
            print(patient)
        print()

    def total_revenue(self):
        """Calculate total treatment cost collected."""
        return sum(p.treatment_cost for p in self.patients)

    def remove_patient(self, patient_id):
        """Remove a patient record by ID."""
        for p in self.patients:
            if p.patient_id == patient_id:
                self.patients.remove(p)
                print(f"🗑️  Patient ID {patient_id} removed.\n")
                return
        print(f"⚠️  Patient ID {patient_id} not found.\n")


def main():
    hospital = Hospital("Sunrise General Hospital")

    # Adding sample patients
    hospital.add_patient(101, "Ramesh Kumar", 5000)
    hospital.add_patient(102, "Anjali Sharma", 15000)
    hospital.add_patient(103, "Vikram Singh", 8000)
    hospital.add_patient(104, "Priya Nair", 25000)
    hospital.add_patient(101, "Duplicate Test", 3000)   # duplicate ID test

    # Display all records
    hospital.display_all_records()

    # Display by category
    hospital.display_by_category("Special")
    hospital.display_by_category("General")

    # Total revenue
    print(f"💰 Total Revenue Collected: ₹{hospital.total_revenue():.2f}\n")

    # Remove a patient
    hospital.remove_patient(103)
    hospital.display_all_records()


if __name__ == "__main__":
    main()
