# Maximum Workflow Upload File Size

**Technical Name:** MaximumWorkflowUploadFileSize

**Category:** Workflow

**Default Value:** 

**Impact Level:** Medium

**Description:**

The Maximum Workflow Upload File Size parameter controls the upper limit of the file size that can be uploaded within the workflow processes. It ensures that files exceeding the set limit are not uploaded, safeguarding the system from potential performance issues or security risks associated with handling large files.

**Business Impact:**

Setting an appropriate maximum file size for workflow uploads helps in maintaining system performance and prevents the network from being overloaded with large file transfers. It also assists in enforcing compliance with company policies regarding data handling and storage.

**Technical Impact when configured:**

- Enhances system performance by avoiding the processing of large files that can slow down the system.
- Reduces the risk of running out of storage space due to oversized files.
- Mitigates potential security vulnerabilities associated with the upload of large, possibly malicious files.

**Examples Scenario:**

A company has a policy that all workflow-related documents (e.g., invoices, contracts) must not exceed 10MB to ensure quick processing and to avoid unnecessary storage use. The Maximum Workflow Upload File Size parameter can be set to enforce this policy, preventing users from uploading files that do not comply with the company's document size regulations.

**Related Settings:** 

- AllowedUploadFileTypes

**Best Practices:** 

- **configure when:** It's necessary to align with the organization's data handling policies, and to maintain optimal system performance.
- **avoid when:** If there is no clear need to limit file sizes, as unnecessary restrictions might hinder operational flexibility.