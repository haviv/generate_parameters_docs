# AuthorizationCertificationMakeRejectCommentErrorMessage Documentation

### Category:
Security Settings

### Default Value:
"All rejected items must have a comment"

### Impact Level:
Critical

### Description:
`AuthorizationCertificationMakeRejectCommentErrorMessage` defines the error message that is displayed to the user when a reject comment is mandatory but missing. This setting ensures that every rejection within the authorization certification process is accompanied by a comment, providing clarity on the reason for rejection.

### Business Impact:
Ensuring that reject comments are mandatory and specifying an error message for missing comments enhances the accountability and traceability within the authorization certification process. It supports audit compliance by ensuring that every decision made during the process is well-documented.

### Technical Impact when configured:
When this parameter is configured, the system enforces the inclusion of comments for all rejected items in the certification process. If a reject comment is not provided, the specified error message is displayed to the end-user, prompting them to fulfill the mandatory requirement.

### Example Scenario:
In an organization's user access review process, an auditor rejects a user's access to a specific resource but fails to provide a comment explaining the reason for rejection. With `AuthorizationCertificationMakeRejectCommentErrorMessage` configured, the system will prompt the auditor with a message "All rejected items must have a comment," ensuring that no rejection occurs without clear documentation.

### Related Settings:
- AuthorizationCertificationMakeRejectCommentMandatory

### Best Practices:
- **Configure when**: It is critical to ensure accountability and provide auditable trails of why certain accesses were rejected during authorization certifications.
- **Avoid when**: If your process does not require comments on every rejection or if enforcing this rule could unnecessarily complicate the certification process.

### Context:
This parameter is part of the security and compliance settings in systems that require thorough documentation of authorization certifications. It is crucial for maintaining high standards of governance, risk management, and compliance (GRC) by ensuring that every action taken during these certifications is accompanied by a rationale, thereby preventing unauthorized or inappropriate access to resources.