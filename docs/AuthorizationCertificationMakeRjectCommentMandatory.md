**Technical Name:** AuthorizationCertificationMakeRjectCommentMandatory

**Category:** Compliance

**Default Value:** False

**Impact Level:** High

**Description:**

This parameter requires users to provide a comment when they reject an authorization during the certification process. By enforcing justification for rejections, it enhances audit trails and accountability within the certification workflow.

**Business Impact:**

Mandating rejection comments significantly improves the auditability and traceability of certification processes. This level of detail supports compliance with internal and external audit requirements by providing clear rationales for access denials, thereby enhancing the organization's security posture and compliance status.

**Technical Impact when configured:**

When enabled, any rejection action taken by a user in the authorization certification process will prompt a mandatory input for the user to leave a comment explaining the reason for rejection. This ensures that all rejections are accompanied by an explanation, fortifying the decision-making audit trail.

**Example Scenario:**

In a scenario where a department head is performing a quarterly review of access rights within their department, this parameter will require the head to provide specific reasons for any access rights they decide to reject. For instance, if a particular access is no longer relevant due to a change in job role, the department head must specify this rationale in the comment. This information will prove invaluable during audits, showcasing rigorous and justified access control practices.

**Related Settings:**

- AuthorizationCertificationHideIndirectRoleAssignment
- AuthorizationCertificationShowUserReviewInWideApprovalScreen

**Best Practices:** 

- Configure this parameter when your organization is subject to strict compliance regulations requiring detailed audit trails for access control decisions.
- Avoid configuring this parameter if your process prioritizes speed and your organizational risk assessment deems it unnecessary to require comments for every rejection.