# Workflow Type For Process Verification

**Technical Name:** WorkflowTypeForProcessVerification

**Category:** Workflow

**Default Value:** N/A

**Impact Level:** Medium

**Description:**

The `WorkflowTypeForProcessVerification` parameter is designed to define the type of workflow process for verification purposes within the Pathlock Cloud GRC platform. It specifies how certain types of verification workflows, particularly those involving authorization reviews based on file attachments, should be initiated and processed.

**Business Impact:**

Configuring the `WorkflowTypeForProcessVerification` parameter correctly is crucial for maintaining streamlined and secure verification processes. It impacts how authorization reviews are conducted, ensuring that they adhere to compliance standards and internal policies. This parameter directly affects the efficiency and reliability of the review process, which is vital for managing risks, maintaining security, and ensuring compliance within the organization.

**Technical Impact when configured:**

When the `WorkflowTypeForProcessVerification` parameter is configured, it initiates and guides the workflow for process verification, ensuring that the process is carried out according to the specified parameters. This includes the initiation of authorization reviews based on file attachments, which plays a critical role in managing access controls and security policies efficiently.

**Examples Scenario:**

A scenario where the `WorkflowTypeForProcessVerification` parameter is utilized is in the initiation of an authorization review process based on file attachments. For instance, when a user attaches a file that requires authorization, this parameter helps in determining the workflow type that should be used for the review process, ensuring that the correct verification steps are followed.

**Related Settings:** N/A

**Applicable Workflows Actions:** 

- StartAuthoriztaionReviewBasedOnFileAttachement

**Best Practices:** 

- **Configure when:** You need to ensure that the workflow for process verification is aligned with your organization's security, risk, and compliance requirements. This is particularly important when dealing with file attachments that require authorization.
  
- **Avoid when:** There is no clear requirement for a specific workflow process for verifications. In such cases, using default settings may suffice.