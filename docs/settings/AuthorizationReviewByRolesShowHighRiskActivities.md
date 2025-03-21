# Authorization Review By Roles Show High Risk Activities

**Technical Name:** AuthorizationReviewByRolesShowHighRiskActivities

**Category:** Audit

**Default Value:**

**Impact Level:** High

**Description:**

This parameter controls the visibility of high-risk activities within the authorization review process. When enabled, it filters and displays only those activities deemed high risk according to predefined criteria, facilitating targeted audits and compliance checks.

**Business Impact:**

Enabling this feature aids organizations in prioritizing their audit efforts towards higher-risk areas, reducing the likelihood of security breaches and non-compliance with regulatory standards. It ensures efficient use of resources by focusing on critical vulnerabilities within role-based access controls.

**Technical Impact when configured:**

Configuring this parameter affects how authorization reviews are conducted. Specifically, it alters the data set visible during reviews, allowing auditors to focus exclusively on high-risk activities. This refined focus can aid in the early identification of potential access-related risks and streamline the remediation process.

**Examples Scenario:**

- An organization undergoing an internal audit wishes to streamline their review process to focus on potential compliance issues within their SAP environment. By enabling this parameter, the audit team can directly address the most sensitive areas, enhancing their oversight efficiency.

**Related Settings:**

- `SapRole.MainApplicationArea`

**Best Practices:** 

- **Configure when:** Preparing for internal or external audits, especially in environments where resources are limited, or a high degree of compliance is required.
- **Avoid when:** Full, exhaustive reviews are necessary, or in low-risk environments where such focused scrutiny may divert resources from other necessary tasks.