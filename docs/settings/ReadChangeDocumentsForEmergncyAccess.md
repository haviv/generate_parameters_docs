# Read Change Documents For Emergency Access

**Technical Name:** ReadChangeDocumentsForEmergncyAccess

**Category:** Workflow

**Default Value:** N/A

**Impact Level:** High

**Description:** 

This parameter controls the access to change documents for users granted emergency access, ensuring that only authorized changes are made during critical situations.

**Business Impact:**

Managing this parameter effectively ensures that emergency access is used responsibly and in compliance with internal and external audit and compliance requirements. It aids in minimizing the risk of unauthorized changes, thus protecting business integrity and sensitive data.

**Technical Impact when configured:**

When configured, this parameter allows for the oversight and auditability of changes made under emergency access, facilitating compliance with governance standards. It impacts the ability to review and validate changes made during emergency interventions.

**Examples Scenario:**

An organization faces a critical system issue requiring immediate administrative intervention. A user is granted emergency access to resolve the issue. With the `ReadChangeDocumentsForEmergncyAccess` parameter configured, the organization can later audit the changes made during this emergency access period to ensure all modifications were necessary and authorized.

**Related Settings:** 

N/A

**Best Practices:** 

- **Configure when:** Emergency access is granted frequently or in systems with high sensitivity to unauthorized changes.
- **Avoid when:** If the overhead of managing and reviewing change documents is not justifiable by the criticality of the system or the frequency of emergency access.