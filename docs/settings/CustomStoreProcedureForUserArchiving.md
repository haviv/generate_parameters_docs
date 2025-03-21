# Custom Store Procedure For User Archiving

**Technical Name:** CustomStoreProcedureForUserArchiving

**Category:** User Management

**Default Value:** None

**Impact Level:** Medium

**Description:**

This parameter allows for the integration of custom stored procedures during the user archiving process. Tailoring this process enables organizations to implement specific logic that aligns with their internal policies and requirements for managing user lifecycle events, particularly archiving.

**Business Impact:**

Customizing the user archiving process can significantly affect compliance, by ensuring that user data is handled in accordance with legal and regulatory requirements. It also plays a crucial role in risk management, as it allows for the precise control of who has access to what within the system, thereby reducing the attack surface.

**Technical Impact when configured:**

When configured, this parameter will override the default user archiving behavior, engaging a custom-developed stored procedure that could include operations such as data anonymization, transferring of records to a historical database, or specific logging for audit purposes.

**Example Scenario:**

A financial institution needs to comply with regulatory requirements concerning the retention and protection of former employees' data. By setting the `CustomStoreProcedureForUserArchiving` parameter, they can implement a custom logic to anonymize personal identifiers while retaining essential audit trails required for compliance.

**Related Settings:**

- `SetAppliactionUserStatusByActiveDirectoryUserStatus`

**Best Practices:** 

- **Configure when:** You have specific compliance requirements or need to implement business logic not covered by the default user archiving functionality.
  
- **Avoid when:** The default user archiving process meets all organizational requirements as custom configurations may increase complexity and require additional maintenance.