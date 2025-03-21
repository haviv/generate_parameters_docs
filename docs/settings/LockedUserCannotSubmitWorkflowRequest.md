# Locked User Cannot Submit Workflow Request

**Technical Name:** LockedUserCannotSubmitWorkflowRequest

**Category:** Workflow

**Default Value:**

**Impact Level:** High

**Description:**

This parameter controls whether users with a locked status are permitted to submit requests within workflow processes. Typically, this addresses security measures by preventing inactive or suspended user accounts from initiating workflow actions.

**Business Impact:**

Implementing this parameter enhances security and compliance by ensuring that only active and authorized users can participate in workflow processes. It reduces the risk of unauthorized access and actions within the system, reinforcing the organization's control environment.

**Technical Impact when configured:**

When enabled, the system will check the user's account status before allowing workflow request submissions. If the user is found to be locked, the submission will be blocked, thereby ensuring that only users with the appropriate permissions can initiate or partake in workflow activities.

**Examples Scenario:**

- **Situation:** An organization is undergoing an audit and must demonstrate control over who can initiate processes within their GRC platform.
  
  **Implementation:** By configuring the `LockedUserCannotSubmitWorkflowRequest` parameter to prevent locked users from submitting requests, the organization can provide evidence of enforced security controls, satisfying audit requirements.

**Related Settings:** 

- `IsApproved`
- `IncludeAuthorizationObjectsInSoD`

**Best Practices:** configure when,
- Security policies demand strict control over process initiation by ensuring only authorized, active users can perform actions.
  
  avoid when,
- There is a need for flexibility in allowing temporarily suspended users to submit workflow requests under exceptional circumstances.