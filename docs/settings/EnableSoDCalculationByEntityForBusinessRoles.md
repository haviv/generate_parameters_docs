# Enable SoD Calculation By Entity For Business Roles

**Technical Name:** EnableSoDCalculationByEntityForBusinessRoles

**Category:** SOD

**Default Value:** False

**Impact Level:** High

**Description:** This parameter enables the segregation of duties (SoD) calculation by entity for business roles. When enabled, it allows the system to compute SoD at a more granular level, considering specific entity associations within the business roles.

**Business Impact:** Enables organizations to have finer control over their SoD policies and helps in minimizing the risk of fraud by ensuring that critical tasks are appropriately segregated within business roles. This is particularly beneficial for organizations with complex business processes requiring precise access control and compliance requirements.

**Technical Impact when configured:** Once enabled, this parameter instructs the Pathlock GRC platform to perform SoD analysis considering the entities associated with business roles. This ensures that SoD checks are not just carried out at a global level but also take into account the specific areas of operation, further refining compliance and security measures.

**Examples Scenario:** If an organization wants to ensure that individuals involved in financial approvals do not have access to edit financial records, enabling SoD calculation by entity for business roles can help identify such conflicts at a more detailed level, thereby preventing potential fraud or errors.

**Related Settings:** N/A

**Best Practices:** 
- Configure when: The organization requires detailed SoD checks to ensure precise access control within its operations, particularly when operating in highly regulated industries.
- Avoid when: The organization has simple business processes with minimal risk of access-related compliance issues, as enabling this feature may unnecessarily complicate the management of SoD policies.