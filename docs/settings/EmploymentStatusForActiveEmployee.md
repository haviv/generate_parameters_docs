# Employment Status For Active Employee

**Technical Name:** EmploymentStatusForActiveEmployee

**Category:** User Management

**Default Value:** Not Provided

**Impact Level:** High

**Description:**

The `EmploymentStatusForActiveEmployee` parameter is used within the Pathlock Cloud GRC platform to facilitate and manage the employment status of active employees. This parameter ensures only currently employed individuals have their actions approved within specified workflows, particularly the `ApproveStep` workflow. It plays a critical role in maintaining the integrity and security of the organization's processes by limiting access and actions to authorized personnel only.

**Business Impact:**

Implementing the `EmploymentStatusForActiveEmployee` parameter correctly ensures that only active employees can influence critical workflow decisions. This safeguard is vital for maintaining compliance with internal security policies and external regulatory requirements, thus significantly mitigating the organization's risk exposure. It directly impacts human resources and security management processes by automatically enforcing employment status as a criterion for system access and action approval.

**Technical Impact when configured:**

Once configured, the `EmploymentStatusForActiveEmployee` parameter acts as a filter within workflow actions, particularly the `ApproveStep`, by removing instances that do not meet the condition of having the concerned employee status marked as active based on the expected end date or employment status fields. This ensures actions, such as authorization certifications, are only processed for employees currently recognized as active, enhancing security protocols and compliance adherence.

**Examples Scenario:**

An organization has set forth a policy where only current employees can request access to specific high-security areas within its infrastructure. A workflow designed to approve access requests utilizes the `EmploymentStatusForActiveEmployee` parameter to evaluate requests. If an employee's status is not active—indicating they are either on leave, have resigned, or have been terminated—their request will automatically be disqualified, thus preventing unauthorized access.

**Related Settings:** 

- `AuthoirizationCertification.ExpectedEndDate`
- Active Directory Services Integration
- `HR` category information handling (from `RegistryKeysCategoriesMapping`)

**Best Practices:** configure when an organization requires stringent control over who is allowed to make approvals within critical workflows. Avoid when the organization's operational model does not differentiate actions based on employment status or where employment status is managed via a different mechanism not integrated with the Pathlock GRC platform.