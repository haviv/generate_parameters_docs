# Create New Doctor Sap System

**Technical Name:** CreateNewDoctorSapSystemId

**Category:** Workflow

**Default Value:** 

**Impact Level:** High

**Description:**

The 'CreateNewDoctorSapSystemId' parameter is used during workflow actions related to creating new SAP system entries for doctors within the Pathlock Cloud GRC platform. This parameter acts as an identifier for initiating and tracking the process of adding new doctor profiles to the SAP system, ensuring that the necessary user permissions and access controls are configured correctly according to compliance and governance rules.

**Business Impact:**

Incorporating the 'CreateNewDoctorSapSystemId' parameter into SAP system user creation workflows ensures that healthcare organizations maintain rigorous standards of access control and data protection. This is critical for protecting sensitive patient data and ensuring that only authorized medical personnel have access to their necessary systems, thus mitigating risks related to data breaches, unauthorized access, and non-compliance with healthcare regulations.

**Technical Impact when configured:**

When configured, the 'CreateNewDoctorSapSystemId' parameter triggers additional logic in the workflow to accurately integrate the doctor's profile into the SAP system. This includes setting up specific roles, permissions, and access levels tailored to the individual's job requirements, ensuring that access governance policies are adhered to and that the system remains secure against potential threats.

**Examples Scenario:**

- When a new doctor joins a hospital, the admin initiates a 'CreateNewDoctor' workflow, where the 'CreateNewDoctorSapSystemId' parameter is used to create a new SAP system profile for the doctor, ensuring they have access to the necessary medical records and systems from day one.

**Related Settings:**

- None explicitly mentioned in the provided code references.

**Best Practices:** configure when a new healthcare professional requires access to the SAP system, avoid when the user's role does not necessitate direct interaction with the SAP system.