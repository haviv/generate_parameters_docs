# Authorization Certification For Report Push Approvals To Report

**Technical Name:** AuthorizationCertificationForReportPushApprovalsToReport

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The `AuthorizationCertificationForReportPushApprovalsToReport` parameter is used within the Pathlock Cloud GRC platform, specifically in the context of authorization certification workflow actions. It facilitates the process of pushing approval reports related to authorization certification to designated managers or responsible parties.

**Business Impact:**

Implementing this parameter streamlines the process of reporting and certifying authorizations, thus enhancing the transparency and accountability of access controls within the organization. It ensures that managers are promptly informed about certification actions, which is critical for maintaining compliance standards and mitigating security risks associated with unauthorized access.

**Technical Impact when configured:**

When this parameter is configured, it triggers the automated sending of bulk emails to managers with the details of the authorization certification reviews. This operation is part of the tail operations in the submission process of authorization certifications, ensuring that all relevant parties are kept informed about the status of authorization approvals.

**Examples Scenario:**

- In a scenario where an organization needs to certify that employees have the correct level of access to financial systems, the `AuthorizationCertificationForReportPushApprovalsToReport` can be configured. Following the review process, reports detailing the outcome of these certifications are automatically generated and pushed to the managers of those employees. This ensures that any discrepancies are quickly identified and remedied.

**Related Settings:**

**Applicable Workflows Actions:** AuthoirizationCertificationBO

**Best Practices:** 

- Configure when: There's a need for automated communication of authorization certification outcomes to enhance transparency and ensure timely updates.
- Avoid when: The organizational workflow or compliance requirement does not mandate direct report push to managers or where manual reporting is preferred for specific cases.