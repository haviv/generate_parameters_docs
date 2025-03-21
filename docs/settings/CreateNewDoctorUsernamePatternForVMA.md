# Create New Doctor Username Pattern For VMA

**Technical Name:** CreateNewDoctorUsernamePatternForVMA

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

The CreateNewDoctorUsernamePatternForVMA parameter is designed for configuring the username pattern for new doctors within the VMA (Virtual Medical Assistant) context. It allows for the specification of a unique format which usernames assigned to new doctors should follow, enhancing username management and consistency across the system.

**Business Impact:**

Setting an appropriate username pattern for doctors in the VMA environment can significantly streamline user administration by ensuring consistency and easy recognition of user accounts. It impacts both operational efficiency and security by reducing the potential for username duplication and simplifying the task of managing access rights for new users.

**Technical Impact when configured:**

When configured, this parameter influences the process flow within the GetOrCreateVMAUser workflow action by applying the specified username pattern to generate new usernames for doctors. This ensures adherence to standardized naming conventions, facilitating easier user identification, support, and audit processes within the Pathlock Cloud GRC platform.

**Examples Scenario:**

For instance, if a healthcare institution prefers to use a username pattern that combines a doctor's first initial with their last name and a unique identifier (e.g., jdoe01 for John Doe), configuring this parameter to reflect such a pattern ensures that all newly created doctor accounts in the VMA system follow this convention. It simplifies user management and enhances security by creating predictable yet unique usernames.

**Related Settings:** 

- RankingForBusinessRole

**Best Practices:** 

- **Configure when:** You are setting up the Pathlock Cloud GRC platform for a healthcare provider or any organization that utilizes the VMA system and requires a systematic approach to creating usernames for new doctors.
- **Avoid when:** If the organization does not have a specific need for custom username patterns or if the creation of usernames is managed through another system that could conflict with this setting.