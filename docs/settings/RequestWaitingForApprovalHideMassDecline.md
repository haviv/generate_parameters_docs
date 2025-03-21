# Request Waiting For Approval Hide Mass Decline

**Technical Name:** RequestWaitingForApprovalHideMassDecline

**Category:** Workflow

**Default Value:** Not Provided

**Impact Level:** Medium

**Description:**

This parameter controls the visibility of mass decline options in the request waiting for approval process within Pathlock's GRC platform. When enabled, it hides the ability to mass decline requests, ensuring that each request is considered individually.

**Business Impact:**

Enabling this parameter reinforces the meticulous scrutiny of access requests, contributing to tighter security and compliance by preventing bulk declinations that might bypass necessary evaluation. This ensures that all requests are adequately reviewed, supporting compliance with internal policies and external regulations.

**Technical Impact when configured:**

When this parameter is set, the options for mass decline in the GridView of requests waiting for approval are hidden. This means reviewers must address each request individually, rather than declining multiple requests in a bulk action. This setting directly impacts the workflow for managing access requests by enforcing a more granular review process.

**Examples Scenario:**

A security team wants to ensure that every access request is carefully reviewed to meet strict compliance requirements. By enabling this parameter, they can remove the temptation or possibility for reviewers to quickly decline multiple requests without proper consideration.

**Related Settings:** No directly related settings provided from the code references.

**Applicable Workflows Actions:** 

This parameter does not directly correspond to specific workflow actions named in the provided context but is integral to the overall workflow and approach to request management within the Pathlock GRC platform.

**Best Practices:** 

- **Configure when:** You require a thorough review process for each request within your organization to meet compliance standards.
- **Avoid when:** Your organization has a high volume of requests and trusts automated policies to accurately pre-filter requests before manual review, allowing for bulk actions without compromising security or compliance standards.