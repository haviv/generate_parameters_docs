# External User Enable Comments

**Technical Name:** ExternalUserEnableComments

**Category:** User Management

**Default Value:** Not Specified

**Impact Level:** Medium

**Description:**

The `ExternalUserEnableComments` parameter allows external users to add comments within specific workflows or modules where comments are applicable. This feature aims to enhance collaboration and communication by enabling stakeholders who are not part of the internal team to provide input or feedback directly within the system.

**Business Impact:**

Enabling comments for external users facilitates better collaboration with vendors, contractors, or any third parties who need to interact with internal processes or compliance data. It ensures that all stakeholders can provide their feedback, making the process more transparent and inclusive.

**Technical Impact when configured:**

When configured, external users gain the ability to add comments in designated areas, which can lead to improved decision-making processes due to the inclusion of diverse perspectives. It also means that there is a need to closely monitor and manage these comments to maintain the integrity and accuracy of the data within the platform.

**Examples Scenario:**

- A vendor is required to review and comment on a compliance document. Granting them access to add comments directly within the document streamlines the review process.
- External auditors need to provide feedback on risk assessments. Enabling comments allows them to add their insights directly, facilitating a more efficient audit process.

**Related Settings:**

- ExternalUserRole

**Best Practices:** 

- **Configure when:** needing to enhance collaboration with external parties directly within the GRC platform, especially during audits, compliance reviews, or risk assessments.
- **Avoid when:** there is no clear governance on who can comment or if the process does not benefit from external input.