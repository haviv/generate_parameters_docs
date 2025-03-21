**SoD Check For Single System Only**

**Technical Name:** SodCheckForSingleSystemOnly

**Category:** SOD

**Default Value:**

**Impact Level:** Medium

**Description:**

The "SodCheck For Single System Only" parameter ensures that the Separation of Duties (SoD) checks are only applied to a single, specified system within the Pathlock GRC platform. This is particularly useful for organizations that need to enforce SoD controls on a per-system basis, allowing for more granular security and compliance enforcement.

**Business Impact:**

Using this parameter allows organizations to isolate and address SoD conflicts within a specific system, without the noise from other systems. This can result in more accurate SoD enforcement, reducing the risk of unauthorized access or fraudulent activities while not overcomplicating the compliance processes for systems that do not require such stringent controls.

**Technical Impact when configured:**

When "SodCheck For Single System Only" is configured, the Pathlock GRC platform will limit its SoD analysis to transactions, roles, and permissions within the specified system. This means SoD violation reports, and potential SoD conflicts will only reflect data from that single system, simplifying the compliance and audit processes for administrators.

**Example Scenario:**

An organization uses multiple systems for its operations, including an ERP system and a separate HR management system. By configuring this parameter, the IT security team can ensure that SoD checks are performed exclusively on the ERP system, where financial transactions occur, without being diluted by unrelated permissions in the HR system.

**Related Settings:**

- ExcludedCompositeRolesFromUserSoD

**Best Practices:** configure when you need to focus SoD checks on a system with high compliance requirements or where specific risks have been identified. Avoid when comprehensive checks across multiple systems are necessary for enterprise-wide risk management.