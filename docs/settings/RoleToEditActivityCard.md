# Role To Edit Activity Card

**Technical Name:** RoleToEditActivityCard

**Category:** User Management

**Default Value:** 

**Impact Level:** High

**Description:**

Allows designated roles to edit the Activity Card within the Pathlock Cloud GRC platform. This parameter controls access to modify transactional information on the activity level, ensuring that only authorized personnel can make edits.

**Business Impact:**

Improper configuration could result in unauthorized modifications to transactional data, affecting the integrity of the audit trail and potentially leading to compliance issues. Correct configuration ensures that only users with the necessary roles can edit sensitive transactional information, maintaining the integrity of the audit and compliance records.

**Technical Impact when configured:**

Ensures that edits to transaction details in the Activity Card are restricted to users with the appropriate roles. This contributes to a secure audit trail and compliance environment by preventing unauthorized data manipulation.

**Examples Scenario:**

- **Given:** An organization must comply with strict audit and compliance regulations.
  
  **When:** The RoleToEditActivityCard parameter is correctly configured to restrict editing capabilities.
  
  **Then:** Only users with designated roles can edit the Activity Card, ensuring adherence to compliance standards and securing the audit trail.

**Related Settings:** 

**Applicable Workflows Actions:** 

**Best Practices:** 
- **Configure when:** Setting up roles and permissions to ensure that only users who need to edit transactional information can do so, supporting compliance and security requirements.
- **Avoid when:** All users are indiscriminately given the ability to edit Activity Cards, which could compromise data integrity and compliance.