# Authorization Review For SoD Activity Drill Down

**Technical Name:** AuthorizationReviewForSoDActivityDrillDown

**Category:** SOD

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls the depth and detail of information displayed during the authorization review process for Segregation of Duties (SoD) related activities. When enabled, it allows for an expanded view, including specific roles involved in SoD violations and relevant approval details.

**Business Impact:**

Enabling this feature enhances the transparency and accountability in managing SoD risks by providing detailed insights into the authorization aspects of SoD violations. It facilitates informed decision-making in the approval process, ensuring that SoD risks are managed effectively and in compliance with organizational policies and regulations.

**Technical Impact when configured:**

When configured, this parameter expands the authorization review details to include roles involved in SoD risks and their corresponding approval attributes, such as who approved a violation and until when the approval is valid. This level of detail is crucial for audit and compliance purposes, offering a deeper understanding of the SoD management process within the organization.

**Examples Scenario:**

An auditor conducting a compliance review requires detailed information on how SoD conflicts are authorized and managed within the organization. By enabling AuthorizationReviewForSoDActivityDrillDown, the auditor can see not just that a violation was approved, but also who approved it and the validity of that approval, thereby assessing whether appropriate controls are in place and are being effectively utilized.

**Related Settings:**

- IncludeRolesForSoDRisks

**Best Practices:** 

- **Configure when:** Detailed tracking and logging of authorization reviews are required for audit purposes or to enhance the risk management process.
- **Avoid when:** The extra detail might overwhelm the review process or if there is a need to restrict the visibility of sensitive role information during the review process.