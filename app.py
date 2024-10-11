import streamlit as st

class SalaryGroup:
    def __init__(self, name, base_salary, num_members):
        self.name = name
        self.base_salary = base_salary
        self.num_members = num_members
        self.increment = 0.0
        self.new_salary = base_salary

    def update_salary(self):
        self.new_salary = self.base_salary + self.increment


class SalaryManager:
    def __init__(self, budget):
        self.groups = {}
        self.budget = budget

    def add_group(self, name, base_salary, num_members):
        self.groups[name] = SalaryGroup(name, base_salary, num_members)

    #def update_members(self, name, num_members):
        #if name in self.groups:
            #groups = self.groups[name]
            #groups.num_members = num_members
            #self.update_members()

    def update_salary(self):
        total_members = sum(group.num_members for group in self.groups.values())
        increments = self.calculate_increments()

        for group_name, increment in increments.items():
            group = self.groups[group_name]
            group.increment = increment * self.budget / total_members
            group.update_salary()

    def calculate_increments(self):
        increments = {}
        base_increment = 0.25
        salary_groups = list(self.groups.keys())

        for i in range(len(salary_groups) - 1, -1, -1):
            increments[salary_groups[i]] = base_increment
            base_increment -= 0.0025

        for group in increments:
            if increments[group] < 0:
                increments[group] = 0

        return increments

    def update_salary_based_on_changes(self):
        self.update_salary()


# Streamlit app
# Title in green color
st.markdown("<h1 style='color: green;'>JKUSA Salary Increment Management Dashboard</h1>", unsafe_allow_html=True)

# Initialize SalaryManager with budget
budget = st.number_input("Enter Budget for Salary Increments:", value=50000, step=1000)
salary_manager = SalaryManager(budget=budget)

# Adding groups
group_names = ["A - Ksh11850", "B - Ksh10650", "C - Ksh9650", "D - Ksh8650", "E - Ksh6250", "F - Ksh5250", "G - 4750", "H - Ksh4250", "I - Ksh2750", "J - Ksh2250"]
base_salaries = [11850, 10650, 9650, 8650, 6250, 5250, 4750, 4250, 2750, 2250]
num_members = [10, 1, 20, 10, 50, 1, 2, 28, 4, 3]

for i in range(len(group_names)):
    with st.expander(f"Group {group_names[i]}"):
        members = st.number_input(f"Number of Members in Group {group_names[i]}:", value=num_members[i])
        salary_manager.add_group(group_names[i], base_salaries[i], members)

# Update salaries based on the current budget
if st.button("Update Salaries"):
    salary_manager.update_salary()

    # Display new salaries
    st.subheader("New Salaries:")
    for group_name, group in salary_manager.groups.items():
        st.write(f"Group {group_name}: New Salary = {group.new_salary:.2f}, Members = {group.num_members}")


# Add a notice about the model development
#st.markdown("___")  # Optional line for separation
#st.write("Model developed by Mathew Shem and officiated by Finance Secretary Kevin Muga.")
# Add a notice about the model development in green color
st.markdown("<p style='color: green;'>Model developed by Mathew Shem and officiated by Finance Secretary Kevin Muga.</p>", unsafe_allow_html=True)



# Functionality to update members dynamically
#st.header("Update Group Members")
#selected_group = st.selectbox("Select Group to Update:", group_names)
#new_member_count = st.number_input("New Number of Members:", value=10)

#if st.button("Update Members"):
    #salary_manager.update_members(selected_group, new_member_count)
   # st.success(f"Updated members in Group {selected_group} to {new_member_count}.")

# Ensure to run the Streamlit app using the command:
# streamlit run <script_name>.py
