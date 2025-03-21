# Run SoD In Memory

**Technical Name:** RunSoDInMemory

**Category:** Compliance

**Default Value:** Not Specified

**Impact Level:** High

**Description:**

The RunSoDInMemory parameter controls whether the Segregation of Duties (SoD) analysis for users within the Pathlock Cloud GRC platform is executed in memory. This setting optimizes how SoD violations are identified and reported, potentially leading to performance improvements during compliance checks.

**Business Impact:**

Enabling RunSoDInMemory can significantly affect how quickly SoD checks are performed, directly impacting the time to compliance and the ability for organizations to respond to and remediate compliance issues. This means faster audit cycles and potentially lower compliance costs.

**Technical Impact when configured:**

- **Enabled:** SoD checks are performed in memory, leading to faster processing times and immediate results. This is beneficial for environments requiring rapid compliance assessments.
- **Disabled:** SoD checks may take longer to process as they may not utilize optimized in-memory operations, which could be preferable for environments with limited system resources.

**Examples Scenario:**

- **Scenario 1:** A financial institution requires daily SoD checks across thousands of users to ensure compliance with stringent regulatory requirements. Enabling RunSoDInMemory allows the institution to streamline these checks, reducing the impact on system resources and ensuring that compliance reports are generated promptly.

**Related Settings:** Not Specified

**Best Practices:** 
- **Configure when:** Fast processing of SoD checks is a priority, and there is sufficient memory available to support in-memory operations without affecting other applications.
- **Avoid when:** System memory is limited, or the environment cannot sustain the additional memory load without impacting other critical services.