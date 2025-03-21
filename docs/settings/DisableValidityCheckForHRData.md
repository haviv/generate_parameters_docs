# Disable Validity Check For HR Data

**Technical Name:** DisableValidityCheckForHRData

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls whether the validity checks for HR data are bypassed during data synchronization or integration processes within the Pathlock Cloud GRC platform. When enabled, it allows the system to accept HR data without validating certain constraints that are normally checked.

**Business Impact:**

Enabling this parameter can speed up HR data processing and integration tasks by skipping over detailed validity checks. This may be beneficial in scenarios where data is pre-validated or when quick integration is prioritized over data accuracy. However, it also carries the risk of importing incorrect or incomplete HR data into the system, which can affect downstream processes and decision-making based on this data.

**Technical Impact when configured:**

- Increased speed in HR data integration processes due to bypass of validity checks.
- Potential introduction of incorrect or incomplete HR data into the system.

**Examples Scenario:**

- A company undergoing a major HR system migration may temporarily enable this parameter to quickly integrate large volumes of HR data into the Pathlock Cloud GRC platform. This can help maintain operational continuity during the transition period.
- During initial setup or testing phases, an organization might disable validity checks to streamline the setup process, planning to enforce data validation in later stages.

**Related Settings:**

- EmployeeCustomSubtypeForMailField

**Best Practices:** 

- Configure when: Data is pre-validated, during initial system setup, or in test environments to speed up integration processes.
- Avoid when: In production environments where data accuracy and completeness are critical for compliance and operational decision-making.